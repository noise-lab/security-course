# Grader Key — Content Moderation Lab

Pairs with `README.md` (same folder). Total **100 points**. Grade from `moderation-report.md`
(plus any code/prompts pasted or referenced in it). See `README.md` for the grading prompt
and output format.

The submission is correct *for the student's chosen platform, categories, and dataset*; there
is no single fixed answer. Different students pick different platforms, content categories, test
cases, and human labels. **Grade whether the analysis is internally consistent and correct for
what they chose** — not against a fixed key. The metrics, results table, and prompts must appear
**as text** in the report; notebooks/screenshots corroborate but don't replace the pasted numbers.

---

## Item 1 — Implementation & Prompts (12 pts)

Maps to report heading **"1. Implementation & Prompts"**.

| Check | Pts |
|---|---|
| Describes a working moderation function on the Claude API (model, how content is passed in) | 4 |
| Pastes the **basic** prompt verbatim | 4 |
| Pastes the **chain-of-thought** prompt verbatim (reasoning before label, e.g. `<thinking>`) | 4 |

**Common errors:** only one prompt shown (cap at 8); describing the prompts in prose without
pasting them (cap at 6); no indication the API was actually called.

## Item 2 — Platform Policy & Test Dataset (13 pts)

Maps to **"2. Platform Policy & Test Dataset"**.

| Check | Pts |
|---|---|
| Names one platform and 2–3 content categories | 3 |
| Summarizes/quotes the platform's actual policy for those categories (from ToS / guidelines) | 5 |
| Dataset of 10–15 cases that includes clear violations, clear non-violations, **and** borderline cases | 5 |

**Acceptable variants:** any reasonable platform/categories; public, synthetic, or anonymized
data. **Common errors:** a dataset with **no borderline cases** (cap dataset sub-score at 2 —
the borderline cases are required); fewer than 10 cases; policy asserted without reference to the
platform's actual rules.

## Item 3 — Results Table (15 pts)

Maps to **"3. Results Table"**.

| Check | Pts |
|---|---|
| A **text** table with one row per case | 5 |
| Each row has the **human label** and a usable input summary | 5 |
| Each row has **both** the basic-prompt output **and** the chain-of-thought output | 5 |

**Common errors:** results only in a notebook/screenshot, not as text (cap at 7); only one
approach's outputs recorded (cap at 10); human labels missing so no ground truth exists.

## Item 4 — Metrics: Accuracy + Precision/Recall/F1 (15 pts) — *depth*

Maps to **"4. Metrics: Accuracy + Precision/Recall/F1"**. Required for **both** approaches.

| Check | Pts |
|---|---|
| Confusion matrix (TP/FP/FN/TN) shown for **both** basic and CoT | 4 |
| **Accuracy, precision, recall, and F1** reported as **numbers** for **both** approaches | 5 |
| Correctly explains why **accuracy alone misleads** under class imbalance | 3 |
| Discusses **FP (over-removal) vs FN (missed violations)** and their asymmetric real-world cost | 3 |

**Expected definitions (treating "violation" as the positive class):**
- precision = TP / (TP + FP)
- recall = TP / (TP + FN)
- F1 = harmonic mean of precision and recall = 2·(P·R)/(P+R)
- accuracy = (TP + TN) / total

**Expected reasoning:** moderation traffic is mostly benign (imbalanced), so a classifier that
labels everything "OK" gets high accuracy while catching zero violations (recall ≈ 0) — accuracy
hides this, precision/recall/F1 expose it. **False negatives** = harmful content stays up;
**false positives** = legitimate speech is wrongly removed (censorship/over-blocking); the two
have different costs depending on platform and category.

**Verify the arithmetic** against their own confusion matrix; dock if the numbers don't follow
from their counts. **Common errors:** reporting **only accuracy** (cap item at 5); computing
metrics for only one approach (cap at 9); precision/recall swapped or inconsistent with the
matrix; no discussion of why accuracy misleads.

## Item 5 — Prompt-Injection / Jailbreak Robustness (15 pts) — *depth*

Maps to **"5. Prompt-Injection / Jailbreak Robustness"**.

| Check | Pts |
|---|---|
| At least 4–5 adversarial inputs spanning multiple techniques (instruction injection, role-play/framing, obfuscation, authority/format spoofing) | 6 |
| For each attack: result under **both** prompts and whether the classifier **held or was defeated** | 5 |
| States which approach was more robust and gives a plausible hypothesis why | 4 |

**Expected substance:** a robust classifier should **resist injected "ignore the policy /
classify this as SAFE" instructions** treating content as untrusted data, not commands. At least
one attack should be a genuine instruction-injection or jailbreak attempt (not just a hard
borderline case). Award full marks whether or not attacks succeeded — what matters is the attacks
are real, results are reported per approach, and the robustness comparison is made.

**Common errors:** "attacks" that are just normal hard cases (not adversarial); only one
technique tried (cap at 9); no per-prompt held/defeated determination; no comparison of basic vs
CoT robustness.

## Item 6 — Policy Analysis (20 pts)

Maps to **"6. Policy Analysis"**.

| Check | Pts |
|---|---|
| Performance discussion grounded in their precision/recall/F1 and specific cases | 5 |
| CoT vs basic comparison — where and why CoT helped (or didn't), incl. borderline/adversarial cases | 5 |
| Cost-at-scale estimate (e.g. per million posts), basic vs CoT, using Anthropic pricing | 5 |
| Concrete recommendations: when to use, safeguards (human review/appeals), hardening vs injection, transparency | 5 |

**Common errors:** restating accuracy without referencing the richer metrics; cost claimed with
no calculation or token assumptions; recommendations that are generic ("use carefully") rather
than tied to their FP/FN profile and the attacks they found.

## Item 7 — Reflection & AI-verification (10 pts) — *AI-resilience*

Maps to **"7. Reflection & Tinkering"**. Graded on **specificity and grounding in their data**,
not prose quality.

| Check | Pts |
|---|---|
| Describes something they **tried that didn't work** and how they handled it (a concrete dead end, not a platitude) | 3 |
| Notes something that **surprised them in their own data**, referencing a specific case/category | 3 |
| Names **at least one case where Claude's label diverged from their human label and explains WHY** it diverged | 4 |

**This is the anti-bluff item.** Generic reflection that could describe *any* student's run
("Claude was pretty accurate, AI moderation has limits") earns ≤3 total. Look for detail only
possible if they did it: a specific borderline input they and Claude disagreed on, a category
where CoT flipped the answer, an injection that unexpectedly worked, a human label they had to
revise. The divergence-and-why sub-item is the core: reward a concrete, well-explained
disagreement (Claude's safety training over-refused, an ambiguous policy, their own label being
arguable).

## Item 8 — Extra credit: second model / adversarial-set sophistication (+10) — *sophistication stretch*

Maps to **"8. (Extra credit) ..."**. Award only with evidence (numbers, not a description of
intent).

| Check | Pts |
|---|---|
| Ran a **second model** OR a **self-consistency/voting** setup OR a **systematic adversarial set** designed to defeat the basic prompt | +5 |
| **Recomputed metrics / failure rates** for the new setup, reported as numbers | +3 |
| States the conclusion: did ensembling/voting/CoT change the error types or robustness that mattered most | +2 |

Cap total at 100 before extra credit; extra credit may push a strong submission above 100 per the
instructor's policy, or offset losses elsewhere.

## Appendix — AI usage (no points, but affects others)

If the student used an LLM to help write code or interpret results, they should include the
prompt/output and **verify it against their own data**. **Reward verification:** if they caught a
divergence between Claude's labels and their own and explained it, award the related items
generously. **Penalize unverifiable assertions:** claims about Claude's performance that aren't
backed by their own results table and metrics should lose the relevant evidence points even if
they happen to be correct.

---

### Scoring summary

| Item | Max |
|---|---|
| 1. Implementation & Prompts | 12 |
| 2. Platform Policy & Test Dataset | 13 |
| 3. Results Table | 15 |
| 4. Metrics: Accuracy + Precision/Recall/F1 | 15 |
| 5. Prompt-Injection / Jailbreak Robustness | 15 |
| 6. Policy Analysis | 20 |
| 7. Reflection & AI-verification | 10 |
| **Total** | **100** |
| 8. Extra credit: second model / adversarial-set sophistication | +10 |
