# Figure recovery: XX-AI-Fairness

Source: `docs/slides/ppt-archive/XX-AI-Fairness.pptx`, 12 slides, rendered 2026-10-16
(headless LibreOffice, 110 dpi contact sheet). No slide animates; no pen-ink annotations.

Result: nothing to recover. The deck draws no diagrams in PowerPoint itself. Its only
graphics are six embedded pictures, all saved by the earlier media extraction as
`images/slideNNN_imgNNN.png` and all already embedded in `slides.qmd`. The only drawn
shapes outside placeholders are two text boxes (a caption on slide 8 and a quotation on
slide 12), which are text, not figures.

| pptx slide | class | target Quarto slide | figure name | notes |
|---|---|---|---|---|
| 1 | skip | | | title |
| 2–3 | skip | | | bullets ("Overview", "What We Know") |
| 4 | media | "Societal Bias vs. Statistical Bias" | `slide004_img001.png` | should-be / is / data bias-flow diagram; an embedded picture, already used |
| 5 | media | "Bias in Training Data" | `slide005_img002.png` | Google Translate screenshot; already used |
| 6 | media | "COMPAS: Predicting Re-Offense" | `slide006_img003.png`, `slide006_img004.png` | ProPublica decile histograms; already used |
| 7 | media | "What the Model Actually Weighs" | `slide007_img005.png` | logistic-regression coefficient table; already used |
| 8 | media | "Minimizing Average Error Fits the Majority" | `slide008_img006.png` | Gender Shades error-rate table; already used. "TextBox 4" is only the caption "Example: Facial Recognition" |
| 9–11 | skip | | | bullets ("Definitions of Fairness", "Flavors of Fairness", "Open Questions") |
| 12 | skip | | | bullets plus a quotation text box (Chouldechova-style PPV/NPV vs demographic-parity passage); its content is already paraphrased on "So — Is COMPAS Unfair?" |

No images captured; no slides or speaker-notes rows added.
