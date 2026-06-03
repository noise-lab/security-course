# 05-DoS — instructor notes

## Current-events updates made (point 2)
- Added a `.vignette` hook built on **Cloudflare's Q4 2025 DDoS threat report
  (published Feb 2026)**: a record **31.4 Tbps** attack, lasting ~35 s, mitigated
  autonomously. Verified via Cloudflare's blog, NETSCOUT ASERT, and trade press.
- Attributed it to the **Aisuru / Kimwolf "TurboMirai" botnet** — a Mirai
  descendant of **300,000+ compromised IoT devices** (including Android TV /
  streaming boxes). This deliberately ties the freshest example back to the
  historical **Mirai (2016)** case study, showing the playbook is unchanged and
  only the scale (~1 Tbps Dyn → 31.4 Tbps) has grown ~30×.
- Noted the **March 19, 2026** international law-enforcement takedown of the
  Aisuru/Kimwolf C2 infrastructure, illustrating that mitigation is now also a
  legal/operational effort, not just technical.
- Reframed the defenses section around **autonomous scrubbing** (the 31.4 Tbps
  attack was stopped in seconds) and added the centralization/policy implication
  that a few scrubbing providers now front much of the web's traffic.
- Kept SYN-flood / SYN-cookie / Great Cannon material but scoped it lighter, since
  the agenda lists those as "not covered in detail." Dropped the dated MS Blaster
  example from the main slide (moved to a note) in favor of the asymmetry principle.

## Suggested missing coverage on broad themes (point 3)
- **Ransom DDoS (RDoS) / extortion.** The dominant commercial motive in 2024–2026
  is extortion ("pay or we keep flooding you"). Worth a slide connecting DoS to the
  ransomware economy and to the gaming/extortion motives behind Aisuru.
- **Hacktivist and geopolitical DDoS.** Groups like NoName057(16) and wartime DDoS
  (e.g., against Ukrainian, EU, and election infrastructure) make DoS a political
  tool. Strong tie-in to the policy half of the course and the censorship lecture.
- **The IoT-security policy angle.** The root cause (insecure consumer devices) is a
  regulation story: US Cyber Trust Mark, EU Cyber Resilience Act, UK PSTI Act,
  default-password bans. This is the natural "what should the law do?" debate hook.
- **Anycast and BGP as DoS defense/attack surface.** Anycast (why DNS root survives)
  deserves more than a passing mention; it also previews the routing-security lecture
  and BGP-based traffic diversion / RTBH and FlowSpec mitigation.
- **Quantifying amplification.** A short table of reflectors and their amplification
  factors (DNS ~28–54×, NTP ~556×, memcached ~10,000–51,000×, CLDAP, SSDP) would
  make the asymmetry point concrete and is highly midterm-testable.
- **Algorithmic complexity attacks.** Generalize application-layer DoS beyond TLS:
  hash-collision DoS, ReDoS (catastrophic regex backtracking), zip bombs — small
  input, pathological server cost.
- **Measuring/attributing DoS.** Backscatter analysis and the spoofing-measurement
  work (e.g., the Spoofer/CAIDA project) show how researchers estimate spoofing
  prevalence and motivate BCP 38 deployment — good empirical grounding.
- **Cost/economics of mitigation.** Who pays for scrubbing, and the resulting
  market concentration, is a consumer-protection and competition-policy question.

## Next-year refresh notes

Refresh the dated content below per `../TEMPLATE.md` → "Annual current-events refresh" (web-verify; swap only for something fresher and confirmed). Items placed in prior refreshes that will age:

- Added a `.vignette` hook built on Cloudflare's Q4 2025 DDoS threat rep…
- Attributed it to the Aisuru / Kimwolf "TurboMirai" botnet — a Mirai
- Noted the March 19, 2026 international law-enforcement takedown of the
- Reframed the defenses section around autonomous scrubbing (the 31.4 Tb…
- Kept SYN-flood / SYN-cookie / Great Cannon material but scoped it ligh…
- Flag any stronger alternative vignette you find but choose not to use yet.

## Curated images
- **Used:** `slide003_img002.png` (NYT "army of vulnerable gadgets" Mirai story —
  strong headline for the Dyn case study); `slide004_img003.png` (US outage map from
  the Dyn attack); `slide032_img013.png` (Cisco uRPF asymmetric-routing diagram —
  clear teaching figure); `slide035_img016.png` (Great Cannon intercept/reroute
  diagram — clean attack flow).
- **Dropped:** `slide002_img001.png`, `slide004_img004.png` (decorative news-headline
  crops, redundant with the NYT image used); `slide033_img014.png`,
  `slide034_img015.png`, `slide036/037` (additional Great Cannon screenshots —
  redundant once one diagram is shown); `slide038_img019.png`, `slide039_img020.png`
  (Great Cannon client-geography / referrer plots — interesting but the topic is now
  a single light slide; details captured in speaker notes); all `*.wmf` files
  (`slide010_*`, `slide022_*`, `slide023_*`) — Windows metafiles don't render in
  HTML/reveal.js, so the amplification and TLS-handshake flows are described in text
  and notes instead.

## Source
- Rebuilt from `_source-extract.md` (39 slides) + `agenda.md` Meeting 3 (Denial of
  Service Attacks and Botnets). Consolidated to 21 slides; prioritized the agenda's
  emphasized topics (three characteristics, Mirai/Dyn death spiral, reflection/
  amplification, open-resolver incentives, the stateful-firewall "new vulnerability"
  punchline) and scoped down the SYN-flood/SYN-cookie/Great Cannon material that the
  agenda flagged as not covered in detail.
