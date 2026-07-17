# AI and Privacy

**Format.** Break into groups of 4–5. Each group picks **one** of the two breakouts below (or takes both if time allows). Spend ~5 minutes skimming the prep reads, then ~10 minutes debating. A designated reporter brings the group's position — and any dissents — back to the full class for a ~3-minute report-back.

Lecture 13's primary vignette is *NYT v. OpenAI*: a May 2025 magistrate order that OpenAI preserve *all* ChatGPT logs (including deleted chats), followed by a November 2025 order to produce 20M "de-identified" chat logs. Free/Plus/Pro/Team users swept in; Enterprise/Edu excluded. A copyright lawsuit turned into a privacy crisis. The EU AI Act's GPAI transparency obligations bit on 2 Aug 2025.

---

## Breakout A: When "Delete" Doesn't Delete
<!-- breakout id="A" status="current" refreshed="2026-07-16" -->

**Motion.** *"The NYT v. OpenAI preservation order proved that consumer-tier AI users have no meaningful privacy from litigation preservation orders — even for content they explicitly deleted. Free and Plus tier users should be entitled to the same zero-retention terms as Enterprise/Edu customers, and courts should not be able to override user-initiated deletion for adversary-third-party discovery."*

<!-- current-events:start topic="nyt-openai-preservation-order-retention" -->
**Prep reads (5–10 min).**
- [How we're responding to The New York Times' data demands in order to protect user privacy](https://openai.com/index/response-to-nyt-data-demands/) — OpenAI, 2025. OpenAI's own account of the preservation fight, the September 26, 2025 sunset of the indefinite-retention order, and the April–September 2025 data still being held.
- [OpenAI Must Turn Over 20 Million ChatGPT Logs, Judge Affirms](https://news.bloomberglaw.com/ip-law/openai-must-turn-over-20-million-chatgpt-logs-judge-affirms) — Bloomberg Law, January 2026. Judge Sidney Stein's January 5, 2026 affirmance of Magistrate Wang's order compelling production of the full 20M-log sample, rejecting OpenAI's securities-law analogy.
- [New York Times says OpenAI hid evidence in ChatGPT copyright trial](https://techcrunch.com/2026/07/09/new-york-times-says-openai-hid-evidence-in-chatgpt-copyright-trial/) — TechCrunch, July 2026. The July 9, 2026 sanctions motion: plaintiffs allege OpenAI over-redacted the December 2025 sample into unusability, deleted billions of outputs post-suit, and substituted millions of logs.
- [OpenAI Loses Privacy Gambit: 20 Million ChatGPT Logs Likely Headed to Copyright Plaintiffs](https://natlawreview.com/article/openai-loses-privacy-gambit-20-million-chatgpt-logs-likely-headed-copyright) — National Law Review, 2025. Explainer on the "attorneys' eyes only" designation, the de-identification protocol, and why Enterprise/Edu tiers were carved out by contract.
<!-- current-events:end -->

**Discussion prompts.**
- Enterprise/Edu customers were excluded from the preservation order. That's a *contractual* protection (zero-data-retention terms in the master service agreement). Should the same protection be a *statutory* right for consumers, or is it a legitimate paid-tier differentiation?
- The 20M "de-identified" logs are still full-text conversations rich in quasi-identifiers (names of employers, medical conditions, home addresses in prompts). Do standard de-identification techniques apply to free-text conversations, or is this the Netflix Prize / Sweeney problem all over again?
- The lecture's "Beyond PII" thread (Wang et al. CHI 2026) showed that users anticipate inference only slightly better than chance and that abstraction/ambiguity beats paraphrase. If users cannot predict what a model will infer, what does *informed consent* even look like for AI conversations?
- Persistent memory features (ChatGPT and Claude's "memory") store facts across sessions. Are these subject to the same preservation orders, and should they be opt-in-with-explicit-scope rather than default-on?

**Bring back.** The single privacy protection your group would legislate as a floor for consumer AI chat products, and one thing you'd leave to market differentiation.

---

## Breakout B: Prompt Injection, Agents, and the New Attack Surface
<!-- breakout id="B" status="current" refreshed="2026-07-16" -->

**Motion.** *"Agentic assistants with tool access (browsing, file systems, MCP servers, email, calendars) turn every model into an attack surface for indirect prompt injection via untrusted content. Providers who ship agent capabilities to consumers before solving the injection problem should be strictly liable for exfiltrated data — even in the absence of a specific security bug."*

<!-- current-events:start topic="prompt-injection-agentic-ai-liability" -->
**Prep reads (5–10 min).**
- [LLM01:2025 Prompt Injection](https://genai.owasp.org/llmrisk/llm01-prompt-injection/) — OWASP Gen AI Security Project, 2025. Prompt injection ranks #1 on the OWASP Top 10 for LLM Applications; the entry treats indirect injection as a first-class threat with a documented data-exfiltration pattern.
- [Samsung Bans ChatGPT Among Employees After Sensitive Code Leak](https://www.forbes.com/sites/siladityaray/2023/05/02/samsung-bans-chatgpt-and-other-chatbots-for-employees-after-sensitive-code-leak/) — Forbes, May 2023. The founding enterprise incident: three engineers pasted proprietary chip source code and meeting transcripts into ChatGPT within three weeks of an internal lift on the ban.
- [European Commission Releases Mandatory Template for Public Disclosure of AI Training Data](https://www.wilmerhale.com/en/insights/blogs/wilmerhale-privacy-and-cybersecurity-law/european-commission-releases-mandatory-template-for-public-disclosure-of-ai-training-data) — WilmerHale, 2025. Explains the Article 53 training-data-summary template that binds GPAI providers from August 2, 2025 and the enforcement window opening August 2, 2026.
- [From LLM to agentic AI: prompt injection got worse](https://christian-schneider.net/blog/prompt-injection-agentic-amplification/) — Christian Schneider, 2025. Walks through EchoLeak (CVE-2025-32711) — the zero-click Microsoft 365 Copilot exfiltration — and why tool-using agents make a single injected instruction a multi-system compromise.
<!-- current-events:end -->

**Discussion prompts.**
- The lecture's threat models: memorization (training data leaks out), inference (model deduces sensitive attributes), and injection (untrusted input redirects behavior). Which of these is the *worst* privacy risk for a typical consumer, and which for an enterprise?
- Indirect prompt injection — malicious content in a webpage the model browses tells it to exfiltrate your data via a tool call — has no widely accepted defense. Is this a "wait for the research to mature" problem, a "don't ship agents to consumers" problem, or a "regulate model providers" problem?
- Differential privacy and federated learning are the marketed technical mitigations. The deck flags them as "hard (utility cost)." Are these real defenses for user privacy, or credential-washing?
- The EU AI Act GPAI transparency obligations (in force since 2 Aug 2025) require training-data summaries. Would that have helped in the NYT case, or is it targeted at the wrong risk?

**Bring back.** Whether your group would impose strict liability for prompt-injection-driven data loss, and one carve-out you'd accept.

---

## Instructor notes

Breakout A is the more universally-accessible one — every student in the room has used ChatGPT or Claude and is unsettled by "delete doesn't delete." Breakout B assumes some familiarity with agent tools (MCP, function-calling); it's stronger in CS-heavy classes. If time is short, run A: the discovery-order story is a rare privacy issue that unifies contract law, evidence, and technology. Both benefit from a 30-second reminder that "AI privacy" now spans training data (Lecture 15), inference in use (this lecture), and downstream discovery/retention.

<!--
breakout-metadata:
  lecture: 13
  class: "AI and Privacy"
  last_refreshed: 2026-07-16
-->
