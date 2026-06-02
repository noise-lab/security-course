# Lecture Deck Template Spec

Every lecture deck follows this spec. The canonical worked example is
**`01-Overview/`** — read it before authoring a deck. Goal: a **content-driven
rebuild** in Quarto reveal.js (not a slide-for-slide port of the old pptx).

## Folder layout (one per lecture)

```
NN-Name/
  slides.qmd          # the Quarto reveal.js deck (authored)
  coverage-notes.md   # instructor-facing: current-events updates + missing-coverage suggestions
  images/             # extracted originals; reference the genuinely useful ones
  _source-extract.md  # raw pptx extraction (input only; gitignored)
```

## Quarto setup

- Decks inherit `slides/_quarto.yml` (reveal.js defaults, footer, slide numbers) and
  `slides/theme.scss` (UChicago maroon). **Do not** restate format options already in
  the shared config.
- Per-deck front matter is minimal:
  ```yaml
  ---
  title: "Deck Title"
  subtitle: "Security, Privacy, and Consumer Protection"
  author: "Nick Feamster · University of Chicago"
  date: last-modified
  ---
  ```
- The deck **must `quarto render` cleanly** (`quarto render NN-Name/slides.qmd`).

## Slide conventions

- **Titles in Title Case.** Capitalize principal words; lowercase short articles /
  conjunctions / prepositions (*a, an, the, and, or, for, to, of, in, on, by*); always
  capitalize the first and last word. (e.g., "Why This Course Exists", "Is This Course
  for You?")
- `##` starts a slide; `#` starts a section divider. Use `{.center}` for divider/quote
  slides, `{.smaller}` for dense slides.
- Two-column layout:
  ```
  ::: {.columns}
  ::: {.column width="50%"} ... :::
  ::: {.column width="50%"} ... :::
  :::
  ```
- **Bold key terms** (the theme renders them maroon). Keep bullets tight — a slide is a
  cue, not a paragraph.
- **Current-events vignette box** (use at least one per deck, see point 2):
  ```
  ::: {.vignette}
  A short, dated, real-world hook tied to this lecture's theme.
  :::
  ```
- **Speaker notes inline** on most slides:
  ```
  ::: {.notes}
  What to say / the story / the cold-call. Not shown on the slide.
  :::
  ```

## Images (curate — don't dump)

- Reference only the **genuinely useful** images from `images/`: architecture diagrams,
  attack flows, real screenshots that teach something, data plots.
- **Drop** clip-art, logos, decorative headshots, and redundant screenshots.
- Caption figures with `![Caption](images/file.png)`. For multiple images use the
  columns layout (see `01-Overview` "Where This Can Take You").
- If a deck needs a diagram that doesn't exist, describe it in a `::: {.notes}` block or
  in `coverage-notes.md` rather than inventing a misleading one.

## Content approach (the three asks)

1. **Agenda alignment.** Build from `_source-extract.md` **and** the matching section(s)
   of `../../agenda.md` (the detailed record of what was *actually* covered, by
   Meeting). Prefer what was actually taught over the old slide order. If the deck's
   topic spans part of a Meeting, scope to its theme.
2. **Update examples to current events.** Replace dated examples with current ones
   (today is 2026). **Use web search** to ground at least one fresh, accurate, dated
   example per deck; put the freshest hook in a `.vignette`. Don't fabricate facts —
   verify before stating.
3. **Suggest missing coverage.** In `coverage-notes.md`, list (a) the current-events
   updates you made and (b) concrete suggestions for missing coverage on the lecture's
   broad themes. Keep slides focused; put the meta-commentary in coverage-notes, not on
   slides.

## coverage-notes.md format

```
# NN-Name — instructor notes
## Current-events updates made (point 2)
- ...
## Suggested missing coverage on broad themes (point 3)
- ...
## Curated images
- which images were used / dropped and why
## Source
- rebuilt from _source-extract.md (N slides) + agenda.md Meeting M
```

## Length guidance

Lean. A rebuilt deck is typically **15–30 slides** even if the original had 70–150 —
consolidate, cut redundancy, and keep one idea per slide. The old slide count is not a
target.
