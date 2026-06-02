# 18-Broadband — instructor notes

## Current-events updates made (point 2)
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
