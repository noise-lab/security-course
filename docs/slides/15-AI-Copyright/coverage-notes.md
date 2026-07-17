# 15-AI-Copyright — instructor notes

## Current-events updates made (point 2)
- **2026-07-16 refresh (annual):** Web-verified the vignette against primary sources.
  Updated *Bartz* settlement dating to **Sept 2025** (preliminary approval by Judge Alsup,
  ~500k works, $3k/work, destruction of LibGen/PiLiMi corpora). Added *Kadrey v. Meta*
  (Jun 25, 2025) alongside *Bartz* on the pro-training-fair-use side, with a note about
  Chhabria's "market-dilution" dicta. Added the **NYT 20M-log discovery order** (Jan 5,
  2026, Judge Stein) and the **June 2026 amended complaint** (dedicated-supercomputer
  theory against Microsoft). Added *Andersen v. Stability / Midjourney* (trial set
  **Sept 8, 2026**) and swapped **Getty v. Stability (UK)** for the *US* Getty row — the
  UK High Court **rejected** Getty's copyright claim on Nov 4, 2025 (only a narrow
  trademark win on early-version watermarks). Also noted the **Third Circuit *Ross*
  interlocutory appeal argued June 11, 2026** — first appellate word on AI fair use.
- **Replaced the stale "case ongoing as of late 2024" framing** with the actual 2025–26
  ruling landscape. The old Marp deck predated every major decision.
- **Vignette hook (verified, dated):** the law is now *splitting*:
  - *Thomson Reuters v. Ross Intelligence* (D. Del., **Feb 11, 2025**): training a legal-
    research AI on Westlaw headnotes was **not** fair use — first federal ruling rejecting
    the defense for AI training (commercial, directly competing tool).
  - *Bartz v. Anthropic* (N.D. Cal., **Jun 23, 2025**): training on books "exceedingly
    transformative" / fair use, but pirating 7M+ books to build a library was **not**;
    Anthropic later settled for **~$1.5B** (~$3,000/work).
  - *Kadrey v. Meta*: Meta won a parallel training fair-use ruling (**Jun 2025**).
  - *NYT v. OpenAI*: survived dismissal (**Mar 2025**, Judge Stein); as of early 2026 the
    fight centers on **"regurgitation"/memorization** and market substitution.
- **Added the ownership half of the title:** U.S. Copyright Office report (**Jan 29,
  2025**) — purely AI-generated output is not copyrightable; prompts alone don't confer
  authorship; human selection/arrangement/modification can be protected; existing law
  deemed "adequate."
- **Added the 2026 doctrinal shift** (Norton Rose Fulbright / Bochner summaries): courts
  increasingly require plaintiffs to show a **specific output is substantially similar** —
  moving the battleground from *input* (training) to *output*.
- **Trimmed from 61 Marp slides to a lean ~17-slide Quarto deck**, consolidating redundant
  argument/policy/prediction slides and deferring the four-factor *mechanics* + Google v.
  Oracle to the prior 14-Copyright deck (which already teaches them in depth).

## Suggested missing coverage on broad themes (point 3)
- **Liability for infringing outputs.** Who infringes when a model emits protected
  content — the prompting user, the provider, or both (contributory/vicarious)? The deck
  flags it; a dedicated slide or short reading would help, as it is the live next frontier.
- **GitHub Copilot / code generation** (Doe v. GitHub). The course emphasizes software-as-
  expression; a code-specific fair-use angle (and the DMCA §1202 attribution-removal
  theory) connects directly to the CS audience and to Oracle.
- **The piracy-acquisition vs. fair-use-training distinction** could be its own beat —
  Anthropic's split turned on it, and it generalizes (lawful acquisition is a precondition,
  not a fair-use factor). Worth a concrete walk-through.
- **Creator-side technical defenses:** Glaze and Nightshade (UChicago projects) and the
  "Have I Been Trained?" opt-out database — strong local hook, currently only in notes.
- **EU AI Act training-data transparency in practice:** what a "sufficiently detailed
  summary" of training data actually requires once obligations bite — ties this deck to
  the Compliance and Privacy-Law decks.
- **Output substantial-similarity standard:** as litigation shifts to outputs, students
  should see how courts test "substantial similarity" (a different doctrine from fair use).
- **Suggested diagram (none exists; text-driven deck):** a data-flow figure —
  *works → copy into training pipeline → model weights → output → (possible) memorized
  reproduction* — with the infringement-exposure point marked at each arrow.

## Next-year refresh notes

Refresh the dated content below per `../TEMPLATE.md` → "Annual current-events refresh" (web-verify; swap only for something fresher and confirmed). Items placed in prior refreshes that will age:

- **Third Circuit *Ross* appeal** — decision may drop in the 2026–27 cycle; if it does,
  it becomes the freshest single hook and demotes the current district-court split.
- **NYT v. OpenAI trial or settlement** — no trial date as of mid-2026; watch the SDNY
  MDL docket and Third Circuit outcomes for a settlement trigger.
- **Andersen trial** — set Sept 8, 2026; either verdict or settlement will land before
  the next refresh and change the "images" row of the lawsuit table.
- ***Bartz* settlement finalization** — preliminary approval Sept 2025; final approval
  hearing pending. Confirm class-notice numbers, then restate "$1.5B" only if final.
- **UK Government copyright/AI report** — due March 2026; check whether a TDM exception
  with opt-out has been proposed and update the "International Approaches" table row.
- **Anthropic music-publishers piracy claims** — court denied late amendment; watch for
  a new complaint or settlement that would parallel Bartz.
- Replaced the stale "case ongoing as of late 2024" framing
- Vignette hook (verified, dated)
- Added the ownership half of the title
- Added the 2026 doctrinal shift
- Trimmed from 61 Marp slides to a lean ~17-slide Quarto deck
- Flag any stronger alternative vignette you find but choose not to use yet.

## Curated images
- None. This deck is text-driven; the source has no `images/` folder, and the TEMPLATE
  says to describe a needed diagram in notes/coverage rather than invent one (see the
  data-flow diagram suggestion above).

## Source
- Rebuilt from `15-AI-Copyright/slides.md` (Marp, ~61 slides) + `speaker-notes.md` +
  `agenda.md` (Meeting on Copyright Law and Fair Use, lines ~1158–1264), with current
  events grounded via web search (June 2026). Four-factor mechanics and Google v. Oracle
  are intentionally left to the sibling `14-Copyright` deck to avoid duplication.

## Additional context (preserved from prior long-form speaker-notes)

Content preserved from the old long-form `speaker-notes.md` that doesn't fit neatly in
table rows but is useful as instructor background. Anything already surfaced on the deck
(vignette dates, four-factor breakdown, case one-liners) has been dropped as duplicative.

### Evocative quotations
- **Jonathan Franzen on AI training:** "It's a washing machine that washes together all
  the texts and reduces them to a few archetypal narratives, and spits out a narrative on
  command. It's against the whole spirit of writing and reading." Useful cold-call
  opener for the human-learning-analogy slide.

### Deeper case-study background
- **Music publishers v. Anthropic** (Concord/Universal/ABKCO, Oct 2023): 500+ song
  lyrics identified, including *Sweet Caroline*, *American Pie*, *Gimme Shelter*.
  Anthropic later implemented filters; separate from *Bartz*. In late 2025 the music
  publishers tried to add piracy claims after the *Bartz* settlement — the court
  **denied** the amendment as unfairly late.
- **GitHub Copilot / Doe v. GitHub** (Nov 2022): Programmers sued Microsoft/GitHub/
  OpenAI over training Copilot on public repos with restrictive licenses; DMCA §1202
  (attribution-removal) is the more novel theory. Litigation site:
  <https://githubcopilotlitigation.com/>.
- **Sarah Silverman v. OpenAI/Meta** (Jul 2023): ChatGPT could summarize her memoir
  *The Bedwetter*. Case merged into *Kadrey v. Meta* on the Meta side and into the
  consolidated OpenAI author actions.

### Reading list for students / instructor prep
- **Pamela Samuelson, *Generative AI Meets Copyright*** (2023) — comprehensive legal
  analysis, four-factor test applied to training.
- **Mark Lemley & Bryan Casey, *Fair Learning*** (Tex. L. Rev., 2021) — argues AI
  training is fair use under the intermediate-copying doctrine.
- **Matthew Sag, *Copyright Safety for Generative AI*** (Houston L. Rev., 2023) —
  memorization risk and mitigation strategies.
- **Stanford Law School, *Generative AI Has an Intellectual Property Problem*** (2023) —
  short accessible framing piece.

### Instructor policy landing pages (evergreen)
- U.S. Copyright Office AI reports and registrations page:
  <https://www.copyright.gov/ai/>
- EU AI Act consolidated resource: <https://artificialintelligenceact.eu/>
- UK IPO copyright/AI consultations landing:
  <https://www.gov.uk/government/consultations/copyright-and-artificial-intelligence>

### Common student questions (worth pre-answering)
- *"If I make an AI image, do I own the copyright?"* — U.S. Copyright Office: no
  automatic copyright for the raw output (no human authorship). Your creative
  additions/selection/arrangement may be protected as your contribution.
- *"Why don't AI companies just use public domain?"* — Insufficient volume + quality;
  most post-1928 material is copyrighted. Trade-off, not a technical impossibility.
- *"Can I detect AI-generated text?"* — Detectors exist (GPTZero, etc.) but are
  imperfect (false positives and negatives) and get worse as models improve.

### Timing
- 75-minute class: the rebuilt ~17-slide Quarto deck runs comfortably in the slot
  (roughly 3-min opening + 10 min vignette/setup + 15 min lawsuits/memorization +
  10 min fair-use factors + 10 min policy/international + 12 min for the pair-share
  activity + 15 min buffer for questions and cold-calls).
