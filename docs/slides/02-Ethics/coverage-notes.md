# 02-Ethics — instructor notes

## Current-events updates made (point 2)
- **New primary vignette: University of Zurich AI bots on Reddit r/changemyview
  (April 2025).** Replaces Emotional Contagion as the *freshest* hook. ~1,700
  AI-generated comments under fabricated personas, four months, no consent, no
  community approval; Reddit sent formal legal demands and the team agreed not to
  publish. Maps cleanly onto all four principles. Verified against Washington Post
  (2025-04-30), NBC News, and Engadget reporting. Emotional Contagion is kept as a
  supporting case study and explicitly framed as the 2012 precursor to the 2025 case.
- **Added a "The Law Is (Slowly) Catching Up" slide** with two verified rulings that
  postdate the original deck: **Van Buren v. United States (2021)** (SCOTUS narrowed
  CFAA's "exceeds authorized access") and **hiQ v. LinkedIn (2022)** (9th Cir.:
  scraping public web data generally falls outside the CFAA). Also notes the renewable
  **DMCA §1201 security-research exemption**. These directly update the old
  "scraping = jail" framing while preserving the point that legal ≠ ethical.
- Kept the historical anchors (Tuskegee, Belmont 1979, Menlo 2012) since they are the
  load-bearing lineage, not dated examples to be swapped out.

## Suggested missing coverage on broad themes (point 3)
- **Coordinated vulnerability disclosure (CVD) / bug-bounty ethics** — the everyday
  version of these dilemmas (disclosure timelines, safe-harbor language, ISO/IEC 29147).
  The deck covers law and abstract principles but not the practical disclosure workflow.
- **IRB exemption categories and the "is this even human-subjects research?" question** —
  much security/measurement work (scanning, public-data scraping) is arguably exempt or
  out of scope. Students should know how that determination is actually made, and the
  risk of using "it's exempt" as an ethics off-ramp.
- **Data ethics specifics:** de-identification failure modes (Sweeney, Netflix Prize,
  Strava heatmap), k-anonymity vs. differential privacy as risk-mitigation tools, and
  data-retention/destruction plans. The deck names "informational risk" but offers no
  concrete mitigations.
- **AI-specific research ethics** beyond the Reddit vignette: training-data consent and
  copyright, model/dataset documentation (model cards, datasheets), red-teaming ethics,
  and whether LLM "subjects" or LLM-generated personas count as deception.
- **Dual-use / offensive research** — when publishing an attack is itself the ethical
  question (exploit release, ML model weights, the "active response continuum" mentioned
  only in the original appendix).
- **International dimension:** GDPR Art. 89 research provisions and how non-U.S. IRB/ethics
  regimes differ — relevant since the headline 2025 case was a *European* university.
- **Worked Belmont/Menlo application** as a reusable rubric students can apply to their
  own lab and debate proposals, not just to historical cases.

## Next-year refresh notes

Refresh the dated content below per `../TEMPLATE.md` → "Annual current-events refresh" (web-verify; swap only for something fresher and confirmed). Items placed in prior refreshes that will age:

- Added a "The Law Is (Slowly) Catching Up" slide
- Flag any stronger alternative vignette you find but choose not to use yet.

## Curated images
- **Used:** `slide002_img001.png` (Tuskegee photo — historical anchor);
  `slide011_img013.png` (Salganik frameworks→principles→rules diagram — the spine of the
  lecture; the four identical copies on slides 19/23/29 were dropped as duplicates);
  `slide032_img017.png` (Menlo Report cover — useful artifact on the Law/Public-Interest
  slide).
- **Dropped:** decorative/screenshot-only images on slides 4–7, 35–39 (news-clipping
  screenshots of Hypocrite Commits, Carna, GDPR-email "scam," CFAA/DMCA op-eds). Their
  content is captured as text bullets and is more legible that way; the screenshots are
  low-resolution and not self-explanatory on a slide. The Carna and Hypocrite Commits
  cases are retained as text in the "Why This Hits Close to Home" and breakout slides.

## Source
- Rebuilt from `_source-extract.md` (43 original slides → 22 rebuilt slides) +
  `agenda.md` (no dedicated Meeting-2 ethics section; informed-consent/respect-for-persons
  threads at lines ~1097–1102 and the CFAA debate at line 438 confirm the framing and
  cross-references used here). Relied on source + domain knowledge for the bulk, grounded
  current events via web search.
