---
permalink: /
title:
excerpt: "Postdoc at EPFL."
author_profile: true
homepage: true
redirect_from: 
  - /about/
  - /about.html
---

<div class="home-shell">
  <section class="home-hero">
    <div class="home-hero__grid">
      <div>
        <!-- <p class="home-kicker">Computer vision, mobile robotics, and spatial AI</p> -->
        <h1><span class="home-hero__line">Connecting street-level</span><span class="home-hero__line">perception with aerial views for</span><span class="home-hero__line"><span class="home-hero__accent">Spatial Intelligence</span></span></h1>
        <p class="home-hero__subhead">Incoming Tenure-track Assistant Professor (Starting August&nbsp;2026)<br>
        at Southern University of Science and Technology (<a href="https://www.sustech.edu.cn/en/">SUSTech</a>)</p>
        <p class="home-hero__notice">I am actively recruiting motivated PhD and MSc students, as well as research assistants, to work on spatial intelligence, computer vision, and robotics. If this aligns with your interests, feel free to email me at <a href="mailto:zimin.xia@epfl.ch">zimin.xia@epfl.ch</a>.</p>
        <div class="home-hero__divider"></div>
        <p class="home-hero__summary home-hero__summary--intro">
          I am Zimin Xia, a postdoctoral researcher in the <a href="https://www.epfl.ch/labs/vita/">Visual Intelligence for Transportation Lab</a> at EPFL, advised by <a href="https://people.epfl.ch/alexandre.alahi">Prof. Alexandre Alahi</a>. My research lies at the intersection of computer vision and mobile robotics, with a focus on ground-to-aerial cross-view localization, mapping, and representation learning for autonomous systems. I am particularly interested in methods that remain effective beyond tightly curated benchmarks.
        </p>
        <p class="home-hero__summary">
          Before joining EPFL, I completed my PhD at the <a href="https://intelligent-vehicles.org/">Intelligent Vehicles Group</a> at TU Delft under the supervision of <a href="https://jkooij.github.io/">Prof. Julian F. P. Kooij</a> and <a href="http://www.gavrila.net/">Prof. Dariu M. Gavrila</a>, while collaborating with the Autonomous Driving Department at TomTom in Amsterdam. Earlier, I studied Geomatics Engineering at the University of Stuttgart and Wuhan University, and spent time at Carl Zeiss.
        </p>
      </div>
    </div>
  </section>

  <section class="home-manifesto">
    <details class="home-manifesto__toggle">
      <summary class="home-manifesto__summary">
        <span class="home-manifesto__eyebrow">Vision</span>
        <span class="home-manifesto__summary-chip">
          <span class="home-manifesto__summary-closed">Read more</span>
          <span class="home-manifesto__summary-open">Hide</span>
        </span>
      </summary>
      <div class="home-manifesto__content">
        <p class="home-manifesto__lead">
          <strong>Spatial intelligence</strong>, originally conceived as a human cognitive ability, refers to the capacity to perceive the visual world accurately, to perform transformations upon one's perceptions, and to re-create aspects of one's visual experience even in the absence of relevant physical stimuli <a class="home-manifesto__cite" href="#ref-gardner">(Gardner, 2011)</a>.
        </p>
        <p>
          Extending beyond human cognition, this capability now underpins the development of <strong>Embodied AI</strong>: physical systems that integrate artificial intelligence to perceive and interact with the physical world.
        </p>
        <p>
          By instilling this distinctly human faculty of spatial intelligence into machines, we are reshaping how societies move, sense, and connect across altitudes. In <strong>ground-level transportation</strong>, spatial intelligence empowers autonomous vehicles to perceive complex urban environments, localize themselves amid dynamic traffic, and make real-time decisions that enhance safety and efficiency on our roads. Within the rapidly expanding <strong>low-altitude economy</strong>, autonomous drones rely on spatial intelligence to navigate dense environments, inspect and maintain critical infrastructure, deliver goods, and support disaster response.
        </p>
        <p>
          Together, these advances mark a paradigm shift toward embodied AI agents that extend human perception and action across all layers of the physical world.
        </p>
        <div class="home-manifesto__question">
          <span class="home-manifesto__question-label">Driven by this vision, my research asks:</span>
          <strong>How can we build unified spatial intelligence that enables embodied AI agents across altitudes to act seamlessly in the world?</strong>
        </div>
      </div>
    </details>
  </section>

  <section class="home-section home-section--research">
    <p class="home-section__eyebrow">Selected publication</p>

    <div class="home-section__bridge">
      <p>
        Jean Piaget, the Swiss psychologist who pioneered the study of children's cognitive development, observed that a key aspect of emerging spatial intelligence is the ability to coordinate spatial relationships and find one's way between different locales <a class="home-section__cite" href="#ref-piaget">(Piaget, 1957)</a>.
      </p>
      <p>
        Hence, <strong>self-localization</strong>, the task of identifying one's ego-location within an external reference frame, constitutes a fundamental problem in the development of spatial intelligence.
      </p>
    </div>
    <div class="paper-grid">
      <article class="paper-card">
        <div class="paper-card__media">
          <div class="paper-card__meta">
            <span class="paper-chip">ICLR 2026</span>
          </div>
          <img src="{{ '/images/Loc2.png' | relative_url }}" alt="Overview figure from Loc squared">
          <p class="paper-card__authors"><span class="paper-card__author-self">Zimin Xia*</span>, Chenghao Xu*, Alexandre Alahi</p>
          <p class="paper-card__note">* Equal contribution</p>
          <div class="paper-card__links">
            <a href="https://arxiv.org/abs/2509.09792">Paper</a>
            <a href="https://github.com/vita-epfl/Loc2/tree/main">Code</a>
            <a href="https://iclr.cc/virtual/2026/poster/10011719">Video</a>
          </div>
        </div>
        <div class="paper-card__body">
          <h3>Loc<sup>2</sup>: Interpretable Cross-View Localization via Depth-Lifted Local Feature Matching</h3>
          <p class="paper-card__summary">Learns interpretable ground-to-aerial correspondences, lifts them with monocular depth, and estimates pose through scale-aware alignment.</p>
        </div>
      </article>

      <article class="paper-card">
        <div class="paper-card__media">
          <div class="paper-card__meta">
            <span class="paper-chip">CVPR 2025</span>
          </div>
          <img src="{{ '/images/FG2.png' | relative_url }}" alt="Overview figure from FG2">
          <p class="paper-card__authors"><span class="paper-card__author-self">Zimin Xia</span>, Alexandre Alahi</p>
          <div class="paper-card__links">
            <a href="https://arxiv.org/abs/2503.18725">Paper</a>
            <a href="https://github.com/vita-epfl/FG2">Code</a>
            <a href="https://www.youtube.com/watch?v=GStVKsoLDl4">Video</a>
          </div>
        </div>
        <div class="paper-card__body">
          <h3>FG<sup>2</sup>: Fine-Grained Cross-View Localization by Fine-Grained Feature Matching</h3>
          <p class="paper-card__summary">Pushes cross-view localization toward fine-grained pixel correspondences between ground-level perception and aerial imagery.</p>
        </div>
      </article>

      <article class="paper-card">
        <div class="paper-card__media">
          <div class="paper-card__meta">
            <span class="paper-chip">ECCV 2024</span>
          </div>
          <img src="{{ '/images/Adapting_CVM.png' | relative_url }}" alt="Overview figure from Adapting Fine-Grained Cross-View Localization">
          <p class="paper-card__authors"><span class="paper-card__author-self">Zimin Xia</span>, Yujiao Shi, Hongdong Li, Julian F. P. Kooij</p>
          <div class="paper-card__links">
            <a href="http://arxiv.org/abs/2406.00474">Paper</a>
            <a href="https://github.com/tudelft-iv/Adapting_CVL">Code</a>
            <a href="https://www.youtube.com/watch?v=U9njuEIdVL8">Video</a>
          </div>
        </div>
        <div class="paper-card__body">
          <h3>Adapting Fine-Grained Cross-View Localization to Areas without Fine Ground Truth</h3>
          <p class="paper-card__summary">Adapts fine-grained cross-view localization to regions where accurate localization labels are unavailable.</p>
        </div>
      </article>

      <article class="paper-card">
        <div class="paper-card__media">
          <div class="paper-card__meta">
            <span class="paper-chip">T-PAMI 2023</span>
          </div>
          <img src="{{ '/images/CCVPE.jpg' | relative_url }}" alt="Overview figure from Convolutional Cross-View Pose Estimation">
          <p class="paper-card__authors"><span class="paper-card__author-self">Zimin Xia</span>, Olaf Booij, Julian F. P. Kooij</p>
          <div class="paper-card__links">
            <a href="https://ieeexplore.ieee.org/document/10373898">Paper</a>
            <a href="https://github.com/tudelft-iv/CCVPE">Code</a>
          </div>
        </div>
        <div class="paper-card__body">
          <h3>Convolutional Cross-View Pose Estimation</h3>
          <p class="paper-card__summary">Formulates cross-view pose estimation with convolutional feature matching and spatial reasoning, turning dense ground-to-aerial evidence into a structured estimate of camera pose.</p>
        </div>
      </article>

      <article class="paper-card">
        <div class="paper-card__media">
          <div class="paper-card__meta">
            <span class="paper-chip">CVPR 2023</span>
          </div>
          <img src="{{ '/images/SliceMatch.jpg' | relative_url }}" alt="Overview figure from SliceMatch">
          <p class="paper-card__authors">Ted Lentsch*, <span class="paper-card__author-self">Zimin Xia*</span>, Holger Caesar, Julian F. P. Kooij</p>
          <p class="paper-card__note">* Equal contribution</p>
          <div class="paper-card__links">
            <a href="https://openaccess.thecvf.com/content/CVPR2023/html/Lentsch_SliceMatch_Geometry-Guided_Aggregation_for_Cross-View_Pose_Estimation_CVPR_2023_paper.html">Paper</a>
            <a href="https://github.com/tudelft-iv/SliceMatch">Code</a>
            <a href="https://www.youtube.com/watch?v=gql1dkQQNrA">Video</a>
          </div>
        </div>
        <div class="paper-card__body">
          <h3>SliceMatch: Geometry-guided Aggregation for Cross-View Pose Estimation</h3>
          <p class="paper-card__summary">Introduces geometry-guided aggregation to better align ground and aerial evidence for pose estimation.</p>
          <p class="paper-card__summary">Slice-specific cross-view attention and precomputed aerial slice masks allow the model to build pose-dependent descriptors efficiently, improving localization accuracy while keeping inference efficient.</p>
        </div>
      </article>

      <article class="paper-card">
        <div class="paper-card__media">
          <div class="paper-card__meta">
            <span class="paper-chip">ECCV 2022</span>
          </div>
          <img src="{{ '/images/ECCV22.jpg' | relative_url }}" alt="Overview figure from Visual cross-view metric localization with dense uncertainty estimates">
          <p class="paper-card__authors"><span class="paper-card__author-self">Zimin Xia</span>, Olaf Booij, Marco Manfredi, Julian F. P. Kooij</p>
          <div class="paper-card__links">
            <a href="https://link.springer.com/chapter/10.1007/978-3-031-19842-7_6">Paper</a>
            <a href="https://github.com/tudelft-iv/CrossViewMetricLocalization">Code</a>
            <a href="https://www.youtube.com/watch?v=BnVEk-Mp0xU">Video</a>
          </div>
        </div>
        <div class="paper-card__body">
          <h3>Visual Cross-View Metric Localization with Dense Uncertainty Estimates</h3>
          <p class="paper-card__summary">Models dense uncertainty to improve metric localization when cross-view evidence is ambiguous or noisy.</p>
        </div>
      </article>

      <article class="paper-card">
        <div class="paper-card__media">
          <div class="paper-card__meta">
            <span class="paper-chip">IEEE RA-L 2021</span>
          </div>
          <img src="{{ '/images/RAL21.PNG' | relative_url }}" alt="Overview figure from Cross-view matching for vehicle localization">
          <p class="paper-card__authors"><span class="paper-card__author-self">Zimin Xia</span>, Olaf Booij, Marco Manfredi, Julian F. P. Kooij</p>
          <div class="paper-card__links">
            <a href="https://ieeexplore.ieee.org/abstract/document/9449965">Paper</a>
            <a href="https://github.com/tudelft-iv/Visual-Localization-with-Spatial-Prior">Code</a>
            <a href="https://www.youtube.com/watch?v=s0uoswTOVG8">Video</a>
          </div>
        </div>
        <div class="paper-card__body">
          <h3>Cross-View Matching for Vehicle Localization by Learning Geographically Local Representations</h3>
          <p class="paper-card__summary">Learns geographically local features to improve localization by embedding a spatial prior into the representation.</p>
        </div>
      </article>

      <article class="paper-card">
        <div class="paper-card__media">
          <div class="paper-card__meta">
            <span class="paper-chip">ECCV Workshop 2020</span>
          </div>
          <img src="{{ '/images/ECCVW20.png' | relative_url }}" alt="Overview figure from geographically local representation learning">
          <p class="paper-card__authors"><span class="paper-card__author-self">Zimin Xia</span>, Olaf Booij, Marco Manfredi, Julian F. P. Kooij</p>
          <div class="paper-card__links">
            <a href="https://link.springer.com/chapter/10.1007/978-3-030-66096-3_38">Paper</a>
            <a href="https://github.com/tudelft-iv/Visual-Localization-with-Spatial-Prior">Code</a>
            <a href="https://www.youtube.com/watch?v=4ii0ALys6cY&t=4331s">Video</a>
          </div>
        </div>
        <div class="paper-card__body">
          <h3>Geographically Local Representation Learning with a Spatial Prior for Visual Localization</h3>
          <p class="paper-card__summary">An early step toward learning location-aware representations that remain grounded in geographic structure.</p>
        </div>
      </article>
    </div>
    <div class="home-section__footer">
      <p class="home-note">For a full list, please visit my Google Scholar.</p>
      <a class="home-btn home-btn--ghost" href="{{ site.author.googlescholar }}">View Google Scholar</a>
    </div>
  </section>

  <section class="home-talks">
    <p class="home-section__eyebrow">Invited talk</p>
    <article class="talk-card">
      <div class="talk-card__meta">
        <span class="paper-chip">WACV 2026 Tutorial</span>
        <span class="talk-card__date">March 7, 2026</span>
      </div>
      <h3>From Retrieval to Precision: Fine-Grained Cross-View Geo-Localization</h3>
      <p class="talk-card__summary">Invited speaker for the tutorial <em>Beyond Vision: Multimodal Perspectives for Cross-View Geo-Localization</em> at WACV 2026.</p>
      <div class="talk-card__links">
        <a href="https://zxh009123.github.io/WACV26_CVGL_Tutorial/">Tutorial page</a>
      </div>
    </article>
  </section>

  <section class="home-references">
    <p class="home-section__eyebrow">References</p>
    <ol class="home-reference-list">
      <li id="ref-gardner">
        Howard Gardner. <em><a href="https://books.google.com/books/about/Frames_of_Mind.html?id=wxj6npSaykgC">Frames of Mind: The Theory of Multiple Intelligences</a></em>. Basic Books, 2011.
      </li>
      <li id="ref-piaget">
        Jean Piaget, Baerbel Inhelder, F. J. Langdon, and J. L. Lunzer. "The Child's Conception of Space." <em>British Journal of Educational Studies</em> 5.2 (1957), pp. 187-189. <a href="https://doi.org/10.2307/3118882">DOI: 10.2307/3118882</a>.
      </li>
    </ol>
  </section>

</div>
