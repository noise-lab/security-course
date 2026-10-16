# Figure recovery: 06-Routing

Source: `docs/slides/ppt-archive/06-Routing.pptx`, 58 slides (15 hidden:
5, 45–58), rendered 2026-10-16 at 220 dpi with `pptx-figures.py`. Slide 2
(BGP overview + routing table) was recovered separately on 2026-10-14
(commit a2cf1d3) and is not repeated here.

| pptx slide | class | target Quarto slide | figure name | notes |
|---|---|---|---|---|
| 1 | skip | | | title |
| 2 | done | "BGP in One Picture" | bgp-overview.png, bgp-routing-table.png | recovered 2026-10-14 |
| 3 | skip | | | bullets |
| 4 | media | "Case Study: The 1997 Route Leak" | slide004_img002.png | already embedded |
| 5 | skip | | | hidden; Renesys blog screenshot, duplicate of 11 |
| 6 | media | "Case Study: China's "Accidental" Hijack (2010)" | slide006_img004.png | already embedded |
| 7 | skip | | | Renesys AS-graph already embedded as slide007_img005.png; the render adds one live pen-ink scribble (red circles, "100", "?") which is a lecture annotation, not a figure |
| 8 | skip | | | bullets (famous hijacks) |
| 9 | media | "Case Study: Pakistan vs. YouTube (2008)" | slide009_img006.png | already embedded |
| 10–15 | skip | | | bullets; 11–12 duplicate 5–6 |
| 16 | keep | new, "Redirection, Drawn: Two Routes to Lie About" | hijack-phishing-redirect.png | WMF clip-art (slide016_img009.wmf, previously dropped as unrenderable) now rendered via LibreOffice; no build to strip |
| 17 | skip | | | bullets (duplicate of 15) |
| 18 | keep | new, "Control Plane vs. Data Plane, Drawn" | data-plane-deflection.png | final build state kept (announcement + deflection) |
| 19–21 | skip | | | bullets (Pilosov/Kapela MITM concept and setup) |
| 22 | keep | new, "Interception, Step by Step" (left) | bgp-mitm-before.png | stripped Text Box 22, Text Box 34, Lines 23–33 (exited overlays that LibreOffice stacks) |
| 23 | skip | | | planning step of the same build; narrated in the notes instead |
| 24 | keep | new, "Interception, Step by Step" (right) | bgp-mitm-after.png | final state; figure after Pilosov and Kapela, DEFCON 16 (2008), credited on the slide |
| 25 | skip | | | bullets (TTL anonymising) |
| 26–28 | skip | | | raw traceroute dumps; coverage-notes already dropped them |
| 29 | skip | | | bullets |
| 30 | skip | | | two clouds and a line (TCP-MD5); no content beyond the bullets |
| 31 | keep | "Bonus Defenses You'll See in the Wild" (GTSM column) | gtsm-ttl-hack.png | final build state; small enough to sit under the existing bullets |
| 32–33 | skip | | | bullets (S-BGP, soBGP proposals) |
| 34 | skip | | | S-BGP update-format table; attestation-format detail intentionally trimmed per coverage-notes |
| 35–39 | skip | | | bullets |
| 40 | keep | new, "The Address Hierarchy Is Already a Tree" | address-block-pki-hierarchy.png | embedded OLE object; figure after Kent, Lynn and Seo (S-BGP, IEEE JSAC 2000), credited in caption and notes |
| 41 | skip | | | bullets (duplicate of 36) |
| 42 | keep | new, "Path Shortening, Drawn" | path-shortening-attack.png | no animation; "AS Path = 2 4" label wraps in the LibreOffice render, noted on the slide |
| 43 | keep | new, "What the Signature Must Cover" (top) | path-shortening-sbgp-fix.png | final build state (signature callout kept) |
| 44 | skip | | | bullets |
| 45–53 | skip | | | hidden soBGP section (goals, EntityCert/AuthCert/PolicyCert, soBGP shortening and false-edge diagrams); the Quarto deck trims soBGP entirely |
| 54 | keep | new, "What the Signature Must Cover" (bottom) | false-edge-sbgp-fix.png | hidden slide, but it is the S-BGP false-edge picture that pairs with 43 |
| 55–58 | skip | | | hidden; soBGP bullets and the S-BGP vs soBGP comparison table |

## Sources

- `images/hijack-phishing-redirect.png` — source: ppt-archive/06-Routing.pptx slide 16, crop 420,250,1740,695 at 220 dpi (1320×445)
- `images/data-plane-deflection.png` — source: ppt-archive/06-Routing.pptx slide 18, crop 300,624,1780,1235 (1480×611)
- `images/bgp-mitm-before.png` — source: ppt-archive/06-Routing.pptx slide 22, shapes Text Box 22, Text Box 34, Line 23–33 stripped, crop 290,130,1900,1235 (1610×1105)
- `images/bgp-mitm-after.png` — source: ppt-archive/06-Routing.pptx slide 24, crop 290,150,1880,1200 (1590×1050)
- `images/gtsm-ttl-hack.png` — source: ppt-archive/06-Routing.pptx slide 31, crop 510,590,1740,1150 (1230×560)
- `images/address-block-pki-hierarchy.png` — source: ppt-archive/06-Routing.pptx slide 40 (OLE object), crop 460,250,1740,1065 (1280×815)
- `images/path-shortening-attack.png` — source: ppt-archive/06-Routing.pptx slide 42, crop 270,260,1920,850 (1650×590)
- `images/path-shortening-sbgp-fix.png` — source: ppt-archive/06-Routing.pptx slide 43, crop 270,340,1920,760 (1650×420)
- `images/false-edge-sbgp-fix.png` — source: ppt-archive/06-Routing.pptx slide 54 (hidden), crop 360,290,1940,950 (1580×660)
