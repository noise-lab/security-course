# 12-Compliance — instructor notes

## Status (2026-11-18)

The deck carries every slide of `ppt-archive/12-Compliance.pptx` (70 slides) in
order: same claims, numbers, wording (tidied for Markdown), and examples, with every
pptx graphic embedded and the pptx speaker notes carried into each slide's
`::: {.notes}` block (followed by the course's teaching points). Build sequences are
collapsed into one slide showing the final state (the build order is described in the
notes). The course's own slides from the previous version are kept in their original
places: the framing slide, GPC, the 2026 enforcement vignette, the Study 2 bridge, the
control-method definitions, the ~30% roll-up, Three Families, Clear Violations vs.
Loopholes (with the Disney note), the Enforcement Gap section, and the closing
Discussion prompt. Nothing was removed.

### pptx → qmd mapping

| pptx | qmd slide | note |
|---|---|---|
| — | From Law on the Books to Law in Action | course framing slide (kept) |
| 1 | Study 1 section divider | title + authors |
| 2 | Where Does Our Data Go? | `data-flow-to-third-parties.png` (whole drawing) |
| 3 | Potential Harms to Consumers | |
| 4 | The California Consumer Privacy Act | |
| 5 | Who Is Subject to the CCPA? | build collapsed: both versions of threshold 2 |
| 6 | Opt-out Methods | icon inline; placement/icon rule line kept |
| — | Global Privacy Control (GPC): Opt Out Once | course slide (kept) |
| — | A 2026 Enforcement Wake-Up Call | course current-events slide (kept, integrated) |
| 7 | Research Questions | |
| 8 | Outline | |
| 9 | A. Vantage Point & Dataset Selection (states) | state glyphs as a table |
| 10 | A. Vantage Point & Dataset Selection (measurements) | |
| 11 | B. Methodology (keywords) | `keyword-list-sources.png` |
| 12 | B. Methodology (pipeline) | `method-keyword-pipeline.png` |
| 13 | Verify Methods (false positives/negatives) | |
| 14 | Verify Methods (source vs. screenshot) | `slide014_img021/022.png` |
| 15 | Outline (Findings) | |
| 16 | Research Questions (RQ1) | |
| 17 | RQ1 | `slide017_img023.png` |
| 18 | Research Questions (RQ2) | |
| 19 | Opt-out Methods (recap) | |
| 20 | RQ2 | `rq2-compliance-tree.png`; the 45% callout build is text |
| 21 | Research Questions (RQ3) | |
| 22 | RQ3 (chart) + RQ3 (table) | two build states that hide each other → two slides; `optout-link-by-state-over-time.png` (new) and `slide022_img025.png` |
| 23 | Research Questions (RQ4) | |
| 24 | Frictionless Opt-Out Preference Signals | `gpc-support-table.png`; the three boxes of the first build state are bullets |
| 25 | Who Is Subject to the CCPA? (recap) | |
| 26 | RQ4 | `slide026_img028.png` |
| 27 | Reasons for Potential Non-Compliance | `rq4-noncompliance-reasons.png` |
| 28 | D. Limitations | full talk script from the pptx notes kept in the notes block |
| 29 | Summary | as a two-column table; "Questions?" and the presenter's email dropped |
| 30 | Future Direction | |
| 31 | Study 2 section divider | |
| — | Beyond the Link: Does Opt-Out Actually Work? | course bridge slide (kept) |
| 32 | Summary of Findings | |
| 33 | The CCPA | |
| 34 | The CPRA | pptx said "January 2021"; corrected to January 2023 (matches pptx slide 4), noted in the slide notes |
| 35 | CCPA Opt-Out Requirements | |
| 36 | Research Questions | |
| 37 | Outline | |
| 38 | Dataset Selection | `dataset-selection-funnel.png` + the previous version's method bullets |
| 39 | Method | icon row as three columns |
| 40 | Opt-Out Metrics | |
| — | Opt-Out Control Methods (definitions) | course slide (kept) |
| 41 | Opt-Out Control Methods (screenshots) | `slide041_img032–034.png` |
| 42 | Dark Patterns Taxonomy Development | |
| 43 | Data Collection & Labelling Process | `labelling-process.png` |
| 44 | Follow-Up Process | |
| 45 | Findings divider | |
| 46 | RQ1 divider | |
| 47 | Categorizing Opt-Out Request Outcome | `outcome-decision-flow.png` |
| 48 | Opt-Out Request Outcomes (failure to submit) | `slide048_img035.png` |
| 49 | Opt-Out Request Outcomes (failure to fulfill) | |
| 50 | Opt-Out Request Outcomes (resolved) | |
| — | ~30% of Opt-Out Attempts Fail | course roll-up slide (kept) |
| 51 | RQ2 divider | |
| 52 | Opt-Out Control Methods (Table 2) | `control-methods-by-vendor-table.png` (new) |
| 53 | Number of Clicks | `clicks-by-control-method.png` |
| 54 | Personal Information Required | `slide054_img036.png` |
| 55 | Do Opt-Out Processes Violate CCPA Requirements? | `outcomes-vs-ccpa.png` |
| 56 | RQ3 divider | |
| — | Three Families of Dark Patterns | course slide (kept) |
| 57 | Obstruction (verified email, separate submissions) | `slide057_img037/038.png` |
| 58 | Obstruction (asymmetry, identity confirmation) | `slide058_img039/040.png` |
| 59 | Interface Interference | `slide059_img041.png` |
| 60 | Misdirection | `slide060_img042.png` |
| 61 | RQ3 (violations or loopholes) divider | |
| 62 | Clear Violations vs. Loopholes | `slide062_img043.png`; pptx slide is untitled, the previous version's title, text, and Disney note kept |
| 63 | RQ4 divider | |
| 64 | Prevalence of Dark Patterns (histogram) | `dark-pattern-count-histogram.png` |
| 65 | Prevalence of Dark Patterns (table) | `dark-pattern-prevalence-table.png` |
| 66 | Distribution Across Opt-Out Control Methods | `dark-patterns-by-control-method.png` (new) |
| 67 | Distribution Across Third-Party Platforms | `dark-patterns-by-third-party.png` (new, Fig. 10 + Table 8) |
| 68 | Discussion | |
| — | Why Automated Compliance Is Hard / The Enforcement Gap / What Measurement Tells Policy | course section (kept) |
| 69 | (folded into Summary of Findings) | draft slide listing three RQs without answers |
| 70 | Summary of Findings | |
| — | Discussion (prompt) | course closing slide (kept) |

## Next-year refresh notes

Only the 2026 enforcement slide and the Disney note on "Clear Violations vs. Loopholes" are dated. Refresh it per `../TEMPLATE.md` →
"Annual current-events refresh" (web-verify; swap only for something fresher and
confirmed):

- **Disney CA-AG settlement — Feb 11, 2026, $2.75M** (fragmented opt-out / GPC not
  honored across streaming services). Swap if a bigger GPC-specific settlement lands.
- **General Motors CA-AG settlement — May 8, 2026, $12.75M** (data minimization +
  purpose limitation; OnStar → LexisNexis/Verisk). Watch for the next automaker
  telematics action.
- **Healthline $1.55M (Jul 1, 2025)** — the previous CCPA record.
- Watch **CPPA enforcement** for a distinct, sizable CPPA-only action; some
  aggregators conflate a Feb 2026 CPPA streaming action with the AG's Disney case.
- The Study 1 five-state design uses Illinois as the no-law control; 20 states had
  comprehensive laws by January 2026, so note in class whether Illinois still works
  as a control.

## Curated images

- Paper figures and screenshots from the two studies (own group): see the mapping
  table and `figure-recovery.md` for crop provenance.
- Not embedded (decorative): title/logo images (slide001/031), the slide 3 padlock
  icon (slide003_img006), the slide 24 DuckDuckGo logo (slide024_img026), pipeline
  icons and repeated state-map glyphs (slide009/010/012/019), and the slide 24
  base-state boxes. The slide 2 clip art is inside `data-flow-to-third-parties.png`.

## Source

- Rebuilt 2026-11-18 from `ppt-archive/12-Compliance.pptx` (70 slides, two papers)
  so that every pptx slide and graphic is present, with the previous version's course
  slides kept; the earlier 25-slide consolidation is in git history.
