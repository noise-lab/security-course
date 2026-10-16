# Figure recovery: 05-DoS

Source: `docs/slides/ppt-archive/05-DoS.pptx`, 39 slide files of which 4 are
hidden (20, 21, 23, 26), so a plain headless render shows 35 pages. Rendered
2026-10-16 at 220 dpi from a scratch copy with the hidden flags removed, so
the slide numbers below are the pptx's own `slideN.xml` numbers and two of
the recovered figures come from hidden slides.

| pptx slide | class | target Quarto slide | figure name | notes |
|---|---|---|---|---|
| 1 | skip | | | title |
| 2 | media | | | news clippings (`slide002_img001.png`), dated; coverage notes already dropped it |
| 3 | media | "Case Study: Mirai and the Dyn Attack" | | NYT page, already embedded as `slide003_img002.png` |
| 4 | media | "Why a 'Small' Botnet Hurt So Much" | | outage map, already embedded as `slide004_img003.png`; headline crop `img004` dropped |
| 5 | skip | | | Dyn post-mortem quotation, text only; covered in notes |
| 6 | skip | | | attacker/victim boxes with four arrows; carries nothing the heading does not |
| 7–9 | skip | | | bullets |
| 10 | keep | new, after "Reflection and Amplification" | smurf-broadcast-amplification.png | two-step build (request, replies) captured in final state |
| 11 | skip | | | TCP divider |
| 12, 13 | skip | | | bullets |
| 14 | keep | new, after "TCP SYN Flooding" | tcp-three-way-handshake-timeline.png | no builds |
| 15, 16 | skip | | | bullets |
| 17 | keep | new, after "The Handshake as a Timeline" | syn-flood-timeline.png | no builds |
| 18 | skip | | | MS Blaster bullets; in notes already |
| 19 | skip | | | DNS divider |
| 20, 21 | skip | | | hidden bullets (DNS DoS, 2007 root attack); root attack is in the notes |
| 22 | keep | new, after the Smurf slide | dns-amplification-reflection.png | three-step build captured in final state; the "Prevention" line left out (it is the Open Resolvers slide) |
| 23 | keep | new, after "Application-Layer and Crypto DoS" | tls-handshake-dos.png | hidden slide; builds are bullet entrances only |
| 24 | skip | | | Defenses divider |
| 25 | skip | | | bullets |
| 26 | keep | new, after "Defense: Ingress Filtering" | ingress-filtering-edge.png | hidden slide; builds are entrances only; cropped below the title |
| 27, 28 | skip | | | bullets |
| 29 | keep | new, after "SYN Cookies: The Exchange" | syn-cookie-sequence-number-layout.png | no builds |
| 30 | keep | new, after "Defense: SYN Cookies" | syn-cookie-exchange.png | 19 build steps, all entrances; final state is the full exchange |
| 31 | keep | new, after "Defense: uRPF and Its Limits" | urpf-strict-mode-check.png | embedded object (appears to follow Cisco's uRPF documentation; credited in the notes) |
| 32 | media | "Defense: uRPF and Its Limits" | | asymmetric-routing picture, already embedded as `slide032_img013.png` |
| 33 | media | | | Great Cannon news photo (`slide033_img014.png`); dropped by coverage notes |
| 34 | media | | | Citizen Lab on-path system figure (`slide034_img015.png`); dropped by coverage notes as redundant with slide 35 |
| 35 | media | "Weaponizing the Network: China's Great Cannon" | | already embedded as `slide035_img016.png` |
| 36, 37 | media | | | further Great Cannon steps (`img017`, `img018`), redundant once one is shown |
| 38, 39 | media | | | client-geography and referrer charts (`img019`, `img020`); details are in the notes |

Nine figures captured, nine new slides, nine speaker-notes rows.

source: `ppt-archive/05-DoS.pptx` slide 10, final build state, box 340,260,1800,760 at 220 dpi, auto-trimmed → `images/smurf-broadcast-amplification.png` (1414×470)
source: `ppt-archive/05-DoS.pptx` slide 14, box 540,290,1700,1150 → `images/tcp-three-way-handshake-timeline.png` (1084×821)
source: `ppt-archive/05-DoS.pptx` slide 17, box 540,290,1700,1170 → `images/syn-flood-timeline.png` (1073×841)
source: `ppt-archive/05-DoS.pptx` slide 22, final build state, box 420,350,1860,900 → `images/dns-amplification-reflection.png` (1414×523)
source: `ppt-archive/05-DoS.pptx` slide 23 (hidden), box 400,330,1840,760 → `images/tls-handshake-dos.png` (1415×399)
source: `ppt-archive/05-DoS.pptx` slide 26 (hidden), box 280,217,1890,665 → `images/ingress-filtering-edge.png` (1577×448)
source: `ppt-archive/05-DoS.pptx` slide 29, box 390,900,1750,1225 → `images/syn-cookie-sequence-number-layout.png` (1343×305)
source: `ppt-archive/05-DoS.pptx` slide 30, final build state, box 1215,300,1740,1095 → `images/syn-cookie-exchange.png` (495×775)
source: `ppt-archive/05-DoS.pptx` slide 31, box 560,345,1680,925 → `images/urpf-strict-mode-check.png` (1113×576)
