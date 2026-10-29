---
layout: default
title: Projects | Zvirox
description: Explore the software projects built and maintained across desktop applications, audio production, and Android TV. Built with curiosity and shaped by code.
permalink: /projects/
---

<div class="zv-container">

  <!-- =====================================================
       HERO SECTION
       ===================================================== -->

  <section class="zv-about-hero">
    
    <div class="zv-about-hero-content">
      
      <div class="zv-card-category">
        PORTFOLIO • OPEN SOURCE
      </div>

      <h1 class="zv-about-hero-title">
        Projects.
        <span>Built with code.</span>
      </h1>

      <p class="zv-about-hero-lead">
        Explore the software projects I'm building and maintaining across desktop 
        applications, audio production, and Android TV. Each project brings together 
        practical engineering, thoughtful design, and a commitment to open-source development.
      </p>

    </div>

  </section>


  <!-- =====================================================
       PROJECTS GRID
       ===================================================== -->

  <section class="zv-section">
    
    <div class="zv-section-header">
      <h2 class="zv-section-title">
        Featured Projects
      </h2>
    </div>

    <div class="zv-article-grid" style="grid-template-columns: repeat(3, minmax(0, 1fr));">

      <!-- Easy Edits Pro -->
      <article class="zv-card">
        <div class="zv-card-body" style="display: flex; flex-direction: column; height: 100%;">
          <div class="zv-card-category">
            DESKTOP VIDEO EDITOR • ACTIVE ALPHA
          </div>
          <h3 class="zv-card-title">
            <a href="{{ '/projects/eep/' | relative_url }}">Easy Edits Pro</a>
          </h3>
          <p class="zv-card-excerpt" style="flex-grow: 1;">
            An alpha-stage Linux desktop video editor built with Rust, Tauri, React, and GStreamer. 
            It combines a multitrack editing workflow with a Rust-owned project model and automation interfaces.
          </p>
          <div style="margin-bottom: 16px; display: flex; flex-wrap: wrap; gap: 6px;">
            <span class="zv-tag">Rust</span>
            <span class="zv-tag">Tauri</span>
            <span class="zv-tag">React</span>
            <span class="zv-tag">GStreamer</span>
            <span class="zv-tag">Linux</span>
          </div>
          <div style="display: flex; align-items: center; justify-content: space-between; pt-12; border-top: 1px solid var(--zv-border);">
            <a href="{{ '/projects/eep/' | relative_url }}" class="zv-section-link">
              Explore Project →
            </a>
            <a href="https://github.com/zvirox/easy-edits-pro" target="_blank" rel="noopener noreferrer" style="color: var(--zv-text-muted); font-size: 13px; font-weight: 600;">
              GitHub ↗
            </a>
          </div>
        </div>
      </article>


      <!-- Audio Labs Pro -->
      <article class="zv-card">
        <div class="zv-card-body" style="display: flex; flex-direction: column; height: 100%;">
          <div class="zv-card-category">
            AUDIO WORKSTATION • ALPHA v0.0.1
          </div>
          <h3 class="zv-card-title">
            <a href="{{ '/projects/alp/' | relative_url }}">Audio Labs Pro</a>
          </h3>
          <p class="zv-card-excerpt" style="flex-grow: 1;">
            A Linux audio studio built with Rust for multitrack recording, editing, mixing, and export, 
            with offline AI voice tools, dictation, voice profiles, and CLAP/LV2 plugin hosting.
          </p>
          <div style="margin-bottom: 16px; display: flex; flex-wrap: wrap; gap: 6px;">
            <span class="zv-tag">Rust</span>
            <span class="zv-tag">Linux</span>
            <span class="zv-tag">Iced</span>
            <span class="zv-tag">Audio DSP</span>
            <span class="zv-tag">Local AI</span>
          </div>
          <div style="display: flex; align-items: center; justify-content: space-between; pt-12; border-top: 1px solid var(--zv-border);">
            <a href="{{ '/projects/alp/' | relative_url }}" class="zv-section-link">
              Explore Project →
            </a>
            <a href="https://github.com/zvirox/audio-labs-pro" target="_blank" rel="noopener noreferrer" style="color: var(--zv-text-muted); font-size: 13px; font-weight: 600;">
              GitHub ↗
            </a>
          </div>
        </div>
      </article>


      <!-- Climin TV Friend -->
      <article class="zv-card">
        <div class="zv-card-body" style="display: flex; flex-direction: column; height: 100%;">
          <div class="zv-card-category">
            ANDROID TV • CLEANUP & LAUNCHER
          </div>
          <h3 class="zv-card-title">
            <a href="{{ '/projects/cft/' | relative_url }}">Climin TV Friend</a>
          </h3>
          <p class="zv-card-excerpt" style="flex-grow: 1;">
            A non-destructive Android TV cleanup toolkit and native television launcher (Climin UI). 
            Combines ADB-based package disabling tools with 5 customizable launcher visual styles.
          </p>
          <div style="margin-bottom: 16px; display: flex; flex-wrap: wrap; gap: 6px;">
            <span class="zv-tag">Java</span>
            <span class="zv-tag">Android TV</span>
            <span class="zv-tag">ADB</span>
            <span class="zv-tag">Python</span>
            <span class="zv-tag">Android</span>
          </div>
          <div style="display: flex; align-items: center; justify-content: space-between; pt-12; border-top: 1px solid var(--zv-border);">
            <a href="{{ '/projects/cft/' | relative_url }}" class="zv-section-link">
              Explore Project →
            </a>
            <a href="https://github.com/zvirox/climin-tv-friend" target="_blank" rel="noopener noreferrer" style="color: var(--zv-text-muted); font-size: 13px; font-weight: 600;">
              GitHub ↗
            </a>
          </div>
        </div>
      </article>

    </div>

  </section>

</div>
