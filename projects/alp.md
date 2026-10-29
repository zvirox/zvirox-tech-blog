---
layout: default
title: Audio Labs Pro | Zvirox
description: A Linux audio studio built with Rust for multitrack recording, editing, mixing, and export, with offline AI voice tools, dictation, and CLAP/LV2 hosting.
permalink: /projects/alp/
---

<div class="zv-container">

  <article class="zv-post" style="max-width: 960px; margin: 0 auto;">

    <!-- Breadcrumb -->
    <div style="margin-bottom: 24px; color: var(--zv-text-muted); font-size: 14px;">
      <a href="{{ '/' | relative_url }}" style="color: var(--zv-text-secondary);">Home</a> &rarr; 
      <a href="{{ '/projects/' | relative_url }}" style="color: var(--zv-text-secondary);">Projects</a> &rarr; 
      <span style="color: var(--zv-text);">Audio Labs Pro</span>
    </div>

    <!-- Header -->
    <header class="zv-post-header" style="margin-bottom: 40px;">
      <div class="zv-card-category">
        AUDIO WORKSTATION • ALPHA v0.0.1-alpha.2
      </div>

      <h1 class="zv-post-title">
        Audio Labs Pro
      </h1>

      <p class="zv-post-description">
        A Linux audio studio built with Rust for multitrack recording, editing, mixing, and export, 
        with offline AI voice tools, dictation, voice profiles, and CLAP/LV2 plugin hosting.
      </p>

      <div style="margin: 20px 0; display: flex; flex-wrap: wrap; gap: 8px;">
        <span class="zv-tag">Rust</span>
        <span class="zv-tag">Linux</span>
        <span class="zv-tag">Iced</span>
        <span class="zv-tag">Audio DSP</span>
        <span class="zv-tag">Local AI</span>
      </div>

      <div class="zv-post-meta" style="margin-top: 20px; display: flex; gap: 16px; align-items: center;">
        <a href="https://github.com/zvirox/audio-labs-pro" target="_blank" rel="noopener noreferrer" class="zv-button zv-button-primary" style="min-height: 38px; padding: 0 16px; font-size: 13px;">
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
        <strong>Audio Labs Pro</strong> is an advanced open-source audio workstation written in Rust for Linux environments. 
        It bridges traditional digital audio workspace (DAW) workflows with offline-first AI speech capabilities, providing 
        multitrack recording, editing, mixing, CLAP/LV2 plugin hosting, and local speech generation without telemetry or cloud dependency.
      </p>

      <h2>Seven Core Workspaces</h2>
      <p>
        The application is organized into seven specialized workspaces designed for focused audio and voice production:
      </p>
      <ul>
        <li><strong>Generate:</strong> Voice cards, prompt editor, generation/playback controls, and take history.</li>
        <li><strong>Stories:</strong> Multi-line scripts, per-line rendering, audio stitching, and docked track editor.</li>
        <li><strong>Captures:</strong> Live recording, dictation, VAD transcription, input meters, and transcript editor.</li>
        <li><strong>Voices:</strong> Profile library, inspector, designed voices, and the cloning consent gate.</li>
        <li><strong>Effects:</strong> Cleanup chain, signal path routing, and hosted CLAP/LV2 plugins.</li>
        <li><strong>Models:</strong> Model catalogue, licenses, offline policy controls, and storage management.</li>
        <li><strong>Settings:</strong> Appearance, motion, AI control, storage, delivery, and panel configurations.</li>
      </ul>

      <h2>Key Features & Audio Engine</h2>
      <ul>
        <li><strong>Real-Time Safe Audio Engine:</strong> Engineered with zero allocations, zero locks, and zero logging in the audio callback thread using `cpal`.</li>
        <li><strong>Plugin Hosting:</strong> Dynamic C-ABI loading for CLAP and LV2 plugins via the `alp-plugin` engine, featuring a scanner with cached registry and real-time-safe scratch buffers.</li>
        <li><strong>Offline AI Integration:</strong> Text-to-speech, dictation, and voice profiles powered by ONNX Runtime and GGUF inference running in a separate process.</li>
        <li><strong>Privacy-First Design:</strong> Fully offline operation — network traffic is strictly limited to user-initiated model downloads, with zero telemetry or background listeners.</li>
        <li><strong>Automation:</strong> Comprehensive CLI tools (`alp-cli`, `alp-infer`, `alp-mcp`) supporting scriptable workflows and Model Context Protocol integration.</li>
      </ul>

      <h2>Technology Stack</h2>
      <ul>
        <li><strong>Language:</strong> Rust 1.89+ for memory safety and zero-cost abstractions.</li>
        <li><strong>Graphics & UI:</strong> Built with `iced 0.14 + kit` for a high-performance native GPU rendering pipeline.</li>
        <li><strong>Audio Stack:</strong> `cpal` for cross-platform audio device interaction and low-latency buffer management.</li>
      </ul>

      <h2>Current Status & Limitations</h2>
      <p>
        Audio Labs Pro is currently released as an <strong>alpha</strong> (v0.0.1-alpha.2). It targets Linux environments 
        (requiring ALSA headers and pkg-config). While core multitrack mixing, plugin hosting, and AI speech generation 
        are operational, support varies across specific hardware configurations and plugin implementations.
      </p>

      <h2>Resources & Links</h2>
      <ul>
        <li>Repository: <a href="https://github.com/zvirox/audio-labs-pro" target="_blank" rel="noopener noreferrer">GitHub Repository</a></li>
        <li>Releases: Check GitHub releases for alpha tarballs and build instructions.</li>
      </ul>

    </div>

    <!-- Navigation Footer -->
    <div style="margin-top: 60px; padding-top: 30px; border-top: 1px solid var(--zv-border); display: flex; justify-content: space-between; align-items: center;">
      <a href="{{ '/projects/eep/' | relative_url }}" class="zv-section-link">
        &larr; Previous: Easy Edits Pro
      </a>
      <a href="{{ '/projects/cft/' | relative_url }}" class="zv-section-link">
        Next Project: Climin TV Friend &rarr;
      </a>
    </div>

  </article>

</div>
