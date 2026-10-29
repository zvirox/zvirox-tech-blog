---
layout: default
title: Easy Edits Pro | Zvirox
description: An alpha-stage Linux desktop video editor built with Rust, Tauri, React, and GStreamer. Combines multitrack editing with a Rust-owned project model.
permalink: /projects/eep/
---

<div class="zv-container">

  <article class="zv-post" style="max-width: 960px; margin: 0 auto;">

    <!-- Breadcrumb -->
    <div style="margin-bottom: 24px; color: var(--zv-text-muted); font-size: 14px;">
      <a href="{{ '/' | relative_url }}" style="color: var(--zv-text-secondary);">Home</a> &rarr; 
      <a href="{{ '/projects/' | relative_url }}" style="color: var(--zv-text-secondary);">Projects</a> &rarr; 
      <span style="color: var(--zv-text);">Easy Edits Pro</span>
    </div>

    <!-- Header -->
    <header class="zv-post-header" style="margin-bottom: 40px;">
      <div class="zv-card-category">
        DESKTOP VIDEO EDITOR • ACTIVE ALPHA DEVELOPMENT
      </div>

      <h1 class="zv-post-title">
        Easy Edits Pro
      </h1>

      <p class="zv-post-description">
        An alpha-stage Linux desktop video editor built with Rust, Tauri, React, and GStreamer. 
        It combines a multitrack editing workflow with a Rust-owned project model and automation interfaces.
      </p>

      <div style="margin: 20px 0; display: flex; flex-wrap: wrap; gap: 8px;">
        <span class="zv-tag">Rust</span>
        <span class="zv-tag">Tauri</span>
        <span class="zv-tag">React</span>
        <span class="zv-tag">GStreamer</span>
        <span class="zv-tag">Linux</span>
      </div>

      <div class="zv-post-meta" style="margin-top: 20px; display: flex; gap: 16px; align-items: center;">
        <a href="https://github.com/zvirox/easy-edits-pro" target="_blank" rel="noopener noreferrer" class="zv-button zv-button-primary" style="min-height: 38px; padding: 0 16px; font-size: 13px;">
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
        The application is structured around a strict separation of concerns:
      </p>
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

    <!-- Navigation Footer -->
    <div style="margin-top: 60px; padding-top: 30px; border-top: 1px solid var(--zv-border); display: flex; justify-content: space-between; align-items: center;">
      <a href="{{ '/projects/' | relative_url }}" class="zv-section-link">
        &larr; Back to Projects Index
      </a>
      <a href="{{ '/projects/alp/' | relative_url }}" class="zv-section-link">
        Next Project: Audio Labs Pro &rarr;
      </a>
    </div>

  </article>

</div>
