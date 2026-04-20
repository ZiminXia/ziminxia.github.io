#!/usr/bin/env python3
from __future__ import annotations

import argparse
import json
import os
import subprocess
import threading
import time
from http import HTTPStatus
from http.server import SimpleHTTPRequestHandler, ThreadingHTTPServer
from pathlib import Path
from urllib.parse import urlsplit


ROOT = Path(__file__).resolve().parents[1]
DEFAULT_BUILD_DIR = Path("/tmp/zimin-homepage-build")
WATCH_SUFFIXES = {
    ".css",
    ".gif",
    ".html",
    ".jpeg",
    ".jpg",
    ".js",
    ".json",
    ".md",
    ".pdf",
    ".png",
    ".scss",
    ".svg",
    ".webp",
    ".xml",
    ".yml",
}
EXCLUDED_DIRS = {
    ".git",
    ".sass-cache",
    ".bundle",
    "_site",
    "node_modules",
}
RELOAD_SNIPPET = """
<script>
(() => {
  const endpoint = "/__live_reload__";
  let currentToken = null;

  async function checkForChanges() {
    try {
      const response = await fetch(endpoint, { cache: "no-store" });
      if (!response.ok) {
        return;
      }

      const payload = await response.json();
      if (currentToken === null) {
        currentToken = payload.token;
        return;
      }

      if (payload.token !== currentToken) {
        window.location.reload();
      }
    } catch (error) {
      console.debug("Live reload check failed", error);
    }
  }

  setInterval(checkForChanges, 1000);
  checkForChanges();
})();
</script>
"""
RUBY_BUILD_SCRIPT = """
require "jekyll"

conf = Jekyll.configuration(
  "source" => ENV.fetch("LIVE_PREVIEW_SOURCE"),
  "destination" => ENV.fetch("LIVE_PREVIEW_DEST"),
  "url" => ENV.fetch("LIVE_PREVIEW_URL"),
  "baseurl" => "",
  "plugins" => [],
  "gems" => []
)

site = Jekyll::Site.new(conf)
site.process
"""


class PreviewState:
    def __init__(self) -> None:
        self._lock = threading.Lock()
        self._token = str(time.time_ns())
        self._last_error: str | None = None

    def token(self) -> str:
        with self._lock:
            return self._token

    def mark_success(self) -> None:
        with self._lock:
            self._token = str(time.time_ns())
            self._last_error = None

    def mark_error(self, message: str) -> None:
        with self._lock:
            self._last_error = message

    def status_payload(self) -> bytes:
        with self._lock:
            payload = {
                "token": self._token,
                "error": self._last_error,
            }
        return json.dumps(payload).encode("utf-8")


def should_watch(path: Path) -> bool:
    if not path.is_file():
        return False

    if any(part in EXCLUDED_DIRS for part in path.parts):
        return False

    if path.name.startswith(".") and path.name != ".gitignore":
        return False

    return path.suffix.lower() in WATCH_SUFFIXES or path.name in {
        "Gemfile",
        "Gemfile.lock",
    }


def snapshot_tree(root: Path) -> dict[str, int]:
    snapshot: dict[str, int] = {}
    for path in root.rglob("*"):
        if should_watch(path):
            snapshot[str(path)] = path.stat().st_mtime_ns
    return snapshot


def build_site(root: Path, destination: Path, state: PreviewState, preview_url: str) -> bool:
    env = os.environ.copy()
    env["LIVE_PREVIEW_SOURCE"] = str(root)
    env["LIVE_PREVIEW_DEST"] = str(destination)
    env["LIVE_PREVIEW_URL"] = preview_url

    result = subprocess.run(
        ["ruby", "-e", RUBY_BUILD_SCRIPT],
        cwd=root,
        env=env,
        capture_output=True,
        text=True,
    )

    if result.stdout:
        print(result.stdout, end="")
    if result.stderr:
        print(result.stderr, end="", file=os.sys.stderr)

    if result.returncode == 0:
        state.mark_success()
        print(f"[live-preview] build succeeded at {time.strftime('%H:%M:%S')}")
        return True

    state.mark_error(result.stderr.strip() or "Build failed")
    print(
        f"[live-preview] build failed with exit code {result.returncode}",
        file=os.sys.stderr,
    )
    return False


def watch_and_rebuild(root: Path, destination: Path, state: PreviewState, preview_url: str) -> None:
    previous = snapshot_tree(root)
    while True:
        time.sleep(1.0)
        current = snapshot_tree(root)
        if current == previous:
            continue

        previous = current
        print("[live-preview] change detected, rebuilding...")
        build_site(root, destination, state, preview_url)


def inject_reload_snippet(html: bytes) -> bytes:
    marker = b"</body>"
    if marker in html:
        return html.replace(marker, RELOAD_SNIPPET.encode("utf-8") + marker, 1)
    return html + RELOAD_SNIPPET.encode("utf-8")


def make_handler(build_dir: Path, state: PreviewState):
    class LiveReloadHandler(SimpleHTTPRequestHandler):
        def __init__(self, *args, **kwargs):
            super().__init__(*args, directory=str(build_dir), **kwargs)

        def do_GET(self) -> None:
            parsed = urlsplit(self.path)
            if parsed.path == "/__live_reload__":
                payload = state.status_payload()
                self.send_response(HTTPStatus.OK)
                self.send_header("Content-Type", "application/json; charset=utf-8")
                self.send_header("Content-Length", str(len(payload)))
                self.send_header("Cache-Control", "no-store")
                self.end_headers()
                self.wfile.write(payload)
                return

            file_path = Path(self.translate_path(parsed.path))
            if file_path.is_dir():
                file_path = file_path / "index.html"

            if file_path.exists() and file_path.suffix.lower() == ".html":
                raw = file_path.read_bytes()
                payload = inject_reload_snippet(raw)
                self.send_response(HTTPStatus.OK)
                self.send_header("Content-Type", "text/html; charset=utf-8")
                self.send_header("Content-Length", str(len(payload)))
                self.send_header("Cache-Control", "no-store")
                self.end_headers()
                self.wfile.write(payload)
                return

            super().do_GET()

        def log_message(self, format: str, *args) -> None:
            print(f"[server] {self.address_string()} - {format % args}")

    return LiveReloadHandler


def parse_args() -> argparse.Namespace:
    parser = argparse.ArgumentParser(
        description="Serve the Jekyll site locally with rebuild-on-change and live reload.",
    )
    parser.add_argument("--host", default="127.0.0.1")
    parser.add_argument("--port", default=4174, type=int)
    parser.add_argument("--build-dir", default=str(DEFAULT_BUILD_DIR))
    return parser.parse_args()


def main() -> int:
    args = parse_args()
    build_dir = Path(args.build_dir).expanduser().resolve()
    build_dir.mkdir(parents=True, exist_ok=True)
    preview_url = f"http://{args.host}:{args.port}"

    state = PreviewState()
    if not build_site(ROOT, build_dir, state, preview_url):
        return 1

    watcher = threading.Thread(
        target=watch_and_rebuild,
        args=(ROOT, build_dir, state, preview_url),
        daemon=True,
    )
    watcher.start()

    handler = make_handler(build_dir, state)
    server = ThreadingHTTPServer((args.host, args.port), handler)
    print(f"[live-preview] serving {build_dir} at http://{args.host}:{args.port}/")
    print("[live-preview] watching for changes...")
    try:
        server.serve_forever()
    except KeyboardInterrupt:
        print("\n[live-preview] shutting down...")
    finally:
        server.server_close()

    return 0


if __name__ == "__main__":
    raise SystemExit(main())
