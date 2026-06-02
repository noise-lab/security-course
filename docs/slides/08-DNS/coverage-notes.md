# 08-DNS — instructor notes

## Current-events updates made (point 2)
- **Opening vignette — AWS us-east-1 outage (Oct 20, 2025).** Replaced generic
  "DNS matters" framing with the verified DynamoDB DNS-automation failure (latent
  race condition → empty/stale records → ~15h cascade across Fortnite, Snapchat,
  Signal, Coinbase, Ring). Used as the centralization/single-point-of-failure
  hook and called back on the "Architectural Crisis" slide. Sourced from AWS
  post-event summary and ThousandEyes/InfoQ analyses; framed explicitly as a
  fault, not an attack.
- **ODoH now deployed (2026 vignette).** Updated the Oblivious DNS story to note
  Cloudflare shipped it as "Oblivious DoH" and that it underpins Apple iCloud
  Private Relay DNS as of 2026 — turning the original research pitch into a
  real-world standard. Kept the "Nick Sullivan / too much latency" anecdote from
  the agenda.
- **Protocol landscape refreshed.** Added DNS-over-QUIC alongside DoT/DoH to
  reflect current encrypted-DNS options; kept DoT-vs-DoH mechanics conceptual per
  the agenda's "not covered in detail" note.
- **Kaminsky cache poisoning (2008)** named on the integrity slide as the classic
  example, kept high-level (agenda flags mechanics as out of scope), satisfying
  the deck's "cache poisoning" topic without over-drilling.

## Suggested missing coverage on broad themes (point 3)
- **ECH / Encrypted Client Hello.** DoH closes the DNS leak, but the TLS SNI and
  the destination IP still expose the site. Worth one slide on what encrypted DNS
  does *not* hide, and how ECH (now broadly deployed) closes the SNI gap — and the
  residual IP-address leak in a CDN-consolidated web.
- **Policy/regulatory angle.** The Jan 2025 US executive guidance pushing DNS
  encryption for federal systems, plus the UK/EU tension where DoH can bypass
  ISP-level content filtering (CSAM blocklists, court-ordered blocks). Strong
  debate material: encryption vs. lawful filtering vs. centralization.
- **DoH as a censorship-circumvention and a censorship-evasion-detection tool.**
  Ties directly to the later censorship lecture; also covert-channel/malware C2
  abuse of DoH.
- **Resolver business models.** Why is 1.1.1.1/8.8.8.8 free? Make the data-vs-ad
  incentives explicit (NextDNS/Quad9 vs. Google) so the "who do you trust" slide
  has economic teeth.
- **Operational DNS security** beyond resolution privacy: registrar/registry
  hijacking, the 2019 Sea Turtle-style nameserver compromises, and DNSSEC
  deployment reality (still <40% validation globally) — i.e., why integrity tools
  exist but are underused.

## Curated images
- **Used:** `slide006_img009.png` (IoT device DNS query table — memorable
  metadata-leak artifact); `slide007_img010.png` (Tor DNS adversary diagram);
  `slide014_img034.png` (DoH/DoT/Do53 response-time CDF — kills the "too slow"
  objection); `slide021_img062.png` (survey: trust in DNS providers);
  `slide024_img070.png` (Firefox DoH notice + Android Private DNS UI — defaults);
  `slide036_img102.png` (page-load-time CDFs for query-distribution strategies).
- **Dropped:** all the per-slide DNS-flow clip-art fragments
  (slide005/009/010/023/026/027/028 `.jpg`/`.png`/`.wmf` pieces) — these are
  exploded PowerPoint animation layers, not real diagrams; the hierarchy and ODoH
  flow are rebuilt as text/numbered steps instead. Dropped the redundant
  interface-grid screenshots (slide016/017/018/019/020) and the
  `slide007_img011`/`_img012` plots (overlapping fingerprinting message;
  `_img010` carries it). Dropped `slide011`–`013` and `slide024_img071` decorative
  screenshots. `.wmf` files are unrenderable in Quarto regardless.

## Source
- rebuilt from `_source-extract.md` (36 slides) + `agenda.md` "DNS Security and
  Privacy" section (lines 439–568), consolidated to 24 slides.
