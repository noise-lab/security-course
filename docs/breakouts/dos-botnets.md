# Denial of Service and Botnets

**Format.** Break into groups of 4–5. Each group picks **one** of the two breakouts below (or takes both if time allows). Spend ~5 minutes skimming the prep reads, then ~10 minutes debating. A designated reporter brings the group's position — and any dissents — back to the full class for a ~3-minute report-back.

The Mirai → Dyn → Aisuru arc (2016 ~1 Tbps → 2025 31.4 Tbps, same playbook, 30× the scale) is the lecture's core teaching case. Two structural problems fall out of it: insecure IoT is an *externality* the market keeps failing to fix, and a handful of scrubbing providers now front much of the web's traffic. Both breakouts pick one.

---

## Breakout A: Regulate the IoT Externality or Live With It
<!-- breakout id="A" status="current" refreshed="2026-07-16" -->

**Motion.** *"Consumer IoT insecurity is a classic externality — the buyer of the cheap camera isn't the party harmed. The U.S. Cyber Trust Mark and the EU Cyber Resilience Act aren't enough. Manufacturers should face strict liability for downstream DDoS damage caused by devices they shipped with default passwords or no update mechanism."*

<!-- current-events:start topic="iot-security-liability-cyber-trust-mark" -->
**Prep reads (5–10 min).**
- [White House Launches "U.S. Cyber Trust Mark"](https://bidenwhitehouse.archives.gov/briefing-room/statements-releases/2025/01/07/white-house-launches-u-s-cyber-trust-mark-providing-american-consumers-an-easy-label-to-see-if-connected-devices-are-cybersecure/) — The White House, January 2025. The launch announcement for the voluntary FCC-administered IoT security label — Executive Order 14144 then makes it a federal procurement requirement by January 2027.
- [Authorities disrupt world's largest IoT DDoS botnets responsible for record breaking attacks](https://www.justice.gov/usao-ak/pr/authorities-disrupt-worlds-largest-iot-ddos-botnets-responsible-record-breaking-attacks) — U.S. Department of Justice, District of Alaska, March 2026. The primary source for the coordinated Aisuru/Kimwolf/JackSkid/Mossad takedown against 3M+ compromised devices — the "takedown model" alternative to regulation.
- [How the EU Cyber Resilience Act Transforms Cybersecurity Into Product Liability Law](https://www.law.berkeley.edu/research/bclt/bclt-legal-analysis/how-the-eu-cyber-resilience-act-transforms-cybersecurity-into-product-liability-law/) — UC Berkeley Law BCLT, 2025. Analysis of the CRA's actual mandatory obligations for IoT manufacturers (in force Dec 2024; vuln reporting Sept 2026; full compliance Dec 2027) and how the revised Product Liability Directive picks up the civil-liability tail.
- [Cloudflare 2025 Q4 DDoS threat report: A record-setting 31.4 Tbps attack](https://blog.cloudflare.com/ddos-threat-report-2025-q4/) — Cloudflare, 2026. Measurement of the actual downstream harm — the Aisuru-Kimwolf botnet's 31.4 Tbps peak (Nov 2025), primarily off compromised off-brand Android TVs and routers.
<!-- current-events:end -->

**Discussion prompts.**
- The lecture's "death spiral" (compromised → recruited → attacks others → new compromises) treats the botnet as a self-sustaining ecosystem. Which intervention would actually break the cycle: device-side (secure-by-default), ISP-side (BCP 38 / source-address validation), takedown-side (Aisuru C2 seizure March 2026), or all three together?
- The March 2026 DoJ Aisuru takedown coordinated with cloud/CDN providers and international partners against 3M+ infected devices. If takedowns work, is *regulation* even the right answer, or is the criminal-market whack-a-mole fine as-is?
- BCP 38 (source-address validation at ingress) would kill spoofed-source amplification attacks. It has been recommended since 2000 and is still not universally deployed because there's no *incentive* for the deploying network — the benefit accrues to everyone else. Is this a market failure that requires regulation, or a coordination problem that requires MANRS-style voluntary norms?
- Compare U.S. Cyber Trust Mark (voluntary label), EU Cyber Resilience Act (mandatory security obligations), UK PSTI Act (default-password ban), California SB-327 (default-password ban). Which one does the most work, and which is most likely to be diluted by lobbying?

**Bring back.** Your group's proposed one-sentence liability rule for IoT manufacturers, and one class of device (e.g., pacemaker, doorbell, toothbrush) where the rule would break.

---

## Breakout B: Cloudflare, Akamai, and the Concentration of Defense
<!-- breakout id="B" status="current" refreshed="2026-07-16" -->

**Motion.** *"A handful of scrubbing providers now sit in front of most of the web's traffic, and 'autonomous mitigation' means their unilateral decisions determine who stays online. DDoS-protection providers should be regulated as common carriers — required to serve any legal site at cost-based rates, and forbidden from cutting off customers based on content."*

<!-- current-events:start topic="cloudflare-scrubbing-common-carrier-project-galileo" -->
**Prep reads (5–10 min).**
- [Cloudflare's 2025 Q3 DDoS threat report — including Aisuru, the apex of botnets](https://blog.cloudflare.com/ddos-threat-report-2025-q3/) — Cloudflare, October 2025. Cloudflare's own operational data on the scale of DDoS it now autonomously mitigates (average 5,376 attacks/hour) — the empirical basis for "essential infrastructure" arguments.
- [Cloudflare, Kiwi Farms, and the challenges of deplatforming](https://www.cjr.org/the_media_today/cloudflare-kiwi-farms-and-the-challenges-of-deplatforming.php) — Columbia Journalism Review, September 2022. The Kiwi Farms deplatforming that Matthew Prince himself called "dangerous" and "not comfortable" — the case that most cleanly tees up the common-carrier argument.
- [Cutting a Hydra's Head: Infrastructure-Level Content Moderation and the Case of Kiwi Farms](https://gnet-research.org/2025/12/23/cutting-a-hydras-head-infrastructure-level-content-moderation-and-the-case-of-kiwi-farms/) — Global Network on Extremism and Technology, December 2025. Recent academic analysis of what actually happened to Kiwi Farms post-deplatforming (site migration to smaller/foreign providers) — data for or against the "deplatforming works" claim.
- [When Cloudflare Goes Dark: What the November 2025 Outage Really Exposed About Your Risk Posture](https://www.cloudskope.com/post/when-cloudflare-goes-dark-what-the-november-2025-outage-really-exposed-about-your-risk-posture) — Cloudskope, November 2025. The concentration-risk counterweight: when Cloudflare's Bot Management feature file crashed the proxy on Nov 18, 2025, X, ChatGPT, PayPal and thousands of others went with it.
<!-- current-events:end -->

**Discussion prompts.**
- Cloudflare's 31.4 Tbps mitigation (Nov 2025) happened in seconds, autonomously. Without that capability, the target would have been offline. Does that operational reality argue *for* common-carrier obligations (the service is now essential infrastructure) or *against* them (the service exists only because of Cloudflare's willingness to build it)?
- Cloudflare has three faces: paid enterprise scrubbing, free consumer tier, and Project Galileo (free protection for civil society, gated by ACLU/EFF/Amnesty/ADL review). Which of those, if any, should be regulated? Does regulation change the incentives to run Galileo?
- Matthew Prince dropped Daily Stormer (2017), 8chan (2019), and Kiwi Farms (2022), each time saying he shouldn't have the power he used. Is a common-carrier mandate the right response, or does it actually make things worse (harder to remove genuine bad actors)?
- The lecture calls DDoS defense the "asymmetry" problem — attackers pay pennies, defenders pay millions. Under a common-carrier regime, who pays for that scrubbing capacity, and what happens when the numbers stop working for the provider?

**Bring back.** Whether your group would impose common-carrier obligations on DDoS scrubbing, and one specific site that would test your rule.

---

## Instructor notes

Breakout B is the more consequential of the two — it previews the "infrastructure as governance" thread that runs through Lectures 8, 16, and 17. Breakout A is more concrete and pairs well with the [Backdoors](../debates/backdoors.md) whole-class debate scheduled for this day. If time is short, run B: the Cloudflare deplatforming cases are memorable and the report-backs are consistently strong. If you have systems-heavy students, spend the last 5 minutes drawing the amplification-factor table on the board (DNS ~28×, NTP ~556×, memcached ~10,000×) as a springboard into either breakout.

<!--
breakout-metadata:
  lecture: 5
  class: "Denial of Service and Botnets"
  last_refreshed: 2026-07-16
-->
