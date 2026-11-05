# Grading notes: Security, Privacy, and Consumer Protection midterm, Autumn 2026

Instructor decisions about this exam that grading must follow. The
`grade-exam` skill reads this file before grading and before entering or
returning any grade. Notes that change scoring are also mirrored as a `note:`
on the part in `rubric.yaml`, so the grader applies them; this file is the
source of truth, and the two must agree. Exam given 2026-11-04; source in
`~/Dropbox/Tmp/exams/security-course/midterm/2026/` until it is published.

## Standing policy

The instructor's standing grading policy applies to this exam as to every
exam: benefit of the doubt on marks, the higher of two independent grades,
partial credit everywhere, one correct reason answers "why or why not", a
correct answer not in the key gets credit, ambiguity goes to the student,
and a class-wide fix never lowers a score. It is written out in the
`grade-exam` skill (instructor-tools) and built into the grader's prompts.
This file records only decisions specific to this exam.

## Grader settings (decided 2026-11-04)

`image_if_confidence: 0.8`, `second_opinion: higher`, `ambiguous_bubbles:
favor_student`, per the standing policy. Q24 and Q25's dashed box are
answers drawn on the printed figures (`figure_answers: [24, 25]` in
exam.yaml) and are graded from the scan image.

## Rubric fixes made before any grade was released (2026-11-04)

- **Q6 (SSH first connection):** the generated rubric gave 1 point for saying
  the client has no prior key. The question asks how Mallory mounts the
  attack and what the user must do; that the client has no prior key is
  context. The point moved to the attack (2) and the defense (2).
- **Q19b (why the same-origin policy does not help):** the generated rubric
  also graded "stored" here, which 19a's bubbles already grade. 19b now
  grades only the why (2 points).
- **Q11 points:** (a) least privilege 1.5; Subject, Verb, Object 0.5 each.
- **Q25:** what the attacker sends is graded in the dashed box on the figure
  (25b), why it works in the box below (25a). Content written in either
  place counts for either part.
- **Short answers with a single letter or number** (Q9's role letters, for
  example): the first run read some of these as blank, because OCR drops a
  lone letter and printed diagram labels were taken for writing outside the
  box. Every box with ink and no text is now graded from the scan image, and
  printed figure text is ignored. Fixed in the grader before release.

## Q10 (authentication vs. authorization terms): first option

Status: decided 2026-11-04 (see the end of this section).

The first option reads "Presenting the token and having Slack verify it is
*authentication*" and is marked correct in the key. A student pointed out
during the exam that it is ambiguous: a token like this is an authorization
credential (it carries what the agent may do), so checking it can reasonably
be read as part of authorization. Read with a comma ("Presenting the token,
and having Slack verify it, is authentication"), it is correct.

Plan: once the scans are graded, look at how the class split on this option.
If a sizable share left it blank, credit it either way (marked or blank),
as the ML midterm did for Q2 option E. Record the split and the decision here.

**Split.** 55 of 60 marked the first option; 5 left it blank.

**Decision.** The option is ambiguous, so it is **credited whether marked or
blank** for everyone (`correct: either` on option A in rubric.yaml; grading
note added to the solutions). The 5 students who left it blank gain 1 point
each. Thanks to the student who raised the wording during the exam and wrote
the comma and a margin note on the paper, as asked. Other margin notes on
Q10 were read and graded on their own.

## Q8 (Alice posts her public key on Slack)

The key says No: posting a key does not bind it to Alice. 11 of 60 said
Yes. Posting a public key does remove the n-squared part of the problem
(one key pair each instead of a shared key per pair), so **a Yes with that
explanation earns 1 of 2 on the explanation (8b)**. A Yes without it earns
nothing. Rubric note on 8b; solutions updated.

## Q11c (the Verb in Subject, Verb, Object)

The key is "read (only)". "Track" and "view" also describe a non-modifying
use and get the full 0.5. Rubric solution and criteria updated; solutions
updated.

## Bubble reads fixed by hand

Check marks and light fills count as marked (standing policy). Fixed in
overrides.yaml after reading the scan: a check in a bubble, a check with a
question mark beside it, and a light fill plus a check.

## Second-opinion disagreements (resolved to the higher grade)

20 parts were graded differently by the two independent passes; each was
given the higher grade, and each is flagged "(resolved) second opinion
disagrees ... kept the higher" in details.csv and review.html, with both
grades and the scan crop. The instructor read all 20 on 2026-11-05 and agreed the higher grade is right in every case. By
question: Q13 (5), Q15 (4), Q6 (3), Q12b (2), Q16 (2), Q21 (2), Q9c (1),
Q18 (1).

## Partial credit for written answers scored 0 (2026-11-05)

Every written answer the grader scored 0 was reread. A zero stands for a
blank, wholly wrong, or explicitly excluded answer; any correct element
earns partial credit. 35 answers were raised, by part:

- **1a, 1b, 1c** (0.5 each): an asset, property or adversary named or
  described without the rest (6 answers).
- **2a, 2b, 2c** (0.5 each): the right chain of trust named one level below
  the root or trust anchor (CA-signed certificate; a key in the DNSSEC
  chain; a ROA or RPKI certificate) (15 answers).
- **4b** (1 or 2): weighs benefit against risk, or makes the model answer's
  argument in other words (3 answers).
- **6** (1): impersonation by key substitution, without the first-connection
  setup (1).
- **7b** (0.5): the right cause of the warning (1).
- **11a** (1): "grant only the minimum needed" had been read as blank (1).
- **11b** (0.5): "viewer" as a read-only subject (1).
- **12b** (1): resource exhaustion explained correctly, wrong conclusion (1).
- **18** (0.5 or 1): an injection attack of the wrong kind (2).
- **19b** (0.5): relevant defenses without the same-origin reasoning (1).
- **25a** (0.5): the poisoning or enumeration idea without the ID reasoning (3).

Effect: mean 73.0 to 73.4 of 85.
