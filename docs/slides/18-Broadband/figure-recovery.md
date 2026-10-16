# Figure recovery: 18-Broadband

Source: `docs/slides/ppt-archive/18-Broadband.pptx`, 34 slides, rendered 2026-10-16
(headless LibreOffice, 110 dpi contact sheet, 220 dpi captures). No hidden slides, no
pen ink.

| pptx slide | class | target Quarto slide | figure name | notes |
|---|---|---|---|---|
| 1 | skip | | | title |
| 2 | skip | | | bullets (Five Lessons, already in deck) |
| 3 | media | "Speed" Has Many Facets | | `slide003_img001.png` already embedded; the drawn labels (throughput/latency/jitter/loss arrows) are carried by the slide's bullets |
| 4 | media | Different Techniques Measure Different Things | | `slide004_img002.png` already embedded; the drawn "NDT = transport capacity / Ookla = link capacity" callouts are in the notes; the annotated form is recovered from slide 19 instead |
| 5 | skip | | | bullets |
| 6 | keep | new, "The Device Can Be the Bottleneck" (after "Many Factors Limit…") | device-bottleneck-by-model.png | box plot by tier × iPhone model with the 802.11ac callout; one-step build, final state kept |
| 7 | media | The Home Network Is Often the Bottleneck | | `slide007_img004.png` already embedded; drawn callouts carried by the bullets |
| 8 | skip | | | latency-to-Africa bar chart (Gupta et al. 2014); coverage-notes already dropped it as off-theme for the US framing |
| 9 | media | Faster "Speed" Doesn't Mean Better Performance | | `slide009_img006.png` already embedded; the "stops improving above 16 Mbps" callout is the slide's headline |
| 10 | keep | new, "Applications Rarely Use the 'Top Speed'" (before "User Experience Lives in the Application") | app-utilization-vs-capacity.png | scatter with the "apps often do not consume link capacity" callout; no animation |
| 11 | skip | | | bullets (application-quality metrics, already in deck) |
| 12 | skip | | | NCTA "Tracking Cable's Top Internet Speeds" vendor graphic, no attribution |
| 13 | skip | | | news/infographic collage with a "No data!" arrow on the Chicago test map; the point is carried by slide 17 |
| 14 | skip | | | news clippings and NSF/city screenshots, dated |
| 15 | skip | | | Centre Daily Times clipping plus PA map, dated |
| 16 | skip | | | bullets plus a video thumbnail |
| 17 | media (embedded) | new, "Limitation: Where the Tests Actually Ran" (before "Who Runs the Test?") | slide017_img019.png | three-city test-density map, extracted earlier but never used; 886×405, full-width banner |
| 18 | media | Limitation: Who Runs the Test? | | `slide018_img020.png` already embedded |
| 19 | keep | new, "Where M-Lab Sits on the Curve" (after "The Test Itself Lies") | ndt-vs-reality-cdf.png | the CDF with the "M-Lab/NDT" and "Reality" labels; builds end with the labels, final state kept; the M-Lab map behind it is already embedded as `slide019_img021.png` |
| 20, 23, 27 | skip | | | step dividers |
| 21 | skip | | | paper and city-document screenshots with an arrow |
| 22 | skip | | | screenshots (router-based speed test time series; the app scatter duplicates slide 10) |
| 24 | skip | | | raw time-series plots with no axes context |
| 25 | media | The Divide Is Local | | `slide025_img030.png` already embedded |
| 26 | skip | | | latency table/plot, dropped by coverage-notes |
| 28 | media | Step 2: Sometimes You Must Build the Instrument | | `slide028_img032.jpg` already embedded |
| 29 | skip | | | WSJ screenshot collage |
| 30 | skip | | | bullets (Passive Measurement Yields Real Insight, already in deck) |
| 31 | skip | | | bullets plus paper screenshots |
| 32 | keep | new, "Deployment Tradeoffs: Where the Device Sits" (after "Step 2") | measurement-device-placement.png | modem–router–switch–AP chain with the drawn blue frame on the switch; one-step build, final state kept |
| 33 | skip | | | 2019 pilot: survey bar chart with illegible labels and a device-count map; dated and low intuition |
| 34 | skip | | | conclusion bullets |

Captured images (all under `images/`, `git add -f` because the directory is gitignored):

- `device-bottleneck-by-model.png` 1200×997 — source: ppt-archive/18-Broadband.pptx slide 6, 220 dpi render, box 640,318–2248,1656, auto-trimmed, downscaled from 1608 wide
- `app-utilization-vs-capacity.png` 1600×759 — source: slide 10, box 336,390–2664,1626, auto-trimmed, downscaled from 2270 wide
- `ndt-vs-reality-cdf.png` 1465×640 — source: slide 19, box 0,196–1484,844 (the red-framed CDF with its labels), auto-trimmed
- `measurement-device-placement.png` 1600×661 — source: slide 32, box 196,486–2604,1414, auto-trimmed, downscaled from 2246 wide
- `slide017_img019.png` 886×405 — source: slide 17 embedded media, from the earlier extraction, embedded unchanged
