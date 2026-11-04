---
layout: default
title: Your TV Friend | Zvirox
description: A non-destructive Android TV cleanup tool and Your UI, a native television launcher, with reversible ADB-based package controls.
permalink: /projects/ytf/
---

<div class="zv-container">

  <article class="zv-post zv-project-page">
    <a class="zv-project-back" href="{{ '/projects/' | relative_url }}">&larr; All projects</a>

    <section class="zv-project-hero" aria-labelledby="project-title">
      <header class="zv-project-intro">
        <h1 class="zv-post-title" id="project-title">Your TV Friend</h1>
        <p class="zv-post-description">A non-destructive Android TV cleanup tool and a native television launcher. The project combines reversible ADB-based debloating tools with Your UI, a customizable launcher for Android TV.</p>
        <p class="zv-project-status">Android TV · Cleanup tools and launcher</p>
        <div class="zv-project-tags" aria-label="Technologies"><span class="zv-tag">Java</span> <span class="zv-tag">Android TV</span> <span class="zv-tag">ADB</span> <span class="zv-tag">Python</span> <span class="zv-tag">Android</span></div>
        <div class="zv-project-actions">
          <a href="https://github.com/zvirox/your-tv-friend" target="_blank" rel="noopener noreferrer" class="zv-button zv-button-primary">View on GitHub <span aria-hidden="true">↗</span></a>
          <a href="{{ '/projects/' | relative_url }}" class="zv-project-text-link">Explore all projects <span aria-hidden="true">&rarr;</span></a>
        </div>
      </header>
            <figure class="zv-project-visual">
        <img class="zv-project-image" src="{{ '/assets/images/projects/your-tv-friend-mockup.png' | relative_url }}" alt="Your TV Friend Your UI concept screen with For You recommendations, five round glass controls, and a translucent app shelf over a cinematic landscape." decoding="async">
        <figcaption class="zv-project-caption">Concept mockup inspired by Your UI's Glass UI home-screen layout.</figcaption>
      </figure>
    </section>

    <div class="zv-post-content zv-project-content">
      <h2>Overview</h2>
      <p>
        <strong>Your TV Friend</strong> is an open-source Android TV project with two parts: non-destructive,
        reversible cleanup tools and <strong>Your UI</strong>, a native television launcher for Android 8.0 and newer.
      </p>

      <h2>Two Core Components</h2>
      
      <h3>1. Non-Destructive Debloater</h3>
      <p>
        The debloating tools avoid deleting system files. They operate
        via a pure-Python ADB client using Android's native package manager:
      </p>
      <ul>
        <li>Uses <code>pm disable-user --user 0</code> to safely disable telemetry, bloatware, and unwanted vendor applications.</li>
        <li><strong>Fully Reversible:</strong> Disabled packages can be restored at any time without factory resetting the television.</li>
        <li>No root access required; communicates directly over local network ADB or USB.</li>
      </ul>

      <h3>2. Your UI Launcher</h3>
      <p>
        A fast, native TV launcher written in clean Java, providing five selectable visual styles:
      </p>
      <ul>
        <li><strong>Glass UI:</strong> Sleek translucent tiles and modern blur effects.</li>
        <li><strong>Material 3 Expressive:</strong> Contemporary Android design language with dynamic color accents.</li>
        <li><strong>Win UI:</strong> Clean grid layout inspired by modern desktop interfaces.</li>
        <li><strong>Cyberpunk:</strong> High-contrast neon accents and futuristic styling.</li>
        <li><strong>Retro UI:</strong> Classic 80s/90s aesthetic with pixelated typography and nostalgic styling.</li>
      </ul>

      <h2>Integrated TV Features</h2>
      <ul>
        <li><strong>Media Recommendations:</strong> TMDB-powered trending movies and shows right on the home screen.</li>
        <li><strong>Weather & Utility:</strong> Open-Meteo live weather forecasts and customizable widgets.</li>
        <li><strong>Screensaver & Sleep Timer:</strong> Photo screensaver with automatic sleep scheduling.</li>
        <li><strong>Localization:</strong> Multilingual support covering 26 languages out of the box.</li>
      </ul>

      <h2>Safety & Device Compatibility</h2>
      <p>
        Your UI supports televisions and streaming boxes running Android 8.0 and newer. Because television
        hardware and manufacturer firmware modifications vary significantly between brands, users should exercise care 
        and consult the project's documentation before disabling system packages.
      </p>

      <h2>Resources & Links</h2>
      <ul>
        <li>Repository: <a href="https://github.com/zvirox/your-tv-friend" target="_blank" rel="noopener noreferrer">GitHub Repository</a></li>
        <li>Releases & APKs: Available via GitHub Releases for manual sideloading.</li>
      </ul>
    </div>

    <nav class="zv-project-navigation" aria-label="Project navigation">
      <a href="{{ '/projects/alp/' | relative_url }}" class="zv-section-link">
        &larr; Previous: Audio Labs Pro
      </a>
      <a href="{{ '/projects/' | relative_url }}" class="zv-section-link">
        Back to Projects Index &rarr;
      </a>
    </nav>

  </article>


</div>
