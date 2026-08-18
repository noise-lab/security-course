# Computer and Network Security Course

Course website and other content for the Computer and Network Security course.

## Contents

- `docs/` - Course website
  - `assignments/` - Course assignments
  - `slides/` - Lecture slides
  - `midterm/` - Old midterms and solutions
  - `final/` - Old finals and solutions
  - `debates/` - Debate topics and resources
  - `notes/` - Course notes
  - `syllabus.md` - Course syllabus
- `archive/` - Older versions of the course
- `hooks/` - Git hooks (activate once per clone: `git config core.hooksPath hooks`)

## Slides

Lecture slides are authored in Quarto (`docs/slides/NN-Name/slides.qmd`); the
rendered `slides.html` files are gitignored build artifacts. Render with
`quarto render` from `docs/slides/` (all decks) or `quarto render
NN-Name/slides.qmd` (one deck). The pre-commit hook re-renders any deck whose
source is part of a commit, and the post-merge hook re-renders decks changed
by a pull, so local HTML never goes stale.
