# AI and Copyright

**Format.** Break into groups of 4–5. Each group picks **one** of the two breakouts below (or takes both if time allows). Spend ~5 minutes skimming the prep reads, then ~10 minutes debating. A designated reporter brings the group's position — and any dissents — back to the full class for a ~3-minute report-back.

Lecture 15 catches the doctrine mid-split: Ross Intelligence (Feb 2025) said no to fair use for training a competing legal AI; Bartz v. Anthropic (June 2025) said yes to book-training but no to piracy-sourced corpora; Kadrey v. Meta (June 2025) matched Bartz; NYT v. OpenAI survived dismissal (Mar 2025) and the fight has moved to *regurgitation* and market substitution. The U.S. Copyright Office (Jan 29, 2025) closed the ownership half: prompts alone don't confer authorship.

---

## Breakout A: Who Infringes When the Model Emits Protected Content?
<!-- breakout id="A" status="current" refreshed="2026-07-16" -->

**Motion.** *"When a user prompts an AI model and receives a substantially similar copy of a copyrighted work, the correct locus of liability is the *model provider*, not the prompting user or the enterprise deployer. Providers should face strict liability for regurgitation of any training-data work above a similarity threshold — the users cannot know what's in the training set, and the deployers cannot audit it."*

<!-- current-events:start topic="ai-output-regurgitation-liability" -->
**Prep reads (5–10 min).**
- [In re OpenAI Copyright Infringement Litigation — MTD Opinion](https://www.nysd.uscourts.gov/sites/default/files/2025-04/yf%2023cv11195%20OpenAI%20MTD%20opinion%20april%204%202025.pdf) — Judge Sidney Stein, S.D.N.Y., April 4, 2025. The opinion that allowed the "output stage" regurgitation and contributory-infringement theories to survive dismissal — the doctrinal ground for output-based liability.
- [Andersen v. Stability AI: The Landmark Case Unpacking the Copyright Risks of AI Image Generators](https://jipel.law.nyu.edu/andersen-v-stability-ai-the-landmark-case-unpacking-the-copyright-risks-of-ai-image-generators/) — NYU Journal of IP & Entertainment Law, 2025. Judge Orrick's August 2024 order let direct/induced infringement claims proceed against Stability, Midjourney, and DeviantArt; trial set for September 8, 2026.
- [Anthropic pays authors $1.5 billion to settle copyright infringement lawsuit](https://www.npr.org/2025/09/05/nx-s1-5529404/anthropic-settlement-authors-copyright-ai) — NPR, September 2025. The settlement releases past training claims but explicitly does NOT release claims based on model outputs — reserving the regurgitation front for future litigation.
- [The Files are in the Computer: On Copyright, Memorization, and Generative AI](https://james.grimmelmann.net/files/articles/the-files-are-in-the-computer.pdf) — James Grimmelmann, 2024. Argues that memorization and regurgitation are the same phenomenon under any technical definition — so "output-only" liability rules collapse into training-data liability.
<!-- current-events:end -->

**Discussion prompts.**
- The 2026 doctrinal shift (per Norton Rose Fulbright / Bochner) moves litigation from *input* (was training fair use?) to *output* (does a specific output substantially copy?). Does that shift favor plaintiffs or defendants overall?
- The NYT v. OpenAI complaint attached examples of near-verbatim output of NYT articles. Even if training was fair use (Bartz-style), does *output* memorization break the shield? Where's the technical line — is dedup and unlearning enough?
- Contributory / vicarious liability doctrines were built for VCRs and photocopiers. Does a model provider have "specific knowledge" of infringing potential when they've trained on 500B tokens and can't recite what's in the corpus?
- Doe v. GitHub (Copilot) alleges DMCA §1202 attribution-removal violations for code emitted without license/author metadata. Is attribution removal the right lens for AI outputs, and would it apply beyond code (music, images, prose)?

**Bring back.** Your group's proposed liability allocation rule (provider / deployer / user) for regurgitated content, and one edge case where your rule shifts.

---

## Breakout B: Can We Own AI Output? Should We?
<!-- breakout id="B" status="current" refreshed="2026-07-16" -->

**Motion.** *"The U.S. Copyright Office's Jan 29, 2025 position (purely AI-generated output is not copyrightable; prompts alone don't confer authorship; human selection/arrangement/modification can be protected) is right on the merits but wrong on the incentives. Congress should create a *sui generis* short-duration right (10 years, no derivatives) in AI-generated works for the party who materially prompted and curated the output — otherwise the AI-content commons becomes an untouchable industrial input."*

<!-- current-events:start topic="ai-output-copyrightability-copyright-office" -->
**Prep reads (5–10 min).**
- [Copyright and Artificial Intelligence, Part 2: Copyrightability](https://www.copyright.gov/ai/Copyright-and-Artificial-Intelligence-Part-2-Copyrightability-Report.pdf) — U.S. Copyright Office, January 29, 2025. The official report: prompts alone do not confer authorship; "re-rolling" is not creative control; the Office declines to recommend a sui generis right.
- [Copyright Office Publishes Report on Copyrightability of AI-Generated Materials](https://www.skadden.com/insights/publications/2025/02/copyright-office-publishes-report) — Skadden, February 2025. Skadden's summary of the four categories of protectable human contribution (assistive use, prompts, expressive inputs, modifications) and where each falls.
- [European Commission Releases Mandatory Template for Public Disclosure of AI Training Data](https://www.wilmerhale.com/en/insights/blogs/wilmerhale-privacy-and-cybersecurity-law/european-commission-releases-mandatory-template-for-public-disclosure-of-ai-training-data) — WilmerHale, 2025. The Article 53 training-data-summary template (in force August 2, 2025) — the regulatory-disclosure alternative to voluntary opt-outs and Glaze/Nightshade self-help.
- [Andersen v. Stability AI Ltd.](https://www.loeb.com/en/insights/publications/2024/08/andersen-v-stability) — Loeb & Loeb, August 2024. The DMCA §1202 (CMI-removal) claims were dismissed with prejudice, undermining one of the leading legal theories for "attribution-plus-license" protection of AI-generated outputs.
<!-- current-events:end -->

**Discussion prompts.**
- The Copyright Office's "human authorship" requirement traces to Burrow-Giles (1884, photograph as human expression). If a prompt is "expression" enough for the photograph analogy, is *ChatGPT plus prompt* copyrightable? Where does the Office draw the line, and is it drawable?
- Glaze and Nightshade (UChicago) let creators poison their own works against unauthorized training. If those tools work at scale, does that make the fair-use / licensing debate irrelevant — creators just self-help?
- "Have I Been Trained?" and the OpenAI web crawler opt-out are voluntary. The EU AI Act GPAI transparency obligations (in force 2 Aug 2025) require training-data summaries. Which framework — technical opt-out or regulatory disclosure — actually gives creators meaningful control?
- If AI-generated output is uncopyrightable, is the natural equilibrium that everything gets a light human "polish" to qualify? Does that undermine the doctrinal line entirely?

**Bring back.** Whether your group would create a *sui generis* AI-output right, and one specific feature of your proposal (duration, scope, or exclusions).

---

## Breakout format note

The [Moderation](../debates/moderation.md) whole-class debate is on this day. Keep breakouts to 10 minutes so the debate gets its full time.

## Instructor notes

Breakout A is the *infringement* half; Breakout B is the *ownership* half — together they cover both sides of the Jan 2025 Copyright Office framework. If time is short, run A — the regurgitation / liability question is the live 2026 fight after NYT v. OpenAI. Both benefit from a quick reminder that plaintiff-side litigation has now proven three things: (1) training fair use often wins, (2) piracy sourcing often loses, (3) output substantial similarity is where the next fights land. Class-heavy in policy? Run B; the sui-generis-rights debate is exciting for IP-focused students.

<!--
breakout-metadata:
  lecture: 15
  class: "AI and Copyright"
  last_refreshed: 2026-07-16
-->
