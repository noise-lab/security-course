# Grader Key — Internet Access Measurements Lab

Pairs with `../access.md` (the student-facing lab, one level up; this lab is not in its
own folder). Total **100 points**. Grade from `access-report.md` plus the pasted
numbers, tables, and figure descriptions. The student also pushes a notebook or script
(name contains `access` or `equity`); you cannot run it, so grade from the report text.
See `../GRADING.md` for the grading prompt and output format.

Submissions **vary by chosen question and subset**: students pick a raw-data release, a
file set (download, upload, ping, webget), a time window, and their own policy question.
There is no single fixed answer for Items 5 and 6. Grade whether the analysis is
**correct for the subset the student chose** and whether the numbers they paste are
consistent with what they say they loaded. Items 1 to 3 and 7 have expected answers;
accept variants that capture the same point.

---

## Item 1 — Sampling (10 pts)

Maps to report heading **"1. Sampling"** (Part 1, Q1a/Q1b).

| Check | Pts |
|---|---|
| Q1a: names at least two question types the ISP-stratified panel supports | 5 |
| Q1b: names at least two question types it cannot support, with the reason (no geographic stratification; only panelists on the ten evaluated ISPs) | 5 |

**Expected answer (Q1a):** the sample supports **ISP-level** and **national** comparisons:
advertised vs. actually delivered speed per ISP, comparisons across the ten ISPs or
across access technologies in the panel, and **trends over time** for the panel itself
(the same units are measured repeatedly). Accept "per-tier within an ISP" if the tier is
in the panel.

**Expected answer (Q1b):** it cannot answer **geographic** questions (state, city, rural
vs. urban, "is service worse on the South Side"), questions about **ISPs or tiers not in
the panel** (small or regional providers, new tiers), questions about **non-subscribers
or unserved areas** (every panelist is by construction a subscriber), or questions
about the **in-home Wi-Fi experience** (see Item 3). Any two of these with the reason
earns full marks.

**Common errors:** "it can answer anything about US broadband"; claiming the sample is
representative of the population because n = 5,242 (size is not representativeness;
cap Q1a at 2); listing what it cannot answer without saying *why* (cap Q1b at 3).

## Item 2 — Metrics (8 pts)

Maps to **"2. Metrics"** (Part 1, Q2a/Q2b).

| Check | Pts |
|---|---|
| Q2a: explains why latency matters, including that more bandwidth does not reduce it | 4 |
| Q2b: explains why web browsing time matters as a user-experienced metric distinct from throughput | 4 |

**Expected answer (Q2a):** latency governs **interactive** applications (gaming, VoIP,
videoconferencing), the **TCP throughput ramp** (slow start and congestion control take
more round trips on a high-RTT path, so even a fat pipe fills slowly), **DNS lookups**,
and **page loads** (many small sequential fetches). It is a property of the path, not the
pipe, so **buying more bandwidth does not improve it**. Full marks need the "not fixed by
bandwidth" point plus at least one application class.

**Expected answer (Q2b):** page-load time is **what users actually experience**; it
**plateaus** with throughput (beyond a few tens of Mbps, more bandwidth barely changes
it) while remaining **latency-sensitive**, so it exposes problems a speed test hides.
Accept "speed tests measure capacity, web tests measure experience."

**Common errors:** "latency is the speed of the connection" (confuses it with
throughput; cap Q2a at 1); "web browsing matters because people browse the web" with no
link to the throughput plateau or latency (cap Q2b at 2).

## Item 3 — Method (7 pts)

Maps to **"3. Method"** (Part 1, Q3).

| Check | Pts |
|---|---|
| States that the whitebox is **wired directly** to the home router or modem, so Wi-Fi is not on the measured path | 4 |
| States that tests run only when the home network is **idle** (cross-traffic detection), so other household traffic does not depress the measurement | 3 |

**Expected answer:** the FCC measures from a dedicated **whitebox** connected by
**Ethernet** to the modem or gateway; the box monitors cross-traffic and **defers tests
until the home network is quiet**. Together these isolate the ISP's access link from
in-home limitations, which is exactly the caveat the report raises.

**Common errors:** "they use a Wi-Fi survey" or "they average over many homes" (neither
removes Wi-Fi from the path; cap at 2); describing speed-test servers without saying
where the client sits.

## Item 4 — The Data (10 pts)

Maps to **"4. The Data"** (Part 2).

| Check | Pts |
|---|---|
| Names the **raw-data release** (month/year) and the specific **files** used (e.g., `curr_httpgetmt.csv`, `curr_ping.csv`, `curr_webget.csv`) | 3 |
| Gives **row counts** and the **date range** actually loaded | 3 |
| States the **subset** taken (a day, a week, one ISP, one target) and a reason for it | 2 |
| Identifies the key columns they relied on (`unit_id`, `dtime`, `target`, and the measurement column) and the pushed notebook or script by name | 2 |

**Acceptable variants:** any release since 2010; a single file is fine if the question
only needs one; a subset as small as one day is fine if stated. **Common errors:** quoting
the FCC's aggregate report tables instead of the raw data (cap at 3); no row counts or
date range (dock the second row); "I used the FCC data" with no file names.

## Item 5 — Your Policy Question (10 pts)

Maps to **"5. Your Policy Question"** (Part 3).

| Check | Pts |
|---|---|
| States **one** precise question that the chosen subset can actually answer | 5 |
| Justifies its **policy relevance**: names the decision or rule it informs and who would act (FCC reporting standards, advertised-speed disclosure, BEAD "served" thresholds, consumer protection, a state broadband office) | 5 |

**Acceptable variants:** the three examples in the lab (80/80 vs. other aggregations;
throughput vs. page-load time; variability of one user's experience over time) or any
question consistent with Item 1's limits. **Common errors:** a question that needs
**geography** the data lacks ("which states have the worst broadband"; cap at 2 unless
they note the limit and reframe); a vague topic rather than a question ("I will look at
latency"); "this matters for policy" with no named decision or actor (cap the second row
at 2).

## Item 6 — Analysis & Results (25 pts) — *depth*

Maps to **"6. Analysis & Results"**.

| Check | Pts |
|---|---|
| Pastes **summary numbers or tables** (as text) that are consistent with the release, files, and subset named in Item 4 | 8 |
| Describes the **method**: grouping keys (`unit_id`, `target`, time), the aggregation used (mean, median, percentile, 80/80), units and conversions, and how **failed tests** or outliers were handled | 7 |
| Gives a **direct answer** to the Item 5 question, supported by the pasted numbers | 5 |
| Describes at least one **figure** in words (axes, what it shows, what to look for), or an equivalent table | 3 |
| States the **limitations** of the answer, tied back to the sampling limits in Item 1 | 2 |

**What "consistent" means:** the row counts, ISPs, targets, and dates in the tables match
Item 4; the aggregation they name is the one the numbers reflect (a "median" table
should not be labelled "80/80"); magnitudes are plausible (download speeds in the tens
to hundreds of Mbps, RTTs in the tens of ms). **Unit traps to watch for:** throughput
columns are in **bytes per second** (multiply by 8 and divide by 10^6 for Mbps); the ping
file reports RTTs in **microseconds**; a table of "Mbps" in the thousands or "ms" in the
tens of thousands means a missed conversion. Do not fail the item for a unit slip they
caught and corrected in Item 8; cap the method row if the slip is uncaught and the
conclusion depends on it.

**Common errors:** figures only, no pasted numbers (cap the first row at 3); a result
stated with no method (cap at 12 total); averaging across targets or units without
saying so; treating a one-day subset as a trend; no limitations (dock the last row).

## Item 7 — Digital Equity (15 pts) — *depth*

Maps to **"7. Digital Equity"** (Part 4, Q1 to Q3).

| Check | Pts |
|---|---|
| Q1: explains why MBA **cannot identify unserved or underserved locations** | 5 |
| Q2: names the **additional data** needed and the **challenges** of collecting it | 5 |
| Q3: explains how a **hyper-local** approach addresses under-sampled geographies | 5 |

**Expected answer (Q1):** MBA is a panel of a **few thousand volunteers**, **stratified by
ISP**, with **no geographic coverage guarantee**, drawn only from **subscribers of the ten
largest ISPs**. Every panelist already has service, so the data say nothing about
places with no or poor service, and the sample may contain zero units in a given county
or neighborhood. Full marks need the "subscribers only" or "no geographic guarantee"
point plus the consequence for BEAD-style unserved/underserved maps.

**Expected answer (Q2):** data needed: **address- or block-level availability and
performance**, **pricing and affordability**, **adoption** (who subscribes), and
**device access**. Challenges: **cost** of dense deployment, **consent and privacy** of
in-home measurement, **self-selection** of volunteers, and reliance on
**provider-reported** availability (the FCC Broadband Data Collection) whose incentives
favor over-reporting. Any two data types plus two challenges earns full marks.

**Expected answer (Q3):** a hyper-local effort (the Internet Equity Initiative at
UChicago) **densely samples specific neighborhoods** so that within-city disparities,
which a national panel averages away, become visible; it pairs measurement with local
partners who can recruit in under-sampled places. Full marks for the "within-city
disparity that averaging hides" point; strong answers also note the trade-off (dense
local coverage, less national generalizability).

**Common errors:** "the data is old" or "the sample is too small" as the only reason
(cap Q1 at 2); listing data types with no collection challenges (cap Q2 at 3); "more
data is better" with no explanation of what local density reveals (cap Q3 at 2).

## Item 8 — Reflection & AI-verification (15 pts) — *AI-resilience*

Maps to **"8. Reflection & Tinkering"**. This item rewards work that is demonstrably the
student's own. It is graded on **specificity and grounding in their subset**, not prose
quality.

| Check | Pts |
|---|---|
| Describes something they **tried that didn't work** and how they resolved it (a concrete dead end, not a platitude) | 5 |
| Notes something that **surprised them in their own subset**, referencing a specific unit, target, ISP, column, or value | 5 |
| If AI was used: names **one claim they checked against their data** and the outcome. If AI was not used: a correct extra observation about their subset earns these points | 5 |

**This is the anti-bluff item.** Generic reflection that could describe *any* student's
run ("I learned that data analysis is hard") earns ≤3 total. Look for detail that is only
possible if they actually did it: a file that would not fit in memory and how they
chunked it, a `unit_id` join that dropped rows, a target server that dominated the
sample, an RTT column they first read as milliseconds, an AI-generated snippet that
summed `bytes_sec` across threads when it should not have.

## Item 9 — Extra credit: 80/80 vs. distribution, or second-dataset join (+10) — *sophistication stretch*

Maps to **"9. (Extra credit) 80/80 vs. Distribution, or Second-Dataset Join"**. Award
only with evidence. One variant only.

| Check | Pts |
|---|---|
| **80/80 variant:** computes the 80/80 statistic **and** medians or other percentiles on their own subset and pastes them side by side **OR** **join variant:** names the second dataset, the join key, and pastes the joined summary | +6 |
| Explains **what changes**: which ISPs, users, or places look different under the other statistic or with the second dataset, and why a regulator should care | +4 |

**80/80 definition to check against:** the speed such that 80% of panelists achieve at
least 80% of the advertised (or of that speed) at least 80% of the time; accept the
student's stated operationalization if they apply it consistently. **Common errors:**
quoting the FCC's published 80/80 numbers rather than computing their own (no credit for
the first row); a join on a key that does not exist in both datasets.

Cap total at 100 before extra credit; extra credit may push a strong submission above 100
per the instructor's policy, or offset losses elsewhere.

## Appendix — AI usage (no points, but affects others)

If the student used an LLM, they should include the prompt/output and **verify it
against their data**. **Reward verification:** if they caught the model in an error (a
wrong column meaning, a wrong unit, a fabricated field, a summary number that did not
reproduce), award the related item's points generously. **Penalize unverifiable
assertions:** a number or interpretation that matches nothing they pasted and that they
cannot back up should lose the relevant item's evidence points even if it happens to be
correct.

---

### Scoring summary

| Item | Max |
|---|---|
| 1. Sampling | 10 |
| 2. Metrics | 8 |
| 3. Method | 7 |
| 4. The Data | 10 |
| 5. Your Policy Question | 10 |
| 6. Analysis & Results | 25 |
| 7. Digital Equity | 15 |
| 8. Reflection & AI-verification | 15 |
| **Total** | **100** |
| 9. Extra credit: 80/80 vs. distribution, or second-dataset join | +10 |
