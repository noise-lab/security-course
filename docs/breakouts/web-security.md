# Web Security

**Format.** Break into groups of 4–5. Each group picks **one** of the two breakouts below (or takes both if time allows). Spend ~5 minutes skimming the prep reads, then ~10 minutes debating. A designated reporter brings the group's position — and any dissents — back to the full class for a ~3-minute report-back.

Lecture 7's uncomfortable through-line: SQLi, XSS, and CSRF have been the OWASP Top 10 for 20 years, and they *still* land — most spectacularly when the vulnerable product is a WAF (FortiWeb, CVE-2025-25257). The Same-Origin Policy is 30 years old and every "modern" web platform choice (CORS, CSP, SameSite, SRI) is a patch on top of it. Both breakouts pick a live tension.

---

## Breakout A: CFAA Safe Harbor for Web Security Research
<!-- breakout id="A" status="current" refreshed="2026-07-16" -->

**Motion.** *"The CFAA should provide an explicit safe harbor for security researchers who discover and exploit vulnerabilities on production web systems — even when doing so violates the target's Terms of Service — provided they follow coordinated-disclosure norms."*

<!-- current-events:start topic="cfaa-safe-harbor-web-research" -->
**Prep reads (5–10 min).**
- [DOJ's New CFAA Policy is a Good Start But Does Not Go Far Enough to Protect Security Researchers](https://www.eff.org/deeplinks/2022/05/dojs-new-cfaa-policy-good-start-does-not-go-far-enough-protect-security) — EFF, May 2022. EFF critique of the post-Van Buren DOJ policy: it is only prosecutorial restraint, does not bind courts, and offers no protection against civil CFAA suits or state anti-hacking laws — still the leading argument for a statutory safe harbor as of 2026.
- [DOJ Acknowledges Limits to the CFAA, but Questions (and Possible Civil Liability) Remain for Security Researchers and Others](https://www.wsgr.com/en/insights/doj-acknowledges-limits-to-the-cfaa-but-questions-and-possible-civil-liability-remain-for-security-researchers-and-others.html) — Wilson Sonsini, 2022. Careful lawyer's read of the "good faith" carve-out and how "solely" and "mixed motive" language preserves prosecutorial discretion.
- [Pre-Auth SQL Injection to RCE — Fortinet FortiWeb Fabric Connector (CVE-2025-25257)](https://labs.watchtowr.com/pre-auth-sql-injection-to-rce-fortinet-fortiweb-fabric-connector-cve-2025-25257/) — watchTowr Labs, July 2025. The disclosure that fed the CFAA-safe-harbor debate all fall 2025: full technical write-up plus detection tooling, published three days after Fortinet's advisory, with in-the-wild exploitation observed within hours.
- [Disclose.io Safe Harbor Framework](https://disclose.io/) — Disclose.io / Bugcrowd, 2025. The industry-driven contractual safe-harbor project — model policies, VDP directory, and CFAA/DMCA safe-harbor language now shipped by default in Bugcrowd programs; the "let the market solve it" alternative to statutory reform.
<!-- current-events:end -->

**Discussion prompts.**
- Van Buren (2021) narrowed "exceeds authorized access"; hiQ v. LinkedIn (2022) held scraping public data generally falls outside CFAA. Do these rulings already give researchers enough cover, or is a statutory safe harbor still needed?
- watchTowr's public PoC for FortiWeb SQLi came *three days* after Fortinet's advisory. Compromises followed within days. Under a safe-harbor regime, would that timeline be a *feature* (fast defender awareness) or a *bug* (fast attacker uptake)?
- The lecture defines the trust boundary between browser and server: injection attacks live where the boundary is trusted incorrectly. From an ethics standpoint, does a researcher who exploits SQLi on a live production database cross a line the CFAA should still punish, even with disclosure?
- Bug bounty programs (HackerOne, Bugcrowd) are private safe harbors — the target opts in and defines the scope. Is a *statutory* safe harbor even necessary if the market is producing this outcome, or does bug bounty coverage exclude the vulnerabilities most worth finding?

**Bring back.** Your group's one-paragraph safe-harbor rule for web security researchers, and one type of research it would leave uncovered.

---

## Breakout B: Same-Origin Policy Is Dead — Long Live SOP?
<!-- breakout id="B" status="current" refreshed="2026-07-16" -->

**Motion.** *"Modern web security defenses (CORS, CSP, Trusted Types, SameSite cookies, SRI, Cross-Origin-Opener-Policy) have piled up because the Same-Origin Policy is not the right primitive for a web where every page loads 50 third-party scripts and every app is a JavaScript framework. It's time to design a new isolation model."*

<!-- current-events:start topic="sop-cors-csp-supply-chain" -->
**Prep reads (5–10 min).**
- [Polyfill.io Supply Chain Attack Hits Over 100k Websites](https://sansec.io/research/polyfill-supply-chain-attack) — Sansec, June 2024. The primary-source advisory: a legitimate CDN script (cdn.polyfill.io) taken over via ownership change was serving evasive redirect malware to mobile users at over 100k sites, including JSTOR and the World Economic Forum — SRI would have caught it.
- [Polyfill Supply Chain Attack Impacting 100K Sites Linked to North Korea](https://www.securityweek.com/polyfill-supply-chain-attack-impacting-100k-sites-linked-to-north-korea/) — SecurityWeek, 2025. The updated attribution: infostealer forensics tied the operation to a DPRK-linked crew laundering revenue through Suncity-affiliated gambling sites — supply-chain compromise as state-sponsored monetization.
- [Mitigate cross-site scripting (XSS) with a strict Content Security Policy (CSP)](https://web.dev/articles/strict-csp) — Google web.dev, 2025. The canonical "strict-dynamic + nonces + Trusted Types" recipe that Google now recommends as the actual SOP-supplement worth deploying, plus the honest admission that CSP is defense-in-depth and cannot replace input sanitization.
- [Exploits for unauthenticated FortiWeb RCE are public, so patch quickly! (CVE-2025-25257)](https://www.helpnetsecurity.com/2025/07/14/exploits-for-unauthenticated-fortiweb-rce-are-public-so-patch-quickly-cve-2025-25257/) — Help Net Security, July 2025. SQL injection in a security appliance's own admin UI, exploited in the wild within hours of the PoC — evidence that even the vendors selling "web application firewalls" don't apply the framework hygiene the OWASP Top 10 has been asking for since 2003.
<!-- current-events:end -->

**Discussion prompts.**
- The lecture's key SOP subtlety: scripts execute with the *embedding* origin's privileges, not the origin they came from. Polyfill.io (2024) served malware to 100k+ sites through a legitimate third-party script; SRI would have caught it if anyone had used it. Is the fix technical (mandatory SRI), procedural (supply-chain review), or organizational (stop loading third-party JS)?
- React and Django auto-escape user input; SameSite=Lax is now the browser default; framework-standard CSRF tokens ship out of the box. Why do XSS/CSRF still make the OWASP Top 10 — is it legacy code, feature creep, or something else?
- Stored XSS in PAN-OS (CVE-2026-0256) is XSS in a *security appliance's* web interface. SQLi in FortiWeb is SQLi in a *SQLi-blocking product*. Is the problem that web-app frameworks are too permissive, that appliance vendors don't use frameworks, or that WAFs are theater?
- If you were designing a from-scratch web isolation model in 2026, what would you keep (origins? cookies? DOM?) and what would you throw out?

**Bring back.** The one web-security defense your group thinks is doing the most work today, and the one that is mostly theater.

---

## Instructor notes

Breakout A pairs directly with the [CFAA](../debates/cfaa.md) whole-class debate scheduled for this day — running Breakout A first lets students test framings before the formal debate. Breakout B is where the CS-heavy classes have the most fun; it produces the strongest report-backs if students have implemented anything in a modern web framework. If time is short, run A: it's more likely to change students' minds. Both benefit from a live open of the browser's DevTools "Network" tab on a major news site during the setup — the 50-tracker page load is visceral.

<!--
breakout-metadata:
  lecture: 7
  class: "Web Security"
  last_refreshed: 2026-07-16
-->
