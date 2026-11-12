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

## Q1d, Q11a, Q12b, Q13 (answers that asked more than the question): one correct answer is enough, class-wide regrade (2026-11-11)

- **Q1d, the attacker's capability.** The rubric required the answer to
  name possession of the token, but the question already gives the
  attacker the token, and the asset box says "not the token itself". A
  capability that says what holding it lets the attacker do (post or act
  as the agent or the instructor) now earns full credit.
- **Q11a, why sharing a bank password violates least privilege.** The
  rubric required that the password cannot be limited, audited, or revoked.
  Those are real problems with password sharing, but the question asks only
  why it violates least privilege, so "the password gives the app far more
  access than tracking spending needs" now earns full credit.
- **Q12b, why the firewall is a new DoS vulnerability.** The rubric
  required the consequence that a failed firewall blocks everyone. The
  question asks why it is a new vulnerability, so "the firewall has finite
  resources (or keeps state) and the traffic must pass through it, so it
  becomes the new target" now earns full credit.
- **Q13, the SYN-cookie redesign.** The question says a sentence or two of
  design is enough and no cryptographic detail is needed. "Allocate nothing
  on the first request; allocate only after the client returns or proves
  something the server sent it" now earns full redesign credit without the
  word "cookie" or how the cookie is derived.
- Applied to every exam with `grade --parts`, keeping the higher score: no
  score went down. Q1d raised 15 students, Q11a 34, Q12b 18, Q13 18. Notes
  on each part in rubric.yaml.

## Q6, Q7b, Q11d, Q16 (equivalent wording): the key's words are not required, class-wide regrade (2026-11-11)

- **Q6, defeating the SSH man in the middle.** Verifying the fingerprint
  against a value from a source Mallory does not control is what the key's
  "out of band" means, so "verify the fingerprint" earns the defense credit
  without those words. A trusted channel, or a CA-signed host certificate
  the client checks, also defeats the key substitution and earns full
  defense credit.
- **Q7b, the step that silenced the certificate warning.** "Accepted",
  "allowed", or "trusted the certificate locally" is the trust-store step
  when the answer shows it was trust and not a one-time click-through; the
  words "trust store" are not required.
- **Q11d, the object of the narrow scope.** Parts b through d are read
  together as one scope. When the narrow data (spending, transactions,
  balances) appears in the verb or the object, the object earns credit even
  when it names where the data lives (the bank, the bank's database).
- **Q16, why 160's signature naming 174 prevents the attack.** The key says
  a path omitting 174 would need 160 to have signed for 15169. Saying it
  from the other side earns the same credit: 160's signature names 174 as
  the next hop, so a path without 174 does not match any signature 160
  made and is rejected, and 15169 cannot forge one.
- Applied to every exam with `grade --parts`, keeping the higher score: no
  score went down. Q6 raised 21 students, Q7b 4, Q11d 4, Q16 15. Notes on
  each part in rubric.yaml.

## Q2a (the trust anchor for a browser's TLS connection): the root CA is enough, class-wide regrade (2026-11-11)

- **Q2a, where the browser's trust ultimately comes from.** The rubric
  required the root CAs *shipped by the OS or browser*. The root CAs are the
  answer; who ships them is detail. Any answer that names the root or
  pre-trusted CA(s) (root certificates, the root store, a pretrusted CA) now
  earns full credit. A plain "the CA" or a CA-signed certificate is one
  level below the root and stays at partial credit.
- Applied to every exam with `grade --parts 2a`, keeping the higher score:
  no score went down. 7 students went up. Note on the part in rubric.yaml.

## Q8b (a Yes that relies on Slack for the binding): half a point for naming the requirement, class-wide regrade (2026-11-12)

- **Q8b, why posting the key in Slack does or does not solve distribution.**
  Some answers said Yes because Slack accounts tie the post to Alice. That
  names the right requirement (the key must be bound to Alice's identity),
  but it assumes the channel provides the binding, which is what the
  question asks you to doubt: anyone who can post as Alice or alter the
  message can substitute a key. Such an answer now earns **0.5 of 2**. A Yes
  with the n-squared explanation still earns 1 of 2; a Yes with neither
  explanation earns nothing.
- Applied to every exam with `grade --parts 8b`, keeping the higher score:
  no score went down. 2 students went up. Note on the part in rubric.yaml.

## Answers added to the solutions on regrade (2026-11-11)

Reasonable, correct answers the original key did not list. Each is now in
the rubric notes, and the students who gave it received credit.

- **Q6:** a CA-signed SSH host certificate, checked by the client, as the
  defense.
- **Q15:** flooding the hijacked traffic (denial of service) counts as the
  black-hole action.
- **Q20a:** CSRF explained as the muffin page making a request to the bank
  with the stored bank cookie.

## Scan and reading corrections (2026-11-11)

Regrade requests also caught places where the scan, not the answer, was
the problem. Each was checked against the page image and corrected:

- light pencil fills and check marks read as blank on a select-all question
  (Q5, five exams; Q17, one exam);
- a semicolon written tightly before a command read as a letter (Q18);
- a number in the feedback box read as blank (Q26a);
- a box drawn around the right link on the DNS figure, or the link named in
  words beside it, read as no box (Q24, two exams).

After the first Q5 requests, every exam was swept for bubbles read as blank
that had some pencil in them on a question the student lost points on. The
sweep found one more light fill (Q17) that no one had asked about; the
other flagged bubbles were crossed out or check marks already read
correctly.

Bigger answer boxes on the final.

## Regrade batch log

- **2026-11-11.** 12 comments about the midterm on Gradebook issues: 11
  regrade requests and 1 request for a clearer copy of the scan; 3 asked
  for the instructor to read them. All answered on the issue. With the
  class-wide fixes above, 54 of 60 students went up; nobody went down.
  Class mean 73.4 → 75.0 of 85 (median 74.25 → 75.5). A request that
  arrived by Slack, not on the Gradebook issue, raised Q2a, applied
  class-wide the same day (7 students up; mean 75.0 → 75.03).
- **2026-11-12.** 1 further regrade request listing 15 questions. 6 were
  already raised by the 2026-11-11 class-wide fixes and scan corrections; 4
  went up on individual reading of the scan (Q16, Q18, Q19b, Q25b); 1 led to
  the Q8b class-wide rule above (2 students up); 4 kept as graded with the
  reason given on the issue. Class mean 75.03 → 75.1 (median 75.5 →
  75.625).
