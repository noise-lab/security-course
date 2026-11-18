# Figure recovery: 12-Compliance

Source: `docs/slides/ppt-archive/12-Compliance.pptx`, 70 slides, rendered 2026-10-16
(headless LibreOffice, 220 dpi, `src/pptx-figures.py` in instructor-tools). No hidden
slides, no pen ink. Both source papers are the instructor's own group (Tran et al.),
so the paper figures and tables are reused with an in-caption attribution.

| pptx slide | class | target Quarto slide | figure name | notes |
|---|---|---|---|---|
| 1 | skip | | | title, authors, logos |
| 2 | keep | "Where Does Our Data Go?" | data-flow-to-third-parties.png | whole drawing (icons, art, ovals), captured 2026-11-18 |
| 3–8 | skip | | | harms bullets, CCPA/CPRA text, opt-out methods text, RQ list, outline |
| 9–10 | skip | | | vantage-point list with dates, already bullets in "Method: Vantage Points and Keywords" |
| 11 | keep | "B. Methodology" (keywords) | keyword-list-sources.png | captured 2026-11-18 |
| 12 | keep | new, "Method: Two Ways to Find the Link" | method-keyword-pipeline.png | 19-step build captured in final state |
| 13 | skip | | | verification text boxes (now slide text) |
| 14 | media | "Verify Methods" (source vs. screenshot) | slide014_img021/022.png | embedded 2026-11-18 |
| 15–16, 18, 21, 23, 25 | skip | | | outline / RQ interstitials repeated between results |
| 17 | media | already used | slide017_img023.png | RQ1 stacked bars |
| 19 | skip | | | opt-out methods text, duplicate of 6 |
| 20 | keep | new, "RQ2 as a Decision Tree" | rq2-compliance-tree.png | one build step (the 45% callout) left out; tree only |
| 22 | keep + media | "RQ3" chart slide and table slide | optout-link-by-state-over-time.png, slide022_img025.png | chart is the first build state, hidden by the table overlay; stripped Picture 6, TextBox 3 and the four annotation boxes/arrows (annotations are slide text) |
| 24 | keep | new, "GPC Support: Disclosed by About a Quarter of Sites" | gpc-support-table.png | final overlay (table) kept; the base diagram under it is three empty boxes once its screenshot is stripped, not worth a figure |
| 26 | media | already used | slide026_img028.png | RQ4 coverage table |
| 27 | keep | new, "RQ4: Why Is the Link Missing?" | rq4-noncompliance-reasons.png | table only; the chevron label and callout dropped |
| 28–30 | skip | | | limitations, summary, future-direction bullets |
| 31–37 | skip | | | Study 2 title, summary, CCPA/CPRA text, RQ list, outline |
| 38 | keep | "Dataset Selection" | dataset-selection-funnel.png | captured 2026-11-18 |
| 39–40 | skip | | | icon row, metrics bullets |
| 41 | media | "Opt-Out Control Methods" (screenshots) | slide041_img032–034.png | embedded 2026-11-18 |
| 42 | skip | | | taxonomy bullets |
| 43 | keep | new, "Method: How Each Attempt Was Labelled" | labelling-process.png | paper figure (own group) |
| 44–46, 51 | skip | | | follow-up bullets, section titles |
| 47 | keep | new, "Scoring Each Request" | outcome-decision-flow.png | caption dropped, written on the slide instead |
| 48 | media | "Opt-Out Request Outcomes" (failure to submit) | slide048_img035.png | error toast, embedded 2026-11-18 |
| 52 | keep | "Opt-Out Control Methods" (Table 2) | control-methods-by-vendor-table.png | captured 2026-11-18 |
| 53 | keep | new, "How Many Clicks to Opt Out?" | clicks-by-control-method.png | Fig. 5, paper caption dropped |
| 54 | media | "Personal Information Required" | slide054_img036.png | embedded 2026-11-18 |
| 55 | keep | new, "Which Failures Break the Law?" | outcomes-vs-ccpa.png | drawn mapping, no builds |
| 56, 61, 63 | skip | | | RQ title slides |
| 57 | media | already used | slide057_img037.png | CAPTCHA screenshot |
| 57–60 | media | Obstruction ×2, Interface Interference, Misdirection | slide057_img038, slide058_img039/040, slide059_img041, slide060_img042 | embedded 2026-11-18 (slide057_img037 was already used) |
| 62 | media | already used | slide062_img043.png | pattern → principle mapping table |
| 64 | keep | new, "How Common Are Dark Patterns?" (left column) | dark-pattern-count-histogram.png | Fig. 8, caption dropped |
| 65 | keep | same slide (right column) | dark-pattern-prevalence-table.png | Table 6, caption dropped |
| 66 | keep | "Distribution of Dark Patterns Across Opt-Out Control Methods" | dark-patterns-by-control-method.png | Fig. 9 + Table 7, captured 2026-11-18 |
| 67 | keep | "Distribution of Dark Patterns Across Third-Party Platforms" | dark-patterns-by-third-party.png | Fig. 10 + Table 8, captured 2026-11-18; the earlier Fig.-10-only crop dark-patterns-by-vendor.png is no longer embedded |
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

## Added 2026-11-18 (deck conformed to the pptx slide for slide)

- `images/data-flow-to-third-parties.png` — source: slide 2, crop 260,650–2760,1540 at 220 dpi, auto-trimmed (2468×883)
- `images/keyword-list-sources.png` — source: slide 11, crop 430,530–2460,1480 (2011×924)
- `images/dataset-selection-funnel.png` — source: slide 38, crop 490,430–2320,1400 (1809×938)
- `images/optout-link-by-state-over-time.png` — source: slide 22, first build state (Picture 2 + caption TextBox 5), stripped "Picture 6, TextBox 3, TextBox 4, TextBox 9, TextBox 10, TextBox 12, Straight Arrow Connector 8, Straight Arrow Connector 11", crop 1150,40–2934,1470 at 220 dpi, auto-trimmed (1652×1380)
- `images/control-methods-by-vendor-table.png` — source: slide 52, crop 1095,536–2815,1117 (1715×579)
- `images/dark-patterns-by-control-method.png` — source: slide 66, crop 1095,140–2815,1036 (1720×893)
- `images/dark-patterns-by-third-party.png` — source: slide 67, crop 1095,360–2793,1279 (1690×919)
- Previously extracted media newly embedded (`git add -f` needed, `images/` is gitignored): slide006_img007, slide014_img021, slide014_img022, slide041_img032–034, slide048_img035, slide054_img036, slide057_img038, slide058_img039, slide058_img040, slide059_img041, slide060_img042.
