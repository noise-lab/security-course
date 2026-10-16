# Figure recovery: 09-WebPrivacy

Source: `docs/slides/ppt-archive/09-WebPrivacy.pptx`, 41 slides (39 visible; 40–41 hidden), rendered 2026-10-16 with headless LibreOffice at 220 dpi.

| pptx slide | class | target Quarto slide | figure name | notes |
|---|---|---|---|---|
| 1 | skip | | | title |
| 2 | media | | | TCP/IP stack clip art (`slide002_img001.png`), unrelated; not used |
| 3 | media | "On the Internet, They Know You're a Dog" | | Steiner cartoon (`slide003_img002.jpg`); deck quotes the line instead |
| 4 | skip | | | bullets ("Third Party" Online Tracking) |
| 5 | keep | new, after "A Single Page, Dozens of Trackers" | nyt-third-party-request.png | NYT page plus the drawn third-party request box (Cookie + Referer); the extracted `slide005_img003.png` is the page alone. Build is the request box flying in; final state captured |
| 6 | media | "Visualizing the Web of Trackers" | | Lightbeam graph, already embedded (`slide006_img005.png`) |
| 7 | skip | | | text-only request without Referer; covered by "Referer and Cookie Blocking" |
| 8 | keep | new, after "Referer and Cookie Blocking" | cooperative-tracking.png | first party passes its own name in the tracker URL; no animation |
| 9 | media | | | two Chrome cookie-list screenshots (`slide009_img006/007.png`), low-res; dropped in the original conversion |
| 10 | skip | | | "64 independent tracking mechanisms" text slide |
| 11 | skip | | | bullets, 2007-era tracker names |
| 12 | media | "Who Are the Third Parties?" | | already embedded (`slide012_img008.png`) |
| 13 | media | "Why They Track: Behavioral Targeting" | | already embedded (`slide013_img009.png`) |
| 14 | media | | | LUMAscape ad-tech landscape, someone else's figure; skip |
| 15 | skip | | | bullets (Privacy Worries) |
| 16 | skip | | | divider |
| 17 | skip | | | bullet list of tagging mechanisms (text, not a figure) |
| 18 | skip | | | bullets; Quarto fingerprinting slide covers it |
| 19 | media | "Hands-On: Cover Your Tracks" | | already embedded (`slide019_img011.png`) |
| 20 | skip | | | divider |
| 21 | media | | | Cover Your Tracks results table screenshot, unreadable at slide scale |
| 22 | media | "Canvas Fingerprinting" | | already embedded (`slide022_img014.png`) |
| 23 | media | | | canvas-fingerprinting code screenshot, unreadable |
| 24 | skip | | | text |
| 25 | media | | | NHS syphilis page leakage screenshots, dropped in the original conversion |
| 26 | media | | | NHS cookie-policy screenshots, dropped |
| 27 | skip | | | Referer leakage request; Quarto has it as a code block |
| 28 | skip | | | bullets |
| 29 | skip | | | bullets |
| 30 | keep | new, after "Cookie Syncing" | cookie-syncing-redirect.png | trackerX → trackerY redirect inside firstparty.com; five build steps add pieces, nothing covers the base, final state captured including the callout |
| 31 | skip | | | divider |
| 32 | skip | | | bullets |
| 33 | media | | | NOREF extension store screenshot, dated |
| 34 | skip | | | bullets |
| 35 | skip | | | bullets |
| 36 | media | | | Chrome cookie-settings screenshot, dated |
| 37 | skip | | | bullets |
| 38 | media | "Request Blocking: The Most Effective Defense" | | already embedded (`slide038_img022.png`) |
| 39 | media | | | AdBlock Plus / Ghostery logos, decorative |
| 40 | skip | | | hidden in the pptx; DNT screenshot, narrated as history on the GPC slide |
| 41 | skip | | | hidden in the pptx; DNT mechanism screenshot |

## Captured

- `images/nyt-third-party-request.png` (1100×917) — source: `ppt-archive/09-WebPrivacy.pptx` slide 5, Picture 2 + Rectangle 1, final build state, cropped box 140,120,1250,1045 at 220 dpi, auto-trimmed.
- `images/cooperative-tracking.png` (1463×925) — source: `ppt-archive/09-WebPrivacy.pptx` slide 8, all shapes, no animation, cropped box 565,270,2035,1200 at 220 dpi, auto-trimmed.
- `images/cookie-syncing-redirect.png` (2026×1053) — source: `ppt-archive/09-WebPrivacy.pptx` slide 30, all shapes, final build state, cropped box 35,110,2075,1170 at 220 dpi, auto-trimmed.
