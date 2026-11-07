---
layout: default
title: Your TV Friend | Zvirox
description: A non-destructive Android TV cleanup tool and Your UI, a native television launcher, with reversible ADB-based package controls.
permalink: /projects/ytf/
image: "/assets/images/projects/your-tv-friend-mockup.png"
---

<script type="application/ld+json">
{
  "@context": "https://schema.org",
  "@type": "SoftwareApplication",
  "name": "Your TV Friend",
  "operatingSystem": "Android TV",
  "applicationCategory": "UtilitiesApplication",
  "description": "A non-destructive Android TV cleanup tool and native television launcher (Your UI) with reversible ADB-based package controls, 5 visual themes, and 26 supported languages.",
  "url": "https://zvirox.in/projects/ytf/",
  "downloadUrl": "https://github.com/zvirox/your-tv-friend",
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
        <img class="zv-project-image" src="{{ '/assets/images/projects/your-tv-friend-mockup.png' | relative_url }}" alt="Your TV Friend Your UI concept screen with For You recommendations, five round glass controls, and a translucent app shelf over a cinematic landscape." width="1200" height="675" loading="lazy" decoding="async">
        <figcaption class="zv-project-caption">Concept mockup inspired by Your UI's Glass UI home-screen layout.</figcaption>
      </figure>
    </section>

    <div class="zv-post-content zv-project-content">
      <h2>Overview</h2>
      <p>
        <strong>Your TV Friend</strong> is an open-source Android TV project with two parts: non-destructive,
        reversible cleanup tools and <strong>Your UI</strong>, a native television launcher for Android 8.0 and newer.
      </p>

      <h2>Two Core Components & System Architecture</h2>
      <p>
        Your TV Friend decouples system-level package optimization from the visual television interface, ensuring rootless safety and zero brick risk:
      </p>

      <!-- Architecture Teardown Diagram -->
      <div class="zv-teardown-schematic" aria-label="Your TV Friend Architecture Teardown">
        <div class="zv-teardown-header">
          <div class="zv-teardown-title-wrap">
            <span class="zv-teardown-category">DEBLOATER &amp; LAUNCHER TEARDOWN</span>
            <span class="zv-teardown-subtitle">Pure-Python ADB Client · Non-Destructive pm disable · Your UI Native Launcher</span>
          </div>
          <span class="zv-teardown-shield">🔒 ROOTLESS REVERSIBLE</span>
        </div>
        <div class="zv-teardown-body">
          <svg class="zv-teardown-svg" viewBox="0 0 840 380" fill="none" xmlns="http://www.w3.org/2000/svg">
            <!-- Column 1: Control Station (Host) -->
            <rect x="20" y="20" width="220" height="290" rx="8" fill="#0d1410" stroke="#34d399" stroke-opacity="0.4" stroke-width="1.5"/>
            <rect x="20" y="20" width="220" height="34" rx="8" fill="#14211a"/>
            <text x="130" y="42" font-family="'Liberation Mono', monospace" font-size="11" font-weight="700" fill="#6ee7b7" text-anchor="middle">1. CONTROL STATION</text>
            
            <rect x="35" y="70" width="190" height="52" rx="5" fill="#15261d" stroke="#334155" stroke-width="1"/>
            <text x="45" y="90" font-family="'Liberation Sans', sans-serif" font-size="12" font-weight="700" fill="#ffffff">Pure-Python ADB Client</text>
            <text x="45" y="106" font-family="'Liberation Mono', monospace" font-size="10" fill="#34d399">Standalone command hub</text>
            <text x="45" y="117" font-family="'Liberation Mono', monospace" font-size="9" fill="#94a3b8">Zero android-tools dependency</text>

            <rect x="35" y="132" width="190" height="56" rx="5" fill="#15261d" stroke="#334155" stroke-width="1"/>
            <text x="45" y="152" font-family="'Liberation Sans', sans-serif" font-size="12" font-weight="700" fill="#ffffff">297 Device Profiles</text>
            <text x="45" y="168" font-family="'Liberation Mono', monospace" font-size="10" fill="#38bdf8">Xiaomi · TCL · Sony · Chromecast</text>
            <text x="45" y="181" font-family="'Liberation Mono', monospace" font-size="9" fill="#94a3b8">Tested OEM bloatware signatures</text>

            <rect x="35" y="198" width="190" height="54" rx="5" fill="#15261d" stroke="#334155" stroke-width="1"/>
            <text x="45" y="218" font-family="'Liberation Sans', sans-serif" font-size="12" font-weight="700" fill="#ffffff">Transport Options</text>
            <text x="45" y="234" font-family="'Liberation Mono', monospace" font-size="10" fill="#ffa5d0">Wireless ADB (TCP 5555)</text>
            <text x="45" y="246" font-family="'Liberation Mono', monospace" font-size="9" fill="#94a3b8">USB OTG Cable fallback</text>

            <rect x="35" y="262" width="190" height="34" rx="5" fill="#0f1c15" stroke="rgba(52,211,153,0.3)" stroke-width="1"/>
            <text x="130" y="284" font-family="'Liberation Mono', monospace" font-size="10" fill="#6ee7b7" text-anchor="middle">Airgapped Local Subnet</text>

            <!-- Arrow 1 -> 2: ADB Shell Protocol -->
            <path d="M 240,150 L 290,150" stroke="#34d399" stroke-width="2"/>
            <polygon points="295,150 285,145 285,155" fill="#34d399"/>
            <text x="267" y="140" font-family="'Liberation Mono', monospace" font-size="9" fill="#34d399" text-anchor="middle">ADB Shell</text>
            <text x="267" y="170" font-family="'Liberation Mono', monospace" font-size="8.5" fill="#94a3b8" text-anchor="middle">Rootless</text>

            <!-- Column 2: Android TV System & Package Manager -->
            <rect x="295" y="20" width="250" height="290" rx="8" fill="#0c1813" stroke="#34d399" stroke-opacity="0.6" stroke-width="1.8"/>
            <rect x="295" y="20" width="250" height="34" rx="8" fill="#14261e"/>
            <text x="420" y="42" font-family="'Liberation Mono', monospace" font-size="11" font-weight="700" fill="#ffffff" text-anchor="middle">2. ANDROID OS FRAMEWORK</text>

            <rect x="310" y="70" width="220" height="66" rx="5" fill="#132a1f" stroke="#34d399" stroke-opacity="0.4" stroke-width="1"/>
            <text x="320" y="90" font-family="'Liberation Sans', sans-serif" font-size="12" font-weight="700" fill="#ffffff">Reversible Memory Filter</text>
            <text x="320" y="106" font-family="'Liberation Mono', monospace" font-size="10" fill="#34d399">pm disable-user --user 0</text>
            <text x="320" y="120" font-family="'Liberation Mono', monospace" font-size="9.5" fill="#94a3b8">Bypasses system partition write</text>
            <text x="320" y="132" font-family="'Liberation Mono', monospace" font-size="9" fill="#a7f3d0">Zero brick risk · 100% reversible</text>

            <rect x="310" y="146" width="220" height="68" rx="5" fill="#132a1f" stroke="#38bdf8" stroke-opacity="0.4" stroke-width="1"/>
            <text x="320" y="166" font-family="'Liberation Sans', sans-serif" font-size="12" font-weight="700" fill="#ffffff">OEM Telemetry Neutralized</text>
            <text x="320" y="182" font-family="'Liberation Mono', monospace" font-size="10" fill="#ef4444">[DISABLED] Ad Sinks &amp; Daemons</text>
            <text x="320" y="196" font-family="'Liberation Mono', monospace" font-size="9.5" fill="#94a3b8">Stops telemetry packet beaconing</text>
            <text x="320" y="208" font-family="'Liberation Mono', monospace" font-size="9" fill="#e2e8f0">Frees 350MB–800MB active RAM</text>

            <rect x="310" y="224" width="220" height="72" rx="5" fill="#132a1f" stroke="#38bdf8" stroke-opacity="0.4" stroke-width="1"/>
            <text x="320" y="244" font-family="'Liberation Sans', sans-serif" font-size="12" font-weight="700" fill="#ffffff">Package Verification State</text>
            <text x="320" y="260" font-family="'Liberation Mono', monospace" font-size="10" fill="#ffa5d0">Original APKs safely dormant</text>
            <text x="320" y="276" font-family="'Liberation Mono', monospace" font-size="9.5" fill="#94a3b8">Instant 1-click restore command</text>

            <!-- Arrow 2 -> 3: Intent Handshake -->
            <path d="M 545,150 L 595,150" stroke="#38bdf8" stroke-width="2"/>
            <polygon points="600,150 590,145 590,155" fill="#38bdf8"/>
            <text x="572" y="140" font-family="'Liberation Mono', monospace" font-size="9" fill="#38bdf8" text-anchor="middle">CATEGORY_HOME</text>
            <text x="572" y="170" font-family="'Liberation Mono', monospace" font-size="8.5" fill="#94a3b8" text-anchor="middle">Direct Hook</text>

            <!-- Column 3: Your UI Launcher -->
            <rect x="600" y="20" width="220" height="290" rx="8" fill="#0d141d" stroke="#38bdf8" stroke-opacity="0.5" stroke-width="1.5"/>
            <rect x="600" y="20" width="220" height="34" rx="8" fill="#152132"/>
            <text x="710" y="42" font-family="'Liberation Mono', monospace" font-size="11" font-weight="700" fill="#38bdf8" text-anchor="middle">3. YOUR UI (NATIVE)</text>

            <rect x="615" y="70" width="190" height="66" rx="5" fill="#16253c" stroke="#34d399" stroke-opacity="0.4" stroke-width="1"/>
            <text x="625" y="90" font-family="'Liberation Sans', sans-serif" font-size="12" font-weight="700" fill="#ffffff">Clean Native Java</text>
            <text x="625" y="106" font-family="'Liberation Mono', monospace" font-size="10" fill="#34d399">Lean APK under 12MB</text>
            <text x="625" y="122" font-family="'Liberation Mono', monospace" font-size="9.5" fill="#94a3b8">Runs 60fps on 1GB RAM TVs</text>

            <rect x="615" y="148" width="190" height="66" rx="5" fill="#16253c" stroke="#34d399" stroke-opacity="0.4" stroke-width="1"/>
            <text x="625" y="168" font-family="'Liberation Sans', sans-serif" font-size="12" font-weight="700" fill="#ffffff">5 Custom Visual Styles</text>
            <text x="625" y="184" font-family="'Liberation Mono', monospace" font-size="10" fill="#38bdf8">Glass UI · Material 3</text>
            <text x="625" y="200" font-family="'Liberation Mono', monospace" font-size="9.5" fill="#94a3b8">Win UI · Classic · Minimal</text>

            <rect x="615" y="226" width="190" height="70" rx="5" fill="#16253c" stroke="#34d399" stroke-opacity="0.4" stroke-width="1"/>
            <text x="625" y="246" font-family="'Liberation Sans', sans-serif" font-size="12" font-weight="700" fill="#ffffff">26 Global Languages</text>
            <text x="625" y="264" font-family="'Liberation Mono', monospace" font-size="10" fill="#facc15">Zero tracking analytics</text>
            <text x="625" y="282" font-family="'Liberation Mono', monospace" font-size="9" fill="#94a3b8">Total privacy for living rooms</text>

            <!-- Bottom Airgap Shield -->
            <rect x="20" y="325" width="800" height="38" rx="6" fill="#082015" stroke="#22c55e" stroke-opacity="0.6" stroke-width="1"/>
            <text x="420" y="348" font-family="'Liberation Mono', monospace" font-size="11" font-weight="700" fill="#4ade80" text-anchor="middle">✔ ROOTLESS SAFETY: ZERO SYSTEM PARTITION REWRITING · RESTORABLE AT ANY TIME VIA ADB</text>
          </svg>
        </div>
      </div>
      
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
