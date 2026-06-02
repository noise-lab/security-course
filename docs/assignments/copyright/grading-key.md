# Grader Key — Copyright and Content Platforms Lab

Pairs with `README.md` (same folder). Total **100 points**. Grade from `copyright-report.md`
plus the screenshots/links in its appendix. See `README.md` for the grading prompt and
output format.

The submission is correct *for the student's chosen platform and content*; there is no
single fixed answer. A student might use YouTube, TikTok, SoundCloud, etc., and upload
any clips/AI outputs they chose. Check that the analysis is right for what they did. Most
evidence should be **pasted text** (the experiment tables, quoted ToS clauses, the legal
analysis); screenshots corroborate but don't replace it.

---

## Item 1 — Platform Policy Analysis (14 pts)

Maps to report heading **"1. Platform Policy Analysis"**.

| Check | Pts |
|---|---|
| Names the chosen platform and describes how it **detects** copyright (automated matching like Content ID, and/or manual reporting) | 4 |
| Describes what happens on a flag and the **appeals / counter-notification** process | 4 |
| Describes **monetization** handling and any special programs (e.g., Content ID licensing) | 3 |
| States what they will **compare** the stated policy against (their own experiments) | 3 |

**Acceptable variants:** any platform. **Common errors:** describing copyright law in
general instead of *this platform's* policy; no mention of detection method or appeals.

## Item 2 — Fair-Use Experiments Documented (18 pts)

Maps to **"2. Fair Use Experiments"**.

| Check | Pts |
|---|---|
| A **text table** with columns: content uploaded, time-to-detection, outcome, options presented | 6 |
| **2–3 experiments** spanning the transformativeness spectrum (e.g., raw clip vs. commentary/educational/parody/remix) | 6 |
| Outcomes recorded **in text** (up / muted / region-blocked / removed / monetization diverted) with corroborating screenshots referenced | 6 |

**Acceptable variants:** any content, any platform; "never detected" is a valid outcome.
**Common errors:** outcomes only shown in screenshots with nothing in text (cap at 9);
fewer than 2 experiments; no transformativeness variation (all the same kind of use).

## Item 3 — AI-Generated Content Investigation (14 pts)

Maps to **"3. AI-Generated Content Investigation"**.

| Check | Pts |
|---|---|
| 2–3 AI pieces with the **exact prompt** and output (screenshot) recorded | 4 |
| **Platform response** for each recorded in text (flagged / removed / allowed) | 4 |
| Ownership findings **verified against the actual ToS** (quotes the governing clause, not an LLM paraphrase) | 6 |

**Expected ownership findings:** the student should locate the actual ToS clause. Many
generative-AI ToS assign output rights to the *user* (often subject to acceptable-use
terms); the platform-content policy is separate. They should also note U.S. Copyright
Office guidance that **purely AI-generated output lacking human authorship may not be
copyrightable at all**. Accept any answer grounded in the *actual* quoted ToS/guidance.
**Common errors:** stating "the AI company owns it" or "you own it" with no quoted clause;
trusting an LLM's summary of the ToS instead of the ToS itself (cap the ownership sub-item
at 2).

## Item 4 — Legal Analysis (24 pts)

Maps to **"4. Legal Analysis"**.

| Check | Pts |
|---|---|
| Applies **all four fair-use factors** to *each* experiment | 12 |
| Cites **relevant case law** and connects it to their experiments or the platform's policy | 6 |
| **Gap analysis**: law vs. platform policy vs. actual enforcement | 6 |

**Expected — the four factors:**
1. **Purpose and character** of the use — including **transformativeness** and whether the use is **commercial** or noncommercial.
2. **Nature** of the copyrighted work — creative/expressive vs. factual; published vs. unpublished.
3. **Amount and substantiality** used — quantity *and* whether it takes the "heart" of the work.
4. **Effect on the market** (or potential market) for the original.

**Expected — case law:** any apt case, e.g., *Campbell v. Acuff-Rose* (parody/transformative),
*Authors Guild v. Google* / *Google v. Oracle* (transformative purpose), *Sega v. Accolade*
(intermediate copying). Reward correct *application*, not just name-dropping.

**Expected — gap analysis:** the key insight is that **enforcement ≠ law**. A clip that
"wasn't taken down" is **not** thereby established as legal fair use — the matcher may have
missed it, or the rights-holder may not have enforced. Conversely, content can be removed
even where a fair-use defense would likely succeed. Full marks require this distinction.

**Common errors:** treating "it stayed up" as proof of fair use (this is *the* error the
gap analysis must avoid — cap the gap sub-item at 2 if they make it); applying the factors
to only one experiment; listing cases without applying them.

## Item 5 — Detection Mechanism (15 pts) — *depth*

Maps to **"5. Detection Mechanism"**.

| Check | Pts |
|---|---|
| Explains **perceptual/acoustic fingerprinting + content matching against a reference DB** (e.g., Content ID), distinguished from a byte/cryptographic hash | 5 |
| Explains **why fingerprints survive transformations** (re-encoding, crop/letterbox, bitrate, small pitch/tempo shifts, overlays) — robust perceptual features, not bits | 4 |
| Explains **where it breaks** (very short clips, heavy transformation past the similarity threshold, content absent from the reference DB) | 3 |
| **Connects mechanistically to their own results** — why specific experiments evaded or triggered detection | 3 |

**Expected answer:** detection = extract a perceptual/acoustic **fingerprint** of the
content and match it against a **reference database** of fingerprints supplied by
rights-holders (Content ID is the canonical system); on a match, apply the rights-holder's
policy (block / monetize / track). Fingerprints are designed to be **robust to
re-encoding, cropping, resolution/bitrate changes, and small pitch/tempo shifts** because
they capture perceptual features rather than exact bits — so a simple re-upload does not
evade them. They are **defeatable by sufficient transformation** (large pitch/tempo shift,
heavy overlay/layering), **very short clips** (insufficient signal), or content **not in
the reference DB** (e.g., novel AI output). **Common errors:** describing it as a file/MD5
hash comparison (a re-encode would then trivially defeat it — wrong); explaining only the
*legal* reason an upload survived without the *mechanism*; no link to their own outcomes
(cap at 11).

## Item 6 — Reflection & AI-verification (10 pts) — *AI-resilience*

Maps to **"6. Reflection & Tinkering"**. Rewards work that is demonstrably the student's
own. Graded on **specificity and grounding in their experiments**, not prose quality.

| Check | Pts |
|---|---|
| Describes something they **tried that didn't work** and how they adjusted (a concrete dead end, not a platitude) | 4 |
| Notes something that **surprised them in their own experiments**, referencing a specific upload/outcome/latency | 3 |
| If AI was used: names **one ownership/ToS claim they checked against the source** and the outcome. If not used: a correct extra observation about their results earns these points | 3 |

**This is the anti-bluff item.** Generic reflection that could describe *any* student's run
("I learned platforms enforce copyright") earns ≤3 total. Look for detail only possible if
they actually did it: a specific transformation that unexpectedly did/didn't evade, a
detection latency they measured, a ToS clause that contradicted the LLM's summary.

## Item 7 — Evidence completeness (5 pts)

Maps to the **"Appendix"**.

| Check | Pts |
|---|---|
| Screenshots of uploads/flags/outcomes present and referenced from the text | 2 |
| Links to uploaded content (where still available) | 1 |
| Upload and detection **timestamps** corroborating the time-to-detection table | 2 |

**Common errors:** text claims with no corroborating evidence at all; no timestamps to
support the detection-latency claims.

## Item 8 — Extra credit: cross-platform or detection-threshold experiment (+10) — *sophistication stretch*

Maps to **"7. (Extra credit) Cross-platform or detection-threshold experiment"**. Award
only with evidence (a table).

| Check | Pts |
|---|---|
| Ran the **same content across 2–3 platforms** OR systematically varied **one** transformation | +4 |
| Reports results as a **small table** (per platform, or per variant) with detection outcome and latency | +4 |
| States the **threshold/comparison found** and ties it back to the detection mechanism (Item 5) | +2 |

Cap total at 100 before extra credit; extra credit may push a strong submission above 100
per the instructor's policy, or offset losses elsewhere.

## Appendix — AI usage (no points, but affects others)

If the student used an LLM, they should include the prompt/output and **verify it against
the source** (the actual ToS / Copyright Office guidance / their own observed outcomes).
**Reward verification:** if they caught the model overstating or inventing an ownership
term, award the related item's points generously. **Penalize unverifiable assertions:** an
ownership or policy claim that quotes no actual clause and that they can't back up should
lose the relevant item's evidence points even if it happens to be correct.

---

### Scoring summary

| Item | Max |
|---|---|
| 1. Platform Policy Analysis | 14 |
| 2. Fair-Use Experiments Documented | 18 |
| 3. AI-Generated Content Investigation | 14 |
| 4. Legal Analysis (4 factors + case law + gap) | 24 |
| 5. Detection Mechanism | 15 |
| 6. Reflection & AI-verification | 10 |
| 7. Evidence completeness | 5 |
| **Total** | **100** |
| 8. Extra credit: cross-platform or threshold experiment | +10 |
