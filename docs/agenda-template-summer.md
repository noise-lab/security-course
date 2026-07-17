# Class Meeting Agenda Template (2-hour summer Zoom, HS students)

This is the summer-term agenda template for 2-hour Zoom class meetings with
high-school students. For the 3-hour on-campus fall format, see
[agenda-template.md](agenda-template.md).

The summer term compresses the course: expect to cover roughly **two
topics per 2-hour meeting**. Debates are dropped from this format — HS
students on Zoom are less talkative in the main room, and small-group
**breakouts** get the participation share instead. Each breakout doc lives
at `docs/breakouts/<topic>.md` (two prompts per topic; groups pick one and
report back).

Two motifs work well. Pick whichever fits the day's material. For
Lecture 1, when there is no assigned reading yet, see the
[Lecture 1 variant](#lecture-1-variant-no-reading) at the bottom.

## Motif A (default) — Split lecture / breakout after each topic

Best when the two topics on the day are roughly balanced in weight and
each has a good breakout prompt. Keeps the room engaged by shifting to
small-group work every 30 minutes.

| Time      | Min | Block                                                | Notes                                                    |
|-----------|-----|------------------------------------------------------|----------------------------------------------------------|
| 0:00–0:05 |   5 | Housekeeping + warm-up prompt                        | Chat check-in; drop the day's two topics in chat         |
| 0:05–0:35 |  30 | Lecture: Topic A                                     | Book concepts + short demo                               |
| 0:35–0:55 |  20 | Breakout A (Zoom rooms) + report-back                | See `breakouts/<topic-A>.md` — groups pick one of two    |
| 0:55–1:05 |  10 | Break                                                |                                                          |
| 1:05–1:35 |  30 | Lecture: Topic B                                     |                                                          |
| 1:35–1:55 |  20 | Breakout B (Zoom rooms) + report-back                | See `breakouts/<topic-B>.md`                             |
| 1:55–2:00 |   5 | Wrap + reading preview                               |                                                          |

## Motif B — Frontloaded lecture, hands-on close

Best when one of the day's topics needs a long lecture runway (new
technical machinery — crypto, BGP, DNS, OAuth) and the other is a lighter
counterpart. Consolidates both topics up front and closes with one
breakout and a hands-on activity.

| Time      | Min | Block                                                | Notes                                                    |
|-----------|-----|------------------------------------------------------|----------------------------------------------------------|
| 0:00–0:05 |   5 | Housekeeping                                         |                                                          |
| 0:05–0:55 |  50 | Lecture: Topic A (deep) + Topic B (light)            | Cover the heavier topic first while attention is fresh   |
| 0:55–1:05 |  10 | Break                                                |                                                          |
| 1:05–1:35 |  30 | Breakout (one of Topic A or B) + report-back         | Pick whichever breakout has the stronger prompt          |
| 1:35–1:55 |  20 | Hands-on activity                                    | See `activities/<topic>.md`                              |
| 1:55–2:00 |   5 | Wrap + reading preview                               |                                                          |

## Lecture 1 variant (no reading)

The first meeting has no assigned reading. Substitute the reading-Q&A
frame with introductions and a syllabus tour, and keep the first breakout
short so students get a feel for Zoom rooms early.

| Time      | Min | Block                                                | Notes                                                    |
|-----------|-----|------------------------------------------------------|----------------------------------------------------------|
| 0:00–0:15 |  15 | Introductions + expectations                         | Round-robin — name, school, one security question they have |
| 0:15–0:35 |  20 | Syllabus tour                                        | Compressed schedule, grading, breakout format, AI policy |
| 0:35–1:05 |  30 | Lecture 1: Overview + threat modeling                | Anchor concepts for the rest of the term                 |
| 1:05–1:15 |  10 | Break                                                |                                                          |
| 1:15–1:40 |  25 | Lecture: Topic B (light framing)                     | Ethics / warm-up topic                                   |
| 1:40–1:55 |  15 | Short breakout ("meet your room") + report-back      | Low-stakes prompt so students learn the Zoom-room flow   |
| 1:55–2:00 |   5 | Wrap + reading preview                               |                                                          |

## Notes on adaptation

### Housekeeping

- Confirm the day's two topics in chat at the top.
- Remind students where the day's breakout doc lives
  (`docs/breakouts/<topic>.md`) and how to find their assigned room.
- Flag any change to the day's motif or a swap between Motif A / B.

### Running breakouts (this is where participation happens)

- **Rooms:** aim for **3–4 students per room**. Pre-assign when you can —
  HS students on Zoom are slow to self-assign.
- **Two prompts, one pick.** Each breakout doc offers two prompts. Have
  each room pick one; this creates natural variety in report-back.
- **Pop into rooms.** Visit every room at least once during a 15–20 min
  breakout. A quick "how's it going?" resets stalled groups.
- **Report-back is mandatory.** One student per room presents 60–90
  seconds back in the main room. This is where the participation grade
  gets earned.
- **Chat as a parallel channel.** Encourage students to post questions in
  chat during lecture — for shyer students this may be the only
  participation channel they'll use.

### Zoom-specific tips (HS audience)

- **Cold-call warmly.** "X, what did your group think about prompt 2?" is
  better than open questions to the void. Name-based cold calls dramatically
  raise participation on Zoom with HS students.
- **Cameras encouraged, not required.** Push for cameras in breakouts;
  don't die on the hill in the main room.
- **Short lecture segments.** Break the 30-minute lecture blocks into
  ~10-minute sub-segments with a quick chat prompt or hand-raise between
  each. Attention on Zoom drops off fast.
- **Backchannel a co-host** (TA, if available) to monitor chat while you
  lecture and to shepherd late arrivals into rooms.

### Where the day's materials live

- **Breakout prompts (this template's main discussion driver):**
  `docs/breakouts/<topic>.md` — one file per topic, two prompts each.
- **Reading assignments and activities:** the [schedule](index.md#schedule)
  in `../index.md` — same topic list as the fall course, compressed into
  ~2 topics per meeting.
- **Debate materials** live in `docs/debates/<topic>.md` but the summer
  format does **not** run debates — those are fall-only.

### Two-topics-per-meeting pacing

The summer term covers the same 18 topics as the fall course in fewer
meetings. When planning a day:

1. Pair a heavier topic with a lighter one where you can (e.g., a crypto
   primitives lecture paired with an ethics or policy topic).
2. Pick Motif A when both topics have strong standalone breakout prompts;
   Motif B when one topic needs a long lecture runway.
3. Trim reading assignments to the essential one per topic; HS students
   won't get through two dense papers per meeting.

### Cross-reference

- Schedule (all 18 topics, readings, activities): [../index.md](index.md)
- Syllabus (grading, AI policy): [syllabus.md](syllabus.md)
- Breakout prompts (summer participation anchor): `breakouts/<topic>.md`
- Fall (3-hour on-campus) template: [agenda-template.md](agenda-template.md)
