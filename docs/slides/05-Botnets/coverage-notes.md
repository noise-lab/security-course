# 05-Botnets — instructor notes

## Current-events updates made (point 2)
- Added a **2026 vignette** ("A 2026 Bookend: Mirai's Descendants") grounding the
  lecture in verified, dated events:
  - **Aisuru/Kimwolf** botnet — a Mirai-class IoT family (compromised Android TVs,
    home routers) — drove a **31.4 Tbps** DDoS mitigated by Cloudflare in
    **November 2025**, the largest publicly disclosed attack to date (Cloudflare
    Q4 2025 DDoS Threat Report).
  - **March 2026 DoJ / District of Alaska** takedown of Aisuru, Kimwolf, JackSkid,
    and Mossad — **3M+ infected devices**, coordinated with international partners
    and major cloud/CDN providers.
- Framed the modern example as continuity with Dyn (2016): same default-credential,
  unpatched-IoT economics, scaled from gigabits to tens of terabits. This keeps the
  historical Mirai/Dyn case study but shows it is a living template, not history.
- Reframed the whole deck around what was actually taught (agenda.md, Meeting on
  "Denial of Service Attacks and Botnets"): the **three DoS characteristics**,
  the **Mirai/Dyn** case, the **death-spiral**, and **DNS reflection/amplification**
  with the stateful-firewall-as-new-attack-surface principle. Cut the original
  deck's long worm-by-worm catalog (Code Red I/v2/II, Storm internals, Conficker/
  Mega-D/Zeus list) down to a single evolution arc.

## Suggested missing coverage on broad themes (point 3)
- **DDoS-for-hire / "booter" economy.** The lecture treats botnets as attacker-built;
  in practice DDoS is a rented commodity. A slide on the criminal market (and the
  recurring FBI booter-service seizures) would connect to the policy/consumer-
  protection theme of the course.
- **Mitigation services and centralization.** Cloudflare/Akamai/AWS Shield absorb
  these attacks — but that means a handful of firms now sit in front of much of the
  web. Worth a policy discussion: DDoS defense has consolidated the Internet's choke
  points (ties to the "attack the infrastructure everyone depends on" insight).
- **IoT security regulation.** Mirai → Aisuru is fundamentally a market-failure /
  externality story (insecure devices harm third parties). Cover the policy responses:
  US Cyber Trust Mark, California/Oregon default-password laws, UK PSTI Act, EU Cyber
  Resilience Act. Strong fit for this course's regulation angle.
- **BCP 38 / source-address validation in practice.** The deck names ingress
  filtering as the root-cause fix; a slide on *why deployment lags* (no incentive for
  the network that would deploy it — classic misaligned-incentive externality) would
  deepen the economics-of-security thread.
- **TCP SYN floods and SYN cookies.** Explicitly listed as "not covered in detail" in
  the agenda; a brief treatment would round out the connection-state-exhaustion class
  of attacks and pairs naturally with the stateful-firewall principle.
- **Amplification beyond DNS.** NTP, memcached (the 1.3 Tbps GitHub 2018 attack), and
  CLDAP reflectors have higher amplification factors than DNS and would make the
  asymmetry point more vivid.
- **Attribution and norms.** Beyond technical traceback, touch on the legal/diplomatic
  side: when DDoS is nation-state vs. criminal, and how takedowns now require
  multi-jurisdiction cooperation (the 2026 Aisuru action is a concrete hook).

## Next-year refresh notes

Refresh the dated content below per `../TEMPLATE.md` → "Annual current-events refresh" (web-verify; swap only for something fresher and confirmed). Items placed in prior refreshes that will age:

- Aisuru/Kimwolf
- March 2026 DoJ / District of Alaska
- Flag any stronger alternative vignette you find but choose not to use yet.

## Curated images
- **Used:**
  - `slide016_img003.png` — Code Red infected-hosts-over-time curve (shows
    exponential worm growth concretely).
  - `slide029_img007.png` + `slide030_img008.png` — Slammer spread at 05:29 UTC vs.
    30 min later; the before/after pair is a striking visualization of speed.
  - `slide037_img010.png` — Mirai global infection map + per-country table (grounds
    the IoT/global-distribution point).
- **Dropped:**
  - `slide007_img001.jpg` — Morris headshot (decorative, no teaching value).
  - `slide012_img002.png` — "Summer of 2001" graphic (redundant with consolidated
    worm-history slide).
  - `slide017_img004.png`, `slide018_img005.png` — Random Constant Spread model
    equations; cut with the analytical worm-modeling material that the agenda did not
    cover.
  - `slide024_img006.png` — Paxson Code Red I/II plot (redundant with the Code Red
    curve already used).
  - `slide035_img009.jpg` — Storm outbreak clip-art (decorative).

## Source
- Rebuilt from `_source-extract.md` (50 slides) + `agenda.md` Meeting section
  "Denial of Service Attacks and Botnets" (lines ~195–309), consolidated to 21
  slides. Current-events facts verified via web search (Cloudflare Q4 2025 DDoS
  report; DoJ/District of Alaska press release, March 2026).
