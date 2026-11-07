---
layout: default
title: Screen Studio Pro | Zvirox
description: A planned open-source Wayland screen recorder for Linux, with PipeWire capture, webcam picture-in-picture, and hardware-first encoding.
permalink: /projects/ssp/
image: "/assets/images/projects/screen-studio-pro-mockup.png"
---

<script type="application/ld+json">
{
  "@context": "https://schema.org",
  "@type": "SoftwareApplication",
  "name": "Screen Studio Pro",
  "operatingSystem": "Linux",
  "applicationCategory": "MultimediaApplication",
  "description": "A planned open-source Wayland screen recorder for Linux, with PipeWire capture, webcam picture-in-picture, and hardware-first encoding.",
  "url": "https://zvirox.in/projects/ssp/",
  "downloadUrl": "https://github.com/zvirox/screen-studio-pro",
  "license": "https://opensource.org/licenses/MIT",
  "author": {
    "@type": "Person",
    "name": "Prakashpuri Gauswami",
    "url": "https://zvirox.in/about/"
  }
}
</script>

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
        <img class="zv-project-image" src="{{ '/assets/images/projects/screen-studio-pro-mockup.png' | relative_url }}" alt="Screen Studio Pro concept capture window with monitor, window, and region sources, microphone and system audio meters, a webcam preview, encoding settings, and floating recording controls." width="1200" height="675" loading="lazy" decoding="async">
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

      <h2>Technology Direction & Capture Architecture</h2>
      <p>
        Screen Studio Pro bypasses traditional capture bottlenecks by utilizing Wayland's zero-copy DMA-BUF memory sharing and PipeWire media routing:
      </p>

      <!-- Architecture Teardown Diagram -->
      <div class="zv-teardown-schematic" aria-label="Screen Studio Pro Architecture Teardown">
        <div class="zv-teardown-header">
          <div class="zv-teardown-title-wrap">
            <span class="zv-teardown-category">WAYLAND CAPTURE TEARDOWN</span>
            <span class="zv-teardown-subtitle">xdg-desktop-portal · PipeWire DMA-BUF · Rust Crash-Safe Remux</span>
          </div>
          <span class="zv-teardown-shield">🔒 ZERO CLOUD LEAK</span>
        </div>
        <div class="zv-teardown-body">
          <svg class="zv-teardown-svg" viewBox="0 0 840 380" fill="none" xmlns="http://www.w3.org/2000/svg">
            <!-- Column 1: Wayland Compositor & Audio Sources -->
            <rect x="20" y="20" width="220" height="290" rx="8" fill="#140f13" stroke="#ef4444" stroke-opacity="0.4" stroke-width="1.5"/>
            <rect x="20" y="20" width="220" height="34" rx="8" fill="#20141a"/>
            <text x="130" y="42" font-family="'Liberation Mono', monospace" font-size="11" font-weight="700" fill="#fca5a5" text-anchor="middle">1. WAYLAND DESKTOP</text>
            
            <rect x="35" y="70" width="190" height="52" rx="5" fill="#24141c" stroke="#334155" stroke-width="1"/>
            <text x="45" y="90" font-family="'Liberation Sans', sans-serif" font-size="12" font-weight="700" fill="#ffffff">Compositor Surfaces</text>
            <text x="45" y="106" font-family="'Liberation Mono', monospace" font-size="10" fill="#f87171">Hyprland · KDE · Mutter · niri</text>
            <text x="45" y="117" font-family="'Liberation Mono', monospace" font-size="9" fill="#94a3b8">Screen · Window · Region</text>

            <rect x="35" y="132" width="190" height="56" rx="5" fill="#24141c" stroke="#334155" stroke-width="1"/>
            <text x="45" y="152" font-family="'Liberation Sans', sans-serif" font-size="12" font-weight="700" fill="#ffffff">Audio Routing</text>
            <text x="45" y="168" font-family="'Liberation Mono', monospace" font-size="10" fill="#38bdf8">PipeWire Loopback Node</text>
            <text x="45" y="181" font-family="'Liberation Mono', monospace" font-size="9" fill="#94a3b8">System Audio + Microphone sync</text>

            <rect x="35" y="198" width="190" height="54" rx="5" fill="#24141c" stroke="#334155" stroke-width="1"/>
            <text x="45" y="218" font-family="'Liberation Sans', sans-serif" font-size="12" font-weight="700" fill="#ffffff">Webcam Stream</text>
            <text x="45" y="234" font-family="'Liberation Mono', monospace" font-size="10" fill="#34d399">V4L2 / PipeWire video feed</text>
            <text x="45" y="246" font-family="'Liberation Mono', monospace" font-size="9" fill="#94a3b8">Circular PiP overlay with blur</text>

            <rect x="35" y="262" width="190" height="34" rx="5" fill="#1a1117" stroke="rgba(239,68,68,0.3)" stroke-width="1"/>
            <text x="130" y="284" font-family="'Liberation Mono', monospace" font-size="10" fill="#fca5a5" text-anchor="middle">xdg-desktop-portal ScreenCast</text>

            <!-- Arrow 1 -> 2: DMA-BUF Memory Sharing -->
            <path d="M 240,150 L 290,150" stroke="#ef4444" stroke-width="2"/>
            <polygon points="295,150 285,145 285,155" fill="#ef4444"/>
            <text x="267" y="140" font-family="'Liberation Mono', monospace" font-size="9" fill="#ef4444" text-anchor="middle">DMA-BUF</text>
            <text x="267" y="170" font-family="'Liberation Mono', monospace" font-size="8.5" fill="#94a3b8" text-anchor="middle">Zero-Copy</text>

            <!-- Column 2: Rust Recording Core -->
            <rect x="295" y="20" width="250" height="290" rx="8" fill="#141118" stroke="#ef4444" stroke-opacity="0.6" stroke-width="1.8"/>
            <rect x="295" y="20" width="250" height="34" rx="8" fill="#221524"/>
            <text x="420" y="42" font-family="'Liberation Mono', monospace" font-size="11" font-weight="700" fill="#ffffff" text-anchor="middle">2. RUST RECORDING CORE</text>

            <rect x="310" y="70" width="220" height="66" rx="5" fill="#1f182b" stroke="#a855f7" stroke-opacity="0.4" stroke-width="1"/>
            <text x="320" y="90" font-family="'Liberation Sans', sans-serif" font-size="12" font-weight="700" fill="#ffffff">Smooth Cursor &amp; Auto-Zoom</text>
            <text x="320" y="106" font-family="'Liberation Mono', monospace" font-size="10" fill="#c084fc">Mathematical Easing Curves</text>
            <text x="320" y="120" font-family="'Liberation Mono', monospace" font-size="9.5" fill="#94a3b8">Auto-pans to active window bounds</text>
            <text x="320" y="132" font-family="'Liberation Mono', monospace" font-size="9" fill="#38bdf8">Eliminates jerky mouse movements</text>

            <rect x="310" y="146" width="220" height="68" rx="5" fill="#1f182b" stroke="#a855f7" stroke-opacity="0.4" stroke-width="1"/>
            <text x="320" y="166" font-family="'Liberation Sans', sans-serif" font-size="12" font-weight="700" fill="#ffffff">Crash-Proof Stream Sink</text>
            <text x="320" y="182" font-family="'Liberation Mono', monospace" font-size="10" fill="#34d399">Continuous MKV Segmenter</text>
            <text x="320" y="196" font-family="'Liberation Mono', monospace" font-size="9.5" fill="#94a3b8">Guaranteed file recovery if crash</text>
            <text x="320" y="208" font-family="'Liberation Mono', monospace" font-size="9" fill="#e2e8f0">Lossless fast remux to MP4 on stop</text>

            <rect x="310" y="224" width="220" height="72" rx="5" fill="#1f182b" stroke="#a855f7" stroke-opacity="0.4" stroke-width="1"/>
            <text x="320" y="244" font-family="'Liberation Sans', sans-serif" font-size="12" font-weight="700" fill="#ffffff">Floating HUD &amp; Markers</text>
            <text x="320" y="260" font-family="'Liberation Mono', monospace" font-size="10" fill="#ffa5d0">Frosted-glass Wayland layer-shell</text>
            <text x="320" y="276" font-family="'Liberation Mono', monospace" font-size="9.5" fill="#94a3b8">Pause · Resume · Chapter markers</text>

            <!-- Arrow 2 -> 3: Direct Hardware Render -->
            <path d="M 545,150 L 595,150" stroke="#38bdf8" stroke-width="2"/>
            <polygon points="600,150 590,145 590,155" fill="#38bdf8"/>
            <text x="572" y="140" font-family="'Liberation Mono', monospace" font-size="9" fill="#38bdf8" text-anchor="middle">Hardware</text>
            <text x="572" y="170" font-family="'Liberation Mono', monospace" font-size="8.5" fill="#94a3b8" text-anchor="middle">NVENC/VAAPI</text>

            <!-- Column 3: Hardware Encoders & Local Catalog -->
            <rect x="600" y="20" width="220" height="290" rx="8" fill="#0d141e" stroke="#38bdf8" stroke-opacity="0.5" stroke-width="1.5"/>
            <rect x="600" y="20" width="220" height="34" rx="8" fill="#15202f"/>
            <text x="710" y="42" font-family="'Liberation Mono', monospace" font-size="11" font-weight="700" fill="#38bdf8" text-anchor="middle">3. HARDWARE &amp; VAULT</text>

            <rect x="615" y="70" width="190" height="66" rx="5" fill="#162335" stroke="#34d399" stroke-opacity="0.4" stroke-width="1"/>
            <text x="625" y="90" font-family="'Liberation Sans', sans-serif" font-size="12" font-weight="700" fill="#ffffff">HW Codec Selection</text>
            <text x="625" y="106" font-family="'Liberation Mono', monospace" font-size="10" fill="#34d399">VAAPI / NVENC (Preferred)</text>
            <text x="625" y="122" font-family="'Liberation Mono', monospace" font-size="9.5" fill="#94a3b8">Low-power x264 CPU fallback</text>

            <rect x="615" y="148" width="190" height="66" rx="5" fill="#162335" stroke="#34d399" stroke-opacity="0.4" stroke-width="1"/>
            <text x="625" y="168" font-family="'Liberation Sans', sans-serif" font-size="12" font-weight="700" fill="#ffffff">Local SQLite Vault</text>
            <text x="625" y="184" font-family="'Liberation Mono', monospace" font-size="10" fill="#38bdf8">Encrypted local catalog</text>
            <text x="625" y="200" font-family="'Liberation Mono', monospace" font-size="9.5" fill="#94a3b8">Duration · Bitrate · Codec tags</text>

            <rect x="615" y="226" width="190" height="70" rx="5" fill="#162335" stroke="#34d399" stroke-opacity="0.4" stroke-width="1"/>
            <text x="625" y="246" font-family="'Liberation Sans', sans-serif" font-size="12" font-weight="700" fill="#ffffff">Zero-Server Policy</text>
            <text x="625" y="264" font-family="'Liberation Mono', monospace" font-size="10" fill="#facc15">No HTTP daemons</text>
            <text x="625" y="282" font-family="'Liberation Mono', monospace" font-size="9" fill="#94a3b8">No cloud telemetry or tracking</text>

            <!-- Bottom Airgap Shield -->
            <rect x="20" y="325" width="800" height="38" rx="6" fill="#082015" stroke="#22c55e" stroke-opacity="0.6" stroke-width="1"/>
            <text x="420" y="348" font-family="'Liberation Mono', monospace" font-size="11" font-weight="700" fill="#4ade80" text-anchor="middle">✔ ZERO CLOUD LEAK: SCREEN CAPTURES AND AUDIO STREAMS ARE WRITTEN DIRECTLY TO LOCAL DISK VAULT</text>
          </svg>
        </div>
      </div>

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
