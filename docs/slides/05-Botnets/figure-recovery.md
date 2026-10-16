# Figure recovery: 05-Botnets

Source: `docs/slides/ppt-archive/05-Botnets.pptx`, 50 slides (17 and 18
hidden), rendered 2026-10-16 with `pptx-figures.py` at 110 dpi (contact
sheet) and 220 dpi (crops). Scope: botnet-specific figures only. The
DoS material (SYN flood, amplification, SYN cookies, uRPF, Great Cannon)
belongs to the 05-DoS deck and was recovered on its own branch.

| pptx slide | class | target Quarto slide | figure name | notes |
|---|---|---|---|---|
| 1 | skip | | | title |
| 2–5 | skip | | | virus and worm definitions, bullets only |
| 6 | skip | | | divider "Worms: then and now" |
| 7 | media | | | Morris headshot (`slide007_img001.jpg`), decorative; dropped by the Quarto conversion |
| 8–10 | skip | | | Morris worm bullets |
| 11 | skip | | | divider "2000s: worms go mainstream" |
| 12 | media | | | Summer-2001 outbreak plot with red "three major worm outbreaks" arrows (`slide012_img002.png`); worm history, not botnets; superseded by the Code Red curve already in the deck |
| 13–15 | skip | | | Code Red bullets |
| 16 | media | "Worms Go Mainstream" (already embedded) | | Code Red infection curve `slide016_img003.png`, in use; the "exponential infection rate" callout is text only |
| 17–18 | media | | | hidden slides; Random Constant Spread equations (`slide017_img004.png`, `slide018_img005.png`) with callouts; cut with the worm-modeling material |
| 19–23 | skip | | | fast-worm design, Code Red I v2 / II, Nimda, signature defenses; bullets only |
| 24 | media | | | Paxson's Code Red I/II plot (`slide024_img006.png`) with annotations; someone else's figure, and redundant with the Code Red curve |
| 25–28 | skip | | | Slammer bullets |
| 29–30 | media | "Slammer in 30 Minutes" (already embedded) | | CAIDA maps `slide029_img007.png`, `slide030_img008.png`, in use |
| 31–34 | skip | | | Slammer impact, Storm bullets |
| 35 | media | | | Storm spam-tactic date table (`slide035_img009.jpg`); low value |
| 36 | skip | | | "other famous botnets" list |
| 37 | media | "Mirai (2016)" (already embedded) | | `slide037_img010.png`, in use |
| 38 | skip | | | divider "Botnets" |
| 39 | skip | | | botnet definition bullets (already the "What Is a Botnet?" slide) |
| 40 | keep | new, "Rallying the Botnet", after "Command and Control (C&C)" | botnet-rallying-clouds.png | drawn clouds, hosts, spread arrows; the body text and the "Options" box overlap the figure, so both text boxes stripped before cropping |
| 41 | keep | new, "Rendezvous Through Dynamic DNS", after "Rallying the Botnet" | botnet-dynamic-dns-control.png | drawn box diagram: infected machine, dynamic DNS, botnet controller; only the bullet body animates |
| 42 | skip | | | centralized vs. P2P C&C bullets (already the C&C slide) |
| 43 | skip | | | botnet history bullets with a text callout |
| 44 | keep | new, "The Botnet Economy in One Picture", after "What Is a Botnet?" | botnet-spam-economy.png | embedded Wikipedia *Botnet* diagram that the earlier media extraction missed (`ppt/media/image11.png`); the slide squashes it to 486×409, so the native 495×599 file is used instead of a render crop; credited on the slide as "Source: Wikipedia" |
| 45 | skip | | | botnet usage list |
| 46 | skip | | | divider "Defenses" |
| 47–50 | skip | | | IRC monitoring, detection, DNS monitoring bullets (already consolidated into the Defenses slide) |

## Captured

- `images/botnet-rallying-clouds.png` (1098×522) — source: `ppt-archive/05-Botnets.pptx` slide 40, shapes "Rectangle 3" and "Rectangle 4" stripped, 220 dpi render, box 480,460,1660,1060, auto-trimmed.
- `images/botnet-dynamic-dns-control.png` (932×434) — source: `ppt-archive/05-Botnets.pptx` slide 41, 220 dpi render, box 540,235,1500,680, auto-trimmed.
- `images/botnet-spam-economy.png` (495×599) — source: `ppt-archive/05-Botnets.pptx` slide 44, `ppt/media/image11.png` copied as is (Wikipedia *Botnet* article diagram, as credited on the slide).

## Left out

- Slides 12, 17, 18, 24: worm-propagation plots and the Random Constant Spread
  model. The Quarto deck compressed the worm catalog to one arc and already
  carries the Code Red curve; 24 is Paxson's figure.
- Slide 43's "put these pieces together and add a controller" callout is text,
  not a figure; its point is made by the new economy slide.
