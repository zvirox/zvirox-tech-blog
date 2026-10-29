---
layout: default
title: Climin TV Friend | Zvirox
description: A non-destructive Android TV cleanup toolkit and native television launcher. Combines ADB-based package disabling tools with Climin UI.
permalink: /projects/cft/
---

<div class="zv-container">

  <article class="zv-post" style="max-width: 960px; margin: 0 auto;">

    <!-- Breadcrumb -->
    <div style="margin-bottom: 24px; color: var(--zv-text-muted); font-size: 14px;">
      <a href="{{ '/' | relative_url }}" style="color: var(--zv-text-secondary);">Home</a> &rarr; 
      <a href="{{ '/projects/' | relative_url }}" style="color: var(--zv-text-secondary);">Projects</a> &rarr; 
      <span style="color: var(--zv-text);">Climin TV Friend</span>
    </div>

    <!-- Header -->
    <header class="zv-post-header" style="margin-bottom: 40px;">
      <div class="zv-card-category">
        ANDROID TV • CLEANUP & LAUNCHER
      </div>

      <h1 class="zv-post-title">
        Climin TV Friend
      </h1>

      <p class="zv-post-description">
        A non-destructive Android TV cleanup toolkit and native television launcher. The project combines 
        ADB-based debloat and restoration tools with Climin UI, a customizable launcher for Android TV.
      </p>

      <div style="margin: 20px 0; display: flex; flex-wrap: wrap; gap: 8px;">
        <span class="zv-tag">Java</span>
        <span class="zv-tag">Android TV</span>
        <span class="zv-tag">ADB</span>
        <span class="zv-tag">Python</span>
        <span class="zv-tag">Android</span>
      </div>

      <div class="zv-post-meta" style="margin-top: 20px; display: flex; gap: 16px; align-items: center;">
        <a href="https://github.com/zvirox/climin-tv-friend" target="_blank" rel="noopener noreferrer" class="zv-button zv-button-primary" style="min-height: 38px; padding: 0 16px; font-size: 13px;">
          View on GitHub ↗
        </a>
        <a href="{{ '/projects/' | relative_url }}" class="zv-button zv-button-secondary" style="min-height: 38px; padding: 0 16px; font-size: 13px;">
          &larr; Back to Projects
        </a>
      </div>
    </header>


    <!-- Content -->
    <div class="zv-post-content">

      <h2>Overview</h2>
      <p>
        <strong>Climin TV Friend</strong> is an open-source utility designed to give users complete control over their 
        Android TV experience. It pairs a non-destructive cleanup subsystem with <strong>Climin UI</strong>, a lightweight, 
        customizable, ad-free television launcher designed for Android 8.0 through 14.
      </p>

      <h2>Two Core Components</h2>
      
      <h3>1. Non-Destructive Debloater</h3>
      <p>
        Unlike risky scripts that attempt to forcibly delete system files, Climin TV Friend's debloating tools operate 
        via a pure-Python ADB client using Android's native package manager:
      </p>
      <ul>
        <li>Uses <code>pm disable-user --user 0</code> to safely disable telemetry, bloatware, and unwanted vendor applications.</li>
        <li><strong>Fully Reversible:</strong> Disabled packages can be restored at any time without factory resetting the television.</li>
        <li>No root access required; communicates directly over local network ADB or USB.</li>
      </ul>

      <h3>2. Climin UI Launcher</h3>
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
        Climin UI supports televisions and streaming boxes running Android 8.0 through Android 14. Because television 
        hardware and manufacturer firmware modifications vary significantly between brands, users should exercise care 
        and consult the project's documentation before disabling system packages.
      </p>

      <h2>Resources & Links</h2>
      <ul>
        <li>Repository: <a href="https://github.com/zvirox/climin-tv-friend" target="_blank" rel="noopener noreferrer">GitHub Repository</a></li>
        <li>Releases & APKs: Available via GitHub Releases for manual sideloading.</li>
      </ul>

    </div>

    <!-- Navigation Footer -->
    <div style="margin-top: 60px; padding-top: 30px; border-top: 1px solid var(--zv-border); display: flex; justify-content: space-between; align-items: center;">
      <a href="{{ '/projects/alp/' | relative_url }}" class="zv-section-link">
        &larr; Previous: Audio Labs Pro
      </a>
      <a href="{{ '/projects/' | relative_url }}" class="zv-section-link">
        Back to Projects Index &rarr;
      </a>
    </div>

  </article>

</div>
