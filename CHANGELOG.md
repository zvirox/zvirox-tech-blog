# Changelog

## [Unreleased] — AI & Voice AI Section

### Added

- **New categories:** `AI` and `Voice AI` category pages (`categories/ai/`, `categories/voice-ai/`)
- **New article assets directory:** `assets/images/ai/` for AI article screenshots and illustrations
- **New articles (5):**
  - `2026-10-23-voicestudio-review-local-ai-voice-cloning.md` — VoiceStudio open-source AI voice cloning review with comparison table, screenshot gallery, FAQ accordion, and install block
  - `2026-10-23-kilo-ai-vs-cursor-open-source-coding-agent.md` — Kilo AI vs Cursor comparison with FAQ accordion and CLI install block
  - `2026-10-24-running-voice-ai-locally-privacy-first-tts.md` — Local voice AI privacy guide with Docker deployment, screenshot gallery, and FAQ
  - `2026-10-25-ai-coding-agents-2026-model-agnostic-byok.md` — AI coding agents landscape with model-agnostic development, BYOK, and pricing comparison
  - `2026-10-26-from-elevenlabs-to-voicestudio-migration-guide.md` — ElevenLabs to VoiceStudio migration guide with cost comparison and feature mapping

### Changed

- **`index.md`** — Added AI hero section ("Run AI on your own terms") and AI/Voice AI topic cards to homepage topics grid
- **`assets/css/style.scss`** — Added AI design system tokens and components:
  - `.zv-hero-ai` — AI hero section with purple gradient accent
  - `.zv-card-ai` — AI card variant with purple category accent
  - `.zv-screenshot-grid` / `.zv-screenshot-item` — VoiceStudio-inspired screenshot gallery with hover magnify
  - `.zv-comparison-table` — Side-by-side feature comparison table (VoiceStudio vs ElevenLabs style)
  - `.zv-trust-bar` — Kilo AI-inspired trust statistics bar
  - `.zv-install-block` — Copyable install command block (PowerShell/cURL style)
  - `.zv-faq-accordion` / `.zv-faq-item` — Kilo AI-inspired FAQ accordion component
- **`categories/index.md`** — Added AI and Voice AI entries to the categories listing

### Removed

- None

### Fixed

- Post dates adjusted to avoid future-date Jekyll build skips

### Infrastructure

- `plan.md` — Reverse engineering report and phasewise implementation plan for VoiceStudio (voicestudio.sh) and Kilo AI (kilo.ai) analysis
- Jekyll build verified successfully with all 9 posts generating
