---
layout: default
title: Screen Studio Pro | Zvirox
description: A planned open-source Wayland screen recorder for Linux, with PipeWire capture, webcam picture-in-picture, and hardware-first encoding.
permalink: /projects/ssp/
---

<div class="zv-container">

  <article class="zv-post zv-project-page">
    <a class="zv-project-back" href="{{ '/projects/' | relative_url }}">&larr; All projects</a>

    <section class="zv-project-hero" aria-labelledby="project-title">
      <header class="zv-project-intro">
        <h1 class="zv-post-title" id="project-title">Screen Studio Pro</h1>
        <p class="zv-post-description">A modern, open-source screen recorder for Linux: a frosted-glass alternative to OBS, designed for Wayland desktops.</p>
        <p class="zv-project-status">Linux screen recorder · Planning phase</p>
        <div class="zv-project-tags" aria-label="Technologies"><span class="zv-tag">Linux</span> <span class="zv-tag">Wayland</span> <span class="zv-tag">Rust</span> <span class="zv-tag">Tauri 2</span> <span class="zv-tag">React</span> <span class="zv-tag">PipeWire</span></div>
        <div class="zv-project-actions">
          <a href="https://github.com/zvirox/screen-studio-pro" target="_blank" rel="noopener noreferrer" class="zv-button zv-button-primary">View on GitHub <span aria-hidden="true">↗</span></a>
          <a href="{{ '/projects/' | relative_url }}" class="zv-project-text-link">Explore all projects <span aria-hidden="true">&rarr;</span></a>
        </div>
      </header>
            <figure class="zv-project-visual">
        <img class="zv-project-image" src="{{ '/assets/images/projects/screen-studio-pro-mockup.png' | relative_url }}" alt="Screen Studio Pro concept capture window with monitor, window, and region sources, microphone and system audio meters, a webcam preview, encoding settings, and floating recording controls." width="1668" height="938" decoding="async">
        <figcaption class="zv-project-caption">Concept mockup based on Screen Studio Pro's planned Wayland recording workflow.</figcaption>
      </figure>
    </section>

    <div class="zv-post-content zv-project-content">
      <h2>Overview</h2>
      <p>
        <strong>Screen Studio Pro</strong> is a planned Linux screen recorder for Wayland desktops, including Hyprland,
        niri, MangoWC, and KDE. Its product direction pairs native capture with a polished frosted-glass interface.
        The repository currently contains the product specifications; application code and a runnable build do not exist yet.
      </p>

      <h2>Planned MVP Features</h2>
      <ul>
        <li><strong>Screen capture:</strong> Monitor, window, and region recording through xdg-desktop-portal and PipeWire.</li>
        <li><strong>Audio and webcam:</strong> Microphone and desktop audio controls, plus draggable webcam picture-in-picture.</li>
        <li><strong>Recording controls:</strong> A floating HUD for recording, pause, resume, markers, and stop.</li>
        <li><strong>Encoding:</strong> Prefer VAAPI or NVENC hardware encoding, with x264 fallback and a visible notice.</li>
        <li><strong>Safer recordings:</strong> Record to MKV and remux to MP4 on stop, so an interrupted recording keeps its file.</li>
        <li><strong>Local library:</strong> Browse past recordings and their duration, size, and encoder details.</li>
      </ul>

      <h2>Technology Direction</h2>
      <p>
        The planned desktop app uses a Rust capture and encoding core, Tauri 2, and a React with TypeScript interface.
        PipeWire and portals handle Wayland capture; SQLite stores a local recording library. The repository states that
        the app will have no server, HTTP APIs, or telemetry.
      </p>

      <h2>Current Status</h2>
      <p>
        The project is in the planning phase. Its product brief, design system, architecture, database schema, and API
        contract are specified, and implementation is planned to begin with the approved MVP milestone plan. There is
        currently no buildable application or available release.
      </p>

      <h2>Resources & Links</h2>
      <ul>
        <li>Repository: <a href="https://github.com/zvirox/screen-studio-pro" target="_blank" rel="noopener noreferrer">Screen Studio Pro on GitHub</a></li>
        <li>Specifications: See the repository's PRD, design, and architecture documents.</li>
      </ul>
    </div>

    <nav class="zv-project-navigation" aria-label="Project navigation">
      <a href="{{ '/projects/' | relative_url }}" class="zv-section-link">
        Back to Projects Index &rarr;
      </a>
    </nav>

  </article>


</div>
