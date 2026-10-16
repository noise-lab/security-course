# Figure recovery: 08-DNS

Source: `docs/slides/ppt-archive/08-DNS.pptx`, 36 slides (27 visible, 28–36 hidden; LibreOffice renders only the visible 27), rendered 2026-10-16.

| pptx slide | class | target Quarto slide | figure name | notes |
|---|---|---|---|---|
| 1 | skip | | | title |
| 2 | skip | | | bullets, "What is DNS?" |
| 3 | skip | | | bullets, DNS properties and hierarchy |
| 4 | skip | | | bullets, DNS goals |
| 5 | keep | new, "The Lookup in One Picture" (after "A Single Lookup, Step by Step") | dns-lookup-walk.png | base lookup walk; strip "Picture 13", "Picture 57" (eavesdroppers, builds 17–18) and "TextBox 3" (red callout, build 19) |
| 5 | keep | new, "Where the Eavesdroppers Sit" (after "DNS Leaks More Than You Think") | dns-lookup-eavesdroppers.png | final build state with both spies; strip "TextBox 3" only |
| 6 | media | "Your Devices Announce Themselves" | slide006_img009.png | already embedded |
| 7 | media | "Website Fingerprinting" | slide007_img010.png | already embedded; `_img011`/`_img012` dropped earlier |
| 8 | skip | | | bullets, existing approaches |
| 9 | keep | new, "Before and After DoH, Drawn" (left column) | dns-first-hop-adversary.png | ISP resolver as the spy; strip "Picture 36" (on-path spy, exits in build 1), "TextBox 4" (green callout), "Title 1" (descenders bled into the crop) |
| 10 | skip | | | same drawing as 23 without the callouts; superseded |
| 11 | skip | | | dated news screenshot (Firefox TRR announcement) |
| 12 | skip | | | dated blog screenshot plus two bullets already in the deck |
| 13 | skip | | | dated Mozilla announcement plus the Firefox/Android screenshots the deck already has (slide024_img070) |
| 14 | media | "DoH Can Even Perform Well" | slide014_img034.png | already embedded; the pptx adds two red callout boxes, which the Quarto caption already states |
| 15 | skip | | | bullets, "on by default" |
| 16 | media | | slide016_img035–044 | interface screenshot grid, dropped in the earlier curation |
| 17 | media | | slide017_img045–054 | resolver-option screenshot grid, dropped earlier |
| 18 | skip | | | survey questions plus Android screenshots |
| 19 | media | | slide019_img057–058 | Firefox DoH-response bar chart; not embedded (the deck carries the trust chart from 21) |
| 20 | media | | slide020_img059–060 | pie charts, setting choice with/without information; not embedded, the bullet "more information does shift some choices" covers it |
| 21 | media | "Users Don't Understand — or Trust — Resolvers" | slide021_img062.png | already embedded |
| 22 | skip | | | bullets, summary and future directions |
| 23 | keep | new, "Before and After DoH, Drawn" (right column) | doh-third-party-resolver.png | third-party resolver as the spy; strip "TextBox 2", "TextBox 56", "TextBox 4" (the three callouts, builds 2–4); the callouts became the slide's bullets |
| 24 | media | "The Architectural Crisis: Centralization" / "On by Default" | slide024_img070.png | already embedded; `_img071` (dnscrypt.info list) dropped earlier |
| 25 | skip | | | text, ODNS goal and three steps (already the numbered list in "How Oblivious DNS Works") |
| 26 | skip | | | ODNS architecture; the build moves the recursive and adds the ODNS server, and the static render overlaps the two; slide 27's base is the same final state |
| 27 | keep | new, "Oblivious DNS in One Picture" (after "How Oblivious DNS Works") | odns-query-exchange.png | 53-step build of moving labels; kept one label per hop and dropped the ones that overlap: "TextBox 2", "TextBox 59", "Picture 58", "TextBox 56", "Picture 49", "Picture 50", "TextBox 55" |
| 28 | skip | | | hidden; ODNS key distribution via self-certifying `.odns` names, not covered by the Quarto deck |
| 29–32 | skip | | | hidden; bullets (protocol changes, implementation, evaluation, EDNS0 client subnet) |
| 33 | media | | slide033_img101.png | hidden; "which recursives can ODNS use" table with checkmarks; not embedded |
| 34–35 | skip | | | hidden; bullets |
| 36 | media | "Distributing Queries Across Resolvers" | slide036_img102.png | hidden in the pptx but already embedded in the Quarto deck |

## Captured

- `images/dns-lookup-walk.png` (2670×1025) — source: ppt-archive/08-DNS.pptx slide 5, shapes "Picture 13", "Picture 57", "TextBox 3" stripped, 220 dpi, box 30,370,2900,1420 auto-trimmed.
- `images/dns-lookup-eavesdroppers.png` (2670×1025) — source: ppt-archive/08-DNS.pptx slide 5, shape "TextBox 3" stripped, same box.
- `images/dns-first-hop-adversary.png` (2670×1025) — source: ppt-archive/08-DNS.pptx slide 9, shapes "Picture 36", "TextBox 4", "Title 1" stripped, same box.
- `images/doh-third-party-resolver.png` (2670×1025) — source: ppt-archive/08-DNS.pptx slide 23, shapes "TextBox 2", "TextBox 56", "TextBox 4" stripped, same box.
- `images/odns-query-exchange.png` (2815×995) — source: ppt-archive/08-DNS.pptx slide 27, shapes "TextBox 2", "TextBox 59", "Picture 58", "TextBox 56", "Picture 49", "Picture 50", "TextBox 55" stripped, box 30,400,2934,1420 auto-trimmed.

All five are the instructor's own drawings (server clip art plus arrows and labels); no outside attribution needed.
