---
layout: default
title: Zvirox · Open-Source Software for Linux & Android TV
description: Open-source desktop and TV software for Linux and Android TV. Easy Edits Pro, Audio Labs Pro, Screen Studio Pro, and Your TV Friend.
permalink: /
---

<div class="zv-container">

  <!-- =====================================================
       1. HERO SECTION
       ===================================================== -->

  <section class="zv-hero">

    <div class="zv-hero-content">

      <div class="zv-card-category">
        OPEN-SOURCE SOFTWARE • LINUX • ANDROID TV
      </div>

      <h1>
        Open-source video, audio and TV software for
        <span>Linux and Android TV.</span>
      </h1>

      <p>
        Local-first apps you can inspect and run on your own hardware. Easy Edits Pro and
        Audio Labs Pro also ship an MCP server, so AI agents can operate them.
      </p>

      <div style="display:flex; gap:12px; flex-wrap:wrap; align-items:center;">

        <a
          href="#projects"
          class="zv-button zv-button-primary"
        >
          Explore Projects
        </a>

        <a
          href="https://github.com/zvirox"
          target="_blank"
          rel="noopener noreferrer"
          class="zv-button zv-button-secondary"
        >
          View on GitHub ↗
        </a>

      </div>

      <!-- Tech Stack Strip -->
      <div class="zv-hero-stack">
        <span class="zv-hero-stack-label">Stack:</span>
        <span class="zv-hero-stack-item">Rust</span>
        <span class="zv-hero-stack-item">Tauri</span>
        <span class="zv-hero-stack-item">React</span>
        <span class="zv-hero-stack-item">GStreamer</span>
        <span class="zv-hero-stack-item">iced</span>
        <span class="zv-hero-stack-item">Java</span>
        <span class="zv-hero-stack-item">ADB</span>
      </div>

    </div>

  </section>


  <!-- =====================================================
       2. PROJECT GRID
       ===================================================== -->

  <section id="projects" class="zv-section">

    <div class="zv-section-header">
      <div>
        <div class="zv-card-category">
          SOFTWARE PORTFOLIO
        </div>
        <h2 class="zv-section-title">
          Open-Source Projects
        </h2>
      </div>
      <a href="{{ '/projects/' | relative_url }}" class="zv-section-link">
        All project details →
      </a>
    </div>

    <div class="zv-projects-grid">

      <!-- Easy Edits Pro -->
      <article class="zv-card zv-project-card">
        <!-- Motion Graphic: Multitrack Video Timeline -->
        <div class="zv-project-visual zv-visual-eep" aria-hidden="true">
          <div class="zv-visual-toolbar">
            <span class="zv-visual-badge"><span class="zv-dot zv-dot-magenta"></span> VAAPI 60FPS</span>
            <span class="zv-visual-code">00:01:24:18</span>
          </div>
          <div class="zv-timeline-viewport">
            <div class="zv-timeline-track zv-track-video">
              <div class="zv-track-clip zv-clip-vid1"><span>CLIP_A01.mp4</span></div>
              <div class="zv-track-clip zv-clip-vid2"><span>RENDER_PASS.vaapi</span></div>
            </div>
            <div class="zv-timeline-track zv-track-audio">
              <div class="zv-track-clip zv-clip-aud1">
                <svg class="zv-wave-svg" viewBox="0 0 120 12" preserveAspectRatio="none"><path d="M0,6 Q10,0 20,6 T40,6 T60,6 T80,6 T100,6 T120,6" fill="none" stroke="currentColor" stroke-width="1.5"/></svg>
                <span>VOICE_01.wav</span>
              </div>
              <div class="zv-track-clip zv-clip-aud2">
                <svg class="zv-wave-svg" viewBox="0 0 80 12" preserveAspectRatio="none"><path d="M0,6 Q8,1 16,6 T32,6 T48,6 T64,6 T80,6" fill="none" stroke="currentColor" stroke-width="1.5"/></svg>
                <span>SFX_DSP.clap</span>
              </div>
            </div>
            <div class="zv-timeline-playhead"></div>
          </div>
        </div>
        <div class="zv-card-body zv-project-card-body">
          <div class="zv-card-category">
            DESKTOP VIDEO EDITOR • ACTIVE ALPHA
          </div>
          <h3 class="zv-card-title">
            <a href="{{ '/projects/eep/' | relative_url }}">Easy Edits Pro</a>
          </h3>
          <p class="zv-card-excerpt">
            An alpha-stage Linux desktop video editor built with Rust, Tauri, React, and GStreamer. 
            It combines a multitrack editing workflow with a Rust-owned project model and automation interfaces.
          </p>
          <div class="zv-project-card-tags">
            <span class="zv-tag">Rust</span>
            <span class="zv-tag">Tauri</span>
            <span class="zv-tag">React</span>
            <span class="zv-tag">GStreamer</span>
            <span class="zv-tag">Linux</span>
          </div>
          <div class="zv-project-card-footer">
            <a href="{{ '/projects/eep/' | relative_url }}" class="zv-section-link">
              Explore Project →
            </a>
            <a href="https://github.com/zvirox/easy-edits-pro" target="_blank" rel="noopener noreferrer" class="zv-project-github-link">
              GitHub ↗
            </a>
          </div>
        </div>
      </article>

      <!-- Audio Labs Pro -->
      <article class="zv-card zv-project-card">
        <!-- Motion Graphic: Audio DSP Spectrum Analyzer -->
        <div class="zv-project-visual zv-visual-alp" aria-hidden="true">
          <div class="zv-visual-toolbar">
            <span class="zv-visual-badge"><span class="zv-dot zv-dot-cyan"></span> DSP ENGINE • 48kHz</span>
            <span class="zv-visual-code">-3.2 dBFS</span>
          </div>
          <div class="zv-spectrum-viewport">
            <div class="zv-spectrum-bars">
              <span style="--i:1; --h:65%;"></span>
              <span style="--i:2; --h:85%;"></span>
              <span style="--i:3; --h:45%;"></span>
              <span style="--i:4; --h:95%;"></span>
              <span style="--i:5; --h:75%;"></span>
              <span style="--i:6; --h:60%;"></span>
              <span style="--i:7; --h:88%;"></span>
              <span style="--i:8; --h:70%;"></span>
              <span style="--i:9; --h:92%;"></span>
              <span style="--i:10; --h:55%;"></span>
              <span style="--i:11; --h:80%;"></span>
              <span style="--i:12; --h:62%;"></span>
              <span style="--i:13; --h:74%;"></span>
              <span style="--i:14; --h:48%;"></span>
              <span style="--i:15; --h:82%;"></span>
              <span style="--i:16; --h:58%;"></span>
            </div>
            <div class="zv-spectrum-grid"></div>
          </div>
        </div>
        <div class="zv-card-body zv-project-card-body">
          <div class="zv-card-category">
            AUDIO WORKSTATION • ALPHA v0.0.1
          </div>
          <h3 class="zv-card-title">
            <a href="{{ '/projects/alp/' | relative_url }}">Audio Labs Pro</a>
          </h3>
          <p class="zv-card-excerpt">
            A Linux audio studio built with Rust for multitrack recording, editing, mixing, and export, 
            with offline AI voice tools, dictation, voice profiles, and CLAP/LV2 plugin hosting.
          </p>
          <div class="zv-project-card-tags">
            <span class="zv-tag">Rust</span>
            <span class="zv-tag">Linux</span>
            <span class="zv-tag">Iced</span>
            <span class="zv-tag">Audio DSP</span>
            <span class="zv-tag">Local AI</span>
          </div>
          <div class="zv-project-card-footer">
            <a href="{{ '/projects/alp/' | relative_url }}" class="zv-section-link">
              Explore Project →
            </a>
            <a href="https://github.com/zvirox/audio-labs-pro" target="_blank" rel="noopener noreferrer" class="zv-project-github-link">
              GitHub ↗
            </a>
          </div>
        </div>
      </article>

      <!-- Screen Studio Pro -->
      <article class="zv-card zv-project-card">
        <!-- Motion Graphic: Wayland PipeWire Viewfinder -->
        <div class="zv-project-visual zv-visual-ssp" aria-hidden="true">
          <div class="zv-visual-toolbar">
            <span class="zv-visual-badge"><span class="zv-dot zv-dot-red zv-pulse"></span> REC • 00:02:47</span>
            <span class="zv-visual-code">PIPEWIRE PORTAL</span>
          </div>
          <div class="zv-viewfinder-viewport">
            <div class="zv-reticle zv-reticle-tl"></div>
            <div class="zv-reticle zv-reticle-tr"></div>
            <div class="zv-reticle zv-reticle-bl"></div>
            <div class="zv-reticle zv-reticle-br"></div>
            <div class="zv-viewfinder-window">
              <div class="zv-sim-cursor"></div>
              <div class="zv-sim-pip">
                <svg width="18" height="18" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2"><path d="M23 7l-7 5 7 5V7z"/><rect x="1" y="5" width="15" height="14" rx="2" ry="2"/></svg>
              </div>
            </div>
          </div>
        </div>
        <div class="zv-card-body zv-project-card-body">
          <div class="zv-card-category">
            LINUX SCREEN RECORDER • PLANNING PHASE
          </div>
          <h3 class="zv-card-title">
            <a href="{{ '/projects/ssp/' | relative_url }}">Screen Studio Pro</a>
          </h3>
          <p class="zv-card-excerpt">
            A planned open-source Wayland screen recorder with a frosted-glass interface, PipeWire capture,
            webcam picture-in-picture, and hardware-first encoding.
          </p>
          <div class="zv-project-card-tags">
            <span class="zv-tag">Rust</span>
            <span class="zv-tag">Tauri</span>
            <span class="zv-tag">React</span>
            <span class="zv-tag">Linux</span>
            <span class="zv-tag">Wayland</span>
          </div>
          <div class="zv-project-card-footer">
            <a href="{{ '/projects/ssp/' | relative_url }}" class="zv-section-link">
              Explore Project →
            </a>
            <a href="https://github.com/zvirox/screen-studio-pro" target="_blank" rel="noopener noreferrer" class="zv-project-github-link">
              GitHub ↗
            </a>
          </div>
        </div>
      </article>

      <!-- Your TV Friend -->
      <article class="zv-card zv-project-card">
        <!-- Motion Graphic: ADB TV Debloater Bridge -->
        <div class="zv-project-visual zv-visual-ytf" aria-hidden="true">
          <div class="zv-visual-toolbar">
            <span class="zv-visual-badge"><span class="zv-dot zv-dot-emerald"></span> ADB CONNECTED</span>
            <span class="zv-visual-code">192.168.1.104</span>
          </div>
          <div class="zv-tv-viewport">
            <div class="zv-tv-screen">
              <div class="zv-tv-tile"></div>
              <div class="zv-tv-tile zv-tile-active"></div>
              <div class="zv-tv-tile"></div>
            </div>
            <div class="zv-adb-status">
              <div class="zv-adb-packet">
                <span class="zv-packet-dot"></span>
                <span class="zv-packet-dot"></span>
                <span class="zv-packet-dot"></span>
              </div>
              <span class="zv-adb-tag">ROOTLESS SAFE</span>
            </div>
          </div>
        </div>
        <div class="zv-card-body zv-project-card-body">
          <div class="zv-card-category">
            ANDROID TV • v0.0.3
          </div>
          <h3 class="zv-card-title">
            <a href="{{ '/projects/ytf/' | relative_url }}">Your TV Friend</a>
          </h3>
          <p class="zv-card-excerpt">
            A non-destructive Android TV cleanup tool and native television launcher (Your UI). Combines
            reversible ADB-based package controls with 5 customizable launcher visual styles.
          </p>
          <div class="zv-project-card-tags">
            <span class="zv-tag">Java</span>
            <span class="zv-tag">Android TV</span>
            <span class="zv-tag">ADB</span>
            <span class="zv-tag">Python</span>
            <span class="zv-tag">Android</span>
          </div>
          <div class="zv-project-card-footer">
            <a href="{{ '/projects/ytf/' | relative_url }}" class="zv-section-link">
              Explore Project →
            </a>
            <a href="https://github.com/zvirox/your-tv-friend" target="_blank" rel="noopener noreferrer" class="zv-project-github-link">
              GitHub ↗
            </a>
          </div>
        </div>
      </article>

    </div>

  </section>


  <!-- =====================================================
       3. WHY ZVIROX (3 COLUMNS)
       ===================================================== -->

  <section class="zv-section">

    <div class="zv-section-header">
      <div>
        <div class="zv-card-category">
          ENGINEERING PRINCIPLES
        </div>
        <h2 class="zv-section-title">
          Why Zvirox
        </h2>
      </div>
    </div>

    <div class="zv-features-grid">

      <!-- Column 1: Local-first -->
      <div class="zv-feature-card">
        <div class="zv-feature-icon" aria-hidden="true">
          <svg width="20" height="20" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2" stroke-linecap="round" stroke-linejoin="round">
            <rect x="2" y="2" width="20" height="8" rx="2" ry="2"></rect>
            <rect x="2" y="14" width="20" height="8" rx="2" ry="2"></rect>
            <line x1="6" y1="6" x2="6.01" y2="6"></line>
            <line x1="6" y1="18" x2="6.01" y2="18"></line>
          </svg>
        </div>
        <h3 class="zv-feature-title">Local-first & Private</h3>
        <p class="zv-feature-desc">
          No mandatory accounts, no cloud dependencies, and zero telemetry. Easy Edits Pro, Audio Labs Pro,
          and Your TV Friend run on your own hardware. Your media and audio stay strictly on your local disk.
        </p>
      </div>

      <!-- Column 2: Agent-ready -->
      <div class="zv-feature-card">
        <div class="zv-feature-icon" aria-hidden="true">
          <svg width="20" height="20" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2" stroke-linecap="round" stroke-linejoin="round">
            <polyline points="4 17 10 11 4 5"></polyline>
            <line x1="12" y1="19" x2="20" y2="19"></line>
          </svg>
        </div>
        <h3 class="zv-feature-title">Agent-ready Workflows</h3>
        <p class="zv-feature-desc">
          Built to be operated by both humans and AI coding agents. Easy Edits Pro and Audio Labs Pro ship
          Model Context Protocol (MCP) servers and command-line interfaces, enabling programmatic automation.
        </p>
      </div>

      <!-- Column 3: Open with Commercial Option -->
      <div class="zv-feature-card">
        <div class="zv-feature-icon" aria-hidden="true">
          <svg width="20" height="20" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2" stroke-linecap="round" stroke-linejoin="round">
            <path d="M16 16v1a2 2 0 0 1-2 2H3a2 2 0 0 1-2-2V7a2 2 0 0 1 2-2h11a2 2 0 0 1 2 2v1"></path>
            <path d="M18 8h4a2 2 0 0 1 2 2v7a2 2 0 0 1-2 2h-4"></path>
            <circle cx="8" cy="12" r="2"></circle>
          </svg>
        </div>
        <h3 class="zv-feature-title">Open with Commercial Choice</h3>
        <p class="zv-feature-desc">
          All code is open and verifiable under recognized licenses (AGPL-3.0, Apache-2.0, MIT). For organizations
          seeking closed-source embedding, Easy Edits Pro offers an optional commercial license on request.
        </p>
      </div>

    </div>

  </section>


  <!-- =====================================================
       4. BY THE NUMBERS (VERIFIED FACTS ONLY)
       ===================================================== -->

  <section class="zv-section">

    <div class="zv-section-header">
      <div>
        <div class="zv-card-category">
          CODEBASE METRICS
        </div>
        <h2 class="zv-section-title">
          By the Numbers
        </h2>
      </div>
    </div>

    <div class="zv-numbers-grid">

      <div class="zv-number-card">
        <span class="zv-number-val">440</span>
        <span class="zv-number-label">Editor Commands</span>
        <span class="zv-number-sub">Shipped in Easy Edits Pro</span>
      </div>

      <div class="zv-number-card">
        <span class="zv-number-val">7</span>
        <span class="zv-number-label">Workspaces</span>
        <span class="zv-number-sub">Dedicated audio & video workflows</span>
      </div>

      <div class="zv-number-card">
        <span class="zv-number-val">14</span>
        <span class="zv-number-label">MCP Tools</span>
        <span class="zv-number-sub">Local audio automation surface</span>
      </div>

      <div class="zv-number-card">
        <span class="zv-number-val">26</span>
        <span class="zv-number-label">TV Languages</span>
        <span class="zv-number-sub">Supported in Your TV Friend</span>
      </div>

      <div class="zv-number-card">
        <span class="zv-number-val">297</span>
        <span class="zv-number-label">Device Profiles</span>
        <span class="zv-number-sub">Android TV models catalogued</span>
      </div>

    </div>

  </section>


  <!-- =====================================================
       5. LICENSING TEASER
       ===================================================== -->

  <section class="zv-section">

    <div class="zv-teaser-panel">

      <div class="zv-teaser-content">
        <div class="zv-card-category">
          PER-PROJECT LICENSING
        </div>
        <h2 class="zv-teaser-title">
          Transparent, per-project open-source licensing.
        </h2>
        <p class="zv-teaser-text">
          Software is licensed under AGPL-3.0 (Easy Edits Pro), Apache-2.0 (Audio Labs Pro), and MIT (Screen Studio Pro, Your TV Friend). A commercial license for Easy Edits Pro is available on request for closed-source distribution.
        </p>
      </div>

      <a href="{{ '/licensing/' | relative_url }}" class="zv-button zv-button-primary" style="white-space:nowrap;">
        View Licensing Overview →
      </a>

    </div>

  </section>


  <!-- =====================================================
       6. LATEST GUIDES (4 MOST RECENT POSTS)
       ===================================================== -->

  <section class="zv-section">

    <div class="zv-section-header">

      <div>
        <div class="zv-card-category">
          TECHNICAL WRITING
        </div>
        <h2 class="zv-section-title">
          Latest Guides
        </h2>
      </div>

      <a
        href="{{ '/guides/' | relative_url }}"
        class="zv-section-link"
      >
        View all guides →
      </a>

    </div>

    <div class="zv-article-grid">

      {% if site.posts.size > 0 %}

        {% for post in site.posts limit: 4 %}

          <article class="zv-card">

            <div class="zv-card-body">

              {% if post.categories and post.categories.size > 0 %}
                <div class="zv-card-category">
                  {{ post.categories | first }}
                </div>
              {% else %}
                <div class="zv-card-category">
                  GUIDE
                </div>
              {% endif %}

              <h3 class="zv-card-title">
                <a href="{{ post.url | relative_url }}">
                  {{ post.title }}
                </a>
              </h3>

              {% if post.excerpt %}
                <p class="zv-card-excerpt">
                  {{ post.excerpt | strip_html | truncate: 140 }}
                </p>
              {% endif %}

              <div class="zv-card-meta">
                <span>
                  {{ post.date | date: "%b %d, %Y" }}
                </span>
                <span>•</span>
                <span>
                  Read guide →
                </span>
              </div>

            </div>

          </article>

        {% endfor %}

      {% endif %}

    </div>

  </section>


  <!-- =====================================================
       7. CLOSING CALL TO ACTION
       ===================================================== -->

  <section class="zv-section">

    <div class="zv-hero" style="margin-bottom:0; padding:48px 36px;">

      <div class="zv-hero-content" style="max-width:760px;">

        <div class="zv-card-category">
          COMMUNITY & CODE
        </div>

        <h2>
          Built in public.
          <span>Inspect the code.</span>
        </h2>

        <p>
          Read the source, report an issue, or sponsor the work. Every project is maintained
          solo by Prakashpuri Gauswami (@Prakash) with open git histories.
        </p>

        <div style="display:flex; gap:12px; flex-wrap:wrap; margin-top:24px;">

          <a
            href="https://github.com/zvirox"
            target="_blank"
            rel="noopener noreferrer"
            class="zv-button zv-button-primary"
          >
            GitHub Profile ↗
          </a>

          <a
            href="https://github.com/sponsors/zvirox"
            target="_blank"
            rel="noopener noreferrer"
            class="zv-button zv-button-secondary"
          >
            Sponsor on GitHub ↗
          </a>

          <a
            href="mailto:info@zvirox.in"
            class="zv-button zv-button-secondary"
          >
            info@zvirox.in
          </a>

        </div>

      </div>

    </div>

  </section>

</div>
