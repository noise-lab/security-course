# 13-AI-Privacy — instructor notes

## Figures added (2026-11-18 graphics pass)

Deck grew from 16 to 22 content slides (23 with the title slide). No legacy pptx for
this topic, so no clippings; all pictures are Graphviz `{dot}` blocks rendered by
Quarto or live captures under `images/captures/` (gitignored; `git add -f`).

**Graphviz diagrams (8):**

- *Two Kinds of Privacy Risk* — two clustered rows (AI-specific above traditional)
  with the red "draws out more data" edge; prompt injection added as a fourth
  AI-specific box.
- *Where Does a Prompt Go?* (new slide) — prompt → storage → training / human review /
  memory, dashed litigation hold / vendors / breach, red "extractable from weights";
  keyed to the five questions in `activities/llm.md` Step 2.
- *The Interdependent Privacy Problem* — colleague, clients, students, family → "You
  (the only one who consented)" → provider.
- *Memorization* — the five-step chain, replacing the ASCII block.
- *The Interface Itself* — the progressive-disclosure loop (half-width, TB).
- *Agents and Prompt Injection* (new slide) — indirect injection via a page or email
  read by an agent with tools; exfiltration.
- *How Users Cope* — task → accept / avoid / sanitize (→ rewrite, 28%) / follow
  company policy; the fourth strategy was missing from the deck.
- *Enforcement Is Catching Up (2024–2026)* (new slide) — six-event timeline in two rows.

**Live captures (4, all clickable, captured 2026-11-18):** ShareGPT52K dataset card
(Hugging Face) on *What Do People Actually Share?*; "Extracting Training Data from
ChatGPT" (not-just-memorization.github.io, Nov 28, 2023) on a new *Extraction From a
Production Model* slide; Anthropic's Aug 28, 2025 consumer-terms post on a new *Memory
and the Default Flip (2025)* slide; Anthropic's consumer privacy policy on a new
*Hands-On* slide that carries the activity's five questions. **Failed captures (bot
walls), linked in the text instead:** OpenAI Data Controls FAQ, OpenAI Memory FAQ,
OpenAI's NYT-demands response page, both FTC pages (the Feb 2023 AI-claims post and the
Sept 2025 companion-chatbot press release). A WildChat-1M capture was taken and discarded
(the dataset is linked from the ShareGPT caption).

**Current events verified or added:**

- *NYT v. OpenAI* vignette re-verified (Jan 5, 2026 affirmance; July 9, 2026 sanctions
  motion; OpenAI opposition Aug 2026, no ruling). Text unchanged; notes updated.
- Added: Anthropic consumer-terms change (Aug 28, 2025; training unless declined;
  30-day → five-year retention; deadline Oct 8, 2025, first announced as Sept 28;
  commercial/API excluded) — primary source anthropic.com plus TechCrunch's description
  of the Accept-button / toggle-on dialog.
- Added: FTC 6(b) inquiry into companion chatbots (Sept 11, 2025; seven firms; data
  handling, monetization, minors) — ftc.gov press release.
- Added: Italian Garante €15M OpenAI fine (announced Dec 20, 2024) **annulled by the
  Court of Rome on Mar 18, 2026** on one-stop-shop jurisdiction (Irish DPC is lead
  authority; merits not reached); and the Garante's €5M Replika fine (May 19, 2025).
- EU AI Act dates kept; enforcement-powers date (Aug 2, 2026) now on the slide.
- Not added (could not verify from a primary source this pass): the exact default
  state of ChatGPT's "reference chat history" memory by region. The memory slide stays
  on the Anthropic case; the ChatGPT point is phrased generically.

**Exam-coverage check (items from the prior final):** AI-specific vs traditional risks
incl. memorization, human-like interaction, and prompt injection (slides 3, 7–11);
interdependent privacy (slide 6); anthropomorphization raising risk (slide 9, bullet
plus loop); the "remember our chats?" memory prompt as dark pattern (slide 13, now with
the both-readings answer, plus slide 14); user strategies incl. avoiding real financial
numbers, rewriting prompts, accepting the trade-off, company policies (slide 15).

**Type:** `.smaller` removed from four sparse bullet-only slides (NYT vignette,
Implicit Inference, mental-models table, Policy); still on *What Do People Share?*
(picture slide, exempt). Interface-slide bullets trimmed so the quote clears the footer.
Contact sheet checked after render; no collisions.

**Speaker notes:** rewritten in the one-table format with a row per slide in order,
figure descriptions and source links per row.


## Current-events updates made (point 2)

- **2026-07-16 refresh.** Extended the *NYT v. OpenAI* vignette with the **Jan 5, 2026**
  District Judge Stein affirmance of the 20M-log production order, and the **July 9,
  2026** sanctions motion by news plaintiffs alleging OpenAI concealed internal searches
  of its training corpus (verified via TechCrunch, Bloomberg Law, Nat'l Law Review).
  Softened the "Beyond PII" attribution from "CHI 2026" (unverified venue) to arXiv
  2509.12152 (Sept 2025) — the paper is preprint status; verify CHI 2026 acceptance
  before restating. Speaker notes converted to compact table format (see
  `speaker-notes.md`); long-form appendix and per-URL glosses dropped in favor of
  clickable per-slide citations.
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

## Next-year refresh notes

Refresh the dated content below per `../TEMPLATE.md` → "Annual current-events refresh" (web-verify; swap only for something fresher and confirmed). Items placed in prior refreshes that will age:

- **NYT v. OpenAI chat-log vignette** — likely will resolve or move to trial/appeal/settlement by 2027; check whether Stein's affirmance is challenged and whether the sanctions motion produces evasion findings that reframe the case.
- **"Beyond PII"** — currently arXiv preprint (2509.12152); verify CHI 2026 acceptance/publication once program is public and restate venue if published.
- **EU AI Act GPAI obligations dated** — the **2 Aug 2026** enforcement-power date is imminent; watch for the first Commission enforcement action and swap in as a live example.
- Persistent "memory" defaults in ChatGPT/Claude/Gemini are worth a hook if a major consumer product changes the default (currently only implicit in the dark-pattern slide).
- Flag any stronger alternative vignette you find but choose not to use yet.

## Curated images

- Four live captures under `images/captures/` (see the 2026-11-18 entry above); the
  memorization flow is now a Graphviz block. No legacy images exist for this deck.

## Source

- Rebuilt from `slides.md` (Marp, ~30 slides) + `speaker-notes.md` + `agenda.md`
  (AI-and-Privacy lecture coverage, ~lines 1106–1157, plus midterm-emphasis notes at
  1242–1246). Consolidated to 16 slides. Kept `slides.md` in place per instructions.
