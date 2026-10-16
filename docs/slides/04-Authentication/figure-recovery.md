# Figure recovery: 04-Authentication

Source: `docs/slides/ppt-archive/04-Authentication.pptx`, 58 slides (41–58 hidden
in the pptx; rendered anyway), rendered headlessly 2026-10-16 at 110 and 220 dpi.
The Quarto deck had already embedded five extracted media files
(`slide012_img004`, `slide032_img011`, `slide035_img012`, `slide051_img017`,
`slide054_img018`); this pass recovers the diagrams that were *drawn* in
PowerPoint and therefore lost in the text/media extraction.

| pptx slide | class | target Quarto slide | figure name | notes |
|---|---|---|---|---|
| 1 | skip | | | title |
| 2 | skip | | | bullets ("What Access Control Is For") |
| 3 | keep | new, "The Threat Model in One Grid" (after "The Threat Model Has Shifted") | threat-model-grid.png | 2×2 trusted/untrusted × single/multi-user grid with the `??` cell; five build steps; stripped "Rectangular Callout 4" (DOS note moved to the notes). Cell pictures are the clip art and mainframe photo from the original deck (`slide003_img00{1,2,3}`), unattributed stock |
| 4–5 | skip | | | bullets |
| 6 | skip | | | divider |
| 7 | keep | existing, "Identification, Authentication, Authorization" (banner under the sequence paragraph) | security-sequence.png | three-box flow with Authorization / Accountability and Preventive / Reactive labels; no animation |
| 8 | skip | | | bullets |
| 9 | skip | | | users ↔ OS ↔ resources ovals; same idea as slide 50 with less precision, superseded by the reference-monitor figure |
| 10–11 | skip | | | text; already slides "A Common Framework" and "ACLs vs. Capabilities" |
| 12 | media | "Unix: A Simplified ACL Model" | | `ls -l` screenshot already embedded; the xkcd "sudo make me a sandwich" panel is someone else's and was dropped earlier |
| 13–14 | skip | | | bullets ("Hack!" callout is decorative) |
| 15–16 | media | | | Android permission dialog and manifest screenshots, dropped in the earlier curation |
| 17 | skip | | | six stacked "system layers" boxes beside the Android framework stack image; minor |
| 18 | skip | | | bullets |
| 19 | media | | | Google Docs capability-URL screenshot, covered in prose |
| 20–31 | skip | | | bullets and dividers (OAuth definitions, roles, JWT, vulnerabilities, conclusion) |
| 32 | media | "The Flow, Six Steps" | | OAuth abstract flow (Wikimedia), already embedded |
| 33–34 | skip | | | bullets, Google Cloud setup steps |
| 35 | media | "A Real OAuth Flow: Strava API" | | Strava flow, already embedded |
| 36–44 | skip | | | VPN / IPsec block, scoped out of this deck (see coverage-notes.md); 39 is a UChicago VPN screenshot, 40 a breakout divider |
| 45 | skip | | | End-to-end VPN diagram (clouds, IPsec tunnels, FW/VPN box); a good drawing but belongs to the VPN block that is out of scope. Re-run `crop` on `r220/slide-045.png` box 480,560,1850,1050 if a VPN segment is ever added |
| 46 | skip | | | bullets (core-dump, race condition); covered in "Timeless Design Principles" |
| 47 | media | | | TENEX timing-attack figure is Ross Anderson's (*Security Engineering*, fig. 4.25); dropped earlier for attribution, described in notes |
| 48–49 | skip | | | bullets, Java file-descriptor code |
| 50 | keep | new, "The Reference Monitor" (after "A Common Framework: Subject, Verb, Object") | reference-monitor.png | (User, program) → Monitor → Resource with Policy feeding the monitor; no animation; the slide's body text under the figure was masked before cropping |
| 51 | media | "Scaling Access Control: Abstractions" | | protection-domain Venn diagram, already embedded |
| 52–53 | skip | | | bullets |
| 54 | media | "Make the Action the Permission" | | iOS camera prompt, already embedded |
| 55–56 | skip | | | divider, bullets |
| 57 | keep | new, "Levels and Lattices, Drawn" (after "Scaling Access Control: Abstractions") | classification-levels.png | five-level classification ladder (left column) |
| 58 | keep | same new slide | classification-lattice.png | seven-node nuclear/bio compartment lattice (right column) |

## Captured images

- `images/threat-model-grid.png` (942×862) — source: ppt-archive/04-Authentication.pptx slide 3, "Rectangular Callout 4" stripped, 220 dpi
- `images/security-sequence.png` (1179×412) — source: ppt-archive/04-Authentication.pptx slide 7, 220 dpi
- `images/reference-monitor.png` (1237×426) — source: ppt-archive/04-Authentication.pptx slide 50, body placeholder masked, 220 dpi
- `images/classification-levels.png` (440×848) — source: ppt-archive/04-Authentication.pptx slide 57 (graphic frame), 220 dpi
- `images/classification-lattice.png` (1396×935) — source: ppt-archive/04-Authentication.pptx slide 58, 220 dpi

Speaker-notes rows added as 3a, 9a and 25a so the existing footer numbers in
the `#` column and the prose cross-references ("slide 7", "slide 23") stay as
they were; renumber in one pass if the deck's numbering is ever refreshed.
