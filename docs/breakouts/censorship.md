# Internet Censorship

**Format.** Break into groups of 4–5. Each group picks **one** of the two breakouts below (or takes both if time allows). Spend ~5 minutes skimming the prep reads, then ~10 minutes debating. A designated reporter brings the group's position — and any dissents — back to the full class for a ~3-minute report-back.

Lecture 17's headline: 2025 was the worst year on record for deliberate internet shutdowns (Access Now / #KeepItOn — 313 shutdowns across 52 countries; est. $19.7B economic losses; 75 shutdowns still ongoing entering 2026). Iran and Russia have pivoted from blacklisting to *whitelisting* — block everything, allow only "socially significant" services. The Roberts friction/flooding/fear framework organizes both breakouts.

---

## Breakout A: When Democracies Use Censorship Techniques
<!-- breakout id="A" status="current" refreshed="2026-07-16" -->

**Motion.** *"Government-imposed internet restrictions are illegitimate regardless of the political regime imposing them. Age-verification mandates in the U.S. and UK, court-ordered DNS blocks in France and Italy (Champions League piracy blocking, 2026), and platform-carriage laws are all censorship in the Roberts sense — they raise 'friction' to disfavored expression — and democracies should stop pretending otherwise."*

<!-- current-events:start topic="democratic-censorship-age-verification-blocking" -->
**Prep reads (5–10 min).**
- [Social media ban for children under 16 starts in Australia](https://www.npr.org/2025/12/10/nx-s1-5639694/social-media-ban-children-australia) — NPR, December 10, 2025. World-first mandatory under-16 platform ban with A$33M fines; 4.7M under-16 accounts deactivated in the first week and TikTok removed 200,000+ before day one.
- [French Court Orders Google DNS to Block Pirate Sites, Dismisses 'Cloudflare-First' Defense](https://torrentfreak.com/french-court-orders-google-dns-to-block-pirate-sites-dismisses-cloudflare-first-defense/) — TorrentFreak, January 2026. Paris Judicial Court orders Google's public DNS to block 19 domains for the 2025/2026 Champions League season, with dynamic Arcom-managed updates.
- [Ofcom issues update on Online Safety Act investigations](https://www.ofcom.org.uk/online-safety/illegal-and-harmful-content/ofcom-issues-update-on-online-safety-act-investigations) — Ofcom, 2025. Regulator's own tally: 21 investigations across 69 sites since March 2025 enforceability; £20,000 first fine against 4chan, £1M+ against AVS Group, £800K against Kick.
- [ICO hits Reddit with £14.5M fine for not implementing robust age assurance](https://www.biometricupdate.com/202602/ico-hits-reddit-with-14-5m-fine-for-not-implementing-robust-age-assurance) — Biometric Update, February 2026. Coordinated ICO/Ofcom action: Reddit fined for using under-18s' data in recommender systems without a DPIA; the age-verification / children's-code convergence.
<!-- current-events:end -->

**Discussion prompts.**
- The Roberts framework classifies censorship by mechanism: friction (make access harder), flooding (drown out disfavored speech), fear (deter self-expression). Age-verification adds friction; U.S. deplatformings add fear (of losing your account); moderation-by-LLM adds flooding of policy warnings. Are all three equally censorship, or does the intent/actor matter?
- The 2026 French Court of Appeals confirmed public DNS resolvers can be compelled to block domains; the Italian AGCOM fined Cloudflare €14M for refusing. These are democracies with due process. Is this legitimate exercise of state power or the same tool authoritarians use with a court order stapled on?
- U.S. age-verification laws (Utah, Louisiana, Texas, and the UK Online Safety Act) require ID for adult content. The First Amendment / Article 10 case law has been mixed. Is this a friction-based content restriction or an incidental burden justified by child-protection interest?
- Cloudflare's 2017 Daily Stormer / 2019 8chan / 2022 Kiwi Farms deplatformings weren't state action, but they had censorship-scale effects. Should democracies formally regulate infrastructure providers as public utilities (with attendant carriage obligations), or is the current CEO-discretion model preferable?

**Bring back.** Your group's proposed one-sentence test for when a *democratic* government restriction crosses from "regulation" into "censorship," and one specific case that would test it.

---

## Breakout B: Whitelisting, VPN Crackdowns, and the End of the Open Internet
<!-- breakout id="B" status="current" refreshed="2026-07-16" -->

**Motion.** *"Iran's and Russia's pivot to whitelisting (allow only approved services) is the censor's structural answer to circumvention: it makes VPNs and encrypted DNS irrelevant because there's no destination to reach. The open internet as a global commons is over; what remains is a set of national networks with connective tissue at the pleasure of each state."*

<!-- current-events:start topic="whitelisting-vpn-crackdown-splinternet" -->
**Prep reads (5–10 min).**
- [2025 report on internet shutdowns](https://www.accessnow.org/wp-content/uploads/2026/03/KeepItOn-Internet-Shutdowns-2025-Annual-Report.pdf) — Access Now / #KeepItOn, March 2026. Worst year on record: 313 shutdowns across 52 countries; Myanmar (95), India (65), 75 shutdowns still ongoing into 2026, first-time offenders including the U.S.
- [Whitelists For Dark Times: Russian authorities persistently build a 'closed' internet on top of an 'open' one](https://re-russia.net/en/analytics/0364/) — Re: Russia, 2025. The "registry of socially significant services" whitelist introduced September 2025, plus proposed VPN whitelists — the structural pivot away from blacklisting.
- [Iran's Stealth Internet Blackout: A New Model of Censorship](https://arxiv.org/html/2507.14183v1) — arXiv, 2025. Measurement paper on Iran's June 2025 tiered whitelist system: DNS/HTTP/HTTPS only, all other protocols silently dropped, no BGP withdrawal.
- [Russia's internet censorship in 2026: VPN crackdowns, mobile shutdowns, Telegram blocks and the state messenger Max](https://en.zona.media/article/2026/04/07/russian_internet_censorship_2026) — Zona.Media, April 2026. Roskomnadzor blocked 258 VPN services in the first ten months of 2025; VPN use is now an aggravating criminal factor; WhatsApp throttled nationwide by late November.
<!-- current-events:end -->

**Discussion prompts.**
- Blacklisting requires an infinite arms race (new domain, new VPN, new proxy). Whitelisting inverts the default: nothing works by default. Is whitelisting a *stable equilibrium* for censors, or does the economic cost (killing legitimate services) make it self-limiting?
- VPN crackdowns: 2024–2025 saw Russia pressure app stores to remove VPN apps (Apple complied for the Russian App Store); periodic pressure in China, India, Iran. ECH and DoH make protocol-level detection harder — do these advances *matter* if the state controls the exit link?
- Decoy routing / refraction networking (deployed at ISP scale) attempts to make circumvention invisible from the endpoint. Are these plausibly deployable in the next decade, or destined to remain research prototypes?
- Access Now's 313 shutdowns / 52 countries figure is 2025's worst-on-record. Is the trend line reversing at all, or is deliberate connectivity denial simply becoming a normalized state tool?

**Bring back.** Whether your group thinks the "splinternet" is a real trend or an overblown narrative, and one specific 2027 development that would confirm or refute your view.

---

## Breakout format note

The [Censorship](../debates/censorship.md) whole-class debate is on this day. Breakout A workshops the debate directly; run it before the debate.

## Instructor notes

Breakout A is often uncomfortable in a productive way — students who reflexively support content moderation and age-verification have to confront the friction/flooding/fear symmetry. Breakout B is more geopolitical and works best if students have followed the Russia/Iran / China / India stories. If time is short, run A. Both benefit from a whiteboard side-by-side of the Roberts framework applied to (1) a Chinese blocking action, (2) a U.S. age-verification law, (3) a Cloudflare deplatforming — students will disagree on classification, which is the point.

<!--
breakout-metadata:
  lecture: 17
  class: "Internet Censorship"
  last_refreshed: 2026-07-16
-->
