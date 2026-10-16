# Figure recovery: 12-Compliance

Source: `docs/slides/ppt-archive/12-Compliance.pptx`, 70 slides, rendered 2026-10-16
(headless LibreOffice, 220 dpi, `src/pptx-figures.py` in instructor-tools). No hidden
slides, no pen ink. Both source papers are the instructor's own group (Tran et al.),
so the paper figures and tables are reused with an in-caption attribution.

| pptx slide | class | target Quarto slide | figure name | notes |
|---|---|---|---|---|
| 1 | skip | | | title, authors, logos |
| 2 | skip | | | stock clip art (app icons, "personal data" art) with three "Third-party" ovals; coverage-notes already dropped the art |
| 3–8 | skip | | | harms bullets, CCPA/CPRA text, opt-out methods text, RQ list, outline |
| 9–10 | skip | | | vantage-point list with dates, already bullets in "Method: Vantage Points and Keywords" |
| 11 | skip | | | two ovals and a box (requirements + manual inspection → keyword list); folded into the slide 12 narration |
| 12 | keep | new, "Method: Two Ways to Find the Link" | method-keyword-pipeline.png | 19-step build captured in final state |
| 13–14 | skip | | | verification text boxes and screenshots (coverage-notes dropped) |
| 15–16, 18, 21, 23, 25 | skip | | | outline / RQ interstitials repeated between results |
| 17 | media | already used | slide017_img023.png | RQ1 stacked bars |
| 19 | skip | | | opt-out methods text, duplicate of 6 |
| 20 | keep | new, "RQ2 as a Decision Tree" | rq2-compliance-tree.png | one build step (the 45% callout) left out; tree only |
| 22 | media | already used | slide022_img025.png | RQ3 state table |
| 24 | keep | new, "GPC Support: Disclosed by About a Quarter of Sites" | gpc-support-table.png | final overlay (table) kept; the base diagram under it is three empty boxes once its screenshot is stripped, not worth a figure |
| 26 | media | already used | slide026_img028.png | RQ4 coverage table |
| 27 | keep | new, "RQ4: Why Is the Link Missing?" | rq4-noncompliance-reasons.png | table only; the chevron label and callout dropped |
| 28–30 | skip | | | limitations, summary, future-direction bullets |
| 31–37 | skip | | | Study 2 title, summary, CCPA/CPRA text, RQ list, outline |
| 38 | skip | | | sampling funnel (1000 → 542 → 330); numbers already on "Method: Actually Submitting" |
| 39–40 | skip | | | icon row, metrics bullets |
| 41 | media | dropped by coverage-notes | slide041_img032–034 | control-method screenshots |
| 42 | skip | | | taxonomy bullets |
| 43 | keep | new, "Method: How Each Attempt Was Labelled" | labelling-process.png | paper figure (own group) |
| 44–46, 51 | skip | | | follow-up bullets, section titles |
| 47 | keep | new, "Scoring Each Request" | outcome-decision-flow.png | caption dropped, written on the slide instead |
| 48–50 | skip | | | outcome counts already on "~30% of Opt-Out Attempts Fail" |
| 52 | skip | | | Table 2 (control method × vendor); its numbers are narrated on the vendor-irony slide instead of a second table |
| 53 | keep | new, "How Many Clicks to Opt Out?" | clicks-by-control-method.png | Fig. 5, paper caption dropped |
| 54 | media | dropped by coverage-notes | slide054_img036.png | personal-info table |
| 55 | keep | new, "Which Failures Break the Law?" | outcomes-vs-ccpa.png | drawn mapping, no builds |
| 56, 61, 63 | skip | | | RQ title slides |
| 57 | media | already used | slide057_img037.png | CAPTCHA screenshot |
| 58–60 | media | not embedded | slide058–060 images | annotated dark-pattern screenshots; left out to stay selective, the Three Families slide names the examples |
| 62 | media | already used | slide062_img043.png | pattern → principle mapping table |
| 64 | keep | new, "How Common Are Dark Patterns?" (left column) | dark-pattern-count-histogram.png | Fig. 8, caption dropped |
| 65 | keep | same slide (right column) | dark-pattern-prevalence-table.png | Table 6, caption dropped |
| 66 | skip | | | per-control-method small multiples + table; too dense for a slide and the clicks figure already splits by control method |
| 67 | keep | new, "The Vendor Irony in One Figure" | dark-patterns-by-vendor.png | Fig. 10 only; Table 8 below it is narrated in the bullets |
| 68–70 | skip | | | discussion icons, conclusions, summary |

## Sources

- `images/method-keyword-pipeline.png` — source: ppt-archive/12-Compliance.pptx slide 12, final build state, crop 190,690–2820,1500 at 220 dpi, auto-trimmed (2585×750)
- `images/rq2-compliance-tree.png` — source: slide 20, crop 760,60–2934,1360 (2172×1294)
- `images/gpc-support-table.png` — source: slide 24, final overlay "Picture 2" (id 5), crop 320,380–2620,1150 (2282×767)
- `images/rq4-noncompliance-reasons.png` — source: slide 27, crop 1140,390–2790,1240 (1626×829)
- `images/labelling-process.png` — source: slide 43, crop 1301,112–2604,1495 (1256×1355)
- `images/outcome-decision-flow.png` — source: slide 47, crop 272,425–2500,1225 (2138×787)
- `images/clicks-by-control-method.png` — source: slide 53, crop 330,560–2654,1130 (2201×536)
- `images/outcomes-vs-ccpa.png` — source: slide 55, crop 180,404–2520,1470 (2318×1059)
- `images/dark-pattern-count-histogram.png` — source: slide 64, crop 1163,130–2742,1215 (1426×1054)
- `images/dark-pattern-prevalence-table.png` — source: slide 65, crop 1083,243–2822,1295 (1702×1044)
- `images/dark-patterns-by-vendor.png` — source: slide 67, crop 1083,355–2822,760 (1670×402)
