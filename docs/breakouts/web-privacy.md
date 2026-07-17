# Web Privacy and Tracking

**Format.** Break into groups of 4–5. Each group picks **one** of the two breakouts below (or takes both if time allows). Spend ~5 minutes skimming the prep reads, then ~10 minutes debating. A designated reporter brings the group's position — and any dissents — back to the full class for a ~3-minute report-back.

Lecture 9 pivots the course from "security" to "privacy," and lands on two 2025 inflection points: Google *unretired* third-party cookies in April 2025 and shuttered most of the Privacy Sandbox in October 2025; and California's CPPA joined AGs from CA/CO/CT for a joint enforcement sweep on GPC (Global Privacy Control) signals, with revised CCPA regs effective Jan 1, 2026. The tracking model didn't collapse — it consolidated.

---

## Breakout A: Chrome as the Holdout — Regulate the Browser
<!-- breakout id="A" status="current" refreshed="2026-07-16" -->

**Motion.** *"With Google's April 2025 reversal on third-party cookies and October 2025 retirement of Privacy Sandbox APIs, Chrome is now the only major browser that neither blocks third-party tracking by default nor offers a serious alternative. State privacy regulators should treat Chrome's default settings as an unfair business practice under CCPA/CPRA."*

<!-- current-events:start topic="chrome-third-party-cookies-privacy-sandbox" -->
**Prep reads (5–10 min).**
- [Next steps for Privacy Sandbox and tracking protections in Chrome](https://privacysandbox.google.com/blog/privacy-sandbox-next-steps) — Google (Privacy Sandbox blog), October 2025. The primary-source announcement retiring Topics, PAAPI/Protected Audience, Attribution Reporting, IP Protection, Related Website Sets, and most other Sandbox APIs; only CHIPS, FedCM, and Private State Tokens survive.
- [Google Pulls The Plug On Topics, PAAPI And Other Major Privacy Sandbox APIs (As The CMA Says 'Cheerio')](https://www.adexchanger.com/privacy/google-pulls-the-plug-on-topics-paapi-and-other-major-privacy-sandbox-apis-as-the-cma-says-cheerio/) — AdExchanger, October 2025. Trade-press analysis noting the UK Competition and Markets Authority closed its Privacy Sandbox competition case the same week — the regulator that spent three years extracting commitments has nothing left to enforce.
- [Apple Drops iCloud's Advanced Data Protection in the U.K. Amid Encryption Backdoor Demands](https://thehackernews.com/2025/02/apple-drops-iclouds-advanced-data.html) — The Hacker News, February 2025. Cross-reference: even the vendor that most aggressively markets privacy (Apple) will pull a feature when a single regulator applies real pressure — a data point for "browser choice as a lever."
- [Update on Plans for Privacy Sandbox Technologies](https://privacysandbox.google.com/blog/update-on-plans-for-privacy-sandbox-technologies) — Google (Privacy Sandbox blog), April 2025. The earlier reversal that set up the October retirement: Chrome will *not* prompt users to opt out of third-party cookies; users must find Privacy & Security settings themselves.
<!-- current-events:end -->

**Discussion prompts.**
- Safari blocks third-party cookies by default (since 2020); Firefox does with Enhanced Tracking Protection; Chrome does not, and won't. Is a default a "choice" the CCPA can regulate? Compare with the CJEU joint-controller reasoning on the Meta Pixel.
- Manifest V3 constrains the request-blocking APIs uBlock Origin depends on. Google's stated rationale is performance; the effect is weakening one class of user-side tracker defense. Is that platform design, or a self-serving conflict of interest that should be regulated?
- The Privacy Sandbox was pitched as a privacy-preserving alternative to third-party cookies (Topics API, FLEDGE / Protected Audience). Google says adoption was too low; ad-tech says the alternatives were worse than what they replaced. Was the sandbox a good-faith attempt that failed, or was the outcome preordained by the ad-revenue model?
- If the browser is the last line of defense and the browser vendor is also the ad-tech giant, is *browser choice* a meaningful lever, or is that framing letting regulators off the hook?

**Bring back.** The single Chrome default your group would require by regulation, and one thing you'd leave to browser choice.

---

## Breakout B: Does Consent Actually Work?
<!-- breakout id="B" status="current" refreshed="2026-07-16" -->

**Motion.** *"Do Not Track failed. GPC is being enforced in September 2025 sweeps but sites are still ignoring it. Cookie banners are universally hated dark-patterned time sinks. Notice-and-consent is a broken paradigm. Regulators should move to *default* privacy protections (opt-in for tracking, purpose-bounded data use) and abandon consent as a legal fiction."*

<!-- current-events:start topic="gpc-enforcement-consent-dark-patterns" -->
**Prep reads (5–10 min).**
- [California Privacy Protection Agency Announces Joint Investigative Privacy Sweep](https://cppa.ca.gov/announcements/2025/20250909.html) — CPPA press release, September 2025. Primary source for the multi-state (CA/CO/CT, expanded via the eight-state Consortium of Privacy Regulators) enforcement sweep on businesses ignoring GPC opt-out signals.
- [California Won't Let It Go: Attorney General Bonta Announces $2.75 Million Settlement with Disney](https://oag.ca.gov/news/press-releases/california-wont-let-it-go-attorney-general-bonta-announces-275-million) — California OAG, February 2026. The largest CCPA settlement to date at the time (later dwarfed by GM's $12.75M in May 2026): Disney honored GPC only on the device that sent the signal, ignoring the account it was logged into.
- [CNIL Imposes Record Fines on Google (€325M) and Shein (€150M) for Cookie Consent Violations](https://captaincompliance.com/education/frances-cnil-slams-google-and-shein-with-record-fines-for-cookie-violations/) — Captain Compliance, September 2025. Cookie-banner dark patterns treated as consent violations — 83 CNIL sanctions worth ~€487M in 2025 alone.
- [Dark Patterns in Cookie Banners: CNIL issues formal notice to website publishers](https://www.cnil.fr/en/dark-patterns-cookie-banners-cnil-issues-formal-notice-website-publishers) — CNIL, December 2024. Regulator-authored taxonomy of the specific banner designs (button prominence asymmetry, buried reject links, ambiguous phrasing) that trigger enforcement.
<!-- current-events:end -->

**Discussion prompts.**
- The CPPA+AGs GPC sweep (Sept 2025) targeted businesses ignoring the header; revised CCPA regs (Jan 2026) require confirming GPC requests were processed. Is enforcement fixing the model, or dressing up a broken model with more paperwork?
- Real-time bidding (RTB) broadcasts a user's bid request to hundreds of ad-tech firms. Belgian DPA ruled the IAB TCF unlawful. Is "consent" even conceptually coherent when the data flows to hundreds of downstream parties in milliseconds?
- The lecture's fingerprinting arc (canvas, WebGL, audio context, font enumeration) shows that even a user who declines all cookies still gets tracked. Does that mean the *cookie* debate is a distraction, or that consent needs to extend to fingerprinting-class techniques?
- GDPR is opt-in; CCPA is opt-out (with GPC as the enforced signal). Which model actually protects users more in practice, and which is more likely to be adopted federally in the U.S.?

**Bring back.** The one data-collection practice your group would ban outright (no consent option available), and one you'd leave to user consent.

---

## Breakout format note

Today's schedule has the [IoT](../debates/iot.md) debate as the whole-class activity — these breakouts are a lighter warm-up on the privacy side. Keep them tight (10 minutes) so the debate gets its full time.

## Instructor notes

Breakout A is the political-economy version; Breakout B is the paradigm version. Both are enriched if students have installed [EFF Cover Your Tracks](https://coveryourtracks.eff.org/) or Lightbeam before class and can point to their own uniqueness score. If time is short, run B — the "consent is broken" argument gets even the most consent-minded students to soften. Save Breakout A for the CCPA/GDPR-heavy Lecture 11.

<!--
breakout-metadata:
  lecture: 9
  class: "Web Privacy"
  last_refreshed: 2026-07-16
-->
