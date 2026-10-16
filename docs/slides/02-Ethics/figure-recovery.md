# Figure recovery: 02-Ethics

Source: `docs/slides/ppt-archive/02-Ethics.pptx`, 43 slides, rendered 2026-10-16
(headless LibreOffice, 110 dpi contact sheet; slide 43 is hidden in the deck).

**Result: nothing to recover.** The deck contains no diagrams drawn in
PowerPoint. The shape inventory is 32 embedded pictures, title/body
placeholders, seven plain text boxes, one group (slide 14, four screenshot
pieces of a news article), and one connector arrow (slide 39, pointing at a
paragraph in a press-release screenshot). Every picture that carries intuition
was already extracted under `images/slideNNN_imgNNN.png` and the three worth
having are already embedded in `slides.qmd` (Tuskegee photo, Salganik
frameworks→principles→rules diagram, Menlo Report cover). The remaining media
are dated news clippings and first pages of other people's papers, dropped
deliberately in the Quarto rebuild (see `coverage-notes.md`, "Curated images").

| pptx slide | class | target Quarto slide | figure name | notes |
|---|---|---|---|---|
| 1 | skip | | | title |
| 2 | media | "A Cautionary Origin: Tuskegee" | | `slide002_img001.png`, already embedded |
| 3 | skip | | | one-line framing text |
| 4 | media | | | "How a university got itself banned from the Linux kernel" clipping; dated screenshot, text already on "Why This Hits Close to Home" |
| 5 | media | | | Hypocrite Commits paper first page; someone else's document, not a figure |
| 6 | media | | | GDPR/CCPA "scam" email screenshot; personal correspondence, dropped |
| 7 | media | | | Carna botnet / Internet Census 2012 clipping; dated screenshot, text already on the deck |
| 8–10 | skip | | | agenda and definition bullets |
| 11 | media | "Salganik's Layered Approach" | | `slide011_img013.png`, already embedded; Salganik's figure, attributed in the notes |
| 12–13 | skip | | | bullets |
| 14 | media | | | US News "Was Facebook's 'Emotional Contagion' Experiment Ethical?" clipping (group of four screenshots); dated, third-party, content covered by the "Case Study: Emotional Contagion" slide |
| 15–18 | skip | | | bullets; slide 17 has a text callout only |
| 19, 23, 29 | media | | | identical copies of the slide 11 Salganik diagram |
| 20–22, 24–28, 30–31 | skip | | | bullets (Common Rule, Belmont, four principles, areas of difficulty, concepts) |
| 32 | media | "Respect for Law and Public Interest" | | `slide032_img017.png` (Menlo cover), already embedded |
| 33–34 | skip | | | bullets |
| 35 | skip | | | photograph of an identifiable person; never embed |
| 36 | media | | | SDMI "Reading Between the Lines" paper first page plus bullets; third-party document, not a figure |
| 37 | media | | | Sony DRM paper first page and CD clip art; third-party document |
| 38 | media | | | "The Chilling Effects of the DMCA" op-ed clipping; dated screenshot |
| 39 | media | | | ACM USTPC Van Buren press release (Jul 2020) with a pointer arrow; superseded by the "The Law Is (Slowly) Catching Up" slide, which carries the 2021 ruling itself |
| 40–43 | skip | | | bullets (contracts, codes, breakout, other standards; 43 hidden) |

No `source:` lines: no images were captured.
