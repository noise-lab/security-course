# Figure recovery: 07-WebSecurity

Source: `docs/slides/ppt-archive/07-WebSecurity.pptx`, 77 slides in the XML
(slides 13 and 56 are hidden, so the headless render has 75 pages), rendered
2026-10-16 with `src/pptx-figures.py`. Slide numbers below are the XML/pptx
numbers; the rendered page number is one lower from slide 14 on and two lower
from slide 57 on.

The Quarto deck is scoped to web-application security (SOP, injection, XSS,
CSRF); TLS/SSL was deliberately moved to the PKI lecture (see
`coverage-notes.md`), so the TLS figures are listed as skip even though
several are good drawings.

| pptx slide | class | target Quarto slide | figure name | notes |
|---|---|---|---|---|
| 1 | skip | | | title |
| 2 | media | "Little Bobby Tables" | `slide002_img001.png` | xkcd 327, already embedded |
| 3 | media | | | WordPress security-release news screenshot (Jan 2022), dated |
| 4 | skip | | | bullets (Browser Security goal), already the text of "Browser Security: The Goal" |
| 5 | media | "Browser Security: The Goal" | `slide005_img003.png` | security-barrier picture, already embedded |
| 6 | media | "What Is an \"Origin\"?" | `slide006_img004.png` | no-barrier picture, already embedded |
| 7 | skip | | | origin = protocol + host + port, covered by the table in "What Is an Origin" |
| 8 | skip | | | SOP bullets |
| 9 | keep | new, "A Page Load, One Request at a Time" (after the SOP divider) | `http-page-load.png` | base request/response diagram all later figures reuse; builds are additive, final state captured |
| 10 | skip | | | same-origin `$.get` to gmail.com/chat.json from a gmail.com page; superseded by 12 and 19 |
| 11 | skip | | | AJAX (jQuery) version of 10 |
| 12 | keep | new, "SOP in One Picture: A Cross-Origin Read, Blocked" (after "The Rule, and the Key Question") | `sop-cross-origin-read-blocked.png` | evil facebook.com script reading gmail.com/msgs.json, red X on the read; title band whited out before crop |
| 13 | skip | | | hidden slide ("SOP: Objects"), not in the render |
| 14 | skip | | | cross-origin `<img>` load allowed; the load-allowed half is already in 9 and 16 |
| 15 | skip | | | `<script src=gmail.com/chat.js>` before the script runs; 16 is the complete state |
| 16 | keep | new, "Subtlety 1, Drawn: A Script Loaded From Another Origin" (after "Two Subtleties") | `sop-script-embedding-origin.png` | script fetched from gmail.com, runs as facebook.com |
| 17 | skip | | | the red X on chat.json after 16; narrated in the new slide's bullets instead of a second image |
| 18 | skip | | | iframe before the frame's script runs; 19 is the complete state |
| 19 | keep | new, "Subtlety 2, Drawn: An iframe Keeps Its Own Origin" (after the script slide) | `sop-iframe-own-origin.png` | iframe from gmail.com reads gmail.com/chat.json successfully |
| 20 | skip | | | shell-injection request/response with directory listing; the code is already on "Confusing Data and Code" |
| 21 | skip | | | same with `$(rm -rf /)` and a POOF clip-art; no intuition beyond the code block |
| 22 | skip | | | Code Injection bullets |
| 23 | skip | | | SQL bullets |
| 24, 25 | skip | | | SQL injection text, already on "SQL Injection" |
| 26 | media | | `slide002_img001.png` | xkcd repeat |
| 27 | skip | | | SQL injection defense text, already on the defense slide |
| 28 | skip | | | `?user=Bob` request/response; the three-stage escalation is already text on "XSS: HTML Injection" |
| 29 | skip | | | `?user=<u>Bob</u>` version |
| 30 | keep | new, "Reflected XSS, Drawn: The Lure and the Echo" (after "XSS: HTML Injection Becomes Script Injection") | `xss-reflected-lure.png` | lure email, request with script in `?user=`, echoed response, alert |
| 31 | skip | | | "Review: Same-Origin Policy", duplicate of 12 |
| 32 | keep | new, "The Attack, Step 1: Injecting the Script Into gmail.com" (after "Why XSS Is So Dangerous") | `xss-attack-injection.png` | evil facebook.com iframe carrying the script into gmail.com's `?user=`; title band whited out |
| 33 | keep | new, "The Attack, Step 2: Reading Your Mail From Inside the Origin" | `xss-attack-exfiltration.png` | final animation state (first half faded, `new_msgs: 3` callout); the fade is the original's own emphasis, kept |
| 34, 35 | skip | | | PortSwigger reflected/stored XSS text screenshots |
| 36 | skip | | | XSS Defenses bullets |
| 37 | skip | | | duplicate of 9 |
| 38 | skip | | | login POST and `Set-Cookie: login=fde874`; the cookie is already shown in the CSRF slide's code block and in 40 |
| 39 | skip | | | `GET /account` with cookie, `$378.42`; same |
| 40 | keep | new, "CSRF, Drawn: One Click, One Forged Transfer" (after "CSRF: The Browser Sends Your Cookie Automatically") | `csrf-forged-transfer.png` | lure link, forged transfer request with the cookie attached, `-$100.00` |
| 41 | media | | | Google search-history screenshot for the pollution paper; dated UI, the Quarto slide cites the paper instead |
| 42 | skip | | | CSRF defenses bullets |
| 43 | keep | new, "The Token Defense, Drawn" (after "CSRF Defenses") | `csrf-token-defense.png` | hidden token field, `Set-Cookie: token=8d64`, legitimate transfer with cookie and token |
| 44 | skip | | | SameSite cookie text, already on "CSRF Defenses" |
| 45 | skip | | | origin comparison table, already on "What Is an Origin" |
| 46, 47, 48 | skip | | | text: externally hosted scripts, SOP complications, hostnames as trust boundaries |
| 49–55 | skip | | | TLS text slides (scoped out of this deck) |
| 52 | skip | | | application-level protection stack diagram; TLS scope, and it is a redrawn textbook figure |
| 56 | skip | | | hidden |
| 57–64 | skip | | | TLS handshake C/S diagrams (ClientHello, ServerHello, ServerKeyExchange, ClientKeyExchange, full handshake); good drawings but TLS lives in the PKI deck |
| 65 | skip | | | version downgrade attack diagram; TLS scope |
| 66, 67 | skip | | | SSLv2 weaknesses, chosen-protocol attack bullets |
| 68 | skip | | | version check in SSLv3 diagram; TLS scope |
| 69 | skip | | | record protection layering diagram; TLS scope |
| 70 | skip | | | handshake extra features bullets |
| 71 | skip | | | session resumption diagram, a textbook figure ("Protocol 19-3") |
| 72, 73 | skip | | | SSL/TLS security flaws bullets |
| 74 | media | | | Heartbleed logo |
| 75–77 | skip | | | Heartbeat extension, Heartbleed bug, RFC 6520 struct; TLS scope |

Captured images (all 220 dpi crops of the headless LibreOffice render; builds on
every kept slide were additive entrances, so no shapes were stripped):

- source: `ppt-archive/07-WebSecurity.pptx` slide 9, final state → `images/http-page-load.png` (1588×947)
- source: `ppt-archive/07-WebSecurity.pptx` slide 12, final state, title band masked → `images/sop-cross-origin-read-blocked.png` (1629×970)
- source: `ppt-archive/07-WebSecurity.pptx` slide 16, final state → `images/sop-script-embedding-origin.png` (1644×949)
- source: `ppt-archive/07-WebSecurity.pptx` slide 19, final state → `images/sop-iframe-own-origin.png` (1643×949)
- source: `ppt-archive/07-WebSecurity.pptx` slide 30, final state → `images/xss-reflected-lure.png` (1595×806)
- source: `ppt-archive/07-WebSecurity.pptx` slide 32, final state, title band masked → `images/xss-attack-injection.png` (1643×970)
- source: `ppt-archive/07-WebSecurity.pptx` slide 33, final state, title band masked → `images/xss-attack-exfiltration.png` (1643×970)
- source: `ppt-archive/07-WebSecurity.pptx` slide 40, final state → `images/csrf-forged-transfer.png` (1558×681)
- source: `ppt-archive/07-WebSecurity.pptx` slide 43, final state → `images/csrf-token-defense.png` (1619×743)
