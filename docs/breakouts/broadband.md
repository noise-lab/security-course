# Broadband Internet

**Format.** Break into groups of 4–5. Each group picks **one** of the two breakouts below (or takes both if time allows). Spend ~5 minutes skimming the prep reads, then ~10 minutes debating. A designated reporter brings the group's position — and any dissents — back to the full class for a ~3-minute report-back.

Lecture 18's teaching tension: the Affordable Connectivity Program ended June 1, 2024 (23M enrolled households, ~5M lost home internet); BEAD's $42.45B was restructured June 6, 2025 and only started releasing to states in late 2025; the FCC bumped the broadband benchmark to 100/20 Mbps in 2024 and still ~22M Americans lack it. Measurement drives billions in disbursement — and the measurement itself is contested.

---

## Breakout A: Should Broadband Be Regulated as a Utility?
<!-- breakout id="A" status="current" refreshed="2026-07-16" -->

**Motion.** *"Broadband should be permanently classified as a Title II common carrier service — with rate regulation, universal-service obligations, and non-discrimination rules — because the ACP collapse (23M households, ~5M without internet) and the BEAD delays proved that market competition alone will not close the divide or keep prices affordable."*

<!-- current-events:start topic="broadband-title-ii-net-neutrality-acp" -->
**Prep reads (5–10 min).**
- [ACP Has Ended For Now — Consumer Fact Sheet](https://www.fcc.gov/sites/default/files/ACP-Fact-Sheet-Post-ACP-Ending.pdf) — FCC, June 3, 2024. The official record: 23M enrolled households, wind-down through April/May 2024, and no federal replacement — Lifeline's $9.25/month is the surviving alternative.
- [The Broadband Equity, Access, and Deployment (BEAD) Program: Issues for the 119th Congress](https://www.congress.gov/crs-product/R48666) — Congressional Research Service, 2025. CRS on the June 6, 2025 NTIA "Restructuring Policy Notice" — mandatory technology neutrality, lowest-bid preference, and the pivot toward LEO satellite.
- [Federal Register: The Infrastructure Investment and Jobs Act: Prevention and Elimination of Digital Discrimination](https://www.federalregister.gov/documents/2024/01/22/2023-28835/the-infrastructure-investment-and-jobs-act-prevention-and-elimination-of-digital-discrimination) — Federal Register, 2024. Text of the FCC's digital-discrimination rules (effective March 22, 2024) reaching disparate-impact broadband redlining based on income, race, and national origin.
- [SpaceX Seeks Exemption from Certain BEAD Requirements](https://www.benton.org/blog/spacex-seeks-exemption-certain-bead-requirements) — Benton Institute, 2025. Starlink's demand for carve-outs from performance obligations and subscriber-milestone payment schedules — a test case for whether LEO can bear common-carrier-style requirements.
<!-- current-events:end -->

**Discussion prompts.**
- The FCC has reclassified broadband three times in a decade (Title II → Title I → Title II → back). Each reclassification survives one administration. Is that the fault of the underlying statute (Communications Act 1934, amended 1996 — pre-broadband), the courts, or the political cycle?
- ACP subsidized ~$30/mo for 23M households, then ended when Congress didn't refund it. BEAD is $42.45B on the supply side. Is affordability an ACP-style demand-side problem, a BEAD-style supply-side problem, or something no subsidy program will fix?
- LEO satellite (Starlink) as a rural option was the technology-neutrality fight in BEAD 2025. Does mandatory tech-neutrality (fiber vs. LEO vs. fixed-wireless) undermine the case for utility regulation, or reinforce it?
- The FCC's 2023 digital-discrimination rules attempt to reach "same-price-worse-service by neighborhood" (Hyde Park vs. South Shore). Are consumer-protection tools (algorithmic redlining actions) an adequate substitute for common-carrier obligations?

**Bring back.** Whether your group would formally classify broadband as a Title II utility, and one specific obligation you'd impose beyond the current rules.

---

## Breakout B: Who Measures the Internet?
<!-- breakout id="B" status="current" refreshed="2026-07-16" -->

**Motion.** *"The FCC's broadband deployment maps, M-Lab/NDT, Ookla, and Cloudflare Speed Test all disagree — sometimes dramatically — and every measurement methodology has a known bias. Billions in BEAD and USF funds hinge on this data. Congress should require any measurement used for federal disbursement to be produced by an independent, publicly-auditable methodology, not by ISP-reported data or single-vendor tools."*

<!-- current-events:start topic="broadband-measurement-methodology-bead" -->
**Prep reads (5–10 min).**
- [Broadband Data Collection Shows Access to High-Speed Internet Services is Expanding](https://www.fcc.gov/news-events/blog/2025/05/20/broadband-data-collection-shows-access-high-speed-internet-services) — FCC, May 2025. FCC's own numbers under the 100/20 benchmark: 95% of 110M locations "have access," with the methodology and per-location vs. per-block difference disclosed.
- [New Research: Starlink Unlikely to Meet BEAD Speed Needs At Scale](https://communitynetworks.org/content/new-research-starlink-unlikely-meet-bead-speed-needs-scale) — Institute for Local Self-Reliance, 2025. Measurement-based critique of the LEO-pivot: latency routinely exceeds BEAD's 100 ms threshold and speeds collapse during congestion — a direct measurement-vs-eligibility fight.
- [Home | FCC National Broadband Map](https://broadbandmap.fcc.gov/) — FCC, ongoing. The map itself: ISP-reported data with public challenge process; the artifact whose accuracy governs billions in BEAD disbursement.
- [Starlink's latest beef with BEAD: What you need to know](https://www.fierce-network.com/broadband/starlinks-latest-beef-bead-what-you-need-know) — Fierce Network, 2025. Reporting on SpaceX's Louisiana and Virginia complaints — measurement and eligibility disputes now driving real award decisions.
<!-- current-events:end -->

**Discussion prompts.**
- The lecture's Hyde Park vs. South Shore comparison (same 1 Gbps plan, dramatically different delivered performance) is invisible in headline maps. If measurement methodology is contested, whose methodology wins the political fight — and does that answer track "which methodology is technically best"?
- Mobile-only households (a large share of low-income households) are invisible in fixed-broadband maps. Does that mean the entire deployment-map framing is systematically wrong for equity purposes?
- M-Lab/NDT is single-threaded and under-reports at high speeds; Ookla is server-density-dependent; ISP self-reporting is unaudited. If no measurement is neutral, is the honest answer to require *multiple* measurements and report the disagreement?
- In-home passive measurement (as done in the Feamster group work) captures the actual bottleneck (WiFi vs. access link) but requires deploying devices in people's homes with attendant privacy trade-offs. What's the right consent model for continuous measurement infrastructure used in federal decision-making?

**Bring back.** The single measurement standard your group would require for federal broadband disbursement, and one specific privacy protection it must include.

---

## Breakout format note

The [Broadband](../activities/broadband.md) activity has students run Ookla and M-Lab tests on their own connections; both breakouts land harder after students have seen the disagreement firsthand.

## Instructor notes

Breakout A is the standard utility-regulation debate but with the ACP collapse as a fresh forcing function. Breakout B is technically deeper and often the more interesting one for CS students; it reveals that "we should just measure it" is not the neutral tie-breaker most people think it is. If time is short, run A — the ACP story is concrete and consequential. Both benefit from the instructor showing the Hyde Park vs. South Shore slide and asking students what the *right* level of policy analysis is (household? neighborhood? county? state?) before answering either breakout.

<!--
breakout-metadata:
  lecture: 18
  class: "Broadband Internet"
  last_refreshed: 2026-07-16
-->
