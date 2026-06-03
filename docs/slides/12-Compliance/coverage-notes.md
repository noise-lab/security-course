# 12-Compliance — instructor notes

## Current-events updates made (point 2)
- Added a 2026 enforcement vignette grounding the deck in real, dated cases (verified via web search):
  - **Feb 11, 2026** — California AG Rob Bonta announced a **$2.75M** CCPA settlement with **Disney** for failing to honor opt-out signals.
  - **May 8, 2026** — record **$12.75M** settlement with **General Motors** (largest CCPA penalty to date) for selling drivers' location/behavior data to LexisNexis and Verisk without adequate notice/consent; first CCPA action centered on data minimization + purpose limitation. Subject to court approval; GM also agreed to stop selling driving data to consumer reporting agencies for 5 years and delete retained data within 180 days absent express consent.
  - Noted the earlier settlement line (Sephora, DoorDash, Sling TV, Healthline) targeting opt-out/GPC functionality.
  - Sources:
    - https://www.troutmanprivacy.com/2026/02/california-ag-announces-largest-ccpa-enforcement-settlement-to-date/
    - https://oag.ca.gov/news/press-releases/when-it-comes-data-privacy-consumers-must-be-driver%E2%80%99s-seat-attorney-general
    - https://www.whitecase.com/insight-alert/california-announces-landmark-us-1275-million-ccpa-settlement-general-motors-largest
    - https://iapp.org/news/a/california-authorities-announce-largest-ccpa-fine-to-date
- The vignette's "regulators care about practice not paperwork / paper compliance" framing is sourced from the IAPP / Buchanan analyses and directly motivates both studies (functional opt-out, GPC honoring).
- Tightened the GPC slide to reflect that enforcement is now actively targeting universal opt-out signals, not just static links.

## Suggested missing coverage on broad themes (point 3)
- **The federal landscape.** The original deck is California-only. Add a slide on the multiplying state laws (now ~20 states post-2023) and the de facto national floor this creates — ties directly to the RQ3 spillover finding and the "do we need a federal privacy law?" debate.
- **GDPR contrast.** Students see CCPA's opt-out model; a one-slide contrast with GDPR's opt-in/consent model (and "legitimate interest") would sharpen the opt-in vs. opt-out distinction already in the agenda.
- **Universal Opt-Out Mechanisms (UOOMs) beyond GPC.** Several state laws now *mandate* honoring opt-out preference signals (e.g., Colorado, with required recognition deadlines). Worth distinguishing GPC-the-spec from the legal obligation to honor it.
- **Data minimization & purpose limitation.** The 2026 GM case is the first CCPA action on these — a theme the original deck (focused on opt-out links) does not cover at all. Good hook for an "what's next in enforcement" slide.
- **Methodology limits / measurement ethics.** Study 2 submits real opt-out requests with synthetic identities; briefly discussing the research-ethics and IRB dimension of large-scale "mystery shopper" compliance studies would reinforce the course's ethics thread.
- **OneTrust / consent-management platforms (CMPs).** The third-party-vendor irony deserves its own deeper treatment: how CMPs work, why deploying one doesn't equal compliance, and the IAB TCF analogue in the EU.
- **Litigation update.** As of the original talk there was "no litigation on privacy-opt-out dark patterns." The 2026 settlements partially change this; revisit whether any case has squarely litigated a *dark pattern* (vs. failure to honor GPC).

## Next-year refresh notes

Refresh the dated content below per `../TEMPLATE.md` → "Annual current-events refresh" (web-verify; swap only for something fresher and confirmed). Items placed in prior refreshes that will age:

- Feb 11, 2026
- May 8, 2026
- Flag any stronger alternative vignette you find but choose not to use yet.

## Curated images
- Used: `slide017_img023.png` (RQ1 stacked-bar trend), `slide022_img025.png` (RQ3 state-overlap table), `slide026_img028.png` (RQ4 coverage-category table), `slide057_img037.png` (CAPTCHA obstruction screenshot — strong teaching example), `slide062_img043.png` (dark-pattern → CCPA-principle mapping table). All are data plots / real screenshots that teach.
- Dropped: title/logo images (slide001/031 author+logo), decorative data-flow art (slide002 ~1.6MB clip-art), tiny icon/badge PNGs (slide003/006/009/010/012/019/024 — pipeline icons and repeated state-map glyphs), verification-detail screenshots (slide014), and the control-method / personal-info screenshots (slide041/054) — redundant with the consolidated text. slide048 ("Please try that again") is a generic error toast that doesn't stand alone.

## Source
- Rebuilt from `_source-extract.md` (70 slides, two papers: CCPA compliance measurement + dark-patterns-in-opt-out) + `agenda.md` "Automated Compliance Enforcement with Privacy Laws" (Meeting on privacy law/compliance). Consolidated 70 → 25 slides; dropped repeated "Research Questions"/"Outline" interstitials and slide-by-slide outcome breakdowns.
