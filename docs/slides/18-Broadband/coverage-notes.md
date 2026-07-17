# 18-Broadband — instructor notes

## Current-events updates made (point 2)
- **2026-07-16 refresh:**
  - **Lead vignette:** noted that **no federal ACP replacement has passed** as of
    mid-2026, and the **state successor patchwork** now filling the gap:
    **New Mexico LITAP** launched July 1, 2026 (up to $30/mo) and **California
    LifeLine Home Broadband Pilot** launched January 2026 (up to $30/mo). Replaced the
    "restructured in June 2025 / began releasing funds late 2025" wording with the
    current NTIA Progress Dashboard status: **54 of 56 Final Proposals approved and
    52 subgrant agreements signed** by mid-2026, first BEAD-funded household connected
    in Nebraska.
  - **"What counts as broadband":** added a bullet on the **Carr FCC's July 2025
    NPRM** proposing to scrap adoption/affordability metrics from the Section 706
    inquiry and roll back the 1 Gbps long-term goal (decision expected early 2026,
    invoking *Loper Bright*). This connects the deck to the net-neutrality lecture's
    administrative-law throughline.
  - **Policy-stakes slide:** replaced the "26 states added $1.3B in 2025" line (now
    dated) with the mid-2026 NTIA dashboard status and the NM/CA state successors.
  - Sources verified this session: NTIA Progress Dashboard (accessed Jul 2026);
    CRS IF12637; FCC Notice DOC-413059A1 (July 2025); NM LITAP announcement;
    CA LifeLine Home Broadband Pilot launch materials.
- **Lead vignette (verified):** The **Affordable Connectivity Program ended June 1, 2024**
  after Congress declined to refund it — ~$30/mo subsidy, ~23M enrolled households, an
  estimated ~5M lost home internet. Paired with the **$42.45B BEAD** program being
  **restructured June 6, 2025** and only beginning to release funds to states in late
  2025. The demand-side-down / supply-side-still-on-paper contrast is the teaching hook.
  (Sources: FCC ACP fact sheet / CRS IF12637; Sen. Welch & StateScoop on the 23M figure;
  NTIA BEAD Restructuring Policy Notice 6/6/2025; Pew 2026 state-policy analysis on the
  $1.3B / 26 states figure.)
- **"What counts as broadband" slide (verified):** Added the **2024 FCC benchmark increase
  from 25/3 to 100/20 Mbps**, ~22M Americans still lacking 100/20, and the rural (~77%) vs
  urban (~98%) gap. Framed the definition as a policy lever feeding BEAD/USF eligibility.
  (Source: FCC 2024 Section 706 report; Benton "How the FCC Got to 100/20.")
- **Policy-stakes slide:** Added the live affordability-vs-deployment framing and the
  $1.3B / 26-state 2025 figure to make the "measurement drives billions" point concrete.
- Replaced the original deck's undated/implicit framing of M-Lab maps with an explicit
  note that NDT/M-Lab is valuable but has a known single-threaded under-reporting bias
  (kept general; did not invent figures).

## Suggested missing coverage on broad themes (point 3)
- **Net neutrality / Title II whiplash.** The deck never connects broadband quality to the
  regulatory classification fight (FCC reclassified, courts/Congress pushed back). A slide
  on "who has authority to regulate broadband as a consumer-protection matter" would tie
  this lecture to the rest of the course.
- **Satellite / LEO (Starlink) as a divide solution and a measurement headache.** LEO is
  now a real rural option and BEAD's tech-neutrality fight in 2025 centered on it. Worth a
  slide; it also breaks the fixed-line measurement assumptions in this deck.
- **Affordability vs. availability distinction.** The deck measures *performance* well but
  under-covers *adoption* — many homes can buy broadband and don't (cost, digital literacy,
  trust). ACP's end is the perfect case; add an adoption-vs-availability slide.
- **Mobile-only households.** A large share of low-income households are smartphone-only;
  fixed-broadband maps miss them entirely. A sampling-bias angle that complements the
  existing "who runs the test" slide.
- **Algorithmic redlining / digital discrimination.** The 2023 FCC digital-discrimination
  rules and reporting on same-price-worse-service by neighborhood directly extend the
  Hyde Park vs. South Shore slide into a consumer-protection / civil-rights frame.
- **Privacy of in-home sensors — concrete threat model.** The privacy-tradeoff slide is
  qualitative; a short threat model (what metadata reveals: occupancy, app use, household
  size) would land harder and links to the course's surveillance/tracking material.
- **Hands-on element.** Have students run Ookla + an M-Lab/NDT test on their own link and
  reconcile the disagreement — operationalizes Lesson 2 and the sampling discussion.

## Next-year refresh notes

Refresh the dated content below per `../TEMPLATE.md` → "Annual current-events refresh" (web-verify; swap only for something fresher and confirmed). Items placed in prior refreshes that will age:

- **Section 706 outcome** (expected early 2026 → will be settled by 2027 refresh):
  did the Carr FCC formally lower/narrow the benchmark? If yes, update the
  "What counts as broadband" slide with the new rule and the political fight.
- **BEAD construction phase (2026–2030):** by next refresh many states will be
  mid-construction. Swap the "52 subgrant agreements signed" statistic for
  something concrete on delivered service (households connected). NTIA's
  Progress Dashboard is the primary source.
- **Federal ACP successor:** if Congress passes any successor program (partial or
  full), rewrite the affordability half of the vignette. Track: Broadband
  Affordability Act family of bills.
- **State ACP successors:** NM LITAP + CA LifeLine Home Broadband Pilot will have
  adoption data by 2027; several more states (IL, CO, WA, MN) have legislation
  pending — check for launch. NY/CT low-cost-plan mandates are a distinct model
  worth calling out.
- **Starlink / LEO in BEAD:** the tech-neutrality fight remains live; if a state
  awards a substantial share to Starlink, that would be a strong 2027 example.
- Flag any stronger alternative vignette you find but choose not to use yet.

## Curated images
- **Used:** `slide003_img001.png` (speed facets), `slide004_img002.png` (method-vs-method
  CDF), `slide007_img004.png` (Wi-Fi vs access-link bottleneck bubble plot),
  `slide009_img006.png` (page-load plateau ~16 Mbps), `slide025_img030.png` (Hyde Park vs
  South Shore, same 1 Gbps plan — strongest equity figure), `slide018_img020.png` (South
  Shore sampling frame), `slide019_img021.png` (M-Lab/NDT under-reporting),
  `slide028_img032.jpg` (in-line measurement device diagram).
- **Dropped:** logos/clip-art and redundant deployment screenshots
  (slide006/010/012/013/014/015/017/021/022/024/026/029/031/032/033 image sets), the
  Africa-latency map (slide008 — off-theme for a US digital-divide framing), and the
  `.wmf` file (slide019_img022.wmf, not web-renderable; its point is captured by
  slide019_img021.png).

## Source
- Rebuilt from `_source-extract.md` (34 source slides → 21 rebuilt slides incl. dividers).
- `agenda.md` confirms **Topic 12 / Broadband Infrastructure was removed** from the actual
  schedule (Meeting 7 note), so this deck relies on the source extract + domain knowledge
  + verified 2024–2026 current events rather than an as-taught agenda section.
