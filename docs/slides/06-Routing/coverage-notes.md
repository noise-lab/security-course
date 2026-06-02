# 06-Routing — instructor notes

## Current-events updates made (point 2)
- **Freshest hook (vignette, "What Attackers Can Do"):** July 2025 APNIC/LACNIC
  case study — a BGP hijack achieved by **social-engineering an upstream
  provider** into provisioning BGP without verifying corporate identity or
  domain ownership; spread widely because ROV is inconsistently deployed and
  broad ROA `maxLength` values let more-specific hijacks validate. Teaching
  point: crypto is only as strong as the human/provisioning process around it.
  Sources: APNIC Blog (2026-03-31) and LACNIC Blog, "RPKI vs social
  engineering: A case study in route hijacking."
- **RPKI deployment numbers refreshed to 2025:** ~54% of IPv4/IPv6 routes
  covered by ROAs, and ~74% of traffic destined to ROA-covered prefixes (NIST
  RPKI Monitor; Kentik). Used on "Why Origin Authentication Got Deployed."
- **New policy slide (FCC):** June 2024 FCC NPRM requiring retail broadband
  providers to maintain BGP security risk-management plans; nine largest file
  confidential plans + periodic reports; excused if ROAs cover ≥90% of
  originated routes. Source: FCC DOC-403034A1 / Federal Register 2024-13048.
  This makes the "technical problem → policy lever" arc concrete.
- Kept the **historical case studies** (1997 MAI/Virginia leak, 2010 China
  Telecom, 2008 Pakistan/YouTube) because the agenda explicitly teaches them
  and they best illustrate leak-vs-hijack and the AS-path / longest-prefix
  mechanics. Modernized framing (RPKI/ROV/BGPsec) layered on top.

## Suggested missing coverage on broad themes (point 3)
- **A concrete "see it yourself" demo:** the agenda has no live tooling. Adding
  a one-slide walkthrough of a public looking glass or RIPEstat / bgp.tools /
  Cloudflare `is-bgp-safe-yet` would make ROA validity tangible.
- **Recent high-impact incidents beyond hijacks:** the Oct 2021 Facebook BGP
  self-withdrawal outage is a memorable, non-malicious example of how routing
  fragility takes down a giant; worth a sentence as contrast to attacks.
- **MANRS** (Mutually Agreed Norms for Routing Security) as the *voluntary*
  counterpart to the FCC mandate — good for the incentives discussion.
- **IRR vs RPKI:** the deck (rightly, per agenda) omits the older Internet
  Routing Registry filtering. One line distinguishing IRR route objects from
  cryptographic ROAs would pre-empt a common student confusion.
- **Data-plane verification:** mentioned as a gap but not developed; could note
  research directions (path-aware networking, traceroute-based detection,
  RPKI-to-router/RTR). Optional, likely out of scope for this course.
- **Naming consistency:** agenda says NOT to belabor S-BGP vs BGPsec naming.
  Deck uses "BGPsec / S-BGP" once and otherwise says "path authentication" — if
  the instructor prefers, standardize on "BGPsec" (the deployed-spec name).

## Curated images
- **Used:** `slide004_img002.png` (1997 CNET route-leak headline — anchors the
  accidental-leak case); `slide006_img004.png` (Renesys world map of networks
  affected, 2010 China event); `slide007_img005.png` (China Telecom→Verizon
  AS-graph — the core "shortest AS path wins" teaching diagram);
  `slide009_img006.png` (Pakistan→YouTube AS-graph — longest-prefix match +
  censorship-leaks-globally).
- **Dropped:** `slide002_img001.wmf` and `slide016_img009.wmf` (WMF clip-art
  diagrams; Quarto/reveal can't render WMF and the source notes call the first
  one "very confusing" — replaced with text/analogy). `slide005_img003.png`
  and `slide011_img007.png` are duplicate Renesys-blog screenshots of
  `slide006`; `slide012_img008.png` duplicates `slide006`. The raw traceroute
  text dumps (source slides 26–28) were dropped as too dense for a lecture
  slide; the TTL idea is captured in the GTSM bonus slide instead.

## Source
- Rebuilt from `_source-extract.md` (58 slides) + `agenda.md` "Lecture
  Coverage: Internet Routing Security" (Meeting on routing). Consolidated to
  18 slides; original S-BGP/soBGP attestation-format detail intentionally
  trimmed per the agenda's "Topics NOT Covered in Detail."
