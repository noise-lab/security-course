# Figure recovery: XX-Vulnerabilities

Source: `docs/slides/ppt-archive/XX-Vulnerabilities.pptx`, 25 slides, rendered 2026-10-16
(headless LibreOffice, 110 dpi contact sheet). No hidden slides, no pen ink, one animation
(slide 4, a media-play trigger on the embedded video).

Result: **nothing to recover.** The deck has no diagrams drawn in PowerPoint. Every
non-text slide is an embedded screenshot, news clipping, court-document excerpt, or
video poster frame, and the earlier media extraction already saved all of those under
`images/slideNNN_imgNNN.png`. The Quarto deck already embeds the two that teach
(Google VRP payout table, Cure53 Mozilla VPN report); `coverage-notes.md` records why
the rest were dropped (headlines, title banners, a headshot, logos).

| pptx slide | class | target Quarto slide | figure name | notes |
|---|---|---|---|---|
| 1 | skip | | | title |
| 2 | skip | | | bullets ("Vulnerabilities") |
| 3 | media | "Privacy Vulnerabilities Are Real Vulnerabilities" | | Nest-thermostat headline + article text screenshots (`slide003_img001-003`); dated news clip, text already paraphrased on the slide |
| 4 | skip | | | poster frame of the embedded demo video `smart-tv-control.mp4` (Firefox address bar + "User visits a site with a malicious script"); a video still, not a figure; the video itself is not in `images/` |
| 5 | skip | | | bullets (two statute names) |
| 6 | skip | | | bullets (DMCA); "Rectangle 5" is an empty text frame |
| 7 | media | | | Sklyarov headshot (`slide007_img004`); personal photo, dropped per coverage notes |
| 8 | media | | | NYT Markoff clipping on Felten/SDMI (`slide008_img005-006`); someone else's page, dated |
| 9 | skip | | | bullets; the Quarto deck already has the timeline as a table |
| 10 | skip | | | bullets |
| 11 | skip | | | bullets (CFAA); extra text boxes are empty |
| 12 | media | | | two paragraphs of an academic paper on chilling effects (`slide012_img007-008`); text screenshots, unattributed on the slide |
| 13 | media | | | ACLU Sandvig v. Barr page banner + case summary (`slide013_img009-012`); text screenshots |
| 14 | skip | | | bullets; already "Does a ToS Violation Make You a Criminal?" |
| 15 | media | | | EFF Van Buren article screenshot (`slide015_img013-015`); text screenshot |
| 16 | media | | | Van Buren opinion footnote (`slide016_img016`); quoted text, already paraphrased on the Van Buren/Sandvig slide |
| 17 | skip | | | bullets; already "Three Paths After You Find a Bug" |
| 18 | media | | | "Zuckerberg's Facebook page hacked" headline + video poster (`slide018_img017-018`); dated clip, dropped per coverage notes |
| 19 | media | "Bug Bounties: Would You Hire a Hacker?" | | bullets plus HackerOne/bug-bounty-list logos (`slide019_img019-020`); decorative |
| 20 | media | | | Google "How we handle security vulnerabilities" page screenshot (`slide020_img021-022`); wall of text; the 90-day/7-day policy is already stated in the speaker notes with a link |
| 21 | media (used) | "What a Bounty Pays" | | Google VRP payout table (`slide021_img023`); already embedded |
| 22 | skip | | | bullets |
| 23 | skip | | | bullets |
| 24 | media (used) | "What a Pentest Report Looks Like" | | Cure53 Mozilla VPN report excerpt (`slide024_img024-025`); already embedded |
| 25 | skip | | | discussion title |

Figures captured: none.
