# Zvirox Web (`zvirox-tech-dev`)

[![Site Status](https://img.shields.io/website?url=https%3A%2F%2Fzvirox.in&label=zvirox.in&style=flat-square)](https://zvirox.in)
[![GitHub Pages](https://img.shields.io/badge/deployment-GitHub%20Pages-blue?style=flat-square&logo=github)](https://zvirox.in)
[![Maintainer](https://img.shields.io/badge/maintainer-@Prakash-ff50a6?style=flat-square)](https://github.com/zvirox)
[![License: MIT](https://img.shields.io/badge/license-MIT-green?style=flat-square)](LICENSE)

> The official website and engineering documentation hub for **[Zvirox](https://zvirox.in)** — showcasing open-source desktop and TV software crafted for Linux and Android TV, built by solo maintainer **Prakashpuri Gauswami** (@Prakash).

---

## 🚀 Overview

`zvirox-tech-dev` powers [zvirox.in](https://zvirox.in), an independent project site presenting four local-first, privacy-respecting open-source applications alongside in-depth systems engineering guides:

1. **[Easy Edits Pro (EEP)](https://zvirox.in/projects/eep/)** — Active alpha Linux desktop video editor combining a multitrack timeline with a Rust-owned project model, GStreamer backend, and Model Context Protocol (MCP) automation. *(AGPL-3.0 + Commercial option)*
2. **[Audio Labs Pro (ALP)](https://zvirox.in/projects/alp/)** — Alpha v0.0.1 Linux audio studio built with Rust and iced for multitrack recording and editing. Features offline local AI voice tools and a 14-tool MCP automation server. *(Apache-2.0)*
3. **[Screen Studio Pro (SSP)](https://zvirox.in/projects/ssp/)** — Planned open-source Wayland screen recorder for Linux with a frosted-glass interface, PipeWire capture, webcam picture-in-picture, and hardware-first encoding. *(MIT — Planning phase)*
4. **[Your TV Friend (YTF)](https://zvirox.in/projects/ytf/)** — v0.0.3 Android TV non-destructive debloater and 5-theme customizable television launcher (*Your UI*) with reversible ADB controls. *(MIT)*

---

## 🛠️ Architecture & Tech Stack

- **Static Site Generator:** [Jekyll 4](https://jekyllrb.com/) hosted on **GitHub Pages**
- **Domain:** Custom apex domain `zvirox.in` with HTTPS enforced via GitHub Pages
- **Design System:** Custom VoiceStudio-inspired dark aesthetic (`#0a0a0a` deep surface, `#ff50a6` signature accent, high-contrast typography, and glassmorphism elements)
- **Styling:** Custom SCSS (`assets/css/style.scss`) compiled via Dart Sass with responsive grid layouts and `@media (prefers-reduced-motion)` compliance
- **Privacy-First:** Zero third-party analytics, zero ad beacons, zero telemetry. Browser `localStorage` is used exclusively for theme preference (`zvirox-theme: dark | light`).
- **Jekyll Plugins:**
  - `jekyll-feed` — Atom RSS feed generation (`/feed.xml`)
  - `jekyll-sitemap` — Automated root sitemap (`/sitemap.xml`)
  - `jekyll-seo-tag` — Open Graph, Twitter Cards, and schema markup
  - `jekyll-redirect-from` — Server-side redirect handling for clean canonical URLs

---

## 📁 Repository Structure

```text
zvirox-tech-dev/
├── _config.yml               # Jekyll site configuration & plugin definitions
├── CNAME                     # Custom apex domain configuration (zvirox.in)
├── robots.txt                # Search engine crawler directives & sitemap pointers
├── index.md                  # Homepage: Hero, 4-project grid, Why Zvirox, Proof metrics
├── about.md                  # About maintainer narrative, mission & verification block
├── contact.md                # Contact channels, GitHub issue trackers & security policy
├── licensing.md              # Per-project licenses & AGPL-3.0 commercial dual-licensing
├── privacy.md                # Truthful per-application privacy statement (DPDP Act 2023)
├── terms.md                  # Plain-language website terms of service & trademark policy
├── cookies.md                # Transparent cookie statement (localStorage theme only)
├── sitemap/
│   ├── sitemap.xml           # Google Search Console XML sitemap (canonical 200 URLs)
│   └── index.html            # User-facing HTML visual sitemap
├── projects/
│   ├── index.md              # Projects portfolio showcase
│   ├── eep.md                # Easy Edits Pro detailed specification
│   ├── alp.md                # Audio Labs Pro detailed specification
│   ├── ssp.md                # Screen Studio Pro detailed specification
│   └── ytf.md                # Your TV Friend detailed specification
├── guides/
│   └── index.md              # Technical guides hub & topic explorer (was /articles/)
├── categories/
│   ├── index.md              # All categories directory
│   ├── voice-audio-ai/       # Voice & Audio AI guides (clean slug, no %20)
│   ├── ai/                   # AI & coding agents guides
│   ├── networking/           # Network protocols & architecture
│   ├── linux/                # Linux systems & administration
│   ├── cybersecurity/        # Defensive security fundamentals
│   ├── it/                   # IT infrastructure & troubleshooting
│   └── development/          # Software development notes
├── _posts/                   # 9 published technical guides & architectural articles
├── _layouts/
│   ├── default.html          # Global layout (header, mobile drawer, 4-column footer)
│   ├── post.html             # Article layout with dynamic table of contents
│   └── category.html         # Category archive layout
└── assets/
    ├── css/style.scss        # Master stylesheet & custom CSS variables
    └── images/               # Logos, mockups, screenshots & media assets
```

---

## 🔍 Google Search Console & SEO

This website includes a dedicated, validated XML sitemap structured for **Google Search Console** and Bing Webmaster Tools:

- **Primary Submission URL:** `https://zvirox.in/sitemap/sitemap.xml`
- **Fallback URL:** `https://zvirox.in/sitemap.xml`
- **Visual Directory:** `https://zvirox.in/sitemap/`

### Features:
- 100% canonical HTTPS endpoints with accurate W3C `lastmod` timestamps.
- Zero broken links, zero 404s, and zero redirected URLs.
- Legacy URLs (`/articles/` and `/voice%20ai/`) seamlessly forward to canonical endpoints via `jekyll-redirect-from` and meta-refresh fallbacks.
- Open Graph and Schema.org metadata verified via `jekyll-seo-tag`.

---

## 💻 Local Development

### 1. Clone the Repository
```bash
git clone git@github.com:zvirox/zvirox-tech-dev.git
cd zvirox-tech-dev
```

### 2. Compile Stylesheet (Dart Sass)
```bash
npx --yes sass assets/css/style.scss assets/css/style.css
```

### 3. Build & Run Locally (Jekyll)
If Ruby and Bundler are installed:
```bash
bundle install
bundle exec jekyll serve --livereload
```
Preview at `http://localhost:4000/`.

---

## 📜 Licensing

- **Website Source & Content:** Copyright © 2026 Prakashpuri Gauswami. Released under the [MIT License](LICENSE).
- **Associated Software Repositories:**
  - [Easy Edits Pro](https://github.com/zvirox/easy-edits-pro): GNU Affero General Public License v3.0 ([AGPL-3.0](https://www.gnu.org/licenses/agpl-3.0.html)) + Commercial License available on request.
  - [Audio Labs Pro](https://github.com/zvirox/audio-labs-pro): Apache License 2.0 ([Apache-2.0](https://www.apache.org/licenses/LICENSE-2.0)).
  - [Screen Studio Pro](https://github.com/zvirox/screen-studio-pro): MIT License ([MIT](https://opensource.org/licenses/MIT)).
  - [Your TV Friend](https://github.com/zvirox/your-tv-friend): MIT License ([MIT](https://opensource.org/licenses/MIT)).

For complete details, visit the [Licensing Page](https://zvirox.in/licensing/).

---

## 👤 Maintainer Verification

- **Maintainer:** Prakashpuri Gauswami (@Prakash)
- **Role:** Solo Maintainer & Creator
- **Location:** Gujarat, India
- **Official Domain:** [zvirox.in](https://zvirox.in)
- **Email:** [info@zvirox.in](mailto:info@zvirox.in)
- **GitHub:** [@zvirox](https://github.com/zvirox)
