# 07-WebSecurity — instructor notes

## Current-events updates made (point 2)
- **Headline vignette — FortiWeb SQL injection (CVE-2025-25257).** Replaced undated
  "SQL injection is dangerous" framing with a current, verified case: an unauthenticated
  SQLi in Fortinet's *web application firewall* (CVSS 9.6), public PoC from watchTowr on
  2025-07-11, dozens of compromised appliances tracked by Shadowserver within days, added
  to CISA's KEV catalog with an Aug 8, 2025 patch deadline. The irony (a SQLi-blocking
  product with a SQLi bug) makes it the freshest hook. Sources: Fortinet PSIRT
  FG-IR-25-151; CISA Known Exploited Vulnerabilities catalog; watchTowr Labs; Shadowserver
  Foundation; Help Net Security (2025-07-14).
- **Stored-XSS still-current vignette (2026).** Added a second dated box on the
  reflected-vs-stored slide: stored XSS in Palo Alto PAN-OS web interface (CVE-2026-0256)
  and ongoing WordPress-plugin XSS (e.g., CVE-2026-1923, disclosed 2026-04-23), to show
  XSS remains a live, present-day class, not a historical curiosity. Sources: Palo Alto
  Networks security advisories; published CVE disclosures.
- **Modernized API examples.** Used `fetch`/framework language and React/Django
  auto-escaping rather than dated jQuery `$.get` AJAX framing from the original deck.
- **CSRF defenses modernized.** Foregrounded **SameSite cookies** (Lax now the browser
  default) alongside the classic token defense, matching the source deck's newer slide 44
  and current browser behavior.
- **Scoped TLS/SSL out.** Per agenda.md, "TLS details beyond what was covered in PKI
  lecture (slides in deck but not tested)." Dropped the ~25 TLS/SSL handshake, version-
  history, downgrade-attack, and Heartbleed slides (original slides 49–77) so this deck
  stays the *web-application security* lecture and doesn't duplicate the PKI deck. Channel
  vs. application security is flagged in the closing notes and pointed to the PKI lecture.

## Suggested missing coverage on broad themes (point 3)
- **CORS as the deliberate exception to SOP.** The deck explains SOP isolation but not
  how `Access-Control-Allow-Origin` lets sites *opt in* to cross-origin reads — worth a
  slide, since misconfigured CORS (`*` with credentials) is a common real bug.
- **Supply-chain / compromised CDN scripts.** The "scripts take the embedding origin"
  point implies that a hijacked third-party script owns your page. The 2024 Polyfill.io
  incident (100k+ sites served malware) is a clean, recent case; ties to the privacy/
  tracking lecture where third-party code runs in the first-party origin by design.
  Subresource Integrity (SRI) is the matching defense.
- **Authentication & session hardening.** HttpOnly/Secure cookie flags, session fixation,
  and why XSS that steals a session cookie is so damaging — a natural bridge from XSS to
  CSRF that the deck currently leaves implicit.
- **Server-side request forgery (SSRF)** and modern injection variants (NoSQL injection,
  template injection, command injection in serverless/LLM tool-calling contexts). SSRF in
  particular is now a top cloud-era web risk and is absent.
- **The Burp Suite / PortSwigger Web Security Academy labs** referenced in the original
  deck (slides 34–35) would make an excellent hands-on lab; the screenshots themselves
  are low-value as slides, but the resource is worth assigning.
- **HTTPS/TLS handoff note.** Since TLS was moved to PKI, add one explicit sentence in the
  PKI deck (or here) that HTTPS protects the *channel* but does nothing about SQLi/XSS/
  CSRF, which live in the *application* — students conflate the two.

## Curated images
- **Used:** `slide002_img001.png` (xkcd "Little Bobby Tables" — canonical SQLi teaching
  comic); `slide005_img003.png` (security-barrier diagram: two sites isolated in one
  browser); `slide006_img004.png` (no barrier within the same site — the SOP "same origin"
  contrast).
- **Dropped:** the ~130 step-by-step HTTP request/response flow PNGs (slides 9–43) — they
  are sliced screenshot fragments that read as clutter, not standalone diagrams; the flows
  are conveyed more clearly as inline code/bullets. Dropped the PortSwigger reflected/
  stored XSS text screenshots (`slide034`, `slide035`) — pure text, better as prose. All
  `.wmf` decorative arrows/cursors dropped. All TLS handshake diagrams dropped with the
  TLS scope cut.

## Source
- Rebuilt from `_source-extract.md` (77 source slides) + `agenda.md` Meeting 5 (Lecture
  Coverage: Web Security). Condensed to 23 slides; scoped to web-application security
  (SQLi, SOP, XSS, CSRF, CSP, SameSite) per what was actually taught and tested.
