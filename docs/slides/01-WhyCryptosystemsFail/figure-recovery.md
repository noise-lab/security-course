# Figure recovery: 01-WhyCryptosystemsFail

Source: `docs/slides/ppt-archive/01-WhyCryptosystemsFail.pptx`, 22 slides, rendered 2026-10-16 (headless LibreOffice, 110 dpi contact sheet). No slide animates; no pen ink.

The deck has no PowerPoint-drawn diagrams at all: every picture is an embedded screenshot or photo, already extracted to `images/slideNNN_imgNNN.png`. The only two figures that carry intuition and that the Quarto deck lacked are the two excerpts from Anderson's paper on slides 8 and 9, so those were embedded from the extracted media (same resolution as the pptx originals).

| pptx slide | class | target Quarto slide | figure name | notes |
|---|---|---|---|---|
| 1 | skip | | | title |
| 2 | media | "Where Does It Actually Break?" | | xkcd 2347; extracted as `slide002_img001.png`, used by the overview deck's trusting-trust segment, not needed here |
| 3 | media | "When Regulators Treat Patching as a Duty" | | FTC Log4j screenshot already embedded (`slide003_img002.png`); the two tweet screenshots and the blog clip are dated, skip |
| 4–6 | skip | | | bullets, already in the deck |
| 7 | media | "How ATM Fraud Actually Happened" | | skimmer photo already embedded (`slide007_img006.png`) |
| 8 | keep | new, "Hiding the PIN on a Card" (after "How ATM Fraud Actually Happened") | pin-mnemonic-grid.png | Anderson §3.1 squared-card grid (b, l, u, e in columns 2, 2, 5, 6); no builds |
| 9 | keep | new, "Where the PIN Came From" (after "And the Crypto-Adjacent Mistakes") | pin-derivation-example.png | Anderson §3.2.1 worked PIN derivation (account number → DES → decimalise → natural PIN → offset → customer PIN); no builds |
| 10 | skip | | | two paragraphs of the paper as text screenshots; content is in the bullets |
| 11–13 | skip | | | bullets, already in the deck |
| 14 | skip | | | paper text screenshot (security-team churn); quoted in "The Takeaway" |
| 15 | skip | | | bullets |
| 16 | skip | "Two Paradigms for Safety" | | two unattributed stock photos (Boeing 787, DB ICE) plus the two bullet lists the Quarto slide already has; photos are decorative |
| 17–18 | skip | | | paper text screenshots (signalling vs aviation, economics analogy); content is in the slide and notes |
| 19–21 | skip | "Case in Point: Equifax (2017)" | | Equifax logo, news clip, FTC settlement page, FTC Log4j page: dated screenshots, facts are stated in the text |
| 22 | skip | "Food for Thought" | | IDPH identity-verification FAQ screenshot; dated, and the slide now uses the 2026 IDScan.net case |

## Captured

- `images/pin-mnemonic-grid.png` (331×117) — source: `ppt-archive/01-WhyCryptosystemsFail.pptx` slide 8, `ppt/media/image7.png` (extracted as `slide008_img007.png`), auto-trimmed with 6 px pad. Figure is from Anderson, "Why Cryptosystems Fail" (CCS 1993), §3.1; attributed in the caption.
- `images/pin-derivation-example.png` (407×145) — source: `ppt-archive/01-WhyCryptosystemsFail.pptx` slide 9, `ppt/media/image8.png` (extracted as `slide009_img008.png`), auto-trimmed with 6 px pad. Figure is from Anderson, §3.2.1; attributed in the caption.

Both are small text figures, so they sit in a 50–55% column at roughly 1.5× their native size rather than full width.
