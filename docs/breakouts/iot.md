# Device Privacy (IoT)

**Format.** Break into groups of 4–5. Each group picks **one** of the two breakouts below (or takes both if time allows). Spend ~5 minutes skimming the prep reads, then ~10 minutes debating. A designated reporter brings the group's position — and any dissents — back to the full class for a ~3-minute report-back.

Lecture 10's freshest hook is the Texas AG's December 2025 ACR lawsuit against Samsung, Sony, LG, Hisense, and TCL — the first-ever TRO against a TV maker, and Samsung's Feb 2026 settlement requiring express consent. IoT Inspector's measurement work (SIGCOMM 2018, CCS 2019, 50k devices) documented what the ACR case is now litigating: opt-outs are ineffective, and the home network is not isolated.

---

## Breakout A: IoT Vendor Liability for Downstream Harm
<!-- breakout id="A" status="current" refreshed="2026-07-16" -->

**Motion.** *"IoT vendors should be held strictly liable for damages resulting from unpatched security vulnerabilities in their devices, and separately for privacy harms from undisclosed data collection (ACR, always-listening microphones, cross-device tracking). Consumer buyers cannot audit these devices, and the market has demonstrated it will not fix this on its own."*

<!-- current-events:start topic="iot-liability-acr-cyber-trust-mark" -->
**Prep reads (5–10 min).**
- [Attorney General Paxton Sues Five Major TV Companies for Spying on Texans](https://www.texasattorneygeneral.gov/news/releases/attorney-general-paxton-sues-five-major-tv-companies-including-some-ties-ccp-spying-texans) — Texas OAG, December 2025. Primary source for the ACR lawsuits against Samsung, Sony, LG, Hisense, and TCL: screenshot capture every 500ms, TROs granted against Hisense and Samsung within days, DTPA framing.
- [U.S. Cyber Trust Mark](https://www.fcc.gov/CyberTrustMark) — FCC program page, launched January 2025. The voluntary consumer IoT labeling scheme (QR-code registry, NIST baseline requirements) that Executive Order 14144 turned into a de facto 2027 federal procurement mandate; ioXt Alliance replaced UL Solutions as Lead Administrator in April 2026.
- [Cyber Resilience Act — Shaping Europe's digital future](https://digital-strategy.ec.europa.eu/en/policies/cyber-resilience-act) — European Commission, 2024–2026. Primary source for the EU's mandatory (not voluntary) IoT security regime: CE marking required, SBOM obligation, vulnerability disclosure duty, first mandatory incident reporting September 11, 2026, full compliance December 11, 2027.
- [Amazon to pay over $30 million to settle claims Ring, Alexa invaded user privacy](https://www.npr.org/2023/06/01/1179381126/amazon-alexa-ring-settlement) — NPR, June 2023. Baseline priors: $25M Alexa/COPPA + $5.8M Ring settlement — indefinite retention of children's voice data, Ring employees browsing bathroom/bedroom feeds, no MFA until 2019. Still the reference point for "market has demonstrated it won't fix this on its own."
<!-- current-events:end -->

**Discussion prompts.**
- The Texas AG's ACR case (Dec 2025) and Samsung's settlement (Feb 2026 — express consent required) are the first meaningful enforcement against smart-TV ambient data collection. Was the missing ingredient a *new law* (Kentucky's ACR-specific statute), *creative use of an old law*, or just a willing AG?
- The 2019 IoT Inspector CCS study found trackers on Roku/Fire TV that a user cannot see and cannot opt out of. Consumer buyers cannot audit these devices; even security researchers had to arp-spoof to see the traffic. Does that information asymmetry justify strict liability?
- Right-to-repair and cloud-abandonment: a device that loses cloud support becomes either a brick or a security liability. Should manufacturers be legally required to open-source firmware after end-of-life, or is that unworkable?
- The lecture's "no isolation LAN" principle: SOP is a browser property, not a network property, so a webpage can talk to your smart bulb via DNS rebinding. Is the fix (network segmentation, MUD) something consumers can realistically do, or does it require ISP/router-vendor intervention?

**Bring back.** Your group's proposed rule for IoT vendor liability, and the device category most likely to break your rule.

---

## Breakout B: Automatic Content Recognition and the Limits of Consent
<!-- breakout id="B" status="current" refreshed="2026-07-16" -->

**Motion.** *"Even with Samsung's express-consent settlement and Kentucky's ACR-specific law, consent is the wrong tool for ambient collection technologies (ACR, always-listening voice, smart-home occupancy sensing). These should be opt-in-with-substantive-limits — no data retained beyond the immediate query, no cross-device joining, no third-party sale — regardless of what a user checks."*

<!-- current-events:start topic="acr-voice-assistant-ambient-collection" -->
**Prep reads (5–10 min).**
- [Attorney General Paxton Secures Major Agreement with Samsung to Ensure that Texans are Protected from Smart TVs Collecting Their Data Without Their Knowledge](https://www.texasattorneygeneral.gov/news/releases/attorney-general-paxton-secures-major-agreement-samsung-ensure-texans-are-protected-smart-tvs) — Texas OAG, February 2026. Primary source for the first ACR consent decree: Samsung must obtain express consent, provide "clear and conspicuous" setup-time disclosures, and stop opt-out-dark-patterning (the complaint documented 15+ clicks to opt out vs. one-click enrollment).
- [Automated content recognition technology takes privacy enforcement spotlight](https://iapp.org/news/a/automated-content-recognition-technology-takes-privacy-enforcement-spotlight) — IAPP, 2026. Analyst-grade overview of the ACR enforcement wave — Kentucky's ACR-specific statute, the Texas suits, and why express-consent regimes may still fail to reach the aggregation harm.
- [Court Approves Order Requiring Disney to Pay $10 Million to Settle FTC Allegations the Firm Enabled the Unlawful Collection of Children's Personal Data](https://www.ftc.gov/news-events/news/press-releases/2025/12/court-approves-order-requiring-disney-pay-10-million-settle-ftc-allegations-firm-enabled-unlawful) — FTC, December 2025. COPPA enforcement anchor: Disney's channel-level "Made-for-Kids" defaults let YouTube collect targeted-ad data on child viewers — an ambient-collection failure at the platform layer, not the device.
- [FTC Finalizes Order Prohibiting Gravy Analytics, Venntel from Selling Sensitive Location Data](https://www.ftc.gov/news-events/news/press-releases/2025/01/ftc-finalizes-order-prohibiting-gravy-analytics-venntel-selling-sensitive-location-data) — FTC, January 2025. The Section 5 order that bans (not "consent-gates") sale of sensitive location data — a template for the "opt-in-with-substantive-limits" model the motion argues for.
<!-- current-events:end -->

**Discussion prompts.**
- Voice assistants have documented false activations, cloud retention of recordings, and law-enforcement request pathways. Should consent for "voice assistant on" cover *all* of these downstream flows, or should each require separate opt-in?
- Encrypted-traffic inference (packet sizes and timing reveal device type and user activity even when traffic is encrypted) means the ISP or a WiFi eavesdropper can profile the home without decrypting anything. What consent regime can even *reach* this vector?
- YouTube's $170M COPPA settlement (Sept 2019) targeted children's data. ACR/voice/smart-home data affects everyone in the home, including children who never signed up. Does that make ACR a COPPA problem, a general-privacy problem, or something new?
- The lecture asks students to think about what "reasonable expectations of privacy" mean for a device you bought and installed in your home. Does the fact that you clicked "agree" during setup change the analysis?

**Bring back.** Whether your group would treat ambient collection as opt-in-with-limits, and one enforcement mechanism you'd require.

---

## Breakout format note

The [Web Tracking](../activities/web.md) activity is scheduled for this day; both breakouts pair naturally with what students see there.

## Instructor notes

Breakout A is the whole-course-in-one — it pulls in security (Mirai), privacy (tracking), law (liability), and consumer protection (labels/mandates). Breakout B is more focused and lands well after students have watched Roku/Fire TV traffic in the activity. Both breakouts have direct pipes to the [IoT](../debates/iot.md) whole-class debate (which appears in Lecture 9's slot); use them to workshop framings for the debate. If time is short, run A: it produces the most memorable report-backs.

<!--
breakout-metadata:
  lecture: 10
  class: "Device Privacy"
  last_refreshed: 2026-07-16
-->
