---
description: Generate the midterm exam for Security, Privacy, and Consumer Protection from the term's agenda file and past midterms
---

You are helping create the midterm for *Security, Privacy, and Consumer
Protection* (CMSC 23206 / 30350). Students may run this prompt to generate
practice exams; the instructor runs it to draft the real one. The recipe is the
same either way: the **agenda file decides what is in scope**, the **past exams
decide how it looks**, and nothing is asked that was not taught.

## Parameters (ask if not given)

| Parameter | Value |
|---|---|
| Exam | `midterm`, given in class in week 6 |
| Agenda | `docs/agenda/<year>-<term>.md` (index at `docs/agenda.md`), the meetings the agenda says the midterm covers; by default Meetings 1–5 |
| Past exams | `docs/midterm/<YYYY>/`, the two or three most recent (each has `questions.tex`, `instructions.tex`, `exam.tex`, `feamster.sty`, a `Makefile`, and any diagram PNGs). From 2026 on, each also carries `rubric.yaml` (how it was scored), `grading-notes.md` (decisions made while giving it), and `analysis.md` (where the class split from the key): read those three first, and do not reuse a question they mark as ambiguous |
| Length | **6 pages, 85 points**, written for about an hour; students may take the whole period. Ends with a 2-point feedback section |
| Must include | at least one question on each lab assignment due in the range (Assignment 1, PKI, is always in range); every bullet the agenda marks **Midterm flag**; at least two diagram-based questions |
| Instructor output | `/Users/feamster/Dropbox/Tmp/exams/security-course/midterm/<YYYY>/`, cloud-backed and outside the public repository. **Never commit an exam before it has been given.** Afterwards, when the instructor says so, it is committed to `docs/midterm/<YYYY>/` with solutions as practice material, together with `rubric.yaml`, `grading-notes.md`, and `analysis.md` from the grading directory in instructor-data (never the scores, details, review pages, or return manifest) |
| Student output | any directory of your own; nothing here is secret |

## What the exam must do

1. **Cover the agenda, in proportion to time spent, and nothing else.** The agenda
   file is the record of what was actually taught. Read every meeting in the range
   end to end before writing a question. The topic lists in older versions of this
   prompt and in past exams are *not* the scope: a topic that was taught in a past
   year but not this year is out.
2. **Honor every exclusion.** Anything the agenda marks "will not be asked", "not
   on the exam", "not covered", "not reached", or "skipped" is out of scope even
   if a past exam asked about it. So is anything a later meeting in the range says
   will not be on the midterm. Debates are not recorded but may be asked about by
   resolution and the arguments the agenda records.
3. **Cover every Midterm flag.** When the agenda says "this would be a good midterm
   question" or carries a **Midterm flag**, write a question that tests exactly
   that, in the form the flag suggests (yes/no with explanation, identify the
   roles, mark the diagram, give the threat model). The flags are the raw material;
   the rest of the exam fills in proportionally. One question may cover several
   related flags (a select-all over definitions, a table of systems).
4. **Use the examples from class.** The agenda records the demos, analogies,
   numbers, and cases the instructor used (the IDScan breach, the campus firewall,
   Mirai and Dyn, Pakistan and YouTube, the muffin page, Cover Your Tracks). Build
   scenarios from those, or from close variants, so a student who was in the room
   recognizes them.
5. **Ask about the assignments** as the student experienced them: what they
   captured, built, or observed, and what it showed. Never require code; the
   agenda says pseudocode or plain English is fine.
6. **Do not repeat past exams.** Read the past `questions.tex` files and avoid
   their questions, including re-wordings. The same concept may recur (it is on
   the agenda every year) but the question must be new: a different scenario, a
   different form, a different angle.
7. **Test understanding, not recall, and do not trick.** A good question gives a
   situation and asks the student to apply something taught; a bad one asks for a
   number or a name from a single sentence. Yes/no questions always ask "Why or
   why not?" for the real points.
8. **Fit exactly:** 6 pages (printed double-sided and stapled), 85 points, a mix of question types in
   roughly the past exams' proportions (about a third multiple choice, a third
   short answer, the rest yes/no-with-explanation and diagrams), sections in the
   order the material was taught. **No question may split across a page:** a
   multiple-choice list stays with its stem, a yes/no stays with its explanation
   box, every sub-part box stays with the question, and a figure stays with its
   text. Put `\Needspace` before any `\prob` that could straddle a break and
   before every section heading. Better, and what the 2026 exam does: wrap every
   `\prob` … `\eprob` in `\par\noindent\begin{minipage}{\linewidth}` …
   `\end{minipage}\par`, and put each section heading inside the minipage of
   its first question (with `\vspace{1.2ex}` before the minipage instead of the
   negative `\vspace*`). A minipage cannot break, so no question can straddle a
   page and no heading can be orphaned, and no `\Needspace` guessing is needed.
   Check the rendered PDF page by page anyway.

## Steps

1. Read the agenda for the meeting range. List, per meeting: the concepts taught,
   the examples used, every Midterm flag, and every exclusion.
2. Read the past exams for form only: LaTeX conventions, point values, section
   style, how diagrams are used, the feedback section (headed **Course Feedback**,
   so students know it is about the course, not the exam).
3. Draft the question list against the agenda list: every flag covered, every
   assignment covered, proportions by time spent, nothing excluded, nothing
   duplicated from a past exam. Decide which two or more questions are
   diagram-based and what the diagrams show.
4. Write `questions.tex` with solutions, `instructions.tex`, `exam.tex`, the
   diagrams, and a `README.md` that lists the sections, the points per section, and
   which flags each question covers. Copy `feamster.sty` and the `Makefile` from the
   most recent past midterm.
5. Build both versions, validate (below), fix, rebuild until the page count and
   point total are exact.

## LaTeX conventions (from `feamster.sty`)

- `\prob{N}` … `\eprob` wraps a question worth N points. **Do not use `\prob{}` for
  the name box in `instructions.tex`**; it would add a phantom point. The name box
  is `\shortanswerbox{4.0}{Nick Feamster}`, labeled inline ("Write your full name
  here to acknowledge these instructions:"), and the first `\prob` is question 1.
  Keep the front matter to one short paragraph (points, bubbles, permitted
  materials) plus the name line: it costs a third of a page otherwise.
- Multiple choice: `\correctanswercircle{text}` for correct options,
  `\answercircle{text}` for the others; say "(Select all that apply.)" or "(Select
  the best answer.)" in the stem. Keep options to one line each.
- **Randomize where the correct answers sit.** The key must not be readable
  from the layout. In every multiple-choice question put the correct options at
  random positions: in a two-column grid spread them across both columns and
  different rows, never all in the left column or the top rows; in a
  single-column list, not always first. Across the exam, correct options should
  land about evenly in every position and column, consecutive single-answer
  questions should not share the key's position, and select-all questions should
  vary in how many options are correct. Balance yes/no keys too: use both
  `\yesnoyes` and `\yesnono`, in no fixed pattern. Before finishing, write out
  the whole key (for example "Q1: B, C, F; Q5: no; Q9: D") and fix any pattern
  you can see in it.
- **Show the answer key as a table before the exam is final**, for the
  instructor to look over, one row per question with an answer to check:

  | Question | Type | Correct answer(s) |
  |---|---|---|
  | Q3 | single answer | 2 of 5 |
  | Q5 | select all | 1, 2, 4 of 5 |
  | Q8 | yes/no | no |

  Give positions as they appear on the page (count across the row, then down,
  in a two-column grid). Note under the table any pattern still visible, such
  as two single-answer keys in the same position, so the instructor can decide.
- Yes/no: **one question, not two.** `\yesnoyes` or `\yesnono` at the end of the
  statement, then `\ Explain why or why not.` in the same `\prob`, then the
  `\answerbox`. Never a separate numbered "Explain why or why not" item. State
  the yes/no claim positively (no "can no longer", no double negatives).
- Multi-part questions: when a question asks for two or more distinct things
  (an argument against and one for; what leaks and what the trust-store step
  does; the attack and its defense), label the parts (a), (b) in the stem and
  give **each part its own box, with that part's instruction written next to
  (or directly above) its box**, not folded into the stem. Short parts get small
  labeled boxes, side by side where they fit. A question asking for N named items (asset, property,
  adversary, capability; subject, verb, object; the three roots of trust) gets a
  grid of labeled small boxes rather than one large box. Define this at the top
  of `questions.tex` and use it for all of them:

  ```latex
  \newcommand{\gridbox}[3]{% raw %}{%{% endraw %}
    \ifthenelse{\equal{\version}{solution}}{% raw %}{%{% endraw %}
      \tikz[baseline=(x.base)]\draw (0,0) rectangle node (x) [text width=\dimexpr#1-6pt\relax, align=left] {\scriptsize #3} (#1, #2);%
    }{% raw %}{%{% endraw %}
      \tikz[baseline=(x.base)]\draw (0,0) rectangle node (x) {\vphantom{Aq}} (#1, #2);%
    }}
  % \gridbox{width}{height}{solution}, e.g. \gridbox{6cm}{1.2cm}{integrity}, in a tabular with the labels
  ```
- "Identify the role" questions (OAuth parties, protocol participants): make
  them **matching**. Name the roles in the stem, letter the parties in the
  diagram, and give a small box per role for the letter. Do not ask students to
  write a role name into a box next to a letter; the term "role" alone is not
  self-explanatory on an exam.
- A box asks for what it can hold. "Name three" needs a box three lines tall;
  if the page budget allows only one or two lines, ask for two.
- Short answer: `\answerbox{height}{solution}`; the height unit is 1.5 cm, and
  0.8–1.1 is the range that fits six pages (1.0 holds about three lines of
  `\small` text, roughly 380 characters at full width). Start the solution with
  `\small`, keep it to one paragraph with no `&`, and put a blank line before the
  box. Very short answers: `\shortanswerbox{width}{text}`. Once the exam fits
  six pages, **grow the boxes until every page is full**: render at 72 dpi,
  measure the free space above the footer on each page, and add it to that
  page's boxes (a box unit is 0.59 in). Students never complain that a box is
  too big.
- Diagrams: place the figure beside its question text in two `[t]` minipages
  (about `0.40` and `0.57\linewidth`, each starting with `\vspace{0pt}`), with
  `\par\noindent` right after `\prob{N}` so the pair starts on its own line; a
  full-width figure under its stem costs a third of a page. The question's
  minipage (above) keeps the figure with its text. Draw labels large enough to
  print at 8 pt or more once the figure is 4 in wide (with matplotlib, shrink the
  canvas rather than the data coordinates; `SCALE = 0.55` and label `fontsize`
  8.5–10 worked in 2026). Any box the student writes in inside a figure must be
  at least two handwriting lines tall and as wide as the figure allows; if the
  figure needs more room for it, extend the canvas rather than shrinking the box.
  Ask for the shortest possible mark in a figure box: a letter (R/A), a number, a
  circled hop, not a sentence. Select the solution variant
  by the version switch:
  ```latex
  \ifthenelse{\equal{\version}{solution}}{% raw %}{%{% endraw %}
  \includegraphics[width=\linewidth]{name-solution.png}%
  }{% raw %}{%{% endraw %}
  \includegraphics[width=\linewidth]{name.png}%
  }
  ```
  Draw the student version with the thing to be labelled left blank, and the
  solution version with it filled in. A figure from the lecture deck
  (`docs/slides/<deck>/images/`) is a good base. Negative `\vspace*` before a figure
  saves space.
{% raw %}- Case studies: a `\framebox[0.9\linewidth]{\parbox{0.8\linewidth}{{\bf Case{% endraw %}
  Study:} …}}` block, centered, followed by two or three questions that apply named
  ethical principles or threat-model elements to it.
- Sections: `\section*{Name}` preceded by `\vspace*{-0.1in}`; never `\newpage`.
  `exam.tex` tightens the spacing globally with
  `\titlespacing*{\section}{0pt}{1.2ex}{0.3ex}` and
  `\setlist[itemize]{topsep=1pt,partopsep=0pt,parsep=0pt}` after loading the
  style file; the heading goes inside the first question's minipage (above).
- Points: multiple choice 3–4; short answer 3–4; yes/no with its explanation
  3–4 as a single question; diagram 3–4; feedback 1 + 1.
- `exam.tex` sets `\term` and uses `\usepackage[]{feamster}`; the Makefile builds
  the solution by substituting `[solution]` (`make exam`, `make solution`, `make
  all`, `make clean`). Margins are 0.5 in.

## Permitted materials (required, verbatim, in `instructions.tex`)

The policy is set in advance and is the same on every exam. `instructions.tex`
must contain exactly:

```latex
\textbf{Permitted materials:} one 8.5x11-inch double-sided note sheet, typed or handwritten. No books, printouts, or other notes, and no electronic devices of any kind (including phones, laptops, tablets, smartwatches, and calculators).
```

(Older exams said "handwritten"; as of Autumn 2026 the sheet may be typed. Past
exams are being recompiled to match.) The instructions do not state how
select-all items are scored; if the instructor sets a policy, add one sentence
there.

## Pre-copy review (required before the copier)

Run two independent reviews of the built PDFs, one on the answer key and one
reading the exam as a student would, and fold both into the source before
printing. The 2026 reviews caught a reversed arrow in a figure, a keyed option
that was true for half the room, a stem that handed students the secret the
attacker was not supposed to know, and a double negative. Each reviewer checks
every item for:

- **Key:** is the keyed answer uniquely right? Could a prepared student defend
  another option? Widen the key (accept X) rather than argue later.
- **Wording:** two readings; a term never used in class ("Anderson's
  taxonomy"); "the two reasons" when other pairs are also right (say "two");
  "by default" claims that differ by browser or OS; a stem that reveals what the
  question pretends is hidden (a transaction ID, a key); a question about the
  lab that does not match what the lab actually did (a loopback capture has no
  DNS query); a yes/no that is a double negative.
- **Select-all:** every option must answer the stem's question, not a nearby
  one (a script's origin vs. its URL's origin); nothing promised "will not be
  asked" (port numbers).
- **Form of answer:** does the stem say what to write (a letter, a word, a
  sentence, three items)? Is the box big enough for it?
- **Lab coverage:** at least one question only a student who did the assignment
  can answer (the trust-store step for a self-signed certificate, not just
  "what leaks over HTTPS").
- **Layout on paper:** nothing straddles a page, no heading orphaned, figures
  legible on a black-and-white copier, every box reachable with a pen.

Record what the review changed in the exam's `README.md`.

## Validation

```bash
make all
pdfinfo exam.pdf | grep Pages                                  # must be 6
grep -o '\\prob{[0-9]*}' questions.tex | grep -o '[0-9]*' | awk '{s+=$1} END {print s}'   # must be 85
```

Open both PDFs. No overlapping text, every answer box starts on its own line, no
multiple-choice option wraps, every diagram has a student and a solution version,
and the solution PDF shows an answer for every question. Too long, in this
order: tighten the stems (the 2025 exam is about 1,700 words in `questions.tex`; a
3,000-word draft runs to seven pages), move figures beside their text, shrink
answer boxes toward 0.9, then cut the weakest multiple-choice question and move
its points to a neighbor. Too short: enlarge boxes or add one short-answer
question on an under-covered meeting.

## Checklist before handing the draft to the instructor

- [ ] Every Midterm flag in the range has a question; list them in `README.md`
- [ ] Every assignment due in the range has a question
- [ ] Nothing the agenda excludes is asked
- [ ] No question duplicates a past exam
- [ ] At least two diagram questions, each with student and solution images
- [ ] 6 pages, 85 points, permitted-materials statement verbatim
- [ ] Files are in Dropbox only; nothing committed
