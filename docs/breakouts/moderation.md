# Content Moderation

**Format.** Break into groups of 4–5. Each group picks **one** of the two breakouts below (or takes both if time allows). Spend ~5 minutes skimming the prep reads, then ~10 minutes debating. A designated reporter brings the group's position — and any dissents — back to the full class for a ~3-minute report-back.

Lecture 16 works from the EU Digital Services Act enforcement (Oct 24, 2025 preliminary DSA findings against TikTok and Meta; April 2025 €200M DMA fine on Meta) and Moody v. NetChoice (July 1, 2024, six-Justice consensus that platform curation is First-Amendment-protected editorial activity). Meta ended third-party fact-checking in Jan 2025 and moved to Community Notes; the field is now visibly split between EU regulatory maximalism and U.S. constitutional deregulation.

---

## Breakout A: Automated Moderation — Rival, Replace, or Retire?
<!-- breakout id="A" status="current" refreshed="2026-07-16" -->

**Motion.** *"Automated content moderation, including LLM-based systems, is more harmful than beneficial: LLMs disagreed on 36.5% of moderation prompts in the 2024 audit, miss implicit toxicity, show author-identity bias, and hide their reasoning. Platforms should be required to disclose which model made each moderation decision, and to offer human review for every automated action on user speech."*

<!-- current-events:start topic="llm-moderation-audits-disclosure" -->
**Prep reads (5–10 min).**
- [More Speech and Fewer Mistakes](https://about.fb.com/news/2025/01/meta-more-speech-fewer-mistakes/) — Meta, January 7, 2025. Meta's own announcement: end of third-party fact-checkers, higher-confidence thresholds for automated takedowns, and using LLMs for "second opinion" review before enforcement.
- [DSA, AIA, and LLMs: auditing moderation in LLM-based chatbots across languages and interfaces in the electoral contexts](https://arxiv.org/abs/2509.19890) — arXiv, September 2025. Cross-model audit across Copilot, ChatGPT, and Gemini in 10 languages during the 2024 EU/US elections — dramatic inconsistency in whether models moderate election content at all.
- [AI Platforms Are Inconsistent in Detecting Hate Speech](https://www.asc.upenn.edu/ai-platforms-are-inconsistent-detecting-hate-speech) — Penn Annenberg (Fasching & Lelkes, ACL Findings), 2025. Large-scale audit of seven moderation systems (Perspective, Claude, GPT-4o, Mistral, DeepSeek, and hosted endpoints) across 1.3M synthetic sentences.
- [Commission preliminarily finds TikTok and Meta in breach of their transparency obligations under the Digital Services Act](https://ec.europa.eu/commission/presscorner/detail/en/ip_25_2503) — European Commission, October 24, 2025. First DSA enforcement wave on researcher data access — the mechanism through which automated-moderation audits become mandatory rather than voluntary.
<!-- current-events:end -->

**Discussion prompts.**
- LLMs rival Perspective API on AUC but miss implicit toxicity and are uncertain on edge cases (2025 ICWSM / arXiv studies). If a platform picks a specific LLM as its moderator, that *choice* is a policy decision. Should the choice be publicly consulted or regulator-approved?
- YouTube receives 300 hours of video per minute. If human review is required for every automated action, is the math even physically possible — and if not, which of the two rights (speech vs. safety) survives?
- The lecture's OCMP-43 findings (per Schaffner et al., CHI 2024): platforms are inconsistent about *what they define* as violative and *what examples they cite*. Does automated moderation exacerbate this inconsistency or (through consistent classification) actually reduce it?
- Meta's Jan 2025 move from third-party fact-checkers to Community Notes shifts labor from a paid workforce to crowdsourced volunteers. Is that "automation of moderation" in disguise, or a genuinely different governance model?

**Bring back.** Your group's proposed one-paragraph disclosure requirement for automated moderation, and one type of moderation decision you'd exempt.

---

## Breakout B: DSA vs. NetChoice — Two Continents, Two Rules
<!-- breakout id="B" status="current" refreshed="2026-07-16" -->

**Motion.** *"After Moody v. NetChoice (July 2024) and the Oct 2025 EU Commission preliminary findings on TikTok and Meta, the U.S. and EU have staked out incompatible positions on platform speech governance: the U.S. says platform curation *is* protected First Amendment speech, the EU says platforms are gatekeepers with statutory carriage-like obligations. This is unsustainable; large platforms will effectively pick one regime, and it will be the EU's."*

<!-- current-events:start topic="dsa-enforcement-netchoice-brussels-effect" -->
**Prep reads (5–10 min).**
- [Moody v. NetChoice, LLC (opinion)](https://www.supremecourt.gov/opinions/23pdf/22-277_d18f.pdf) — U.S. Supreme Court, July 1, 2024. Justice Kagan for the 6-Justice majority: platform curation of third-party content — including algorithmic ranking — is expressive activity protected by the First Amendment.
- [Commission preliminarily finds TikTok and Meta in breach of their transparency obligations under the Digital Services Act](https://ec.europa.eu/commission/presscorner/detail/en/ip_25_2503) — European Commission, October 24, 2025. Preliminary findings against Facebook, Instagram, and TikTok on researcher data access and notice-and-action mechanisms; up to 6% of global turnover in potential fines.
- [EU says TikTok and Meta broke transparency rules under landmark tech law](https://www.cnbc.com/2025/10/24/eu-says-tiktok-and-meta-broke-transparency-rules-under-tech-law.html) — CNBC, October 2025. Framing of the enforcement wave: ~$9.87B in potential Meta fines and ~$1.38B for TikTok, alongside the still-unresolved X paid-verification case from 2024.
- [Moody Decision Confirms First Amendment Protects Online Platforms](https://www.dwt.com/insights/2024/07/scotus-moody-ruling-a-win-for-online-platforms) — Davis Wright Tremaine, July 2024. Practitioner analysis of the doctrinal split with EU regulatory approaches and the "narrower-than-it-looks" scope of the Court's holding.
<!-- current-events:end -->

**Discussion prompts.**
- Moody v. NetChoice (six-Justice consensus) said Texas HB20 and Florida SB7072 must-carry rules are unconstitutional editorial-control mandates. The DSA requires "systemic risk assessments" and mandatory researcher data access — not must-carry, but a lot of *do-more*. Do these regimes conflict at the doctrinal core, or only at the margins?
- The GDPR was famously exported globally (the "Brussels Effect"): companies applied EU rules worldwide because splitting product lines was expensive. Does DSA compliance similarly export, or is it easier to region-lock moderation than data flows?
- Section 230 in the U.S. is under coordinated repeal push (Durbin-Graham sunset). If §230 falls, does the U.S. converge toward the DSA model or does the First Amendment prevent that convergence?
- India IT Rules, Brazil PL 2630, Singapore POFMA, Germany NetzDG — the global picture is fragmented. Does that fragmentation mean the DSA vs. NetChoice tension is overblown (platforms handle many regimes already), or that both regimes end up watered down?

**Bring back.** Whether your group thinks the DSA will effectively govern global moderation by 2030, and one specific factor that would flip your answer.

---

## Breakout format note

The [Moderation](../activities/moderation.md) activity is scheduled for this day, and the [LLM Moderation assignment](../assignments/moderation/README.md) may be due. Breakout A pairs directly with both.

## Instructor notes

Breakout A is the technical-forward version and benefits from any hands-on LLM moderation students have just done. Breakout B is the constitutional / comparative-law version and works best if students have skimmed *Moody*. If time is short, run A — everyone has strong intuitions about "who gets to decide what I see," and the 36.5% LLM-disagreement finding is a great forcing function. Both benefit from the instructor putting a real edge-case content example on the board (irony, in-group reclaimed slurs, non-English idiom) and asking each group to classify it themselves before assessing what an automated system would do.

<!--
breakout-metadata:
  lecture: 16
  class: "Content Moderation"
  last_refreshed: 2026-07-16
-->
