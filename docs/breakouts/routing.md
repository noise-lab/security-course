# Routing Security

**Format.** Break into groups of 4–5. Each group picks **one** of the two breakouts below (or takes both if time allows). Spend ~5 minutes skimming the prep reads, then ~10 minutes debating. A designated reporter brings the group's position — and any dissents — back to the full class for a ~3-minute report-back.

Lecture 6 argues that BGP has three decades of well-documented failure modes (1997 MAI/Virginia, 2008 Pakistan/YouTube, 2010 China Telecom), a deployed cryptographic fix (RPKI/ROV), and *still* covers only ~54% of routes. The July 2025 APNIC/LACNIC hijack — achieved by social-engineering an upstream provider into provisioning BGP without identity verification — reminds us the human process, not the crypto, is the weak link.

---

## Breakout A: FCC BGP Mandates — Right Instrument, Wrong Instrument, or Not Enough?
<!-- breakout id="A" status="current" refreshed="2026-07-16" -->

**Motion.** *"The FCC's June 2024 NPRM requiring retail broadband providers to file BGP security risk-management plans (with the nine largest filing confidential plans) is the right template. Congress should extend it: any AS operating in the U.S. should be legally required to originate ROAs for ≥90% of its routes and to perform ROV on inbound announcements."*

<!-- current-events:start topic="fcc-bgp-mandate-rpki-rov" -->
**Prep reads (5–10 min).**
- [Reporting on Border Gateway Protocol Risk Mitigation Progress; Secure Internet Routing (NPRM)](https://www.federalregister.gov/documents/2024/06/17/2024-13048/reporting-on-border-gateway-protocol-risk-mitigation-progress-secure-internet-routing) — Federal Register / FCC 24-62, June 2024. The primary source: the 90% ROA threshold, the nine named large providers, the confidential-plan structure, and the FCC's Title II authority claim.
- [FCC Proposes Reporting and Other Obligations to Secure Routing of Internet Traffic](https://www.dwt.com/blogs/broadband-advisor/2024/06/fcc-proposes-secure-routing-plans-for-providers) — Davis Wright Tremaine, June 2024. Practitioner-side breakdown of what compliance actually looks like for large vs. small providers, the ROV timelines proposed (Tier 1: 1 year; Tier 2: 2 years), and the legal-authority issues.
- [NIST RPKI Deployment Monitor](https://rpki-monitor.antd.nist.gov/) — NIST, ongoing. Live measurement of global ROA coverage (~60% of prefixes by late 2025) and ROV enforcement (~25-30% of networks) — the empirical basis for judging whether a mandate is needed to close the gap.
- [RPKI vs social engineering: A case study in route hijacking](https://blog.apnic.net/2026/03/31/rpki-vs-social-engineering-a-case-study-in-route-hijacking/) — APNIC / LACNIC, March 2026. The joint APNIC/LACNIC write-up of the July 2025 hijack: attacker used forged docs and a lookalike domain to trick an upstream into provisioning BGP for a hijacked ASN — RPKI wasn't defeated, the human process was.
<!-- current-events:end -->

**Discussion prompts.**
- RPKI ROA coverage sits at ~54% of routes / ~74% of destined traffic (NIST RPKI Monitor 2025). MANRS is voluntary and its membership includes most large networks. Given both, why is coverage stuck below 100% — and does a mandate solve that, or push the last laggards into paper compliance?
- The FCC NPRM excuses filers whose ROAs cover ≥90% of originated routes. Is 90% the right threshold, or does it incentivize gaming (announce only your "important" routes with ROAs; leave dark space unprotected)?
- China Telecom (2010) rerouted 15% of global traffic through China for 18 minutes; Pakistan (2008) took YouTube offline globally by leaking a censorship-intended more-specific. Would RPKI + ROV have stopped either? Would BGPsec (path validation) have stopped both?
- The July 2025 APNIC/LACNIC hijack succeeded by *tricking a human at an upstream provider* — no crypto was defeated. If crypto only fixes half of BGP's problem, is regulation aimed at the crypto half solving the right thing?

**Bring back.** Your group's answer to whether the FCC template should be extended, and one specific enforcement mechanism you'd add.

---

## Breakout B: When Fragility Is the Attacker (Facebook, October 2021)
<!-- breakout id="B" status="current" refreshed="2026-07-16" -->

**Motion.** *"The 2021 Facebook BGP self-withdrawal outage (their own routers withdrew their own prefixes; DNS became unreachable; badge readers stopped working) showed that hyperscale routing fragility is now a bigger risk than routing attacks. RPKI and BGPsec address the wrong threat model — we should be investing in operational safeguards (change-control review, out-of-band access, staged rollouts) instead."*

<!-- current-events:start topic="bgp-outages-operational-fragility" -->
**Prep reads (5–10 min).**
- [More details about the October 4 outage](https://engineering.fb.com/2021/10/05/networking-traffic/outage-details/) — Meta Engineering, October 2021. Facebook's own post-mortem explaining how a routine backbone-capacity audit triggered the DNS "safety mechanism" that withdrew their prefixes globally and locked engineers out of their own recovery systems.
- [When Cloudflare Goes Dark: What the November 2025 Outage Really Exposed About Your Risk Posture](https://www.cloudskope.com/post/when-cloudflare-goes-dark-what-the-november-2025-outage-really-exposed-about-your-risk-posture) — Cloudskope, November 2025. The Nov 18, 2025 Cloudflare outage — a ClickHouse permissions change cascaded into a Bot Management file that panicked the proxy — a 2025 replay of the "fragility, not attacker" pattern.
- [The Pulse: Cloudflare's latest outage proves dangers of global configuration changes (again)](https://blog.pragmaticengineer.com/the-pulse-cloudflares-latest-outage/) — The Pragmatic Engineer, November 2025. Post-mortem-of-post-mortems framing: same class of failure Facebook had in 2021, at a different provider, with the same "our safety mechanism was the failure amplifier" root cause.
- [RPKI vs social engineering: A case study in route hijacking](https://blog.apnic.net/2026/03/31/rpki-vs-social-engineering-a-case-study-in-route-hijacking/) — APNIC / LACNIC, March 2026. The July 2025 hijack shows the counterpoint: even in an actual routing *attack*, the attackers went around the crypto (social-engineered an upstream) rather than through it — so what would BGPsec/ASPA actually buy you?
<!-- current-events:end -->

**Discussion prompts.**
- The 1997 MAI/Virginia leak was accidental (misconfiguration). Facebook 2021 was accidental (self-withdrawal). Cloudflare has had its own operational outages. If most disruption is operational, does the "attacker-centric" framing of BGP security misallocate attention?
- Contrast with the AS-path attack surface. RPKI+ROV validates *origin*; BGPsec validates *path*. BGPsec has near-zero deployment. Is that because path attacks are rare, or because deployment cost is prohibitive?
- Anycast (why DNS root survives DDoS) is BGP working for you. But when BGP misbehaves, anycast can *spread* the outage globally in seconds. Is anycast a defense mechanism or an attack multiplier?
- Data-plane verification (does traffic actually follow the announced path?) is the missing piece — RPKI is a control-plane fix. If someone injected a route that validated cleanly but blackholed traffic, would anyone notice, and how fast?

**Bring back.** The single BGP incident (attack or fragility) your group thinks would be most catastrophic in 2026, and the intervention that would have prevented it.

---

## Instructor notes

The [BGP activity](../activities/bgp.md) that day gives students direct exposure to route announcements and RPKI validity checks — Breakout B is much more concrete after they've seen a live looking glass. Breakout A is heavier on policy; run it if the class is thin on networking background. If time is short, run A — the FCC mandate is the freshest concrete lever. Both breakouts benefit from the instructor drawing the AS-graph from the 2010 China Telecom slide as a warm-up: it grounds "longest-prefix match" and "shortest AS path wins" in one figure.

<!--
breakout-metadata:
  lecture: 6
  class: "Routing Security"
  last_refreshed: 2026-07-16
-->
