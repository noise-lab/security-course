# Figure recovery: XX-Election

Source: `docs/slides/ppt-archive/XX-Election.pptx`, 57 slides (52 and 53 hidden),
rendered 2026-10-16 with `pptx-figures.py` at 110 dpi (triage) and 220 dpi (capture).

This deck has almost no drawn PowerPoint diagrams: it is title/bullet slides plus
embedded pictures, nearly all of which the earlier media extraction already saved
under `images/slideNNN_imgNNN.*`. The one drawn figure (slide 56) is recovered from
the render; three embedded graphics that carry intuition and that the Quarto deck
lacked are embedded from the extracted copies.

| pptx slide | class | target Quarto slide | figure name | notes |
|---|---|---|---|---|
| 1 | skip | | | title |
| 2 | media | new, "The Paper Trail, Six Years Later" | verifier-map-2022.png | Verified Voting Verifier, Nov 2022; cropped from `slide002_img001.png`, site chrome removed; complements the 2016 map already in the deck |
| 3 | skip | | | Verifier Illinois state view, dated screenshot |
| 4, 13 | skip | | | Stark & Wagner quote, already the opening slide |
| 5 | media | already used | slide005_img003.png | Dewey Defeats Truman |
| 6, 51 | skip | | | AP news clipping, dated |
| 7, 8, 10, 11 | skip | | | candidate headshots and headlines, decorative |
| 9 | skip | | | bullets |
| 12 | media | already used | slide012_img013.png | butterfly ballot photo |
| 14–20 | skip | | | requirement bullets, consolidated in "The Core Requirements" |
| 21 | skip | | | Verified Voting "resilient election ecosystem" checklist screenshot; covered by the requirements slides |
| 22 | skip | | | six small stock photos of voting technologies, decorative |
| 23–27 | skip | | | bullets |
| 28 | skip | | | 1893 Australian ballot photo; timeline bullet covers it |
| 29 | skip | | | lever-machine photos plus Saltman "jam at 99" text; anecdote is in the notes |
| 30 | media | new, "Florida 2000, Up Close" | slide030_img024.png | Sun-Sentinel annotated butterfly-ballot graphic (Daniel Niblock); the photo half (img023) duplicates slide 12 |
| 31 | media | new, "Florida 2000, Up Close" | slide031_img025.png | NYT chad diagram; attributed in the image and caption |
| 32 | skip | | | HAVA quote with Act title page; quote already on "The DRE Detour" |
| 33, 43, 45, 46 | skip | | | DRE photos and news screenshots; attack already illustrated by slide 41 |
| 34–36, 39, 40, 42 | skip | | | bullets |
| 37, 38 | skip | | | news text screenshots, dated |
| 41 | media | already used | slide041_img033.png | Diebold vote-stealing control panel |
| 44 | media | already used | slide044_img034.png | Verified Voting 2016 map |
| 47 | skip | | | DRE with VVPAT photo; redundant with the BMD photo already used |
| 48 | media | already used | slide048_img041.png | ballot-marking devices |
| 49, 50 | skip | | | Verifier 2020 and 2018 views; 2022 (slide 2) is the freshest and one is enough |
| 52, 53 | skip | | | hidden in the deck; bullets |
| 54, 55 | skip | | | divider and bullets |
| 56 | keep | new, "RLA: Sample, Check, Grow" | rla-sample-structure.png | the deck's only drawn diagram; builds in three steps (bar, down arrow + sample, right arrow); captured the final state, nothing stripped |
| 57 | skip | | | Augur/blockchain paper title clip; concept covered in text |

## Captured

- source: `ppt-archive/XX-Election.pptx` slide 56, 220 dpi render, crop box 640,220,1620,470 with auto trim; `images/rla-sample-structure.png` 973x243
- source: `ppt-archive/XX-Election.pptx` slide 2, extracted `images/slide002_img001.png`, crop box 0,130,1186,720 with auto trim and the site's state picker and toggle painted out; `images/verifier-map-2022.png` 1182x590 (Verified Voting)
- source: `ppt-archive/XX-Election.pptx` slide 30, extracted `images/slide030_img024.png` 729x577 embedded as is (Sun-Sentinel graphic, Daniel Niblock)
- source: `ppt-archive/XX-Election.pptx` slide 31, extracted `images/slide031_img025.png` 734x496 embedded as is (New York Times graphic)
