# Figure recovery: XX-Surveillance

Source: `docs/slides/ppt-archive/XX-Surveillance.pptx`, 60 slides (7 hidden: 20, 21, 26, 27, 29, 31, 35), rendered 2026-10-16 with headless LibreOffice at 110 dpi (contact sheet) and 220 dpi (crops).

| pptx slide | class | target Quarto slide | figure name | notes |
|---|---|---|---|---|
| 1, 3, 6, 8, 11, 13, 14, 16, 18–20, 22 | skip | | | title, dividers, text-only |
| 2 | media | | | TCP/IP header-fields diagram (`slide002_img001.png`), third-party figure without attribution; not embedded |
| 4, 5 | media | | | Obama photo + quote; the quote is already on the opening slide |
| 7 | skip | | | "Possible Definitions" brace diagram; same content as the "Many Definitions" bullets |
| 9 | skip | | | funnel from channels to the four metadata fields; bullets already carry it |
| 10 | skip | | | envelope address + one CDR row; the "Envelope Analogy" slide has the text |
| 12 | skip | | | person → login → EmailCo cloud; three icons, superseded by slide 21's richer picture |
| 15 | keep | "When the Definition Breaks Down" (banner above bullets) | url-metadata-or-content.png | drawn URL with the metadata / ? / content dividers, no build |
| 17 | media | "Implicit Location" | slide017_img009.png | already embedded |
| 21 | keep | new, "Email Has Layers of Metadata" | email-metadata-path.png | hidden slide; main picture is a `.tif` the earlier extraction skipped, so the render is the only copy; no build |
| 23 | keep | new, "The Section 215 Exchange" | section-215-exchange.png | two-arrow exchange; the 5-step build only adds the arrows, final state is the full picture |
| 24 | keep | new, "Inside the Query Pipeline" | usa-freedom-query-pipeline.png | drawn pipeline with stamps; "Station Table" label clipped in the original; no build |
| 25 | media | "Re-Identification Is Easy" | slide025_img011.png | already embedded |
| 26, 27 | media | | | age histogram, gender pie of study participants (hidden); not needed |
| 28 | media | new, "Why Two Hops Explode" | slide028_img014.png | extracted hop tree, embedded as is |
| 29 | media | "The Graph Has Hubs" | slide029_img015.png | already embedded |
| 30, 31 | media | | | call/text graph plots, USA FREEDOM filtering curves (hidden); paper figures, the 25k number is on the slide |
| 32–38 | media | | | MetaPhone result tables and curves; coverage-notes already decided to summarize as text |
| 39 | media | | | paper abstracts, replaced by the 702 vignette |
| 40 | skip | | | divider |
| 41, 42 | media | | | FCC process flowchart and OIO timeline, credit Jonathan Mayer; FCC section was cut |
| 43–49, 51, 53–55, 57, 59, 60 | skip | | | bullets |
| 50, 52, 56, 58 | media | | | whitepaper cover, FCC letter scan, Upturn cover, paper-title collage; decorative |

Sources:

- `images/url-metadata-or-content.png` — source: ppt-archive/XX-Surveillance.pptx slide 15, 220 dpi render, box 0,440,2200,860 auto-trimmed (1650×382)
- `images/email-metadata-path.png` — source: ppt-archive/XX-Surveillance.pptx slide 21 (hidden), 220 dpi render, box 340,220,1860,1020 auto-trimmed (1500×781)
- `images/section-215-exchange.png` — source: ppt-archive/XX-Surveillance.pptx slide 23, 220 dpi render, box 300,340,1840,900 auto-trimmed (1492×544)
- `images/usa-freedom-query-pipeline.png` — source: ppt-archive/XX-Surveillance.pptx slide 24, 220 dpi render, box 170,80,1920,1238 auto-trimmed (1718×1151)
- `images/slide028_img014.png` — source: ppt-archive/XX-Surveillance.pptx slide 28, embedded picture `exponential_hops.png` from the earlier media extraction (580×380)
