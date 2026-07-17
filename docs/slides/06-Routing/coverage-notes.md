# 06-Routing — instructor notes

## Current-events updates made (point 2)
- **2026-07-16 annual refresh:**
  - Restated the hijack `.vignette` with the primary-source detail from the
    APRICOT 2026 / APNIC 61 SIG presentation (Martínez-Cagnazzo / Sanjaya):
    July 9–12, 2025; three short attacks; forged identity documents + lookalike
    domain used to convince a multinational transit provider; first detected
    when an email silently vanished. Sources: APNIC Blog (2026-03-31), LACNIC
    Blog, LAC Peering Forum 2026 slide deck.
  - Refreshed RPKI numbers to mid-2026 figures: **~60% of IPv4 routes**
    covered by ROAs (Qrator Q1 2026 stats), **~70% of traffic** to ROA-covered
    prefixes (Kentik), and added the sharper deployment-lag number: **only
    ~12.3% of ASes are fully ROV-protected** (RoVista / NANOG 90). This
    strengthens the "coverage != enforcement" teaching point.
  - Added the **status of the FCC NPRM**: comments closed August 2024, no
    final rule as of mid-2026; proceeding still open (PS Docket 24-146). Added
    the political-context caveat in speaker notes (2025 leadership change,
    Title II reclassification vulnerability).
  - Added the June 2026 **Reliance-Telegram BGP incident (India)** as a
    candidate future vignette in Next-year notes but did NOT swap the
    social-engineering case in — the latter better teaches the human-process
    lesson which is unique to this deck.
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

## Next-year refresh notes

Refresh the dated content below per `../TEMPLATE.md` → "Annual current-events refresh" (web-verify; swap only for something fresher and confirmed). Items placed in prior refreshes that will age:

- **July 2025 APNIC/LACNIC social-engineering vignette** — still the sharpest
  hook as of 2026-07 (unique in that RPKI wasn't defeated, the human process
  was). Swap only for another case where the *provisioning layer* is the
  weakness, not for a plain RPKI-invalid hijack.
- **Alternative vignette flagged but not used:** the **June 2026 Reliance vs.
  Telegram** BGP incident (India) — Reliance's internal traffic-engineering
  BGP policy for AS18101 leaked globally due to bad export filters; Telegram
  CEO publicly accused Reliance of a hijack. Good for the "leak vs. hijack"
  ambiguity discussion. Source: Medium/CyberBruhArmy write-up June 2026 and
  general press coverage.
- **RPKI coverage numbers** (~60% routes, ~70% traffic, ~12% ASes fully
  enforcing) — update from NIST RPKI Monitor, Cloudflare Radar RPKI
  sub-page, Kentik, RoVista annual figures.
- **FCC NPRM status** — check whether a final rule or a formal withdrawal has
  happened; the proceeding may have moved substantially by next term.
- **RPKI ROV milestones** — Sparkle (Feb 2026), Bell Canada (Aug 2025),
  Energotel (Oct 2025) all now filter invalids. Cite the next big Tier-1 or
  major-content-network flip.
- Flag any stronger alternative vignette you find but choose not to use yet.

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
