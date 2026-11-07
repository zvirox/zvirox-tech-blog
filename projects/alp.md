---
layout: default
title: Audio Labs Pro | Zvirox
description: A Linux audio studio built with Rust for multitrack recording, editing, mixing, and export, with offline AI voice tools, dictation, and CLAP/LV2 hosting.
permalink: /projects/alp/
image: "/assets/images/projects/audio-labs-pro-mockup.png"
---

<script type="application/ld+json">
{
  "@context": "https://schema.org",
  "@type": "SoftwareApplication",
  "name": "Audio Labs Pro",
  "operatingSystem": "Linux",
  "applicationCategory": "AudioApplication",
  "description": "A Linux audio studio built with Rust for multitrack recording, editing, mixing, and export, with offline AI voice tools, dictation, voice profiles, and CLAP/LV2 plugin hosting.",
  "url": "https://zvirox.in/projects/alp/",
  "downloadUrl": "https://github.com/zvirox/audio-labs-pro/releases",
  "license": "https://www.apache.org/licenses/LICENSE-2.0",
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
        <h1 class="zv-post-title" id="project-title">Audio Labs Pro</h1>
        <p class="zv-post-description">A Linux audio studio built with Rust for multitrack recording, editing, mixing, and export, with offline AI voice tools, dictation, voice profiles, and CLAP/LV2 plugin hosting.</p>
        <p class="zv-project-status">Linux audio workstation · Alpha v0.0.1-alpha.2</p>
        <div class="zv-project-tags" aria-label="Technologies"><span class="zv-tag">Rust</span> <span class="zv-tag">Linux</span> <span class="zv-tag">Iced</span> <span class="zv-tag">Audio DSP</span> <span class="zv-tag">Local AI</span></div>
        <div class="zv-project-actions">
          <a href="https://github.com/zvirox/audio-labs-pro" target="_blank" rel="noopener noreferrer" class="zv-button zv-button-primary">View on GitHub <span aria-hidden="true">↗</span></a>
          <a href="{{ '/projects/' | relative_url }}" class="zv-project-text-link">Explore all projects <span aria-hidden="true">&rarr;</span></a>
        </div>
      </header>
            <figure class="zv-project-visual">
        <img class="zv-project-image" src="{{ '/assets/images/projects/audio-labs-pro-mockup.png' | relative_url }}" alt="Conceptual Audio Labs Pro Stories workspace with a multitrack audio timeline, seven workspace rail, docked transport, and voice effects inspector." width="1200" height="675" loading="lazy" decoding="async">
        <figcaption class="zv-project-caption">Concept mockup inspired by Audio Labs Pro's seven-workspace glass interface.</figcaption>
      </figure>
    </section>

    <div class="zv-post-content zv-project-content">
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

      <h2>Technology Stack & Audio Architecture</h2>
      <p>
        Audio Labs Pro enforces a strict isolation model where real-time audio threads are decoupled from AI inference processes and native GPU rendering:
      </p>

      <!-- Architecture Teardown Diagram -->
      <div class="zv-teardown-schematic" aria-label="Audio Labs Pro Architecture Teardown">
        <div class="zv-teardown-header">
          <div class="zv-teardown-title-wrap">
            <span class="zv-teardown-category">DSP PIPELINE TEARDOWN</span>
            <span class="zv-teardown-subtitle">Lock-Free Audio Thread · CLAP/LV2 Host · Local ONNX AI</span>
          </div>
          <span class="zv-teardown-shield">🔒 ZERO AUDIO EGRESS</span>
        </div>
        <div class="zv-teardown-body">
          <svg class="zv-teardown-svg" viewBox="0 0 840 380" fill="none" xmlns="http://www.w3.org/2000/svg">
            <!-- Column 1: Audio Input & Hardware Drivers -->
            <rect x="20" y="20" width="220" height="290" rx="8" fill="#0c121d" stroke="#38bdf8" stroke-opacity="0.4" stroke-width="1.5"/>
            <rect x="20" y="20" width="220" height="34" rx="8" fill="#141e2f"/>
            <text x="130" y="42" font-family="'Liberation Mono', monospace" font-size="11" font-weight="700" fill="#7dd3fc" text-anchor="middle">1. HARDWARE &amp; DRIVERS</text>
            
            <rect x="35" y="70" width="190" height="52" rx="5" fill="#162238" stroke="#334155" stroke-width="1"/>
            <text x="45" y="90" font-family="'Liberation Sans', sans-serif" font-size="12" font-weight="700" fill="#ffffff">cpal Audio Bridge</text>
            <text x="45" y="106" font-family="'Liberation Mono', monospace" font-size="10" fill="#38bdf8">ALSA · Pulse · PipeWire</text>
            <text x="45" y="117" font-family="'Liberation Mono', monospace" font-size="9" fill="#94a3b8">Low-latency buffer management</text>

            <rect x="35" y="132" width="190" height="56" rx="5" fill="#162238" stroke="#334155" stroke-width="1"/>
            <text x="45" y="152" font-family="'Liberation Sans', sans-serif" font-size="12" font-weight="700" fill="#ffffff">Native GUI Shell</text>
            <text x="45" y="168" font-family="'Liberation Mono', monospace" font-size="10" fill="#34d399">iced 0.14 + kit (GPU)</text>
            <text x="45" y="181" font-family="'Liberation Mono', monospace" font-size="9" fill="#94a3b8">WGPU pipeline · 0 electron overhead</text>

            <rect x="35" y="198" width="190" height="54" rx="5" fill="#162238" stroke="#334155" stroke-width="1"/>
            <text x="45" y="218" font-family="'Liberation Sans', sans-serif" font-size="12" font-weight="700" fill="#ffffff">Automation &amp; MCP</text>
            <text x="45" y="234" font-family="'Liberation Mono', monospace" font-size="10" fill="#ffa5d0">alp-cli · alp-mcp (14 tools)</text>
            <text x="45" y="246" font-family="'Liberation Mono', monospace" font-size="9" fill="#94a3b8">Model Context Protocol server</text>

            <rect x="35" y="262" width="190" height="34" rx="5" fill="#101828" stroke="rgba(56,189,248,0.3)" stroke-width="1"/>
            <text x="130" y="284" font-family="'Liberation Mono', monospace" font-size="10" fill="#7dd3fc" text-anchor="middle">Rust 1.89+ Toolchain</text>

            <!-- Arrow 1 -> 2: Lock-free ringbuffer -->
            <path d="M 240,150 L 290,150" stroke="#38bdf8" stroke-width="2"/>
            <polygon points="295,150 285,145 285,155" fill="#38bdf8"/>
            <text x="267" y="140" font-family="'Liberation Mono', monospace" font-size="9" fill="#38bdf8" text-anchor="middle">Ringbuffer</text>
            <text x="267" y="170" font-family="'Liberation Mono', monospace" font-size="8.5" fill="#94a3b8" text-anchor="middle">Lock-Free</text>

            <!-- Column 2: Real-time Audio Safe Core -->
            <rect x="295" y="20" width="250" height="290" rx="8" fill="#0d1624" stroke="#38bdf8" stroke-opacity="0.6" stroke-width="1.8"/>
            <rect x="295" y="20" width="250" height="34" rx="8" fill="#16243b"/>
            <text x="420" y="42" font-family="'Liberation Mono', monospace" font-size="11" font-weight="700" fill="#ffffff" text-anchor="middle">2. REAL-TIME SAFE CORE</text>

            <rect x="310" y="70" width="220" height="66" rx="5" fill="#14243d" stroke="#34d399" stroke-opacity="0.4" stroke-width="1"/>
            <text x="320" y="90" font-family="'Liberation Sans', sans-serif" font-size="12" font-weight="700" fill="#ffffff">Hard Real-Time Guarantees</text>
            <text x="320" y="106" font-family="'Liberation Mono', monospace" font-size="10" fill="#34d399">ZERO Allocations in Callback</text>
            <text x="320" y="120" font-family="'Liberation Mono', monospace" font-size="9.5" fill="#94a3b8">Zero locks · Zero blocking syscalls</text>
            <text x="320" y="132" font-family="'Liberation Mono', monospace" font-size="9" fill="#e2e8f0">Deterministic latency &lt; 5.3ms</text>

            <rect x="310" y="146" width="220" height="68" rx="5" fill="#14243d" stroke="#38bdf8" stroke-opacity="0.4" stroke-width="1"/>
            <text x="320" y="166" font-family="'Liberation Sans', sans-serif" font-size="12" font-weight="700" fill="#ffffff">CLAP &amp; LV2 Plugin Host</text>
            <text x="320" y="182" font-family="'Liberation Mono', monospace" font-size="10" fill="#38bdf8">alp-plugin engine</text>
            <text x="320" y="196" font-family="'Liberation Mono', monospace" font-size="9.5" fill="#94a3b8">Dynamic C-ABI loading</text>
            <text x="320" y="208" font-family="'Liberation Mono', monospace" font-size="9" fill="#e2e8f0">Pre-allocated scratch buffers</text>

            <rect x="310" y="224" width="220" height="72" rx="5" fill="#14243d" stroke="#38bdf8" stroke-opacity="0.4" stroke-width="1"/>
            <text x="320" y="244" font-family="'Liberation Sans', sans-serif" font-size="12" font-weight="700" fill="#ffffff">32-Bit Float Mixer Matrix</text>
            <text x="320" y="260" font-family="'Liberation Mono', monospace" font-size="10" fill="#ffa5d0">Per-track volume · Pan · Mute · Solo</text>
            <text x="320" y="276" font-family="'Liberation Mono', monospace" font-size="9.5" fill="#94a3b8">Peak &amp; True-RMS meter broadcast</text>

            <!-- Arrow 2 -> 3: IPC to Isolated AI Process -->
            <path d="M 545,150 L 595,150" stroke="#a855f7" stroke-width="2"/>
            <polygon points="600,150 590,145 590,155" fill="#a855f7"/>
            <text x="572" y="140" font-family="'Liberation Mono', monospace" font-size="9" fill="#a855f7" text-anchor="middle">Fork/IPC</text>
            <text x="572" y="170" font-family="'Liberation Mono', monospace" font-size="8.5" fill="#94a3b8" text-anchor="middle">Isolated</text>

            <!-- Column 3: Offline AI Inference Subsystem -->
            <rect x="600" y="20" width="220" height="290" rx="8" fill="#130e1f" stroke="#a855f7" stroke-opacity="0.5" stroke-width="1.5"/>
            <rect x="600" y="20" width="220" height="34" rx="8" fill="#1d1430"/>
            <text x="710" y="42" font-family="'Liberation Mono', monospace" font-size="11" font-weight="700" fill="#c084fc" text-anchor="middle">3. OFFLINE LOCAL AI</text>

            <rect x="615" y="70" width="190" height="66" rx="5" fill="#1e1432" stroke="#a855f7" stroke-opacity="0.4" stroke-width="1"/>
            <text x="625" y="90" font-family="'Liberation Sans', sans-serif" font-size="12" font-weight="700" fill="#ffffff">Out-of-Process Core</text>
            <text x="625" y="106" font-family="'Liberation Mono', monospace" font-size="10" fill="#c084fc">alp-infer standalone binary</text>
            <text x="625" y="122" font-family="'Liberation Mono', monospace" font-size="9.5" fill="#94a3b8">Audio thread NEVER stutters</text>

            <rect x="615" y="148" width="190" height="66" rx="5" fill="#1e1432" stroke="#a855f7" stroke-opacity="0.4" stroke-width="1"/>
            <text x="625" y="168" font-family="'Liberation Sans', sans-serif" font-size="12" font-weight="700" fill="#ffffff">ONNX &amp; GGUF Engines</text>
            <text x="625" y="184" font-family="'Liberation Mono', monospace" font-size="10" fill="#38bdf8">VoiceStudio clone weights</text>
            <text x="625" y="200" font-family="'Liberation Mono', monospace" font-size="9.5" fill="#34d399">646 languages · 0 cloud latency</text>

            <rect x="615" y="226" width="190" height="70" rx="5" fill="#1e1432" stroke="#a855f7" stroke-opacity="0.4" stroke-width="1"/>
            <text x="625" y="246" font-family="'Liberation Sans', sans-serif" font-size="12" font-weight="700" fill="#ffffff">Master WAV/FLAC Out</text>
            <text x="625" y="264" font-family="'Liberation Mono', monospace" font-size="10" fill="#facc15">Lossless export to NVMe</text>
            <text x="625" y="282" font-family="'Liberation Mono', monospace" font-size="9" fill="#94a3b8">Bithooks &amp; metadata intact</text>

            <!-- Bottom Airgap Shield -->
            <rect x="20" y="325" width="800" height="38" rx="6" fill="#082015" stroke="#22c55e" stroke-opacity="0.6" stroke-width="1"/>
            <text x="420" y="348" font-family="'Liberation Mono', monospace" font-size="11" font-weight="700" fill="#4ade80" text-anchor="middle">✔ ZERO AUDIO EGRESS: MICROPHONE STREAMS AND SYNTHESIS BUFFERS REMAIN 100% IN LOCAL MEMORY</text>
          </svg>
        </div>
      </div>

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

    <nav class="zv-project-navigation" aria-label="Project navigation">
      <a href="{{ '/projects/eep/' | relative_url }}" class="zv-section-link">
        &larr; Previous: Easy Edits Pro
      </a>
      <a href="{{ '/projects/ytf/' | relative_url }}" class="zv-section-link">
        Next Project: Your TV Friend &rarr;
      </a>
    </nav>

  </article>


</div>
