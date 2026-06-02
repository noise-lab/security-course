## Copyright and Content Platforms

### Learning Objectives

By completing this assignment, you will:

- Understand how content platforms detect and enforce copyright policies
- Explore the practical application of fair use doctrine through hands-on experiments
- Investigate copyright and ownership questions surrounding AI-generated content
- Understand the *technical mechanism* by which platforms detect copyrighted content (perceptual/acoustic fingerprinting and content matching)
- Analyze the gap between copyright law, platform policies, and actual enforcement practices
- Apply legal frameworks (fair use factors, relevant case law) to real-world scenarios

### Introduction

Copyright law governs much of what we can and cannot do online, from sharing memes to uploading videos to creating AI-generated art. But how do platforms like YouTube, TikTok, and Instagram actually enforce copyright? What survives and what gets taken down? Where are the boundaries of fair use in practice? And *how*, mechanically, does a platform recognize a copyrighted song or clip the instant you upload it?

In this assignment, you'll conduct hands-on experiments with copyrighted content on a platform of your choice, investigate how AI-generated content is treated, explain the detection mechanism that decides the outcome of each experiment, and analyze the results through the lens of copyright law.

**Important**: This assignment involves deliberately testing platform copyright enforcement. Use good judgment:
- Don't upload anything you wouldn't want associated with your account
- Be prepared for content to be flagged, muted, or removed
- Don't monetize any of the content you upload for this assignment
- You may want to create a separate test account
- Follow the platform's terms of service

### Grading & Rubric (100 points)

This rubric is shown up front so you know where to invest your effort. Labs are
graded primarily for thoughtful completion; points reward *understanding*, not polish.

| Component | Points | What earns full marks |
|---|---|---|
| **Platform policy analysis** | 14 | You document how your chosen platform detects, flags, and adjudicates copyright (automated matching, reporting, appeals/counter-notification, monetization, licensing programs) and note what you'll compare it against. |
| **Fair-use experiments documented (table + outcomes)** | 18 | A per-upload **text table** records content uploaded, time-to-detection, outcome, and options presented for 2–3 experiments spanning the transformativeness spectrum. Screenshots corroborate but every claim is in text. |
| **AI-generated content investigation** | 14 | For 2–3 AI pieces you record prompt, output, platform response, and ownership findings **verified against the actual ToS** (not an LLM summary). |
| **Legal analysis (4 factors + case law + gap)** | 24 | You apply all four fair-use factors to *each* experiment, cite relevant case law, and analyze the gap between law, policy, and enforcement. |
| **Detection mechanism (depth)** | 15 | You explain *mechanistically* how fingerprinting/content-matching works and use it to explain why your own experiments evaded or triggered detection. |
| **Reflection & AI-verification** | 10 | You report what you *tried* (including dead ends), what surprised you in **your own** experiments, and — if you used an LLM — at least one ownership/ToS claim you checked against the source and what you found. |
| **Evidence completeness (screenshots/links/timestamps)** | 5 | Appendix contains screenshots, links to uploaded content, and timestamps that corroborate the text. |
| **Extra credit: cross-platform or detection-threshold experiment** | +10 | Run the same content across 2–3 platforms, OR vary one transformation to find the threshold where matching breaks — reported as a small table. See the stretch task below. |

Tie every gradable claim to **your own uploads and outcomes**. Generic prose that could
describe anyone's run earns little credit; the analysis must be grounded in *your*
specific experiments.

### Tasks

#### 1. Platform Copyright Policy Analysis

Choose ONE platform to focus on for this assignment. Options include:
- YouTube
- TikTok
- Instagram
- SoundCloud
- Twitter/X
- Vimeo
- Twitch
- Other platform of your choice (get approval first)

Research and document the platform's copyright policy:
- How does the platform detect copyrighted content? (automated systems like Content ID, manual reporting, etc.)
- What happens when content is flagged as potentially infringing?
- What is the appeals or counter-notification process?
- How does the platform handle monetization of content containing copyrighted material?
- Are there any special programs (e.g., YouTube's Content ID licensing agreements)?

Compare the platform's stated policy with the behavior you observe in your experiments (Tasks 2 and 3).

#### 2. Fair Use Experiments

Upload **2-3 pieces of content** that test different aspects of fair use. Each piece should represent a different point on the spectrum of transformativeness. Suggested experiments:

- **Raw copyrighted clip**: Upload a short segment (5-10 seconds) of copyrighted content with no modification. Then try a longer clip (30+ seconds). Compare results.

- **Commentary or criticism**: Use copyrighted content while providing your own analysis, critique, or commentary. This is a classic fair use scenario (review, criticism).

- **Educational use**: Create content that uses copyrighted material to teach or explain something (e.g., analyzing a film technique, explaining a song's musical structure).

- **Parody or satire**: Create a humorous derivative work that comments on or criticizes the original.

- **Remix or mashup**: Combine multiple sources or transform content in a creative way.

For each upload, document — **as a text table** (screenshots corroborate, but the grader reads the table):

| What I uploaded | Time to detection | Outcome | Options presented |
|---|---|---|---|
| e.g., 8s unmodified pop-song clip | immediate / minutes / hours / never | up / muted / blocked in regions / removed / monetization diverted | dispute / acknowledge / trim / replace audio |

For each row also keep: screenshot of successful upload; screenshot of any warnings, flags, copyright claims, or takedown notices; and a note of the *final* outcome (stays up, muted, region-blocked, removed, monetization disabled, etc.). Paste the table into your report — every gradable claim must be in the text, not only in an image.

#### 3. AI-Generated Content Investigation

Create **2-3 pieces of content** using AI tools (e.g., DALL-E, Midjourney, Stable Diffusion, ChatGPT, Suno, etc.) with varying degrees of similarity to copyrighted works:

- **Direct reference**: Prompt that directly references copyrighted material (e.g., "Create an image of [specific copyrighted character]" or "Generate music in the style of [specific artist/song]")

- **Style mimicry**: Prompt that asks for content "in the style of" a specific artist, franchise, or creator (e.g., "in the style of Studio Ghibli" or "in the style of Taylor Swift")

- **Original creation**: Use AI to generate completely original content as a control/baseline

Upload each piece to your chosen platform and document:
- What was the AI prompt? (paste the exact prompt as text)
- Screenshot of AI-generated output
- Platform response (flagged, removed, allowed, etc.) — recorded in text
- Research findings:
  - What does the AI tool's terms of service say about copyright? **Quote the actual ToS clause** — do not paraphrase from an LLM's summary.
  - Who owns the copyright to AI-generated content per that ToS (you, the AI company, the creators of training data, public domain/no one)? Note where U.S. Copyright Office guidance says purely AI-generated output may not be copyrightable at all.
  - What is your platform's stated policy on AI-generated content?

#### 4. Legal Analysis

Apply what you've learned about copyright law to your experiments:

- **Fair Use Four Factors**: For *each* of your fair use experiments (Task 2), analyze how it performs under the four fair use factors:
  1. Purpose and character of the use (transformative? commercial?)
  2. Nature of the copyrighted work (creative vs. factual?)
  3. Amount and substantiality used
  4. Effect on the market for the original

- **Case Law**: Reference relevant cases discussed in class (e.g., *Google v. Oracle*, *Sega v. Accolade*, *Campbell v. Acuff-Rose*, *Authors Guild v. Google*, etc.) and explain how they might apply to your experiments or to the platform's policies.

- **Gap Analysis**: Discuss any gaps you observed between:
  - Legal theory (what copyright law says)
  - Platform policy (what the platform claims to do)
  - Actual enforcement (what actually happened)

  Be precise here: **the fact that content was *not* taken down does not mean it is legal fair use.** Enforcement is not law. Distinguish "the matcher didn't catch it / the rights-holder didn't enforce" from "this is a defensible fair use." That distinction *is* the gap analysis.

#### 5. Detection Mechanism (depth)

This is the missing technical layer. Explain *how* your platform actually detects copyrighted content, then connect that mechanism to what you observed in Tasks 2 and 3.

- **Fingerprinting / content matching.** Explain perceptual and acoustic **fingerprinting**: instead of comparing files byte-for-byte (a cryptographic hash, which any re-encode would defeat), the platform extracts a compact, perceptually-robust descriptor of the *content* — for audio, a fingerprint of spectral/peak features over time; for video, frame-level perceptual hashes. YouTube's **Content ID** is the canonical example. Describe the upload-time pipeline: extract fingerprint → query a **reference database** of fingerprints supplied by rights-holders → on a match, apply the rights-holder's chosen policy (block, monetize/divert revenue, track).

- **Robustness to transformation.** Explain *why* fingerprints are designed to survive transformations that change the bits but not the perception: re-encoding/transcoding, resolution or bitrate changes, cropping or letterboxing, small pitch/tempo shifts, and added overlays. The fingerprint targets features that are stable under these operations, which is why a simple re-upload or format change usually does **not** evade detection.

- **Where it breaks.** Explain the limits: very short clips (too little signal to match confidently), heavy transformation (large pitch/tempo shifts, dense overlays, time-stretching, layering multiple sources) can push the content outside the matcher's similarity threshold, and content **not present in the reference database** simply has nothing to match against. There is a matching threshold/latency, and rights-holder enforcement choices sit on top of the technical match.

- **Connect to YOUR results.** Using the above, explain **mechanistically** why some of your own experiments in Tasks 2/3 evaded detection while others didn't. For example: "my 8s raw clip matched instantly because it was in the reference DB and 8s is enough signal; my +5-semitone pitch-shifted version evaded because it fell below the acoustic-fingerprint similarity threshold; my AI 'in the style of' track was never matched because no fingerprint of it exists in any reference DB." Tie each observed outcome to a mechanism, not just to the law.

#### 6. Reflection & Tinkering (required)

This is where you show the work is *yours*. In a short reflection (a few paragraphs):
- What did you **try that didn't work** at first (an upload that wouldn't process, a transformation you expected to evade detection but didn't, a platform that silently muted instead of removing)? How did you adjust?
- What **surprised you** in *your own* experiments specifically — a clip that survived when you expected a takedown, a detection latency you didn't expect, an AI-output ownership clause that contradicted what you assumed?
- If you used an LLM anywhere, name **one ownership/ToS claim you checked against the source** (the actual ToS or Copyright Office guidance) and say whether it held up.

#### 7. Stretch — cross-platform or detection-threshold experiment (extra credit, +10)

Anyone can *describe* fingerprinting; prove it by probing the matcher empirically. Pick **one**:

- **Cross-platform comparison.** Upload the *same* piece of content to 2–3 platforms and compare detection behavior and latency. Report which matched, how fast, and what policy each applied, in a small table.

- **Threshold sweep.** Systematically vary a *single* transformation on one copyrighted clip — clip length (e.g., 2s, 5s, 10s, 20s), pitch shift (e.g., 0, +2, +5, +8 semitones), tempo change, or overlay density — and find the **threshold** at which Content-ID-style matching stops detecting it. Report as a small table:

  | Variant | Transformation amount | Detected? | Time to detection |
  |---|---|---|---|
  | clip-2s | 2s length | ... | ... |
  | clip-10s | 10s length | ... | ... |
  | pitch+5 | +5 semitones | ... | ... |

  Then state the approximate threshold you found and connect it back to the detection mechanism (Task 5). This is self-evidently done or not and rewards real tinkering.

> **Using AI (encouraged, with verification).** You may use an LLM to help interpret a
> platform policy or draft a fair-use analysis. If you do, **include the exchange in the
> appendix.** For the AI-generated-content task especially, **verify any claim about who
> owns AI output against the actual ToS** (and U.S. Copyright Office guidance) rather than
> trusting the model's summary — models routinely overstate or invent ownership terms.
> Quote the governing clause that confirms or contradicts the model. Submitting an
> assertion you can't back up against the source will lose points; catching the model in
> an error will earn full marks for that item.

> **Be ready to defend it.** Per the syllabus, we may ask you to reproduce or explain any
> part of this lab live (office hours, a pop quiz, or the exam) — e.g., "re-upload this
> clip and show the Content ID claim," or "walk me through why your pitch-shifted version
> evaded the matcher." Do the work so you can.

### Optional Extensions

If you want to explore further (beyond the graded stretch above), here are some additional ideas:

- **Gray area creative experiments**:
  - Record a cover song (audio only vs. video)
  - Create traced or heavily-referenced artwork at varying levels of similarity
  - Produce fan fiction content (fan-made scenes, animations, etc.)
- **Test edge cases**: Very short clips (1-2 seconds), background music, memes, screenshots
- **DMCA takedown exercise**: Create original content, then file a DMCA takedown notice against your own content (or a partner's) to experience the process firsthand

### Submission Instructions

Submit a single markdown report named **`copyright-report.md`** plus a folder of
screenshots. **Because your report is graded from its text, document every experiment in
the text tables and prose described below** — screenshots are corroboration, not a
substitute for the text. Push the report and the screenshots folder to your **private
GitHub repository** (do not push a zip file).

Your report **must contain these headings, in this order** (they map one-to-one to the
rubric above):

```
# Copyright Lab — <your name>

## 1. Platform Policy Analysis
   (chosen platform; detection method, flagging, appeals/counter-notification,
    monetization, licensing programs; what you'll compare against)

## 2. Fair Use Experiments
   - Per-upload TABLE: content | time-to-detection | outcome | options presented
   - One row per experiment (2–3 experiments across the transformativeness spectrum)

## 3. AI-Generated Content Investigation
   - Per piece (2–3): exact prompt | output (screenshot) | platform response
   - Ownership findings VERIFIED against the actual ToS (quote the clause)

## 4. Legal Analysis
   - Four fair-use factors applied to EACH experiment
   - Relevant case law
   - Gap analysis: law vs. policy vs. enforcement (note: "not taken down" ≠ "legal")

## 5. Detection Mechanism (depth)
   - How fingerprinting/content-matching works; robustness; where it breaks
   - Mechanistic explanation of why YOUR experiments evaded or triggered detection

## 6. Reflection & Tinkering
   - What you tried that didn't work; what surprised you in YOUR experiments;
     one AI ownership/ToS claim you verified against the source

## 7. (Extra credit) Cross-platform or detection-threshold experiment
   - Small table; the threshold or comparison you found; tie back to the mechanism

## Appendix: screenshots, links, timestamps, and AI usage (if any)
   - All screenshots; links to uploaded content; upload/detection timestamps
   - Any AI prompts, model output, and your verification against the source
```

### Resources

- [U.S. Copyright Office - Fair Use Index](https://www.copyright.gov/fair-use/)
- [U.S. Copyright Office - Copyright and Artificial Intelligence](https://www.copyright.gov/ai/)
- [Stanford Copyright & Fair Use Center](https://fairuse.stanford.edu/)
- [YouTube Copyright Center](https://www.youtube.com/howyoutubeworks/policies/copyright/)
- [How Content ID works (YouTube Help)](https://support.google.com/youtube/answer/2797370)
- [EFF - Fair Use and Copyright](https://www.eff.org/issues/intellectual-property/fair-use-and-copyright)
- Platform-specific copyright documentation for your chosen platform

### Academic Integrity Note

This assignment involves creating and uploading content that may be flagged or removed. This is done for educational purposes to understand copyright enforcement. Do not:
- Use this assignment as an excuse to upload genuinely infringing content
- Attempt to profit from any uploaded content
- Violate platform terms of service beyond what's necessary for the educational experiment
- Upload content that could get your account permanently banned

When in doubt, ask the instructor.
