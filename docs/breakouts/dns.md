# DNS Security

**Format.** Break into groups of 4–5. Each group picks **one** of the two breakouts below (or takes both if time allows). Spend ~5 minutes skimming the prep reads, then ~10 minutes debating. A designated reporter brings the group's position — and any dissents — back to the full class for a ~3-minute report-back.

Lecture 8 opens with the AWS us-east-1 outage (Oct 20, 2025) — a *DynamoDB DNS-automation race condition* took Fortnite, Snapchat, Signal, Coinbase, and Ring offline for ~15 hours. Not an attack. Just DNS. Every "fix" the lecture surveys (DoH, DoT, DoQ, DNSSEC, ODoH, ECH) trades one trust problem for another. Both breakouts push on where you'd rather have the failure mode.

---

## Breakout A: Encrypted DNS Just Moved the Chokepoint
<!-- breakout id="A" status="current" refreshed="2026-07-16" -->

**Motion.** *"Browser-default DoH to Cloudflare and Google is a net loss for user autonomy: it hides queries from your ISP only by handing a global veto to three American companies, and it defeats ISP-level content filtering (CSAM blocklists, court-ordered blocks) that democracies rely on."*

<!-- current-events:start topic="doh-centralization-court-orders" -->
**Prep reads (5–10 min).**
- [Italy Fines Cloudflare €14 Million for Refusing to Block Pirate Sites on Public 1.1.1.1 DNS](https://torrentfreak.com/italy-fines-cloudflare-e14-million-for-refusing-to-filter-pirate-sites-on-public-1-1-1-1-dns/) — TorrentFreak, January 2026. AGCOM imposes €14.2M (1% of global revenue) after Cloudflare refuses to filter 1.1.1.1 for the Piracy Shield; Matthew Prince calls the order globally dangerous and threatens to pull Cloudflare's servers from Italy.
- [Google, Cloudflare, Cisco Lose Pirate Site DNS Blocking Appeal in France](https://torrentfreak.com/google-cloudflare-cisco-lose-pirate-site-dns-blocking-appeal-in-france/) — TorrentFreak, March 2026. Paris Court of Appeal rejects the "neutral and passive" defense on all five appeals and confirms that public DNS resolvers can be compelled to block domains and must pay for the plumbing themselves — a rebuttal of the 2023 German Cologne ruling.
- [DNS Provider Quad9 Sees Piracy Blocking Orders as "Existential Threat"](https://torrentfreak.com/dns-provider-quad9-sees-piracy-blocking-orders-as-existential-threat/) — TorrentFreak, November 2025. The Swiss nonprofit warns that being added to the French blocking orders alongside Google and Cloudflare is a survival-level problem — and that its no-geolocation privacy design forces French blocks to apply globally.
- [Apple Drops iCloud's Advanced Data Protection in the U.K. Amid Encryption Backdoor Demands](https://thehackernews.com/2025/02/apple-drops-iclouds-advanced-data.html) — The Hacker News, February 2025. Parallel chokepoint story: even when a big-tech resolver/service *does* resist, a single democratic government's demand (UK Investigatory Powers Act) can pull a security feature offline for an entire country.
<!-- current-events:end -->

**Discussion prompts.**
- Chrome defaults to Google's resolver; Firefox defaults to Cloudflare's. Neither asked. Apple iCloud Private Relay uses Oblivious DoH — splitting knowledge between proxy and resolver so neither sees "who is asking what." If ODoH shipped as the default tomorrow, would that solve the problem or is *takedown power* (not surveillance power) the real issue?
- ECH closes the SNI leak in TLS 1.3, but the destination IP is still visible and increasingly maps to one of a few CDNs. In a Cloudflare-consolidated web, does encrypted DNS actually protect against network-level observability, or does it just relocate the observation point?
- Rank the following as a resolver operator you would trust: your ISP, Cloudflare, Google, your government's public resolver, a nonprofit like Quad9, a resolver you run yourself. Defend the top and bottom of your ranking.
- The 2025 U.S. federal-systems guidance pushes DNS encryption; the UK and parts of the EU want ISPs to keep the ability to filter. Is there a principled middle ground, or is this a genuine values disagreement about who deserves plaintext visibility?

**Bring back.** Your group's rank-ordering of resolver operators, and the single strongest counterargument to your top pick.

---

## Breakout B: Kaminsky at 18 — Why Isn't DNSSEC Everywhere?
<!-- breakout id="B" status="current" refreshed="2026-07-16" -->

**Motion.** *"Eighteen years after Kaminsky (2008) proved cache-poisoning was trivial and DNSSEC was proposed as the fix, we sit at <40% DNSSEC validation globally. This is a market failure worth regulating: any authoritative nameserver serving traffic to U.S. users should be required to publish signed zones by 2028."*

<!-- current-events:start topic="dnssec-deployment-mandate-integrity" -->
**Prep reads (5–10 min).**
- [A single DNS race condition brought AWS to its knees](https://www.theregister.com/2025/10/23/amazon_outage_postmortem/) — The Register, October 2025. The us-east-1 postmortem: an internal DynamoDB DNS-Enactor race deleted every DNS record for `dynamodb.us-east-1.amazonaws.com` and cascaded into a 15-hour outage — a reminder that DNS availability failure modes remain unsolved even at hyperscale.
- [Race Condition in DynamoDB DNS System: Analyzing the AWS US-EAST-1 Outage](https://www.infoq.com/news/2025/11/aws-dynamodb-outage-postmortem/) — InfoQ, November 2025. Deeper technical walkthrough of the DNS Planner / DNS Enactor architecture; note that DNSSEC would not have prevented any of it.
- [DNSSEC Adoption in 2026: Only 0.47% of DNS Queries Validated End-to-End](https://technologychecker.io/blog/dnssec-adoption) — TechnologyChecker, 2026. Cloudflare Radar-based rollup: end-to-end DNSSEC validation grew from 0.32% (Q1 2025) to 0.47% (Q1 2026); signing sits at ~8% of domains; concentration in .com is the main brake on adoption.
- [Towards an industry best practice for DNSSEC automation](https://blog.apnic.net/2026/02/25/towards-an-industry-best-practice-for-dnssec-automation/) — APNIC Blog, February 2026. Why the deployment gap is now operational (multi-signer, key rollover automation, registrar API gaps) rather than protocol — the operator's honest answer to "why isn't DNSSEC everywhere?"
<!-- current-events:end -->

**Discussion prompts.**
- DNSSEC signs answers but doesn't change *who* can answer. If Google's authoritative servers all published signed zones tomorrow, does that prevent the AWS us-east-1 style outage, defend against cache poisoning, both, or neither?
- The registrar/registry compromises of Sea Turtle (2019) style hijacked nameserver delegations at the registrar layer — DNSSEC signatures survived, but the attackers changed *which* signed zone was authoritative. Is DNSSEC's real utility about integrity, availability, or something else?
- Compare the ~54% RPKI ROA coverage from Lecture 6 with <40% DNSSEC validation. What explains the gap? Is one problem "harder" or is one just better regulated / incentivized?
- ODoH, DoH, DoT, DoQ, ECH — the encrypted-DNS zoo. Add DANE (DNS-based TLS anchoring) on top. Is this a healthy protocol ecosystem or a sign that the underlying design is fundamentally not fixable?

**Bring back.** Whether your group would mandate DNSSEC for U.S.-facing authoritative nameservers, and one type of operator you'd exempt.

---

## Instructor notes

Breakout A is the one students engage with most — everyone in the room uses Chrome or Firefox, and the "you already agreed to this" beat is uncomfortable in a productive way. Breakout B is denser and better suited to classes that have already covered PKI (Lecture 3) and Routing (Lecture 6). If time is short, run A. If your class has done the [DNS activity](../activities/dns.md) that day, students will have just run `dig +dnssec` themselves — a natural on-ramp to B. Both benefit from a whiteboard-drawn diagram: client → resolver → authoritative, with plaintext leaks marked at each hop.

<!--
breakout-metadata:
  lecture: 8
  class: "DNS Security"
  last_refreshed: 2026-07-16
-->
