# 05-DoS — instructor notes

## Current-events updates made (point 2)
- **2026-07-16 annual refresh:**
  - Restated the `.vignette` with primary-source detail: attack was in
    **November 2025** (Cloudflare Q4 2025 DDoS report, published Feb 2026),
    peaked at **31.4 Tbps / 35 s**.
  - Corrected botnet size to Cloudflare/XLab's current estimate of
    **1–4 million infected hosts** (older "300,000+" figure was pre-2025 XLab
    estimate; kept as historical anchor in speaker notes).
  - Sharpened the March 19, 2026 takedown to name the four botnets seized
    (Aisuru, Kimwolf, JackSkid, Mossad) and the international coalition (DoJ,
    German BKA, Canadian authorities) — sources: DoJ press release; The Hacker
    News; SecurityAffairs; Help Net Security.
  - Added the Aisuru → KrebsOnSecurity (6.35 Tbps, May 2025) callback to the
    notes, closing the Mirai (2016 attack on Krebs) → Aisuru loop.
  - Added a "botnet cycle continues" coda to the vignette notes (per FastNetMon
    / Flowtriq analysis of post-takedown rescanning).
  - Fixed the **Great Cannon date** on the case-study slide: the GreatFire/
    GitHub attack was **March 2015**, not 2016 (Krebs, Citizen Lab, Marczak
    et al. USENIX FOCI '15).
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

- **31.4 Tbps / Aisuru/Kimwolf record** — will be broken; check Cloudflare's
  latest DDoS threat report and Netscout ASERT before the next term. Candidates
  as of 2026-07: any AI-inference-target attack, or a new botnet family that
  supplanted Aisuru post-takedown (already-observed rebuilding activity).
- **March 19, 2026 takedown** — check DoJ press releases for follow-on
  indictments (Canada/Germany named operators, expect prosecutions to develop).
- **~5,376 mitigations/hour** and **Cloudflare's autonomous scrubbing frame** —
  restate with next annual DDoS-report figures.
- **Aisuru → KrebsOnSecurity 6.35 Tbps (May 2025)** callback — swap for the
  freshest attack on a memorable target if one emerges.
- **US Cyber Trust Mark / EU CRA / UK PSTI / CA SB-327** — these regulations
  are moving through implementation phases; check for the first CRA
  enforcement actions and any DoJ IoT-liability litigation.
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
