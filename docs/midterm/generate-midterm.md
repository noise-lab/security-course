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
| Past exams | `docs/midterm/<YYYY>/`, the two or three most recent (each has `questions.tex`, `instructions.tex`, `exam.tex`, `feamster.sty`, a `Makefile`, and any diagram PNGs) |
| Length | **6 pages, 85 points**, written for about an hour; students may take the whole period. Ends with a 2-point feedback section |
| Must include | at least one question on each lab assignment due in the range (Assignment 1, PKI, is always in range); every bullet the agenda marks **Midterm flag**; at least two diagram-based questions |
| Instructor output | `/Users/feamster/Dropbox/Tmp/exams/security-course/midterm/<YYYY>/`, cloud-backed and outside the public repository. **Never commit an exam before it has been given.** Afterwards it is committed to `docs/midterm/<YYYY>/` with solutions as practice material |
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
8. **Fit exactly:** 6 single-sided pages, 85 points, a mix of question types in
   roughly the past exams' proportions (about a third multiple choice, a third
   short answer, the rest yes/no-with-explanation and diagrams), sections in the
   order the material was taught.

## Steps

1. Read the agenda for the meeting range. List, per meeting: the concepts taught,
   the examples used, every Midterm flag, and every exclusion.
2. Read the past exams for form only: LaTeX conventions, point values, section
   style, how diagrams are used, the feedback section.
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
  is `\shortanswerbox{4.0}{Nick Feamster}` and the first `\prob` is question 1.
- Multiple choice: `\correctanswercircle{text}` for correct options,
  `\answercircle{text}` for the others; say "(Select all that apply.)" or "(Select
  the best answer.)" in the stem. Keep options to one line each.
- Yes/no: `\yesnoyes` or `\yesnono` at the end of the statement, then a separate
  `\prob` "Explain why or why not." with an `\answerbox`.
- Short answer: `\answerbox{height}{solution}`; the height unit is 1.5 cm, and
  0.8–1.1 is the range that fits six pages (1.0 holds about three lines of
  `\small` text, roughly 380 characters at full width). Start the solution with
  `\small`, keep it to one paragraph with no `&`, and put a blank line before the
  box. Very short answers: `\shortanswerbox{width}{text}`.
- Diagrams: place the figure beside its question text in two `[t]` minipages
  (about `0.40` and `0.57\linewidth`, each starting with `\vspace{0pt}`), with
  `\par\noindent` right after `\prob{N}` so the pair starts on its own line; a
  full-width figure under its stem costs a third of a page. Put `\Needspace{2.5in}`
  (needspace package, capital N) before every figure question so it never splits;
  lowercase `\needspace` adds a penalty that TeX takes early. Draw labels large
  enough to print at 7 pt or more once the figure is 4 in wide (with matplotlib,
  shrink the canvas rather than the data coordinates). Select the solution variant
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
- Case studies: a `\framebox[0.9\linewidth]{\parbox{0.8\linewidth}{{\bf Case
  Study:} …}}` block, centered, followed by two or three questions that apply named
  ethical principles or threat-model elements to it.
- Sections: `\section*{Name}` preceded by `\vspace*{-0.1in}`; never `\newpage`.
  `exam.tex` tightens the spacing globally with
  `\titlespacing*{\section}{0pt}{1.2ex}{0.3ex}` and
  `\setlist[itemize]{topsep=1pt,partopsep=0pt,parsep=0pt}` after loading the
  style file; a `\Needspace` before a section heading keeps it with its first
  question.
- Points: multiple choice 3–4; short answer 3–4; yes/no 1–2 plus 2–3 for the
  explanation; diagram 3–4; feedback 1 + 1.
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
exams are being recompiled to match.)

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
