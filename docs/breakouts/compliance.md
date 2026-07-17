# Automated Compliance Enforcement

**Format.** Break into groups of 4–5. Each group picks **one** of the two breakouts below (or takes both if time allows). Spend ~5 minutes skimming the prep reads, then ~10 minutes debating. A designated reporter brings the group's position — and any dissents — back to the full class for a ~3-minute report-back.

Lecture 12 studies compliance *as measured* rather than compliance *as claimed*. The 2026 enforcement pivot is unmissable: California AG hit Disney with $2.75M for ignoring opt-out signals (Feb 2026) and General Motors with a record $12.75M for selling driver data to LexisNexis/Verisk (May 2026) — the first CCPA action centered on data minimization and purpose limitation. Regulators care about practice, not paperwork.

---

## Breakout A: Automated Compliance Auditing — Whose Job?
<!-- breakout id="A" status="current" refreshed="2026-07-16" -->

**Motion.** *"Given that manual compliance audits do not scale and that automated 'mystery-shopper' studies (Study 2 in the deck: real opt-out requests submitted with synthetic identities) reliably surface violations that regulators miss, state AGs and the CPPA should fund or operate continuous automated compliance monitoring across the top 10,000 sites — and treat any site that fails as presumptively in violation."*

<!-- current-events:start topic="automated-compliance-monitoring-gpc" -->
**Prep reads (5–10 min).**
- [California Privacy Protection Agency Announces Joint Investigative Privacy Sweep](https://cppa.ca.gov/announcements/2025/20250909.html) — CPPA press release, September 2025. Primary source: the CPPA/CA/CO/CT sweep specifically targeted GPC noncompliance — a violation regulators can enumerate via automated crawling of browser dev-tools signals, which is exactly the "run the crawler" question.
- [When It Comes to Data Privacy, Consumers Must Be in the Driver's Seat: Attorney General Bonta Announces $12.75 Million General Motors Privacy Settlement](https://oag.ca.gov/news/press-releases/when-it-comes-data-privacy-consumers-must-be-driver%E2%80%99s-seat-attorney-general) — California OAG, May 2026. The first CCPA enforcement centered on *data minimization* and *purpose limitation* (not just an opt-out link's presence) — an inherently discovery-driven case that no crawler could have flagged.
- [Multistate Privacy Investigative Sweep Targeting Website Global Privacy Control (GPC) Noncompliance](https://www.alstonprivacy.com/multistate-privacy-investigative-sweep-targeting-website-global-privacy-control-gpc-noncompliance/) — Alston & Bird Privacy Blog, September 2025. Lawyer's guide to how the multi-state consortium (now eight states via April 2025 MOU) is scaling enforcement — including the January 1, 2026 CCPA rule requiring visible confirmation that UOOM signals were honored.
- [California AG Settles Disney's Alleged CCPA Opt-Out Violations for $2.75M](https://hintzelaw.com/blog/2026/2/17/california-ag-settles-disneys-alleged-ccpa-opt-out-violations-for-275m) — Hintze Law, February 2026. Case study of a violation that *could* have been detected by automation: Disney honored GPC only on the sending device even when users were logged into an account tying multiple devices together.
<!-- current-events:end -->

**Discussion prompts.**
- The GPC enforcement sweep (Sept 2025, joint CPPA/CA/CO/CT) targeted sites ignoring the header. Automated measurement could enumerate every such site continuously. Does *the regulator running the crawler* change the legal posture (e.g., 4th Amendment concerns, ToS violations, discovery vs. surveillance)?
- Study 2 raised ethical questions about submitting real opt-out requests with synthetic identities. Is that mystery-shopper technique acceptable when *researchers* do it, when *regulators* do it, or neither? Where does the Belmont/Menlo analysis land?
- The 2026 GM case broke new ground: first CCPA enforcement on *data minimization* and *purpose limitation* (not just opt-out link presence). Can any automated system detect these violations, or do they inherently require investigation and discovery?
- OneTrust and other consent-management platforms create the appearance of compliance while enforcing very little. Does automated auditing catch this, or does it just check the boxes that CMPs already check?

**Bring back.** The one compliance behavior your group thinks is best measured by automation, and one you think only human investigation can catch.

---

## Breakout B: Dark Patterns and the Limits of "Reasonable Consumer"
<!-- breakout id="B" status="current" refreshed="2026-07-16" -->

**Motion.** *"The CCPA's dark-pattern prohibition and the FTC's ROSCA / Section 5 enforcement have relied on a 'reasonable consumer' standard that assumes users have the patience and technical literacy to navigate opt-out flows. This is fiction. The right rule is *structural*: any opt-out that requires more than two clicks or is more than 25% longer than the opt-in flow is per se unlawful."*

<!-- current-events:start topic="dark-patterns-opt-out-ux-symmetry" -->
**Prep reads (5–10 min).**
- [Dark Patterns in Cookie Banners: CNIL issues formal notice to website publishers](https://www.cnil.fr/en/dark-patterns-cookie-banners-cnil-issues-formal-notice-website-publishers) — CNIL, December 2024. Regulator-authored enumeration of dark-pattern designs (button-color asymmetry, "reject" as link vs. "accept" as button, multi-click reject paths) — the closest thing to a structural test in current EU enforcement practice.
- [Reddit issued with £14.47m fine for children's privacy failures](https://ico.org.uk/about-the-ico/media-centre/news-and-blogs/2026/02/reddit-issued-with-1447m-fine-for-children-s-privacy-failures/) — UK ICO, February 2026. ICO explicitly rules that age self-declaration is not a lawful basis — a structural finding (the mechanism itself fails) rather than a case-by-case reasonable-consumer analysis.
- [Dark Patterns Lawsuits and the FTC's Click-to-Cancel Rule](https://www.coulsonpc.com/coulson-pc-blog/dark-patterns-ftc-click-to-cancel-rule) — Coulson P.C., 2025. Explains why the FTC's structural "click-to-cancel" rule was vacated by the Eighth Circuit on procedural grounds in July 2025 — and why the agency is pushing the same substantive rule via ROSCA + Section 5 (Amazon Prime $2.5B, Chegg $7.5M in September 2025).
- [California AG's $2.75M Disney Settlement: A Landmark GPC Opt-Out Enforcement Action](https://oag.ca.gov/news/press-releases/california-wont-let-it-go-attorney-general-bonta-announces-275-million) — California OAG, February 2026. Case study of the structural failure the motion targets: opt-out worked per-device even for logged-in accounts, "Do Not Sell" only stopped internal Disney ad-sharing not third-party partners, and the in-app opt-out was scoped to the moment of use.
<!-- current-events:end -->

**Discussion prompts.**
- The Sephora, DoorDash, Sling TV, and Healthline settlements all involved opt-out functionality failures. Disney's Feb 2026 $2.75M was specifically for *not honoring GPC*. Is the pattern "sites break opt-out" or "sites design opt-out to be broken by default"?
- CAPTCHAs, multi-step verification, and email confirmation loops on opt-out (but not opt-in) are the textbook dark patterns. Would a "two-click / 25% symmetry" rule work, or would designers just optimize around the letter?
- The lecture's third-party vendor irony: OneTrust and similar CMPs are supposed to enforce compliance and instead often become the mechanism of dark-patterning. Should CMPs face secondary liability?
- Universal Opt-Out Mechanisms (UOOMs) beyond GPC (Colorado requires honoring opt-out preference signals by law). If browser-level signals become universal, do dark patterns matter as much, or do they just move to the "reset your preferences" flow?

**Bring back.** Your group's proposed one-sentence structural test for what counts as a dark pattern under CCPA/CPRA, and one design that would probably squeak past your test.

---

## Breakout format note

The [Copyright](../debates/copyright.md) debate is the whole-class activity today, so keep these breakouts tight (10 minutes).

## Instructor notes

Breakout A is the more novel of the two — students rarely think of regulators as *building* audit infrastructure. Breakout B echoes Lecture 9's consent-is-broken thread but focuses on operationalization. If time is short, run A — it previews the AI-audit thread in Lectures 13 and 15. Both benefit from the instructor pulling up a real cookie banner on the projector (a European news site vs. its U.S. version is ideal) and having students clock the opt-out click count vs. the opt-in click count.

<!--
breakout-metadata:
  lecture: 12
  class: "Automated Compliance Enforcement"
  last_refreshed: 2026-07-16
-->
