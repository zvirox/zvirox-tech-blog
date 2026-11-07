---
layout: default
title: Easy Edits Pro | Zvirox
description: An alpha-stage Linux desktop video editor built with Rust, Tauri, React, and GStreamer. Combines multitrack editing with a Rust-owned project model.
permalink: /projects/eep/
image: "/assets/images/projects/easy-edits-pro-mockup.png"
---

<script type="application/ld+json">
{
  "@context": "https://schema.org",
  "@type": "SoftwareApplication",
  "name": "Easy Edits Pro",
  "operatingSystem": "Linux",
  "applicationCategory": "MultimediaApplication",
  "description": "An alpha-stage Linux desktop video editor built with Rust, Tauri, React, and GStreamer. Combines multitrack editing with a Rust-owned project model and Model Context Protocol (MCP) automation.",
  "url": "https://zvirox.in/projects/eep/",
  "downloadUrl": "https://github.com/zvirox/easy-edits-pro/releases",
  "license": "https://www.gnu.org/licenses/agpl-3.0.html",
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
        <h1 class="zv-post-title" id="project-title">Easy Edits Pro</h1>
        <p class="zv-post-description">An alpha-stage Linux desktop video editor built with Rust, Tauri, React, and GStreamer. It combines a multitrack editing workflow with a Rust-owned project model and automation interfaces.</p>
        <p class="zv-project-status">Desktop video editor · Active alpha development</p>
        <div class="zv-project-tags" aria-label="Technologies"><span class="zv-tag">Rust</span> <span class="zv-tag">Tauri</span> <span class="zv-tag">React</span> <span class="zv-tag">GStreamer</span> <span class="zv-tag">Linux</span></div>
        <div class="zv-project-actions">
          <a href="https://github.com/zvirox/easy-edits-pro" target="_blank" rel="noopener noreferrer" class="zv-button zv-button-primary">View on GitHub <span aria-hidden="true">↗</span></a>
          <a href="{{ '/projects/' | relative_url }}" class="zv-project-text-link">Explore all projects <span aria-hidden="true">&rarr;</span></a>
        </div>
      </header>
            <figure class="zv-project-visual">
        <img class="zv-project-image" src="{{ '/assets/images/projects/easy-edits-pro-mockup.png' | relative_url }}" alt="Conceptual Easy Edits Pro video editor with a mountain lake preview, media bin, inspector, and multitrack timeline." width="1200" height="675" loading="lazy" decoding="async">
        <figcaption class="zv-project-caption">Concept mockup based on Easy Edits Pro's video editing workspaces.</figcaption>
      </figure>
    </section>

    <div class="zv-post-content zv-project-content">
      <h2>Overview</h2>
      <p>
        <strong>Easy Edits Pro</strong> (developed under Project Saturn) is an open-source Linux desktop 
        video editor engineered for performance and reliability. By pairing a robust Rust backend with a 
        modern React and Tauri frontend, it provides a responsive editing environment backed by GStreamer 
        for high-performance media processing.
      </p>

      <h2>Key Features</h2>
      <ul>
        <li><strong>Multitrack Timeline:</strong> Frame-accurate audio and video track management with support for standard editing operations.</li>
        <li><strong>Rust-Owned Project Model:</strong> Versioned project files with transactional state safety, robust undo/redo stacks, and project recovery.</li>
        <li><strong>Modular Workspaces:</strong> Dedicated workspace layouts including Media, Edit, Color, Fairlight audio, Keyframes, Fusion, and Deliver.</li>
        <li><strong>GStreamer Rendering:</strong> High-efficiency export pipelines targeting MP4 and WebM containers with configurable hardware acceleration.</li>
        <li><strong>Automation Interfaces:</strong> Built-in command-line interface (CLI), Model Context Protocol (MCP) server, and control-server capabilities for scriptable editing workflows.</li>
      </ul>

      <h2>Architecture & Technology Stack</h2>
      <p>
        The application is structured around a strict separation of concerns, ensuring low-latency editing responsiveness and zero data leaks:
      </p>

      <!-- Architecture Teardown Diagram -->
      <div class="zv-teardown-schematic" aria-label="Easy Edits Pro Architecture Teardown">
        <div class="zv-teardown-header">
          <div class="zv-teardown-title-wrap">
            <span class="zv-teardown-category">PIPELINE TEARDOWN</span>
            <span class="zv-teardown-subtitle">Rust Core · Tauri 2 IPC · GStreamer HW Accel</span>
          </div>
          <span class="zv-teardown-shield">🔒 AIRGAPPED LOCAL DISK</span>
        </div>
        <div class="zv-teardown-body">
          <svg class="zv-teardown-svg" viewBox="0 0 840 380" fill="none" xmlns="http://www.w3.org/2000/svg">
            <!-- Column 1: Presentation (React + TypeScript) -->
            <rect x="20" y="20" width="230" height="290" rx="8" fill="#0f121d" stroke="#ff50a6" stroke-opacity="0.4" stroke-width="1.5"/>
            <rect x="20" y="20" width="230" height="34" rx="8" fill="#171b2c"/>
            <text x="135" y="42" font-family="'Liberation Mono', monospace" font-size="11" font-weight="700" fill="#ffa5d0" text-anchor="middle">1. PRESENTATION (UI)</text>
            
            <rect x="35" y="70" width="200" height="42" rx="5" fill="#1b2138" stroke="#334155" stroke-width="1"/>
            <text x="45" y="88" font-family="'Liberation Sans', sans-serif" font-size="12" font-weight="700" fill="#ffffff">7 Modular Workspaces</text>
            <text x="45" y="103" font-family="'Liberation Mono', monospace" font-size="10" fill="#94a3b8">Edit · Color · Audio · Deliver</text>

            <rect x="35" y="124" width="200" height="52" rx="5" fill="#1b2138" stroke="#334155" stroke-width="1"/>
            <text x="45" y="143" font-family="'Liberation Sans', sans-serif" font-size="12" font-weight="700" fill="#ffffff">Virtualized Timeline</text>
            <text x="45" y="158" font-family="'Liberation Mono', monospace" font-size="10" fill="#94a3b8">60fps Canvas track renderer</text>
            <text x="45" y="170" font-family="'Liberation Mono', monospace" font-size="9" fill="#ff50a6">Sub-frame clip snip &amp; ripple</text>

            <rect x="35" y="188" width="200" height="50" rx="5" fill="#1b2138" stroke="#334155" stroke-width="1"/>
            <text x="45" y="207" font-family="'Liberation Sans', sans-serif" font-size="12" font-weight="700" fill="#ffffff">Automation Bridges</text>
            <text x="45" y="222" font-family="'Liberation Mono', monospace" font-size="10" fill="#38bdf8">CLI Client (eep-cli)</text>
            <text x="45" y="233" font-family="'Liberation Mono', monospace" font-size="9" fill="#34d399">MCP Server (440 tool calls)</text>

            <rect x="35" y="250" width="200" height="46" rx="5" fill="#141828" stroke="rgba(255,80,166,0.3)" stroke-width="1"/>
            <text x="135" y="278" font-family="'Liberation Mono', monospace" font-size="10" fill="#ffa5d0" text-anchor="middle">React 18 · TypeScript</text>

            <!-- Arrow 1 -> 2: Tauri 2 IPC -->
            <path d="M 250,150 L 300,150" stroke="#ff50a6" stroke-width="2"/>
            <polygon points="305,150 295,145 295,155" fill="#ff50a6"/>
            <text x="277" y="140" font-family="'Liberation Mono', monospace" font-size="9" fill="#ff50a6" text-anchor="middle">Tauri IPC</text>
            <text x="277" y="170" font-family="'Liberation Mono', monospace" font-size="8.5" fill="#94a3b8" text-anchor="middle">Zero-Copy</text>

            <!-- Column 2: Backend Core (Rust Engine) -->
            <rect x="305" y="20" width="240" height="290" rx="8" fill="#101524" stroke="#ff50a6" stroke-opacity="0.6" stroke-width="1.8"/>
            <rect x="305" y="20" width="240" height="34" rx="8" fill="#192238"/>
            <text x="425" y="42" font-family="'Liberation Mono', monospace" font-size="11" font-weight="700" fill="#ffffff" text-anchor="middle">2. RUST TRANSACTION CORE</text>

            <rect x="320" y="70" width="210" height="64" rx="5" fill="#17223b" stroke="#38bdf8" stroke-opacity="0.4" stroke-width="1"/>
            <text x="330" y="90" font-family="'Liberation Sans', sans-serif" font-size="12" font-weight="700" fill="#ffffff">Transactional Project Model</text>
            <text x="330" y="106" font-family="'Liberation Mono', monospace" font-size="10" fill="#38bdf8">ACID Undo / Redo Journal</text>
            <text x="330" y="122" font-family="'Liberation Mono', monospace" font-size="9.5" fill="#94a3b8">Immutable timeline state graph</text>

            <rect x="320" y="146" width="210" height="66" rx="5" fill="#17223b" stroke="#38bdf8" stroke-opacity="0.4" stroke-width="1"/>
            <text x="330" y="166" font-family="'Liberation Sans', sans-serif" font-size="12" font-weight="700" fill="#ffffff">Auto-Recovery Journal</text>
            <text x="330" y="182" font-family="'Liberation Mono', monospace" font-size="10" fill="#34d399">Crash resilience on power loss</text>
            <text x="330" y="198" font-family="'Liberation Mono', monospace" font-size="9.5" fill="#94a3b8">Periodic write-ahead log (.eep)</text>

            <rect x="320" y="224" width="210" height="72" rx="5" fill="#17223b" stroke="#38bdf8" stroke-opacity="0.4" stroke-width="1"/>
            <text x="330" y="244" font-family="'Liberation Sans', sans-serif" font-size="12" font-weight="700" fill="#ffffff">GStreamer Pipeline Host</text>
            <text x="330" y="260" font-family="'Liberation Mono', monospace" font-size="10" fill="#ffa5d0">Dynamic bin constructor</text>
            <text x="330" y="276" font-family="'Liberation Mono', monospace" font-size="9.5" fill="#94a3b8">Audio/Video sync bus</text>

            <!-- Arrow 2 -> 3: Pipeline Bus -->
            <path d="M 545,150 L 595,150" stroke="#38bdf8" stroke-width="2"/>
            <polygon points="600,150 590,145 590,155" fill="#38bdf8"/>
            <text x="572" y="140" font-family="'Liberation Mono', monospace" font-size="9" fill="#38bdf8" text-anchor="middle">GStreamer</text>
            <text x="572" y="170" font-family="'Liberation Mono', monospace" font-size="8.5" fill="#94a3b8" text-anchor="middle">NVMM/DMABUF</text>

            <!-- Column 3: Processing & Hardware Output -->
            <rect x="600" y="20" width="220" height="290" rx="8" fill="#0f1422" stroke="#38bdf8" stroke-opacity="0.5" stroke-width="1.5"/>
            <rect x="600" y="20" width="220" height="34" rx="8" fill="#152136"/>
            <text x="710" y="42" font-family="'Liberation Mono', monospace" font-size="11" font-weight="700" fill="#38bdf8" text-anchor="middle">3. HARDWARE &amp; ENCODE</text>

            <rect x="615" y="70" width="190" height="66" rx="5" fill="#162238" stroke="#34d399" stroke-opacity="0.4" stroke-width="1"/>
            <text x="625" y="90" font-family="'Liberation Sans', sans-serif" font-size="12" font-weight="700" fill="#ffffff">HW Acceleration</text>
            <text x="625" y="106" font-family="'Liberation Mono', monospace" font-size="10" fill="#34d399">VAAPI (Intel / AMD)</text>
            <text x="625" y="122" font-family="'Liberation Mono', monospace" font-size="10" fill="#38bdf8">NVENC (NVIDIA CUDA)</text>

            <rect x="615" y="148" width="190" height="66" rx="5" fill="#162238" stroke="#34d399" stroke-opacity="0.4" stroke-width="1"/>
            <text x="625" y="168" font-family="'Liberation Sans', sans-serif" font-size="12" font-weight="700" fill="#ffffff">Audio DSP Mixing</text>
            <text x="625" y="184" font-family="'Liberation Mono', monospace" font-size="10" fill="#e2e8f0">48kHz / 24-bit floating point</text>
            <text x="625" y="200" font-family="'Liberation Mono', monospace" font-size="9.5" fill="#94a3b8">Bypass / Volume automation</text>

            <rect x="615" y="226" width="190" height="70" rx="5" fill="#162238" stroke="#34d399" stroke-opacity="0.4" stroke-width="1"/>
            <text x="625" y="246" font-family="'Liberation Sans', sans-serif" font-size="12" font-weight="700" fill="#ffffff">Export Containers</text>
            <text x="625" y="264" font-family="'Liberation Mono', monospace" font-size="10" fill="#facc15">MP4 · WebM · MKV · ProRes</text>
            <text x="625" y="282" font-family="'Liberation Mono', monospace" font-size="9" fill="#94a3b8">Target bitrates &amp; multi-pass</text>

            <!-- Bottom Airgap Shield -->
            <rect x="20" y="325" width="800" height="38" rx="6" fill="#082015" stroke="#22c55e" stroke-opacity="0.6" stroke-width="1"/>
            <text x="420" y="348" font-family="'Liberation Mono', monospace" font-size="11" font-weight="700" fill="#4ade80" text-anchor="middle">✔ ZERO-TELEMETRY BOUNDARY: ALL TIMELINE ASSETS STORED LOCALLY ON DISK · ZERO CLOUD API CALLS</text>
          </svg>
        </div>
      </div>

      <ul>
        <li><strong>Backend Engine:</strong> Written in Rust, managing timeline state, rendering graphs, and file I/O.</li>
        <li><strong>Media Processing:</strong> Powered by GStreamer pipelines for decoding, filtering, and encoding.</li>
        <li><strong>Desktop Shell:</strong> Tauri framework bridging native system APIs with web technologies.</li>
        <li><strong>User Interface:</strong> React-based UI delivering a responsive, professional editing layout.</li>
      </ul>

      <h2>Current Status & Limitations</h2>
      <p>
        Easy Edits Pro is currently in <strong>active alpha development</strong> advancing toward a first beta release. 
        While core media import, timeline arrangement, and rendering pipelines are operational, certain advanced 
        workspace features (such as full color grading and complex keyframing) remain incomplete. It is not intended 
        as a drop-in replacement for mature commercial suites in production environments yet.
      </p>

      <h2>Resources & Links</h2>
      <ul>
        <li>Repository: <a href="https://github.com/zvirox/easy-edits-pro" target="_blank" rel="noopener noreferrer">GitHub Repository</a></li>
        <li>Documentation: Available within the repository docs and architecture guides.</li>
      </ul>
    </div>

    <nav class="zv-project-navigation" aria-label="Project navigation">
      <a href="{{ '/projects/' | relative_url }}" class="zv-section-link">
        &larr; Back to Projects Index
      </a>
      <a href="{{ '/projects/alp/' | relative_url }}" class="zv-section-link">
        Next Project: Audio Labs Pro &rarr;
      </a>
    </nav>

  </article>


</div>
