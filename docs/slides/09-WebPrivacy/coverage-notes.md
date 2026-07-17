# 09-WebPrivacy — instructor notes

## Current-events updates made (point 2)
- **2026-07-16 refresh.** Tightened the Chrome-cookie vignette to specify the
  Oct 17, 2025 Privacy Sandbox shutdown (Topics, Protected Audience, Attribution
  Reporting, IP Protection, Related Website Sets) and note no removal timeline
  ~1 year in. Expanded the GPC vignette to the current 12-state UOOM landscape
  (CA, CO, CT, DE, MD, MN, MT, NE, NH, NJ, OR, TX) and added California's
  **AB 566 "Opt Me Out" Act** (effective Jan 1, 2027) forcing browsers to ship
  a GPC control. Rewrote the CJEU vignette to correctly cite **Fashion ID
  (C-40/17, 2019)** as the actual Like-button joint-controllership holding and
  **Meta v. Bundeskartellamt (C-252/21, 2023)** as the follow-on on legal
  bases; Bundeskartellamt closed its Meta case in Oct 2024 on that footing.
  Updated the Manifest V3 speaker note: Chrome permanently disabled MV2 in
  July 2025 (Chrome 138); last flag workarounds removed by Chrome 151
  (July 2026); users get uBlock Origin Lite (declarativeNetRequest, static
  rules), Firefox, or Brave. Verified via Google Privacy Sandbox blog,
  CPPA/OAG.CA.GOV, IAPP, Ofcom, and PCWorld/AdBlock Tester.
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

## Next-year refresh notes

Refresh the dated content below per `../TEMPLATE.md` → "Annual current-events refresh" (web-verify; swap only for something fresher and confirmed). Items placed in prior refreshes that will age:

- **Google Chrome cookie status.** Watch for any resumption of a phase-out plan, adoption of CHIPS/FedCM/Private State Tokens, or a new EC/UK CMA intervention on Chrome defaults. The "12 states" list will grow; refresh with the current count before Fall term.
- **AB 566 "Opt Me Out" Act.** Takes effect **Jan 1, 2027**; by next refresh Chrome/Safari/Edge should have shipped a GPC control — verify shipment and coverage.
- **Manifest V3 endgame.** Chrome 151 (July 2026) removes the last MV2 flags; by mid-2027 look for measurement studies on actual tracker-blocking effectiveness in Chrome-with-uBOL vs. Firefox-with-uBO (a PoPETs 2026 paper already exists).
- **CJEU Fashion ID / Meta v Bundeskartellamt.** Stable historical anchors; refresh only if a newer CJEU ruling supersedes them (watch Meta pay-or-consent / DMA outcomes).
- **Any smarter fresh vignette encountered but not used** — flag here rather than mid-slide.

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
