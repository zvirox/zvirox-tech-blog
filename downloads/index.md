---
layout: default
title: "Downloads | Open-Source Software Releases"
description: "Download verified, privacy-first open source releases of Easy Edits Pro, Audio Labs Pro, Screen Studio Pro, and Your TV Friend directly from official GitHub releases."
permalink: /downloads/
---

<div class="zv-container zv-page-container">

  <!-- Header Section -->
  <header class="zv-downloads-hero">
    <div class="zv-card-category">OFFICIAL BINARIES &bull; PRIVACY FIRST</div>
    <h1 class="zv-downloads-title">Software Downloads</h1>
    <p class="zv-downloads-subtitle">
      Direct Linux and Android installers compiled from audited open-source source trees.
      Zero telemetry, no browser-side tracking, and authoritative SHA-256 checksums hosted transparently on GitHub Releases.
    </p>

    <!-- Quick Jump Anchor Bar -->
    <nav class="zv-downloads-nav-pills" aria-label="Jump to project downloads">
      <a href="#eep" class="zv-nav-pill">Easy Edits Pro</a>
      <a href="#alp" class="zv-nav-pill">Audio Labs Pro</a>
      <a href="#ssp" class="zv-nav-pill">Screen Studio Pro</a>
      <a href="#ytf" class="zv-nav-pill">Your TV Friend</a>
    </nav>
  </header>

  <!-- Product Sections -->
  <div class="zv-downloads-list">
    {% for product in site.data.download_products %}
      {% assign manifest_proj = nil %}
      {% for proj in site.data.release_manifest.projects %}
        {% if proj.id == product.id %}
          {% assign manifest_proj = proj %}
        {% endif %}
      {% endfor %}

      {% include downloads/project-section.html product=product manifest_proj=manifest_proj %}
    {% endfor %}
  </div>

  <!-- Security & Integrity Guidance -->
  <aside class="zv-integrity-card">
    <div class="zv-integrity-header">
      <svg width="24" height="24" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2" class="zv-integrity-icon"><path d="M12 22s8-4 8-10V5l-8-3-8 3v7c0 6 8 10 8 10z"/></svg>
      <div>
        <h3 class="zv-integrity-title">Cryptographic Integrity &amp; Verification</h3>
        <p class="zv-integrity-sub">Every installer can be independently verified on your local terminal prior to execution.</p>
      </div>
    </div>
    <div class="zv-integrity-body">
      <div class="zv-integrity-step">
        <span class="zv-step-number">1</span>
        <div>
          <strong>Check SHA-256 Hash</strong>
          <p>Run <code>sha256sum &lt;downloaded-file&gt;</code> in your terminal and compare it against the checksum displayed under the asset card.</p>
        </div>
      </div>
      <div class="zv-integrity-step">
        <span class="zv-step-number">2</span>
        <div>
          <strong>Air-Gapped Source Audit</strong>
          <p>Every repository includes automated reproducible GitHub Actions release workflows with open git commit histories.</p>
        </div>
      </div>
    </div>
  </aside>

</div>
