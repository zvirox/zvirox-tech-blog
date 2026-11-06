---
layout: default
title: Guides & Engineering Notes | Zvirox
description: Technical guides, system architecture notes, network protocol explainers, and local AI engineering write-ups from Zvirox.
permalink: /guides/
redirect_from:
  - /articles/
  - /articles/index.html
---

<div class="zv-container">

  <!-- =====================================================
       HERO SECTION
       ===================================================== -->

  <section class="zv-about-hero">

    <div class="zv-about-hero-content">

      <div class="zv-card-category">
        DOCUMENTATION • SYSTEMS • LINUX
      </div>

      <h1 class="zv-about-hero-title">
        Guides & Engineering Notes.
        <span>Practical & Tested.</span>
      </h1>

      <p class="zv-about-hero-lead">
        In-depth explanations of network protocols, Linux administration, audio engineering, 
        and local AI coding agents. Notes and guides written by the maintainer.
      </p>

    </div>

  </section>


  <!-- =====================================================
       TOPIC EXPLORER (MOVED FROM HOMEPAGE)
       ===================================================== -->

  <section class="zv-section">

    <div class="zv-section-header">
      <div>
        <div class="zv-card-category">
          TOPIC HUBS
        </div>
        <h2 class="zv-section-title">
          Explore by Category
        </h2>
      </div>
      <a href="{{ '/categories/' | relative_url }}" class="zv-section-link">
        All categories →
      </a>
    </div>

    <div class="zv-article-grid">

      <!-- Voice & Audio AI -->
      <article class="zv-card zv-card-ai">
        <div class="zv-card-body">
          <div class="zv-card-category">
            VOICE & AUDIO AI
          </div>
          <h3 class="zv-card-title">
            Voice & Audio AI
          </h3>
          <p class="zv-card-excerpt">
            Local voice cloning, text-to-speech, audio dubbing, and privacy-first audio tooling running on your own hardware.
          </p>
          <a href="{{ '/categories/voice-ai/' | relative_url }}" class="zv-section-link">
            Explore topic →
          </a>
        </div>
      </article>

      <!-- AI & Agents -->
      <article class="zv-card zv-card-ai">
        <div class="zv-card-body">
          <div class="zv-card-category">
            AI & AGENTS
          </div>
          <h3 class="zv-card-title">
            AI & Coding Agents
          </h3>
          <p class="zv-card-excerpt">
            Model-agnostic development, BYOK workflows, MCP integrations, and how open-source agents compare.
          </p>
          <a href="{{ '/categories/ai/' | relative_url }}" class="zv-section-link">
            Explore topic →
          </a>
        </div>
      </article>

      <!-- Networking -->
      <article class="zv-card">
        <div class="zv-card-body">
          <div class="zv-card-category">
            NETWORKING
          </div>
          <h3 class="zv-card-title">
            Networking & Protocols
          </h3>
          <p class="zv-card-excerpt">
            The OSI model, DNS resolution, DHCP leasing, and understanding how internet packets travel.
          </p>
          <a href="{{ '/categories/networking/' | relative_url }}" class="zv-section-link">
            Explore topic →
          </a>
        </div>
      </article>

      <!-- Linux -->
      <article class="zv-card">
        <div class="zv-card-body">
          <div class="zv-card-category">
            LINUX
          </div>
          <h3 class="zv-card-title">
            Linux Systems
          </h3>
          <p class="zv-card-excerpt">
            Secure Shell (SSH) configuration, Linux command-line utilities, server administration, and desktops.
          </p>
          <a href="{{ '/categories/linux/' | relative_url }}" class="zv-section-link">
            Explore topic →
          </a>
        </div>
      </article>

      <!-- Cybersecurity -->
      <article class="zv-card">
        <div class="zv-card-body">
          <div class="zv-card-category">
            SECURITY
          </div>
          <h3 class="zv-card-title">
            Cybersecurity & Defense
          </h3>
          <p class="zv-card-excerpt">
            Defensive security fundamentals, threat analysis, access controls, and network hardening techniques.
          </p>
          <a href="{{ '/categories/cybersecurity/' | relative_url }}" class="zv-section-link">
            Explore topic →
          </a>
        </div>
      </article>

      <!-- IT & Infrastructure -->
      <article class="zv-card">
        <div class="zv-card-body">
          <div class="zv-card-category">
            IT
          </div>
          <h3 class="zv-card-title">
            IT & Systems
          </h3>
          <p class="zv-card-excerpt">
            Practical systems administration, troubleshooting methodologies, and infrastructure setup.
          </p>
          <a href="{{ '/categories/it/' | relative_url }}" class="zv-section-link">
            Explore topic →
          </a>
        </div>
      </article>

    </div>

  </section>


  <!-- =====================================================
       ALL GUIDES LIST
       ===================================================== -->

  <section class="zv-section">

    <div class="zv-section-header">
      <div>
        <div class="zv-card-category">
          COMPLETE ARCHIVE
        </div>
        <h2 class="zv-section-title">
          All Guides
        </h2>
      </div>
      <span style="font-size:13px; color:var(--zv-text-muted);">
        {{ site.posts.size }} guides published
      </span>
    </div>

    {% if site.posts.size > 0 %}

      <div class="zv-article-grid">

        {% for post in site.posts %}

          <article class="zv-card">

            <div class="zv-card-body">

              {% if post.categories and post.categories.size > 0 %}
                <div class="zv-card-category">
                  {{ post.categories | first }}
                </div>
              {% endif %}

              <h3 class="zv-card-title">
                <a href="{{ post.url | relative_url }}">
                  {{ post.title }}
                </a>
              </h3>

              {% if post.description %}
                <p class="zv-card-excerpt">
                  {{ post.description }}
                </p>
              {% elsif post.excerpt %}
                <p class="zv-card-excerpt">
                  {{ post.excerpt | strip_html | truncate: 150 }}
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

      </div>

    {% else %}

      <div class="zv-panel">
        <h2 class="zv-panel-title">No guides yet</h2>
        <p>Guides are being compiled and will appear here shortly.</p>
      </div>

    {% endif %}

  </section>

</div>
