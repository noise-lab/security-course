# 09-WebPrivacy — instructor notes

## Current-events updates made (point 2)
- **Google's third-party-cookie reversal (April 2025) + Privacy Sandbox retirement
  (October 2025).** The original deck treated third-party cookies as the central,
  soon-to-be-deprecated mechanism. That framing is now wrong: in April 2025 Google
  announced it will NOT deprecate third-party cookies in Chrome (no phase-out, no
  consent prompt), and in October 2025 began retiring most Privacy Sandbox APIs after
  low adoption. This is the vignette on the "Browsers Fought Back — Mostly" slide and
  reframes Chrome as the holdout while Safari/Firefox block by default. Verified via
  Google Privacy Sandbox blog and multiple trade-press reports (Didomi, Usercentrics).
- **GPC multistate enforcement sweep (September 2025) + revised CCPA rules effective
  Jan 1, 2026.** Replaced the dead "Do Not Track" ending with the DNT → GPC arc. The
  CPPA + CA/CO/CT AGs launched a joint investigative sweep of businesses ignoring GPC
  signals; revised CCPA regs effective 2026-01-01 require businesses to confirm GPC
  requests were processed. This is the closing vignette and the bridge to the
  privacy-law lectures. Verified via cppa.ca.gov announcement and law-firm alerts
  (Goodwin, Skadden, Greenberg Traurig).
- **Social-widget joint controllership (CJEU, 2024).** Replaced the stale NSA-ad-cookie
  framing as the sole legal hook with the more current EU joint-controller line tied to
  the Like button / Meta Pixel. Stated as reinforcement of existing doctrine, not a new
  holding, to avoid overclaiming specifics.
- **Manifest V3 caveat** added to the request-blocking speaker notes: Chrome's MV3
  weakens the blocking APIs uBlock Origin and similar extensions rely on — a current,
  concrete instance of the arms race that did not exist when the original deck was made.
- Refreshed tracker examples beyond the original 2007-era names (112.2o7.net, revsci.net)
  to current ones (LiveRamp, Criteo, Meta Pixel, Google Tag Manager) per agenda.md.

## Suggested missing coverage on broad themes (point 3)
- **Real-time bidding (RTB) as a data-broker pipeline.** The deck shows the ad-auction
  diagram but not that the bid-request itself broadcasts user data to hundreds of
  bidders. Worth a slide: the 2022–2024 ICCL/RTB reports and the IAB's TCF being ruled
  unlawful by the Belgian DPA. Strong policy bridge.
- **Server-side tagging / CNAME cloaking / first-party disguising.** The current evasion
  frontier — trackers move to first-party subdomains and server-side endpoints to defeat
  list-based blockers and cookie restrictions. Directly answers the "how would trackers
  evade?" exercise already in the notes.
- **Mobile / app tracking and Apple's ATT.** The deck is web-only. A slide on the
  IDFA/advertising-ID model, App Tracking Transparency (2021), and SDK-based tracking
  would round out "device privacy" (flagged as the next topic in agenda.md).
- **Data brokers and onboarding.** Cookie syncing is covered; the offline side
  (Acxiom/LiveRamp matching online IDs to offline purchase and location data) deserves
  explicit treatment, plus the FTC's recent data-broker / location-data enforcement.
- **Fingerprinting defenses in depth.** Mention Tor Browser's uniformity strategy,
  Firefox/Safari fingerprinting resistance, and the inherent tension: anti-fingerprinting
  by making everyone look identical vs. by adding noise.
- **Consent banners / dark patterns.** GDPR/CCPA cookie banners and the CPPA's work on
  deceptive consent UX connect this lecture to the compliance lectures.

## Curated images
- USED: slide005_img003.png (NYT page with third-party requests boxed — concrete "one
  page, many trackers"); slide006_img005.png (Lightbeam tracker-graph — best abstraction
  visual); slide012_img008.png (two data plots: top trackers by page-load share + share
  of first-parties embedding each — strongest consolidation evidence); slide013_img009.png
  (ad-network/publisher/advertiser diagram — behavioral-targeting business model);
  slide022_img014.png (canvas-fingerprinting test report); slide019_img011.png (EFF Cover
  Your Tracks landing — the hands-on exercise); slide038_img022.png (granular social-widget
  blocking toggles — defenses).
- DROPPED: slide002/003 (clip-art / dog cartoon — used the line in text instead);
  slide009/014/021/023/025/026 (low-res screenshots, redundant or hard to read at slide
  scale — e.g., the NHS Syphilis page leakage example overlaps the Referer-leakage code
  block, which teaches it more cleanly); slide033/036/040/041 (dated extension-store and
  DNT-mechanism screenshots — DNT is now narrated as history via the GPC arc);
  slide039 (AdBlock/Ghostery logos — decorative).

## Source
- Rebuilt from _source-extract.md (41 slides) + agenda.md Meeting 5 ("Lecture Coverage:
  Web Privacy and Tracking"). Consolidated to 21 slides (incl. 5 section dividers).
