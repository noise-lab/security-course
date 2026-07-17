# Breakout Discussion Topics

Each lecture in the course has a corresponding file in this directory with **two breakout debate topics**. In class, students split into small groups, spend ~15 minutes on one (or both) of the topics, then report back to the full group.

Topics are designed to be:

- **Debatable** — framed as a motion or contested claim, not a closed-book question.
- **Grounded in current events** — each includes a short "prep reads" list of recent news, reports, or primary sources students can skim before/during the breakout.
- **Refreshable** — flagged so a future skill can identify and update stale links.

Breakouts are the small-group counterpart to the Oxford-style whole-class debates in `../debates/`. Where a debate stakes out one resolution and runs 45–60 minutes for the whole room, a breakout gives each group its own contested motion to argue in 15 minutes and report back.

## File format

Each file starts with the H1 (no YAML frontmatter — GitHub renders that as an ugly table). Metadata lives in a bottom-of-file HTML comment, which is invisible on both GitHub and the rendered site:

```markdown
# <Topic Title>

**Format.** ...instructor framing...

---

## Breakout A: <Sub-topic>
<!-- breakout id="A" status="current" refreshed="YYYY-MM-DD" -->

**Motion.** *"<contested claim>"*

<!-- current-events:start topic="<slug>" -->
**Prep reads (5–10 min).**
- [Title](https://url) — Publisher, Month YYYY
- [Title](https://url) — Publisher, Month YYYY
<!-- current-events:end -->

**Discussion prompts.**
- ...

**Bring back.** <one-line report-back ask>

---

## Breakout B: <Sub-topic>
...

<!--
breakout-metadata:
  lecture: <int>                # lecture number, matches schedule
  class: "<topic title>"        # class topic from schedule
  last_refreshed: YYYY-MM-DD    # date the current-events links were last verified
-->
```

## Markers a refresh skill should recognize

- **`last_refreshed:` inside the bottom `<!-- breakout-metadata: ... -->` comment** — the last time any current-events block in the file was verified. If older than N weeks, the file is a candidate for refresh.
- **`<!-- current-events:start topic="..." -->` / `<!-- current-events:end -->`** — wraps the block of time-sensitive links. Everything between these markers is fair game to rewrite. The `topic` slug hints at what to search for.
- **`<!-- breakout id="A" status="stub|current" refreshed="YYYY-MM-DD" -->`** — per-breakout status. `status="stub"` means the breakout was seeded from the lecture material without a live current-event lookup and should be refreshed before the lecture is taught. `status="current"` means links were verified on `refreshed`.

Content **outside** these markers (motion, discussion prompts, bring-back, instructor notes) is treated as evergreen — the refresh skill should not rewrite it unless the whole breakout is marked `status="stub"`.

## Adding or refreshing topics

The intended workflow (once the `refresh-breakouts` skill exists):

1. Instructor runs `/refresh-breakouts <lecture-number>` a few days before class.
2. Skill reads the corresponding slide deck (`../slides/<NN>-*/coverage-notes.md` and `slides.qmd`) to identify the topic focus and recent vignettes.
3. Skill runs web searches for recent news on those topics.
4. Skill rewrites the `current-events:start`/`end` block with fresh links, updates `last_refreshed`, and flips `status="stub"` to `status="current"` where applicable.
5. Instructor reviews the diff.

## Relationship to other course materials

- **Slide decks (`../slides/NN-*/`)** — the substantive motions and discussion prompts are grounded in what each deck actually teaches, especially the current-events vignettes flagged in `coverage-notes.md`. Refresh those decks first when the news moves; the breakouts follow.
- **Debates (`../debates/`)** — each debate topic maps loosely to a lecture. One breakout motion per file may echo the corresponding debate resolution (so groups get to workshop the framing before the whole-class debate); the other should push a distinct angle.
- **Activities (`../activities/`)** — hands-on exercises for the same lectures. Breakouts are the *discussion* counterpart; activities are the *doing* counterpart. Some lectures pair the two on the same day.
