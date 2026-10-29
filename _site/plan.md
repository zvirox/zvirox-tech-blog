# TechBlog Plan — Voice AI & AI Coding Agent Feature Report

This document contains a reverse-engineering analysis of **VoiceStudio (voicestudio.sh)** and **Kilo AI (kilo.ai)**, plus a phasewise implementation plan for the Zvirox TechBlog.

---

## Part 1 — Web App Reverse Engineering Reports

---

## 1. VoiceStudio (https://voicestudio.sh/)

### 1.1 Product Overview

| Attribute | Value |
|-----------|-------|
| **Product** | VoiceStudio — Open Source AI Voice Studio |
| **Tagline** | Free Open-Source AI Voice Cloning & Dubbing |
| **Former name** | OmniVoice Studio |
| **License** | AGPL-3.0 (open source), Pro (commercial seat), Cloud (hosted) |
| **GitHub** | debpalash/VoiceStudio — 50,000+ stars |
| **Latest release** | v0.5.6 (observed 30 Sept 2026) |
| **Languages** | 646 languages |
| **Downloads** | ~596,000 GitHub releases · 103,171+ Docker Hub · 40,443+ GHCR |
| **Platforms** | Windows 10/11 x64, macOS (Apple Silicon + Intel), Linux, Docker |
| **Deployment** | Fully-local (runs on your machine) |

### 1.2 Core Functionality

| # | Feature | Description |
|---|---------|-------------|
| 01 | **Voice Clone** | Mirror a voice from just three seconds of audio |
| 02 | **Voice Design** | Describe a voice in text — generate it |
| 03 | **Video Dubbing** | Dub any video into any language, preserving original timing |
| 04 | **Stories** | Cast a script; voice every role with distinct voices |
| 05 | **Audiobook** | A book in → chapters out (audiobook creation pipeline) |
| 06 | **Voice Gallery** | Ready-made voices to try out |
| 07 | **Transcripts** | Audio in → searchable text out |
| — | **WorkflowStudio** | Desktop workflow app (switchable with VoiceStudio) |
| — | **Local API** | Programmatic access to voice features locally |
| — | **Pro Cloud** | Hosted cloud option (early access, coming soon) |

### 1.3 Pricing & Editions

| Edition | Cost | License | Use Case |
|---------|------|---------|----------|
| **OSS (Open Source)** | Free | AGPL-3.0 | Personal / local use |
| **Pro** | $99/year or $299 once | Commercial seat | 1 user, 3 devices, 7-day refund |
| **Cloud** | Credits from $6 | Hosted | Early access, managed |

### 1.4 UI / Visual Implementation Notes

- **Theme:** Dark-first, minimalist, high-contrast
- **Color palette:** Near-black backgrounds (`#141414`-family), white/off-white text, subtle borders (`border-white/10`)
- **Layout:** Left-aligned hero with feature cards, screenshot gallery, comparison table
- **Key UI sections:**
  - **Hero:** "Open Source AI Voice Studio" — fully-local voice cloning, design, dubbing, dictation, transcription, audiobook creation in 646 languages
  - **Install banner:** Free · Open source · Windows/macOS/Linux/Docker with copyable PowerShell install command
  - **Feature carousel:** 7 numbered features (Voice clone, Voice design, Video dubbing, Stories, Audiobook, Voice gallery, Transcripts) with `← →` navigation between `voicestudio` and `workflowstudio` modes
  - **Screenshot gallery:** 13 in-app screenshots (Launchpad, Voice Design, Projects, Quick engine switch, Updates, Studio, Voice Clone, Local API, Logs, Voice Gallery, Dubbing Model Catalogue, Settings) with hover-to-magnify and pause-motion controls
  - **Pro section:** "Pro is for professionals" — Limitless creation, full control, multiple devices, remote devices, early access, +12 more features
  - **Comparison table:** VoiceStudio OSS/Pro/Cloud vs ElevenLabs Cloud (source, cost, commercial use, languages, audio privacy)
  - **Adoption stats:** Downloads, GitHub stars, Docker/GHCR counts, release version
  - **Social proof:** YouTube testimonials with view counts, LinkedIn endorsement
- **CSS class patterns:** BEM-ish hashed classes (e.g., `_actions_1ty8g_155`, `_card_1ty8g_80`, `_badge_1jz33_22`), utility classes like `bg-[#141414]`, `border-white/10`, `bg-white/5`

### 1.5 Key Technical Behaviors Observed

- Local-first architecture: audio stays on user's machine (privacy differentiator vs ElevenLabs)
- Docker-native distribution alongside platform installers
- Engine switching UI (quick engine switch) — suggests multiple TTS/voice-backend support
- OpenAPI docs exposed (`/img/screenshots/openapi.webp`) — indicates REST API surface
- Version badge and live-refreshing star/download counters
- AGPL-3.0 OSS with optional commercial Pro seat

---

## 2. Kilo AI (https://kilo.ai/)

### 2.1 Product Overview

| Attribute | Value |
|-----------|-------|
| **Product** | Kilo — Open Source AI Coding Agent |
| **Tagline** | One open agent for every developer workflow |
| **License** | MIT (open source, self-hostable) |
| **Models** | 500+ models at zero markup (frontier, open-weight, own keys, local) |
| **Trust signals** | Meta, Amazon, Airbnb, PayPal, Square, Red Hat |
| **Adoption** | 5M+ Kilo Coders · 10T+ tokens processed monthly |
| **Accolade** | #1 Open Source Product of the Month |

### 2.2 Core Functionality

| Category | Features |
|----------|----------|
| **Code Agent** | Write, refactor, ship production-ready code with full codebase understanding |
| **Plan Agent** | Plan complex features with structured guidance before writing code |
| **Debug Agent** | Identify and fix bugs fast — reads errors, traces issues, suggests fixes |
| **Auto Model** | Routes to Efficient / Frontier / Free model based on budget and task |
| **Kilo Desktop** | Desktop app (Beta) for macOS, Windows, Linux — run agents side by side |
| **IDE Integrations** | VS Code (Open VSX), JetBrains (IntelliJ, PyCharm, WebStorm) |
| **CLI** | Kilo in any shell, script, or CI job (`curl -fsSL https://kilo.ai/cli/install \| bash`) |
| **Cloud** | Start agents from any browser (Try Cloud free) |
| **Slack** | Mention @Kilo in any channel |
| **Mobile** | Follow and review agents from phone |
| **Gateway** | Model gateway — inspect prompts, context window, decisions; no silent model switching |

### 2.3 Pricing & Model Access

- **Zero markup** on model inference — models at cost
- **Bring your own keys** (BYOK)
- **Local models supported** for privacy
- **Free tier** available (no credit card required)
- **Enterprise:** Free for up to a year for Cursor migrants (promotional)

### 2.4 UI / Visual Implementation Notes

- **Theme:** Dark-first (`bg-[#0e0e0e]`, `bg-[#121212]`, `bg-[#141414]`, `bg-[#181818]`, `bg-[#262626]`)
- **Color palette:** Near-black backgrounds, brand-primary accent (`bg-brand-primary`, `text-brand-primary`), subtle borders (`bg-border/30`)
- **CSS framework:** Tailwind-style utility classes (`animate-pulse`, `backdrop-blur-xl`, `rounded-full`, `transition-all`)
- **Key UI sections:**
  - **Hero:** "One open agent for every developer workflow" — 500+ models, zero markup; free AI agent for VS Code and terminal
  - **Product nav:** GitHub, Product, Models, Enterprise, Resources, Pricing, Sign in, Contact sales, Get Started
  - **Get Kilo section:** Kilo Desktop (Beta) for macOS/Windows/Linux; web-app demo ("Fix flaky checkout test")
  - **IDE integrations:** VS Code (Install extension, Open VSX), JetBrains (Get plugin), CLI (curl install command), Cloud (Try Cloud free), Slack (Add to Slack), Mobile (Get the app)
  - **Trust bar:** Logos of Meta, Amazon, Airbnb, PayPal, Square, Red Hat + "5M+ Kilo Coders · 10T+ tokens/month"
  - **Why Kilo?:** Agent command center, local and cloud agents, aligned pricing, open source (MIT)
  - **Built for agentic engineering:** Code Agent, Plan Agent, Cloud agents & code review, Debug Agent; Ask/Plan/Code/Debug/Custom agent types; Auto Model (Efficient/Frontier/Free)
  - **Blog:** Recent posts with authors and dates (Oct 2026)
  - **FAQ:** Accordion-style frequently asked questions (free?, install?, IDEs?, models?, privacy?, agents?, Copilot comparison?, MCP?, enterprise?, open source?)
  - **Footer:** Community links (Discord, GitHub, Reddit r/kilocode)
- **Icons:** Lucide icon library (lucide-bot, etc.)
- **Interactive patterns:** Accordion FAQs, model leaderboard, token race, KiloBench, provider browsing

### 2.5 Key Technical Behaviors Observed

- Multi-surface distribution: IDE extensions, CLI, desktop app, cloud, Slack, mobile
- Model-agnostic: 500+ models, BYOK, local models, no markup
- Open-source core with MIT license — forkable, self-hostable, auditable
- Session-aware model routing (Auto Model)
- Parallel isolated worktrees for local and cloud agents
- Prompt and context visibility — audit trail for agent decisions

---

## Part 2 — TechBlog Current State Assessment

### 2.1 Stack & Structure

| Attribute | Value |
|-----------|-------|
| **Platform** | Jekyll (static site generator) |
| **Theme** | Custom "Zvirox Cyber Defender" design system |
| **URL** | https://zvirox.in |
| **Author** | Zvirox |
| **Topics** | Technology, IT, Networking, Cybersecurity, Linux |
| **CSS** | Custom SCSS (`assets/css/style.scss`) with CSS custom properties |
| **Layouts** | `default.html`, `post.html`, `category.html` |
| **Content** | Markdown posts in `_posts/`, category index pages |

### 2.2 Design System (from `style.scss`)

- **Tokens:** Red brand (`--zv-red: #ff2633`), dark backgrounds (`#070a0d`–`#121920`), border (`#202830`), text (`#f2f5f7`–`#89939c`)
- **Typography:** Inter (sans), JetBrains Mono (mono)
- **Components:** Header (sticky, blur), hero, buttons (primary/secondary), article grid (4-col → 2-col → 1-col), cards, sidebar panels, TOC, related articles, footer grid
- **Responsive:** Tablet (≤1100px), Mobile (≤760px)
- **Theme toggle:** Dark/light via `data-theme` attribute + localStorage
- **Accessibility:** Focus-visible rings, skip patterns, ARIA labels

### 2.3 Existing Content

- 4 posts: DNS, DHCP, SSH, OSI model (all networking category)
- Categories: networking, cybersecurity, linux, it
- Articles index page listing all posts
- Category pages with post listings

---

## Part 3 — Phasewise Implementation Plan for TechBlog

The plan integrates insights from VoiceStudio and Kilo AI into the techblog: AI/voice tooling coverage, modern UI patterns, and content strategy.

---

### Phase 1 — Foundation & Content Audit (Weeks 1–2)

**Goal:** Stabilize the blog infrastructure and define the AI/voice content vertical.

| Task | Details | Inspired By |
|------|---------|-------------|
| 1.1 | Audit existing 4 posts; add frontmatter consistency (tags, description, featured image) | — |
| 1.2 | Create `ai` and `voice-ai` categories in Jekyll | VoiceStudio (646 languages, voice AI) |
| 1.3 | Add AI tooling tag taxonomy (voice-cloning, coding-agent, local-ai, open-source-ai) | VoiceStudio + Kilo AI |
| 1.4 | Set up `assets/images/ai/` directory for screenshots and diagrams | VoiceStudio screenshot gallery pattern |
| 1.5 | Document design tokens for new AI section (accent color, card styles) | Kilo AI brand-primary, VoiceStudio dark theme |

**Deliverable:** Clean category structure, tag taxonomy, image asset pipeline.

---

### Phase 2 — UI Enhancements: AI/Voice Article Cards & Hero (Weeks 3–4)

**Goal:** Modernize article presentation with patterns observed from both target sites.

| Task | Details | Inspired By |
|------|---------|-------------|
| 2.1 | Add AI-focused hero section on homepage (voice AI + coding agent spotlight) | VoiceStudio hero + Kilo AI hero |
| 2.2 | Create `zv-card-ai` variant with model badge, language count, or token stats | VoiceStudio adoption stats (50K stars, 596K downloads) |
| 2.3 | Add screenshot gallery component with hover-magnify for AI tool articles | VoiceStudio 13-screenshot gallery |
| 2.4 | Implement comparison table component (OSS vs Pro vs Cloud, or tool A vs tool B) | VoiceStudio ElevenLabs comparison table |
| 2.5 | Add "Trust bar" / adoption stats component (logos, stars, downloads, tokens/month) | Kilo AI trust bar (Meta, Amazon, etc.) |

**Deliverable:** AI-ready article cards, hero section, screenshot gallery, comparison tables, trust stats.

---

### Phase 3 — Content: Voice AI & AI Coding Agent Articles (Weeks 5–8)

**Goal:** Publish authoritative articles on voice AI and AI coding agents.

| Article | Focus | Source Reference |
|---------|-------|------------------|
| "VoiceStudio Review: Local AI Voice Cloning in 646 Languages" | Feature walkthrough, local-first privacy, Pro vs OSS | VoiceStudio analysis |
| "Kilo AI vs Cursor: Open Source AI Coding Agent Comparison" | IDE integrations, model routing, pricing, MIT license | Kilo AI analysis |
| "Running Voice AI Locally: Privacy-First Alternatives to Cloud TTS" | Local deployment, Docker, AGPL-3.0 implications | VoiceStudio local architecture |
| "AI Coding Agents in 2026: Model-Agnostic Development with BYOK" | Zero markup, 500+ models, session-aware routing | Kilo AI Auto Model + Gateway |
| "From ElevenLabs to VoiceStudio: Migrating to Open Source Voice Cloning" | Migration guide, cost comparison, commercial licensing | VoiceStudio vs ElevenLabs table |

**Deliverable:** 5 published articles in `ai`/`voice-ai` categories with screenshots and comparison tables.

---

### Phase 4 — Interactive Components (Weeks 9–10)

**Goal:** Add interactive elements seen on both target sites.

| Task | Details | Inspired By |
|------|---------|-------------|
| 4.1 | FAQ accordion component for AI tool articles | Kilo AI FAQ accordion |
| 4.2 | Model/feature comparison table with sortable columns | VoiceStudio comparison table |
| 4.3 | "Try it" / install command code blocks with copy button | VoiceStudio PowerShell install + Kilo CLI curl |
| 4.4 | Live stats widget (GitHub stars, downloads, tokens/month) with fetch | VoiceStudio live-refreshing counters |
| 4.5 | Dark/light theme persistence improvements | Existing Zvirox theme toggle |

**Deliverable:** FAQ accordions, comparison tables, copyable install commands, live stats widget.

---

### Phase 5 — Deployment & Analytics (Week 11–12)

**Goal:** Production-ready AI content section with measurement.

| Task | Details |
|------|---------|
| 5.1 | Deploy AI category pages and articles to GitHub Pages / custom domain |
| 5.2 | Add sitemap and SEO tags for AI/voice-ai categories (jekyll-seo-tag already present) |
| 5.3 | Add RSS feed for AI category (jekyll-feed already present) |
| 5.4 | Set up basic analytics (privacy-friendly, self-hosted option) — aligns with local-first philosophy |
| 5.5 | Cross-link AI articles from networking/cybersecurity posts where relevant |

**Deliverable:** Live AI section, SEO-optimized, RSS-enabled, analytics-integrated.

---

## Part 4 — UI Implementation Reference: Design Tokens for AI Section

Based on analysis of both sites, recommended additions to `style.scss`:

```scss
/* AI section accent (voice AI + coding agent) */
--zv-ai-purple: #8b5cf6;
--zv-ai-purple-dark: #7c3aed;
--zv-ai-surface: #0e1318;
--zv-ai-border: #202830;

/* VoiceStudio-style dark surface */
--zv-voice-bg: #141414;
--zv-voice-border: rgba(255,255,255,0.1);

/* Kilo AI-style brand primary */
--zv-kilo-brand: #0e0e0e;
--zv-kilo-accent: #28c840;
```

**Component patterns to adopt:**
- VoiceStudio: numbered feature list (01–07), screenshot gallery with hover magnify, comparison tables, adoption stats badges
- Kilo AI: Tailwind utility classes, accordion FAQs, model routing badges (Efficient/Frontier/Free), trust logo bar, IDE platform badges

---

## Part 5 — Success Metrics

| Metric | Target | Source |
|--------|--------|--------|
| AI category articles published | 5 (Phase 3) | Content plan |
| Page load time (AI hero) | < 2s | Jekyll static |
| Mobile responsiveness | 100% pass | Existing breakpoints |
| Accessibility (WCAG AA) | Focus rings, contrast | Existing style.scss |
| SEO: AI category indexed | Google Search Console | jekyll-seo-tag |

---

## Appendix — Evidence Captured

- `/tmp/voicestudio.html` — Full VoiceStudio homepage HTML (211 KB)
- `/tmp/kilo.html` — Full Kilo AI homepage HTML (555 KB)
- VoiceStudio images: `/img/screenshots/{launchpad,design,libraryprojects,quick-switch,updates,studio,clone,openapi,logs,gallery,dub,engines,settings}.webp`
- Kilo AI images: `/_next/image?url=%2Fkilo-mobile-app-qr.png`
- TechBlog design system: `/home/zvirox/Projects/techblog/assets/css/style.scss`
- TechBlog layouts: `/home/zvirox/Projects/techblog/_layouts/`

---

*Report generated via reverse-engineering analysis of voicestudio.sh and kilo.ai on 2026-10-23.*
