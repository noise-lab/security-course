# Class Meeting Agenda Template (3-hour on-campus)

This is the standard fall-term agenda template for 3-hour on-campus class
meetings. For the 2-hour summer Zoom format used with high-school students,
see [agenda-template-summer.md](agenda-template-summer.md).

Each 3-hour meeting is built around four blocks: **lecture**, **reading
Q&A**, an **Oxford-style debate**, and a **hands-on activity or short
student-led discussion**. The debate is the anchor of the on-campus format
(35% of the course grade — see [debates/format.md](debates/format.md)) and
the shape below places it **in the middle** of class, right after the first
break. This mirrors how the class has actually been run — see for example
the pattern in [`agenda.md`](agenda.md) around Meeting 8.

Two or three motifs work well. Pick whichever fits the day's material.
For Lecture 1, when there is no assigned reading and no scheduled debate,
see the [Lecture 1 variant](#lecture-1-variant-no-reading-no-debate) at
the bottom.

## Motif A (default) — Lecture, break-and-debate, lecture

The primary shape. Use this whenever the day has a scheduled debate on the
[schedule](index.md#schedule) — most weeks do.

| Time      | Min | Block                                                | Notes                                                    |
|-----------|-----|------------------------------------------------------|----------------------------------------------------------|
| 0:00–0:10 |  10 | Housekeeping + reading Q&A                           | Return to the top reading-response threads               |
| 0:10–1:00 |  50 | Lecture (Topic A)                                    | Book concepts and technical framing                      |
| 1:00–1:10 |  10 | Break                                                |                                                          |
| 1:10–1:50 |  40 | Debate (Oxford-style)                                | Opening poll → arguments → audience Q&A → closing poll   |
| 1:50–2:35 |  45 | Lecture (Topic B) + hands-on activity                | See `activities/<topic>.md`                              |
| 2:35–2:45 |  10 | Break                                                |                                                          |
| 2:45–2:55 |  10 | Student presentation OR discussion                   | Optional — short unpack of the debate or a case study    |
| 2:55–3:00 |   5 | Wrap + reading preview                               |                                                          |

Adjust the exact minutes to feel natural — the **shape** (debate mid-class,
right after the first break) is what matters. If Topic A runs long, steal
from the Topic B lecture, not from the debate.

## Motif B — No-debate weeks (breakout or extended hands-on)

Some meetings don't have a scheduled debate (e.g., topics without a debate
column in [`index.md`](index.md#schedule), or catch-up weeks). Substitute
a small-group breakout for the debate slot, or extend the hands-on
activity to fill that time.

| Time      | Min | Block                                                | Notes                                                    |
|-----------|-----|------------------------------------------------------|----------------------------------------------------------|
| 0:00–0:10 |  10 | Housekeeping + reading Q&A                           |                                                          |
| 0:10–1:00 |  50 | Lecture (Topic A)                                    |                                                          |
| 1:00–1:10 |  10 | Break                                                |                                                          |
| 1:10–1:50 |  40 | Breakout discussion (small groups) + report-back     | Two prompts; groups pick one — see notes on breakouts    |
| 1:50–2:35 |  45 | Lecture (Topic B) + hands-on activity                |                                                          |
| 2:35–2:45 |  10 | Break                                                |                                                          |
| 2:45–2:55 |  10 | Student presentation OR discussion                   |                                                          |
| 2:55–3:00 |   5 | Wrap + reading preview                               |                                                          |

## Motif C (optional) — Frontloaded lecture for technical machinery

Best when the day introduces new technical machinery students need to
absorb before they can meaningfully debate or discuss (e.g., BGP, DNS,
crypto primitives, OAuth flows). Collapses reading Q&A into the lecture
and pushes discussion to the back half.

| Time      | Min | Block                                                | Notes                                                    |
|-----------|-----|------------------------------------------------------|----------------------------------------------------------|
| 0:00–0:10 |  10 | Housekeeping + reading Q&A quick hits                |                                                          |
| 0:10–1:15 |  65 | Lecture (deep technical)                             | Long single lecture — new machinery                      |
| 1:15–1:25 |  10 | Break                                                |                                                          |
| 1:25–2:10 |  45 | Hands-on activity                                    | Apply the machinery — see `activities/<topic>.md`        |
| 2:10–2:50 |  40 | Debate (Oxford-style) OR breakout                    |                                                          |
| 2:50–3:00 |  10 | Break-adjacent wrap + reading preview                |                                                          |

## Lecture 1 variant (no reading, no debate)

The first meeting has no assigned reading and no scheduled debate.
Substitute the reading Q&A + debate slots with introductions, a syllabus
tour, and a get-to-know discussion.

| Time      | Min | Block                                                | Notes                                                    |
|-----------|-----|------------------------------------------------------|----------------------------------------------------------|
| 0:00–0:20 |  20 | Introductions + expectations                         | Go around the room — background, why this course         |
| 0:20–1:00 |  40 | Syllabus tour                                        | Grading (40/35/20/5), AI policy, debates, labs, exams    |
| 1:00–1:10 |  10 | Break                                                |                                                          |
| 1:10–2:10 |  60 | Lecture 1: Overview + threat modeling                | "Why Cryptosystems Fail" + "Reflections on Trusting Trust" framing |
| 2:10–2:20 |  10 | Break                                                |                                                          |
| 2:20–2:50 |  30 | Get-to-know discussion / current events              | Small groups pick a recent security-in-the-news story    |
| 2:50–3:00 |  10 | Wrap + Lecture 2 reading preview + debate sign-up    | Point students at [debates/format.md](debates/format.md) |

## Notes on adaptation

### Housekeeping

- Attendance, deadlines, upcoming assignment due dates, exam logistics
  (permitted materials, dates — see [syllabus §Exams](syllabus.md#exams)).
- Return to any recurring reading-response threads worth surfacing.
- Flag any change to the day's motif (e.g., "no debate today — we're
  running Motif B").

### Reading Q&A

Students post reading responses ahead of class. Use the Q&A slot to work
through the most common questions or points of confusion, not to summarize
the reading. On Motif C days, compress this to "quick hits" and roll the
substantive discussion into the lecture.

### Debates (Motif A default)

- **Format:** Oxford-style — see the full rubric and structure at
  [debates/format.md](debates/format.md).
- **When:** Right after the first break, roughly the 1:10–1:50 slot.
  Placing the debate mid-class keeps energy up and lets the second lecture
  build on ideas surfaced during argument.
- **Topic list:** each meeting's debate topic is linked from the
  In-Class Activity column of the [schedule](index.md#schedule) (e.g.,
  `debates/data-breach.md`, `debates/backdoors.md`, `debates/cfaa.md`).
- **Grading:** the debate is 35% of the course grade. Grade on the quality
  of contribution, not which side "wins" the poll.
- **Running it:** open with the audience poll, keep opening-argument
  timings honest (10 / 15 / 5), reserve the last 10 minutes for audience
  Q&A, close with the second poll.

### Hands-on activities

Weeks with a heavy technical activity (BGP, DNS, OAuth, cert chains, web
tracking) may need the full 45 minutes bundled with the Topic B lecture;
lighter case-study activities can be 30 and reclaim time for a longer
student discussion at 2:45.

### Breakouts (Motif B and Motif C fallback)

For no-debate weeks, use two prompts and let small groups pick one. Report
back at the end. When the parallel breakout docs exist under
`docs/breakouts/<topic>.md`, link directly from your day's agenda entry.

### Breaks

Two 10-minute breaks work well for a 3-hour block. Move them earlier or
later depending on which activity is running long, but keep the mid-class
break immediately before the debate — students come back sharper.

### Cross-reference

- Schedule (all 18 topics, readings, activities, debate links): [../index.md](index.md)
- Syllabus (grading, AI policy, exam rules): [syllabus.md](syllabus.md)
- Debate rubric: [debates/format.md](debates/format.md)
- Past-meeting logs (for pacing calibration): [agenda.md](agenda.md)
