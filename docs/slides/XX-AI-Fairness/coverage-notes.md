# XX-AI-Fairness — instructor notes

## Current-events updates made (point 2)
- **Mobley v. Workday** (vignette, "AI Hiring on Trial"): in **Feb 2026** a CA federal
  court authorized class notice for applicants alleging Workday's AI screening filtered
  them out by age/race/disability, treating the **vendor as the employer's "agent."**
  Used as a live, verifiable disparate-impact hook. (Case is ongoing — slide is careful
  not to assert an outcome.)
- **California ADS regulations** (effective **Oct 2025**) bringing automated decision
  systems under FEHA anti-discrimination law — cited alongside Mobley.
- **EU AI Act high-risk obligations** (vignette, "Regulation Is Catching Up): effective
  **Aug 2, 2026**, covering employment/credit/biometrics and requiring examination of
  training data for bias where technically feasible. Connects the math (impossibility)
  to the law (mandated auditing).
- Replaced the original deck's undated/implicit framing with these dated examples; kept
  the COMPAS case study (2016 ProPublica) as the historical anchor but reframed it as a
  values dispute resolved by the impossibility theorem.

## Suggested missing coverage on broad themes (point 3)
- **State the impossibility theorem with attribution** in a reading: Kleinberg,
  Mullainathan & Raghavan (2016) and Chouldechova (2017). The slides assert it; a
  problem set deriving the 2x2 confusion-matrix tradeoff would cement it.
- **Generative-AI / LLM fairness** is only gestured at. Worth a dedicated treatment:
  representational harms in image generation, stereotype amplification, and allocational
  harms in LLM-driven hiring/ranking — ties directly to the AI privacy and copyright
  lectures.
- **Mitigation techniques** are thin. The deck diagnoses bias but says little about
  pre-processing (reweighting/resampling), in-processing (fairness constraints), and
  post-processing (threshold adjustment per group) — and their legal friction (per-group
  thresholds can themselves be "disparate treatment").
- **Disparate impact vs. disparate treatment** as a legal doctrine deserves its own
  slide; the 80% (four-fifths) rule from EEOC guidance is a concrete, examinable hook
  and pairs with the Workday case.
- **Feedback loops / strategic behavior**: only one slide. Could expand with the
  predictive-policing literature (Lum & Isaac) and performative prediction.
- **Individual fairness in practice**: the similarity-metric problem could use a worked
  example showing how metric choice reintroduces bias.
- **Cross-link to other decks**: explicitly route the AI Accountability debate, the
  privacy-law/compliance lecture (auditing/enforcement), and the dark-patterns material
  (who bears the burden of contesting an automated decision).

## Curated images
- **Used:** `slide004_img001.png` (should-be → is → data bias-flow diagram — the spine of
  the lecture); `slide005_img002.png` (Google Translate Turkish→English gendered-pronoun
  example); `slide006_img003.png` + `slide006_img004.png` (Black vs. White COMPAS decile
  histograms — strong visual contrast); `slide007_img005.png` (recidivism logistic-
  regression coefficient table); `slide008_img006.png` (per-group error-rate table for
  commercial face classifiers, Gender Shades lineage).
- **Dropped:** none — all six extracted images teach something (diagram, real screenshot,
  two data plots, two coefficient/metric tables). No clip-art or decorative logos were
  present.

## Source
- Rebuilt from `_source-extract.md` (12 slides) + `agenda.md` (AI Accountability debate
  + automated-decision/disparate-impact themes around Meeting 8 / privacy-compliance
  block). Consolidated and resequenced into 18 slides emphasizing the impossibility
  result and current enforcement.
