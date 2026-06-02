# 10-IoT — instructor notes

## Current-events updates made (point 2)

- **Added a 2025–2026 ACR enforcement vignette** as the freshest hook. On
  **2025-12-15** Texas AG Ken Paxton sued five TV makers (Samsung, Sony, LG, Hisense,
  TCL) over Automatic Content Recognition; a court issued the first-ever TRO against a
  TV maker two days later (Hisense, 2025-12-17); **Samsung settled on 2026-02-26**
  agreeing to require express consent; **Kentucky** passed the first ACR-specific consent
  law. This directly extends the deck's 2019 smart-TV-crawler finding into live policy.
  Sources: Texas AG press release; Cybernews; The Record; IAPP; State of Surveillance.
- **Reframed the old research-talk deck (146 slides) into a teaching arc** rather than a
  slide-for-slide port. The original was a job-talk-style walk through three papers; the
  rebuild keeps the three studies as Parts 1–3 but foregrounds the *ideas* (no-isolation
  LAN, measurement-at-scale, ineffective opt-outs).
- **Kept the COPPA / YouTube $170M (Sept 2019) example** as a verified, dated anchor for
  children's-privacy, and tied it forward to the ACR vignette so the deck shows a
  research → enforcement progression rather than a single dated case.
- Dated and attributed both core studies (SIGCOMM IoT S&P Workshop 2018; ACM CCS 2019)
  and IoT Inspector's May-2019 release / 5k-user, 50k-device scale, so figures are
  anchored rather than floating.

## Suggested missing coverage on broad themes (point 3)

- **Mirai / IoT botnets as a security externality.** The agenda covers Mirai → Dyn (Oct
  2016) in the DDoS lecture; this deck would benefit from one explicit cross-reference:
  insecure consumer IoT is not just *your* privacy risk, it is *internet-wide* attack
  infrastructure. Good place to discuss the FTC/NIST "security-by-default" and labeling
  push (e.g., the U.S. Cyber Trust Mark for consumer IoT).
- **Encrypted-traffic inference / side channels.** Even when IoT traffic *is* encrypted,
  packet sizes and timing reveal device type and user activity (sleep, presence,
  voice-assistant queries). Connects to the website-fingerprinting material already in
  the agenda (Meeting on DNS/tracking) — same ML-on-metadata idea, applied to the home.
- **Voice assistants specifically.** Always-listening microphones, accidental
  activations, cloud retention of recordings, and law-enforcement requests for Echo/Alexa
  data. The current deck is camera/TV-heavy; a voice-assistant slide would round out
  "smart home."
- **Network defenses in depth.** The deck gestures at segmentation/zero-trust LAN but
  could add a concrete slide: VLANs/guest networks for IoT, manufacturer usage
  descriptions (MUD, RFC 8520), DNS-based blocking (Pi-hole) and its limits, and on-router
  filtering. Pairs with the "opt-outs don't work" slide as the technical alternative.
- **Regulatory landscape, current.** Beyond COPPA: the U.S. state-privacy patchwork as
  applied to device data, the EU **Cyber Resilience Act** (security obligations for
  connected products) and **GDPR** on device identifiers, and the FTC's general Section 5
  authority. A single comparative slide would link this deck to the privacy-law unit.
- **Right-to-repair / longevity / abandonment.** Devices that lose cloud support or stop
  getting security patches become permanent liabilities — a consumer-protection angle the
  course's framing invites.

## Curated images

- **Used** (genuinely teaching-relevant):
  - `slide110_img182.png` — IoT Inspector "Device Activities for Roku" dashboard; the best
    single screenshot of real per-device tracking traffic, with the encryption-view
    selectors visible.
  - `slide079_img142.png` — clean two-column table of top tracker domains by channel count
    (Roku vs Fire TV); concrete data with recognizable tracker names.
  - `slide137_img234.png` — FTC/NY-AG "Google and YouTube Will Pay Record $170 Million"
    COPPA headline; anchors the children's-privacy slide.
- **Dropped** (clip-art / logos / decorative / redundant):
  - Device product shots and dev-board photos (`slide002_*`, `slide042_*`, `slide061_*`),
    vendor logos (Google, Roku — `slide092`, `slide113_img191`), and the dozens of
    near-identical attack-step diagram fragments (`slide004`–`slide022`) which are tiny
    arrow/IP overlays that don't survive extraction; the attack flow is conveyed in text
    + speaker notes instead, per the TEMPLATE guidance on not reproducing misleading
    fragments.
  - The many repeated "Automatically interacting with channels" screenshots
    (`slide063`–`slide072`) and crawler system-design fragments — consolidated into one
    text slide.

## Source

- Rebuilt from `_source-extract.md` (146 slides) + `agenda.md` (Mirai/IoT in the DDoS
  meeting; device privacy as the post-break follow-on to web tracking & fingerprinting).
  Consolidated to 21 slides covering: motivation, web-based device discovery (SOP side
  channel) + DNS rebinding control, IoT Inspector (ARP-spoof measurement + at-scale
  findings), smart-TV crawler (trackers, identifiers, COPPA, ineffective opt-outs), the
  2025–26 ACR enforcement vignette, and synthesis.
