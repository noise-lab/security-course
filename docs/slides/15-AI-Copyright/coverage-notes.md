# 15-AI-Copyright — instructor notes

## Current-events updates made (point 2)
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

## Curated images
- None. This deck is text-driven; the source has no `images/` folder, and the TEMPLATE
  says to describe a needed diagram in notes/coverage rather than invent one (see the
  data-flow diagram suggestion above).

## Source
- Rebuilt from `15-AI-Copyright/slides.md` (Marp, ~61 slides) + `speaker-notes.md` +
  `agenda.md` (Meeting on Copyright Law and Fair Use, lines ~1158–1264), with current
  events grounded via web search (June 2026). Four-factor mechanics and Google v. Oracle
  are intentionally left to the sibling `14-Copyright` deck to avoid duplication.
