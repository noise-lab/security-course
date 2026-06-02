# 11-PrivacyLaw — instructor notes

## Current-events updates made (point 2)

All facts below were web-verified (June 2026) against primary sources before
being placed on slides; dates and figures are exact.

- **Opening vignette — Disney COPPA, $10M (court-approved Dec. 31, 2025).** Fresh
  hook for "FTC sets the floor / no federal law." Disney let children's data be
  collected through YouTube videos it failed to label "Made for Kids," violating
  the COPPA Rule. Source: FTC press release, Dec. 2025; DOJ Office of Public
  Affairs. Replaces the old deck's stale framing (which opened on Warren &
  Brandeis with no current anchor).
- **TikTok GDPR fine — €530M (Irish DPC, May 2, 2025).** Used on the "GDPR
  Enforcement Is Real" slide as the largest 2025 fine, for unlawful EEA→China
  transfers (€485M under Art. 46, €45M under Art. 13). Makes the abstract
  cross-border-transfer rule concrete. Source: Irish DPC / EDPB, May 2025.
- **GDPR all-time record — Meta €1.2B (2023).** Retained and re-anchored as the
  record for EU–US transfer violations; cumulative GDPR fines stated as
  "roughly €7B+ through 2025" (consistent with enforcementtracker.com totals;
  phrased approximately, not as a hard figure).
- **State-law landscape — ~20 comprehensive state laws; no new law passed in
  2025; Indiana/Kentucky/Rhode Island effective Jan. 1, 2026.** New closing
  vignette ("Where U.S. Privacy Law Stands in 2026") replacing the old deck's
  static "statutory landscape" ending. Source: MultiState / IAPP trackers, 2026.
  Teaching point: the wave is leveling off and shifting to *enforcement*.
- **Kochava location-data action (order proposed 2026).** Brief mention beside
  Disney to reinforce "old statutes, new harms" and the data-broker frontier.
- **GoodRx ($1.5M, 2023) and BetterHelp ($7.8M, 2023)** kept on the HIPAA-gap
  slide as the canonical recent FTC health-privacy cases reaching non-covered
  entities; **Twitter 2FA-for-ads (2022)** kept on the Section 5 slide.

> Note for next year: a strong alternative/additional vignette is the
> **FTC's Jan. 2025 final orders against Mobilewalla and Gravy Analytics/Venntel**
> banning sale of *sensitive location data* (clinics, places of worship, LGBTQ+
> venues; 500M+ ad IDs sourced from real-time bidding). It ties the PII problem,
> the HIPAA gap, and the Section 5 "unfair" theory together more tightly than the
> Disney hook and is worth swapping in or adding. (Verified: FTC, Jan. 2025.)

## Suggested missing coverage on broad themes (point 3)

- **CCPA/CPRA in depth.** The deck gestures at "50-state quasi-omnibus" but the
  California regime (signed 2018, effective 2020; CPRA effective 2023; "Do Not
  Sell/Share," sensitive-PI category, dark-pattern ban) is largely deferred to
  Meeting 8. A one-slide CCPA primer here would make the U.S. story self-contained
  for students who only see this lecture.
- **Data brokers as an actor class.** The patchwork is framed around statutes;
  it under-covers the *industry* (Acxiom, Oracle, LiveRamp, location SDKs) that
  the FTC's 2025 actions target. A slide on the ad-tech / RTB data supply chain
  would explain *how* "anonymous" location data is collected and resold.
- **State biometric law (Illinois BIPA).** BIPA's private right of action and
  large settlements (e.g., Facebook $650M) are a major U.S. privacy force absent
  from the deck — and a clean contrast to the FTC's public-enforcement model.
- **Schrems I & II mechanics.** The notes mention Safe Harbor / Privacy Shield
  invalidation and the 2023 Data Privacy Framework, but it stays in speaker
  notes. Given how central cross-border transfer is to GDPR enforcement (Meta,
  TikTok), it merits a slide.
- **Comprehensive federal proposals.** No mention of the American Privacy Rights
  Act (APRA) / ADPPA debates and *why* federal preemption keeps stalling. This is
  the natural "what next for the U.S.?" discussion.
- **AI and privacy interface.** The "age of inference" / FIPPs-don't-fit thread
  is excellent setup but is intentionally handed off to the AI & Privacy lecture;
  flag the handoff explicitly so students see the connection (model training on
  scraped personal data, inference as the new harm, "right to be forgotten" vs.
  model memorization).
- **Privacy harms taxonomy.** A short Solove "taxonomy of privacy" or Calo
  "subjective/objective harm" frame would give students vocabulary for *why*
  these laws exist, beyond the case-by-case anecdotes.

## Curated images

- **Used:** `slide025_img013.png` — montage of real breach headlines (Equifax,
  Under Armour/MyFitnessPal, Uber, Target) on the breach-notification slide;
  genuinely teaches the "regulation by consequence" point.
- **Dropped (decorative / clip-art / redundant):** `slide002_img*` (printing
  press, Warren/Brandeis portraits), `slide021_img011` (HIPAA/FERPA/GLBA/COPPA
  logo collage), `slide030_img016` (FTC seal/building), `slide041_img*` and
  `slide033/034_img*` (article screenshots and logos), `slide040_img*` (fine
  logos). These add no instructional content beyond what the text conveys.
- **Considered but not used (could add):** `slide004_img004` (the 1973 HEW report
  cover letter) on the FIPPs slide — a nice primary-source artifact; and
  `slide019_img009` (Solove & Schwartz "The PII Problem") on the PII slide. Both
  are legitimate teaching images if a more visual FIPPs/PII slide is wanted.
  `slide029_img014` (Equifax-response headline) is redundant with the breach
  montage already in use.

## Source

- Rebuilt from `_source-extract.md` (42 original slides) + `agenda.md` Meeting 7
  ("Privacy Law and Regulation"), consolidated to 26 slides.
