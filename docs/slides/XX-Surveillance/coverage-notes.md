# XX-Surveillance — instructor notes

## Current-events updates made (point 2)
- **FISA Section 702 (freshest hook, in a `.vignette`).** Replaced the old
  "What's New: FISA and Incidental Collection" slide (which referenced a dated
  paper abstract) with the live 2026 reauthorization fight: 2024 RISAA two-year
  extension → April 20, 2026 sunset → **April 30, 2026 45-day stopgap extension**,
  with the unresolved U.S.-person-query warrant requirement and the data-broker
  loophole. Verified against Lawfare, the Brennan Center 702 resource page, and
  CNBC (Apr 30, 2026).
- **Encryption backdoors (second `.vignette`).** Added a current content-side
  example to set up the in-class debate: the UK **Technical Capability Notice**
  (Jan 2025) demanding Apple weaken iCloud encryption, Apple **pulling Advanced
  Data Protection for UK users** (Feb 2025) rather than build a backdoor, and the
  EU **"Chat Control"** client-side-scanning proposal being pushed and then the
  mandatory-scanning version **withdrawn** under the Danish Council presidency in
  2025. Verified against EFF (Feb/Oct/Dec 2025) and TechRadar.
- **FCC broadband-privacy framing updated.** The original deck litigated the
  April 2016 FCC NPRM / Title II / CPNI / "parity" debate at length (≈10 slides).
  Consolidated to two slides (Swire whitepaper argument + the technical rebuttal)
  and added a speaker-note flag that those FCC broadband-privacy rules were
  **repealed by Congress in 2017** — so the lasting lesson is the technical
  argument (DNS/SNI/IoT leakage), not the now-defunct rule.
- **DNS privacy modernized.** Pulled in the agenda's DoH / ECH / ODoH material
  (Meeting on DNS Security and Privacy) so the "can the ISP see your traffic?"
  thread lands on the current protocols and the centralization trade-off, rather
  than ending in 2016.

## Suggested missing coverage on broad themes (point 3)
- **Third-party doctrine and *Carpenter* (2018).** The deck leans on "knowingly
  divulged to a third party" but never names the doctrine or the Supreme Court's
  cell-site-location ruling in *Carpenter v. United States*, which is the key
  modern limit on it. Worth one slide.
- **Data brokers as a surveillance channel.** The 702 debate now turns on agencies
  *buying* location/clickstream data they could not subpoena. A slide on the
  commercial-data-broker pipeline (and proposals like the "Fourth Amendment Is Not
  For Sale Act") would connect government and commercial surveillance.
- **Smartphone / app location SDKs.** MetaPhone is a phone-records study; today the
  richer location dataset comes from advertising SDKs in apps. A short update would
  modernize the "home location inference" result.
- **Encryption-backdoor technical mechanics.** The debate slide states the
  conclusion ("no math opens only for the good guys") but a brief treatment of
  key escrow / the Clipper chip / client-side scanning hash-matching and its
  false-positive and mission-creep failure modes would arm students for the debate.
- **Pattern-of-life / aggregate metadata beyond phones.** Smart-home and IoT
  telemetry, connected-car data, and license-plate readers extend the metadata
  thesis well past call records; one example would generalize the point.
- **Encrypted Client Hello (ECH) deployment status.** ECH is mentioned but its
  real-world rollout (Cloudflare default, browser support, and where it's blocked,
  e.g., some national firewalls) would make the "fixes relocate trust" point concrete.

## Curated images
- **Used:** `slide017_img009.png` (IP geolocated to a building — implicit-location
  teaching point); `slide029_img015.png` (call-graph degree distribution — explains
  the two-hop explosion); `slide025_img011.png` (MetaPhone study screenshots —
  re-identification); plus `slide033`/`slide034` are referenced conceptually but
  the cleanest single re-id figure (`slide025`) is shown instead to avoid figure
  clutter.
- **Considered but dropped:** `slide033_img020.png` and `slide034_img021.png`
  (home-location accuracy curve and relationship-inference ROC) — good plots, but
  the inference results are summarized as text on one slide to keep the deck lean;
  bring them back if you want to dwell on methodology.
- **Dropped:** `slide002/004/005` (decorative Obama/title art), `slide012_*`
  (clip-art person icons), `slide021/023` (logos/diagram fragments),
  `slide026/027/028/032/037/038` (redundant inference snippets),
  `slide039_img025/026` (dense paper abstract — replaced by the live 702 vignette),
  `slide041/042` (FCC-process flowcharts, credit Jonathan Mayer — cut with the
  trimmed FCC section), `slide048/050/052/056/057/058` (whitepaper covers and
  research-logo collages — decorative).

## Source
- rebuilt from `_source-extract.md` (60 slides) + `agenda.md` (Encryption
  Backdoors debate; DNS Security and Privacy meeting). Condensed to 24 slides.
