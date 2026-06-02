# Auto-Grading Harness

Each lab lives in its own folder under `assignments/<slug>/`, containing the
student-facing `README.md` (instructions + up-front rubric) and a `grading-key.md`
used to grade submissions automatically with Claude. Each key encodes the rubric as an
objective, text-checkable checklist that pairs with the `README.md` in the same folder.

## Design contract (what makes a submission auto-gradable)

The assignments are written so that **everything a grader needs is present as text in
the submitted report**:

1. **One report file** per assignment with **fixed, numbered headings** that map 1:1 to
   rubric line items. The grader locates each item by its heading.
2. **Text evidence, not binaries.** Students paste the bytes that matter (HTTP request
   lines, TLS ClientHello/SNI detail, DNS domain tables, OAuth token JSON, accuracy
   numbers). Claude cannot open a `.pcap`, run a server, or call a live API — so the
   gradable evidence must be text. Screenshots are corroboration only; Claude vision can
   read them but they are not required for any point.
3. **Objective criteria.** Every rubric item is phrased so a grader can decide it from
   the report alone ("identifies the SNI in plaintext in the ClientHello"), not "shows
   understanding."

If you write a new assignment, follow this contract or it won't auto-grade reliably.

## AI-resilience (designing for "even if they Claude Code the whole thing")

Students may use AI on these labs — that is course policy. The goal is not to *prevent*
AI use but to design tasks where doing the thinking yourself, with AI as a tool, produces
a visibly better submission than a one-shot prompt. Every assignment includes:

1. **Personal artifacts.** The evidence is the student's own (their capture, account,
   chosen site/platform/dataset). The grader checks that the analysis is *consistent with
   their specific data*, which a generic AI answer won't be.
2. **Verify-and-improve-on-AI.** Students are asked to use an LLM, then catch where it is
   wrong against their own evidence. Caught errors earn full marks; unverifiable
   assertions are penalized even when correct.
3. **Reflection & tinkering (graded).** A required reflection on what they *tried*
   (including dead ends) and what surprised them in *their* run — graded on specificity
   and grounding, not prose. Generic reflection that could describe anyone earns little.
4. **A sophistication stretch (extra credit).** A genuinely deeper hands-on task that
   rewards going beyond the baseline and is self-evidently done or not (e.g., decrypting
   your own TLS with `SSLKEYLOGFILE`).
5. **Defendable live.** Each lab notes that the student may be asked to reproduce or
   explain any part in office hours, a pop quiz, or the exam (per the syllabus).

## How to grade one submission

Give Claude (1) the grader key for the assignment and (2) the student's report, with a
prompt like:

> You are grading a student lab. Use the rubric and checklist in the attached grader
> key. For **each** rubric item, decide whether the submission meets the criterion using
> only the text (and any pasted screenshots) in the report. Output the scoring table
> exactly as specified in the key: one row per item with `points_awarded`,
> `max_points`, and a one-sentence justification that quotes or cites the part of the
> report you relied on. If required evidence is missing, award partial/zero and say what
> was missing. Do not penalize stylistic choices. Sum the total at the end.

### Output format (every key uses this)

```
| Item | Awarded | Max | Justification |
|------|---------|-----|---------------|
| ...  | ...     | ... | ...           |
| **Total** | **X** | **100** | |
```

Followed by a short **Feedback to student** paragraph (2–4 sentences) — this is the
targeted feedback students said they wanted, beyond a bare number.

## Consistency / anti-gaming notes for the grader

- **Reward verification over assertion.** Where a student used an LLM and caught its
  error, that earns full marks; an unverifiable assertion that happens to be right earns
  partial. The keys call this out per item.
- **Don't reward volume.** A correct, cited two-sentence answer beats a page of vague
  prose.
- **Per-student variation is expected.** Students pick different sites/platforms/APIs.
  Grade whether the *analysis* is correct for what they chose, not against a single
  fixed answer. The keys list acceptable answer variants and common errors.

## Keys

- [`pki/grading-key.md`](pki/grading-key.md)
- [`authentication/grading-key.md`](authentication/grading-key.md)
- [`privacy/grading-key.md`](privacy/grading-key.md)
- [`copyright/grading-key.md`](copyright/grading-key.md)
- [`moderation/grading-key.md`](moderation/grading-key.md)
