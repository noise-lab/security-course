# 13-AI-Privacy — instructor notes

## Current-events updates made (point 2)

- **Primary vignette — *NYT v. OpenAI* preservation order (2025).** Replaced the dated
  2023 hooks (Samsung leak, Italy ban, March 2023 Redis bug) with the live story: in
  **May 2025** a magistrate judge ordered OpenAI to preserve *all* ChatGPT logs (incl.
  deleted chats); in **November 2025** the court ordered production of **20 million
  de-identified chat logs** to plaintiffs. Free/Plus/Pro/Team/most API swept in;
  Enterprise/Edu excluded. Teaching frame: "delete" no longer means deleted; a copyright
  suit became a privacy crisis. Verified via OpenAI's public responses and court
  reporting.
- **"Beyond PII" updated to its published form.** The Wang, Peddinti, Taft & Feamster
  implicit-inference paper (arXiv:2509.12152) was published at **CHI 2026** (Apr 2026).
  Added its concrete findings: 240 participants, inference anticipation only slightly
  better than chance, user rewrites effective in **28%** of cases, abstraction/ambiguity
  beating paraphrase. This is now a full slide (Risk 3) plus a vignette.
- **EU AI Act GPAI obligations dated.** General-purpose-AI transparency and
  training-data-summary obligations took effect **2 Aug 2025** (pre-2 Aug 2025 models
  have until Aug 2027). Replaced the vague "adopted 2024" framing on the policy slide.
- **Trimmed stale specifics.** Dropped "Bard" (now Gemini), the $20 GPT-4 pricing aside,
  and the standalone *Google v. Oracle* slide (it belongs to the copyright lecture; kept
  only as a forward-reference in the closing notes).

## Suggested missing coverage on broad themes (point 3)

- **Agentic / tool-using assistants.** The deck treats the LLM as a chat box. 2025–26
  reality is agents with browsing, memory, MCP/tool access, and computer use — which
  expand the attack surface (indirect **prompt injection** via web content, data
  exfiltration through tool calls). Worth at least one slide.
- **Persistent memory features.** ChatGPT/Claude "memory" stores facts across sessions
  by default in some products — a distinct consent and data-retention question from
  per-conversation training opt-out. Currently only alluded to in the dark-pattern prompt.
- **Enterprise vs. consumer data terms.** The litigation hold exempting Enterprise/Edu is
  a teachable contrast: who gets zero-data-retention, and why the protections track
  willingness to pay. Could anchor a "two-tier privacy" discussion.
- **Re-identification of "de-identified" logs.** The 20M-log production is labeled
  de-identified; tie to the broader course theme that de-identification is fragile,
  especially for free-text conversations rich in quasi-identifiers.
- **On-device / open-weight models as a privacy tactic.** Mentioned in one bullet; could
  expand given the maturation of capable local models (Llama, Gemma, Qwen, Apple/Google
  on-device) as a genuine sanitization-free alternative for sensitive use.
- **Children and AI companions.** Minors using companion chatbots (and recent
  litigation/regulatory attention) intersects COPPA and the mental-health/therapy thread;
  not currently covered.
- **Differential privacy / federated learning depth.** Listed as mitigations but not
  explained; a short "why these are hard (utility cost)" note would prevent them reading
  as magic fixes.

## Curated images

- None. This deck is text-driven (no `images/` folder in source). The one diagram — the
  memorization data-flow — is rendered as an inline code/ASCII block, matching the
  source's intent without inventing a misleading figure. If a polished figure is desired
  later, a left-to-right "input → store → train → memorize → extract" flow would suit the
  Memorization slide.

## Source

- Rebuilt from `slides.md` (Marp, ~30 slides) + `speaker-notes.md` + `agenda.md`
  (AI-and-Privacy lecture coverage, ~lines 1106–1157, plus midterm-emphasis notes at
  1242–1246). Consolidated to 16 slides. Kept `slides.md` in place per instructions.
