# 16-Moderation — instructor notes

## Current-events updates made (point 2)
- **Opening vignette (DSA enforcement, dated):** EU Commission's **24 Oct 2025**
  preliminary findings that **TikTok and Meta** breached the Digital Services Act
  (inadequate researcher data access; fines up to 6% of global turnover), plus the
  **April 2025 €200M DMA fine** against Meta. Verified via CNBC (2025-10-24) and SEC
  filings. This replaces the original deck's general "DSA enacted in the new year"
  framing with concrete, current enforcement.
- **Added Moody v. NetChoice (July 1, 2024)** as a US-law vignette: six justices agreed
  platform curation is First-Amendment-protected editorial activity; case vacated and
  remanded on procedural grounds. This grounds the abstract "platforms are de facto
  regulators" claim in a real, recent ruling and explains why US government can't easily
  compel carry/removal. Verified via Supreme Court opinion and CRS summary.
- **Added an LLM-moderation slide** reflecting 2025 research: LLMs now rival older
  classifiers (Perspective API) on AUC but miss implicit toxicity, are uncertain on
  edge cases, and show author-identity bias. Sources: ICWSM "Watch Your Language" and
  2025 arXiv uncertainty/bias papers. Kept claims general (no fabricated metrics beyond
  what sources state) to satisfy the listed "LLM moderation" theme.
- **Modernized examples generally:** "2023" references dropped; framed Section 230 / DSA
  / NetzDG as a live comparative-law contrast as of 2026.

## Suggested missing coverage on broad themes (point 3)
- **Stated vs. enacted policy (audit studies):** the deck flags this gap but the course
  could add a measurement segment — e.g., the follow-on work testing whether platforms
  actually enforce reported policies. Strong tie to the FTC/compliance-measurement
  lectures.
- **The 2025 US deregulatory turn:** Meta's January 2025 end of third-party
  fact-checking / move to Community Notes, and X's Community Notes model. Worth a slide
  on crowd-sourced moderation vs. centralized — verify current details before teaching.
- **CSAM / NCMEC and the SHIELD/STOP CSAM legislative debates:** deliberately scoped out
  of the OCMP-43 study, but a natural addition given its legal clarity and the
  client-side-scanning / encryption tension (links to the crypto and surveillance units).
- **Trust & Safety operations and labor:** human moderator working conditions,
  outsourcing, and the psychological toll — the "human moderators" mechanism on the
  detection slide is otherwise a black box.
- **Section 230 reform debate, current status:** carve-outs (FOSTA-SESTA), and the
  algorithmic-amplification question (Gonzalez v. Google) — good Oxford-debate material.
- **Global South / non-Western regimes:** the source admits a Western bias (US/EU/
  Germany). Add India IT Rules, Brazil's PL 2630 / STF rulings, or Singapore POFMA for
  contrast.
- **Appeals and due process / Oversight Board:** Meta's Oversight Board as a
  quasi-judicial experiment directly addresses the lopsided-appeals finding.

## Curated images
- **Used:** `slide029_img027.png` (annotation codebook — teaches the analytic lens),
  `slide013_img020.png` (OCMP-43 dataset metrics table), `slide036_img030.png` (legal
  justification distribution), `slide039_img034.png` (definitions vs. examples by topic
  — the paper's headline result), `slide044_img035.png` (safeguards: user role vs.
  platform detection), `slide033_img029.png` (scraper control-flow diagram).
- **Dropped:** title/headshot slides (`slide001/002/022_*`), decorative platform-logo
  collages (`slide003_img006-008`, `slide027_img026` ~1.6MB meme image), duplicate
  flag/region clip-art (`slide004/005/006/007_*`, `slide024`), the OCMP screenshot
  (`slide021_img021`), and near-duplicate plot variants (`slide036_img031`,
  `slide037_img032`, `slide038_img033`, `slide045_img036`) — redundant or non-teaching.

## Source
- Rebuilt from `_source-extract.md` (46 original slides) + `agenda.md` Meeting 7
  (content moderation debate; "content moderation (light)" on Midterm 2). Underlying
  paper: Schaffner et al., CHI 2024, OCMP-43. Final deck: 20 slides.
