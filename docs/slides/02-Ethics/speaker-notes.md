# Lecture 2 — Speaker Notes (Ethics in Security and Privacy Research)

Per-slide context + clickable links (one section per slide; case briefs are broken into Read first / What happened / What to say / Course tie-in / Also). In-deck notes (the `::: {.notes}` blocks) are also visible via reveal.js speaker view (press **S**). Every URL was verified this session or is a canonical org landing page.

<!-- glance:start -->

### At a glance

| # | Slide | Cue | Read first |
|---|---|---|---|
| 2 | Why Ethics in Lecture 2? | Why this is live in 2026. | [USENIX Security '26 CFP, ethics section](https://www.usenix.org/conference/usenixsecurity26/call-for-papers) |
| 3 | A Cautionary Origin: Tuskegee | Primary sources: CDC — Tuskegee Study Timeline, HHS — National Research Act (P.L. |  |
| 4 | Why This Hits Close to Home | Hypocrite Commits (Univ. | [Nishi, Laprevotte, Bullock & Andrew, "Go](https://arxiv.org/abs/2609.10740) |
| 5 | A 2026 Lens: AI Bots on Reddit | Primary reporting on the Zurich case: Washington Post — "Reddit slams University of Zurich experiment over sec… | [Oda, Makovi, Yasseri & Tsvetkova, "A fie](https://arxiv.org/abs/2607.00854) |
| 6 | Case Study: Emotional Contagion | the LSE Reddit study (Jul 2026) is literally a "behavioral contagion" experiment run without consent under an … | [Condom-Tibau, Puccetti, Bacciu, Abrate &](https://arxiv.org/abs/2609.21608) |
| 7 | A Framework, Not a Rulebook | Moor's "policy vacuum" formulation: James H. |  |
| 8 | Key Idea: Digital Is Different | The "database of ruin" line is Paul Ohm, "Broken Promises of Privacy," UCLA L. | [Li, "Agentic LLMs as Powerful Deanonymiz](https://arxiv.org/abs/2601.05918) |
| 9 | Salganik's Layered Approach | Direct from Salganik, Bit by Bit Ch. | [Nishi et al.](https://arxiv.org/abs/2609.10740) |
| 10 | IRB, Belmont, Menlo | Primary sources: Belmont Report (1979) — HHS · Menlo Report (2012) — DHS S&T · Menlo Companion. | [Advarra, "2026 DHHS Unified Agenda: Four](https://www.advarra.com/blog/2026-dhhs-unified-agenda-four-areas-hrpp-and-irb-leaders-should-watch/) |
| 11 | The Four Principles | Live worked example to run all four on: the LSE Reddit bot study (arXiv, Jul 2026) — respect for persons (no c… |  |
| 12 | Respect for Persons: Informed Consent | The Zurich vignette explicitly fails this principle twice (undisclosed AI, fabricated identities). | [NeurIPS 2026, "AI-Assisted Reviewing Exp](https://neurips.cc/Conferences/2026/ai-reviewing-experiment) |
| 13 | Beneficence and Justice in Practice | Concepts to review: de-identification failure — Sweeney (1997); Netflix Prize re-identification — Narayanan & … | [Tianshi Li, "Agentic LLMs as Powerful De](https://arxiv.org/abs/2601.05918) |
| 14 | Respect for Law and Public Interest | ToS-vs-ethics tension: the classic case is ProPublica's 2016 Facebook ad discrimination audit, which arguably … | [Jacob van de Kerkhof, "Unpacking the EU'](https://www.techpolicy.press/unpacking-the-eus-digital-services-act-delegated-act-on-data-access-/) |
| 15 | Two Underlying Frameworks | Live 2026 split to diagnose: Microsoft vs. |  |
| 16 | Ethics ≠ Law | The quoted definition is a paraphrase of the working definition in Bynum, "Computer and Information Ethics" — … | [TechCrunch, "Microsoft under fire for th](https://techcrunch.com/2026/05/29/microsoft-under-fire-for-threatening-security-researcher-with-criminal-investigation/) |
| 17 | Laws Every Security Researcher Should Know | Two 2026 anchors for this slide. |  |
| 18 | The Law Is (Slowly) Catching Up | Primary: Van Buren v. | [U.S. Copyright Office, "U.S. Copyright O](https://www.copyright.gov/newsnet/2026/1088.html) |
| 19 | Codes, Contracts, and Other Standards | ACM Code of Ethics (2018 revision) · IEEE Code of Ethics · Nuremberg Code (1947) · Declaration of Helsinki (20… | [TechSpot, "AMD changes rules, denies res](https://www.techspot.com/news/112746-amd-changes-rules-denies-researcher-10000-bounty-after.html) |
| 20 | Breakout: Apply the Four Principles | Fresh 2026 prompts (full briefs in the rows named). |  |
| 21 | Takeaways | Bridge: next lecture is Key Management and PKI — the same "who do you trust?" question, now in the technical c… |  |

<!-- glance:end -->

*Headings carry the slide number shown in the deck footer (title slide is 1 of 21).*

## 2 · Why Ethics in Lecture 2?

**Why this is live in 2026.** **Read first:** [USENIX Security '26 CFP, ethics section](https://www.usenix.org/conference/usenixsecurity26/call-for-papers). **What to say:** "Before we start: every paper submitted to USENIX Security this year had to carry a separate 'Ethical Considerations' appendix naming every stakeholder, every harm and every mitigation, and the chairs could reject it unread if the appendix was missing. CCS bounced 13 papers for exactly that, and 41 more for citations an AI tool invented. So this is not a values lecture; it is the vocabulary for a document you will be required to write." **Course tie-in:** transparency-based accountability (Menlo) as a venue rule; full brief, numbers and links in the **Codes, Contracts, and Other Standards** row.

**Original notes:**

This lecture maps to **[Meeting 2](../../agenda.md)** and precedes the [Key Management](../03-KeyManagement/slides.qmd) block; ethics is placed early on purpose so that every subsequent lab and debate has a shared vocabulary. The framing quote is our own paraphrase of [Salganik, *Bit by Bit* (Princeton, 2018), Ch. 6 "Ethics"](https://www.bitbybitbook.com/en/1st-ed/ethics/) — recommended companion reading. Cold-call: *"Name one thing you could do with a laptop this afternoon that would be legal but you'd still feel bad about."*

## 3 · A Cautionary Origin: Tuskegee

Primary sources: [CDC — Tuskegee Study Timeline](https://www.cdc.gov/tuskegee/timeline.htm), [HHS — National Research Act (P.L. 93-348, 1974)](https://www.hhs.gov/ohrp/regulations-and-policy/belmont-report/read-the-belmont-report/index.html), [Belmont Report (1979)](https://www.hhs.gov/ohrp/regulations-and-policy/belmont-report/index.html). Canonical academic history: [James H. Jones, *Bad Blood* (Free Press, 1993)](https://www.simonandschuster.com/books/Bad-Blood/James-H-Jones/9780029166765). Note the three Belmont principles were literally reverse-engineered from the Tuskegee violations. Cold-call: *"Which of the three Belmont principles does Tuskegee violate most badly?"* — trick question; it violates all three.

## 4 · Why This Hits Close to Home

**Original notes:**

**Hypocrite Commits (Univ. of Minnesota, 2020–2021):** [Original paper — "On the Feasibility of Stealthily Introducing Vulnerabilities in Open-Source Software via Hypocrite Commits"](https://www-users.cse.umn.edu/~kjlu/papers/full-disclosure.pdf) · [Linux TAB report](https://lwn.net/Articles/854645/) · [Greg KH's ban](https://lore.kernel.org/lkml/YIAvxYBK2Rlj4Csl@kroah.com/). **Carna Botnet / Internet Census 2012:** [Anonymous researcher's write-up (Internet Census 2012)](https://web.archive.org/web/20130322064949/http://internetcensus2012.bitbucket.org/paper.html) · [Ars Technica coverage](https://arstechnica.com/information-technology/2013/03/guerilla-researcher-created-epic-botnet-to-scan-billions-of-ip-addresses/). **Encore:** [Burnett & Feamster, "Encore: Lightweight Measurement of Web Censorship with Cross-Origin Requests" (SIGCOMM 2015)](https://dl.acm.org/doi/10.1145/2785956.2787485) — and the [SIGCOMM PC "signing statement" from reviewers](https://conferences.sigcomm.org/sigcomm/2015/pdf/reviews/226pr.pdf) is the interesting artifact. All three end up in the [breakout](../../breakouts/ethics.md) and the [IRB activity](../../activities/ethics.md).

### Case: does ethics review change what researchers do? (July and September 2026)

> **Read first:** [Nishi, Laprevotte, Bullock & Andrew, "Governing AI Research Through Peer Review: A Mixed-Methods Study of the Longitudinal Effects of Ethics Flags Across Resubmissions" (arXiv 2609.10740, Sep 9 2026)](https://arxiv.org/abs/2609.10740) — the abstract and the discussion carry the number you need.

**What happened:**

- Two papers this summer measured what happens after a security or AI venue flags a paper on ethics.
- Nishi and colleagues (posted September 9, 2026) took ICLR submissions that were rejected with an ethics flag, followed them to their next submission, and found that in 83% of 446 cases the authors either left the flagged concern unaddressed or revised the paper without changing the method the flag was about; interviews confirmed that authors typically change framing and presentation, not research direction, and the paper recommends that venues require disclosure of prior ethics flags on resubmission.
- Hantke, Mrowczynski, Dralle and Stock (posted July 31, 2026) interviewed twenty members of the security-and-privacy community about the ethics policies at the top venues and concluded that ethics education is the missing piece and that inconsistent, rapidly changing rules across venues push authors toward superficial compliance instead of reflection; their title gives the prescription, "reflection, education, consistency.
- Both are preprints as of Sept 30 2026; the Nishi study is about AI venues, so extrapolating to USENIX or CCS is an inference, not a finding.{B}**What to say:** "Here is the uncomfortable number for anyone who thinks the fix for Hypocrite Commits is a stricter checklist: when a top AI conference flagged a paper on ethics and rejected it, five times out of six the authors resubmitted with the same method and better wording.
- Rules produce compliance; they do not produce reflection.
- That is why today is about principles you can argue from, not a form you fill in.
- Ask: "If you got an ethics flag on your project, what would you actually change, and what would you be tempted to just reword?"{B}**Course tie-in:** This is the evidence for Salganik's ladder: rules without principles are theater.
- It reframes all three cases on this slide (Hypocrite Commits, Carna, Encore) as failures that a checklist would not have caught.
- In the breakout, use the 83% figure to push groups from "add a rule" answers to "which principle would have changed the design" answers.{B}**Also:** [Hantke, Mrowczynski, Dralle & Stock, "Reflection, Education, Consistency: Towards Best Ethics Practices At Security And Privacy Conferences" (arXiv 2608.00282, Jul 31 2026)](https://arxiv.org/abs/2608.00282) — the qualitative companion.

## 5 · A 2026 Lens: AI Bots on Reddit

**Original notes:**

Primary reporting on the Zurich case: [Washington Post — "Reddit slams University of Zurich experiment over secret AI bots" (Apr 30, 2025)](https://www.washingtonpost.com/technology/2025/04/30/reddit-ai-bot-university-zurich/) · [Science/AAAS — "Unethical AI research on Reddit under fire"](https://www.science.org/content/article/unethical-ai-research-reddit-under-fire) · [Retraction Watch — "AI-Reddit study leader gets warning as ethics committee moves to 'stricter review process'" (Apr 29, 2025)](https://retractionwatch.com/2025/04/29/ethics-committee-ai-llm-reddit-changemyview-university-zurich/) · [NBC News](https://www.nbcnews.com/tech/tech-news/reddiit-researchers-ai-bots-rcna203597). The [r/changemyview mod post](https://www.reddit.com/r/changemyview/comments/1k8b2hj/meta_unauthorized_experiment_on_cmv_involving/) and Reddit CLO Ben Lee's response are the primary community-side sources. Casey Fiesler's *"one of the worst violations of research ethics I've ever seen"* quote is from the Science article. Bring back to the [Belmont/Menlo four principles](https://www.dhs.gov/sites/default/files/publications/CSD-MenloPrinciplesCORE-20120803_1.pdf) before you introduce them formally; then anchor the [Breakout A](../../breakouts/ethics.md) prompt.

### Case: the LSE Reddit bot field experiment (July 2026)

> **Read first:** [Oda, Makovi, Yasseri & Tsvetkova, "A field experiment of social influence and behavioral contagion with bots on Reddit" (arXiv 2607.00854, posted Jul 1 2026)](https://arxiv.org/abs/2607.00854) — read the Methods and the ethics paragraph; it is short and the paper is the primary source.

**What happened:**

- A team led from the London School of Economics (Hiroki Oda, Kinga Makovi, Taha Yasseri, Milena Tsvetkova) ran a live field experiment on Reddit and posted the preprint on July 1, 2026.
- They created accounts, some presented as bots and some as "human" (both actually driven by the same automated procedure), and used them to give real users paid, non-anonymous "Diamonds are Forever" awards (about $1 each) on posts across twelve subreddits including r/science, r/explainlikeimfive and r/lifeprotips, varying the stated justification for the award to see whether recipients would pass the behavior on.
- The design had nine conditions with 263 to 275 observations each, 2,442 in total, and the hypotheses were pre-registered.
- The paper states that the design received LSE research ethics approval (Ref. 490807) and that, because the experiment "relied on realistic interventions," the team "did not obtain informed consent from the participants"; it describes "a mild form of deception" in the human-labelled accounts and in the award rationales.
- There is no mention of asking subreddit moderators; the paper cites Reddit's informal "Bottiquette" norm that bots should say so in their usernames.
- The planned debrief is a post on r/all after publication, listing the research accounts and linking the preprint.
- As of Sept 30 2026 the paper is a preprint; I have found no public reaction from Reddit or the affected communities, no retraction, and no statement from LSE, so treat community response and venue status as unknown.{B}**What to say:** "Fourteen months after Zurich blew up, another university ran bots on Reddit users without telling them.
- The difference: this one had an ethics approval number and a pre-registration.
- The awards were real money, the accounts labelled 'human' were bots, and the debrief is a Reddit post that will go up after the paper is out.
- So here is the question I want you to sit with for the rest of the hour: is this the fix for Zurich, or is it the same playbook with paperwork?
- Hold on the ethics-approval detail; students assume approval and consent are the same thing, and this case separates them cleanly.
- Then throw the room: "Which of the four principles does the approval actually satisfy, and which does it not touch?"{B}**Course tie-in:** Respect for persons is the principle under stress (no consent, mild deception, a debrief that reaches only people who happen to read r/all).
- Beneficence looks better than Zurich (gifts rather than manipulation of trauma survivors) but ask who judged that risk; justice asks why users of twelve unrelated subreddits carry the risk for a social-science result; respect for law and public interest turns on Reddit's bot norms and whether a post-hoc debrief is "transparency-based accountability.
- Versus Zurich: same platform, same lack of consent, but approved and far lower harm; versus Emotional Contagion: same "realism requires no consent" argument that Facebook made in 2014.
- In the IRB breakout, hand this to the LLM-field-experiment group as the "approved but not consented" variant and ask them to write the one design change that would make them comfortable.{B}**Also:** [Condom-Tibau, Puccetti, Bacciu, Abrate & Cresci, "Open Platform Field Experiments" (arXiv 2609.21608, Sep 18 2026)](https://arxiv.org/abs/2609.21608) — the methodological framing that makes this kind of intervention routine (full brief in the Emotional Contagion row).

## 6 · Case Study: Emotional Contagion

the [LSE Reddit study (Jul 2026)](https://arxiv.org/abs/2607.00854) is literally a "behavioral contagion" experiment run without consent under an ethics approval; Fiske's 2014 expression of concern reads differently when the experimenters are us (full brief in the 2026 Lens row).

**Original notes:**

Primary source: [Kramer, Guillory, Hancock, "Experimental evidence of massive-scale emotional contagion through social networks," *PNAS* 111(24), 2014](https://www.pnas.org/doi/10.1073/pnas.1320040111). *PNAS* editorial concern: [Fiske, "Editorial Expression of Concern"](https://www.pnas.org/doi/10.1073/pnas.1412469111). Post-hoc coverage: [*The Atlantic* — "Everything We Know About Facebook's Secret Mood-Manipulation Experiment"](https://www.theatlantic.com/technology/archive/2014/06/everything-we-know-about-facebooks-secret-mood-manipulation-experiment/373648/). Frame explicitly as **the 2012 precursor to the 2025 Zurich case** — the pattern is identical, just with generative AI. Cold-call: *"Would an IRB have approved Emotional Contagion with a debrief? Would you have?"*

### Case: Open Platform Field Experiments (September 2026)

> **Read first:** [Condom-Tibau, Puccetti, Bacciu, Abrate & Cresci, "Open Platform Field Experiments: Expanding the Design Space of Experimental Research on Social Media" (arXiv 2609.21608, Sep 18 2026)](https://arxiv.org/abs/2609.21608).

**What happened:**

- On September 18, 2026 a group of computational social scientists posted a methods paper proposing "Open Platform Field Experiments" (OPFEs): because Bluesky and the AT Protocol expose feeds, moderation labels and other functional components to third parties, independent researchers can now "directly intervene on functional platform components" of a live social network rather than only observing it or running bots inside it.
- The paper maps that design space and argues it occupies territory that was previously reachable only by the platforms themselves.
- This is a framework paper, not a report of an experiment on users, and from the abstract it is not clear how the authors handle consent or ethics review for the designs they propose; treat that as unknown and, if you assign the paper, ask students to find the answer.
- It is on arXiv only as of Sept 30 2026.{B}**What to say:** "In 2014 the defense of Emotional Contagion was 'only Facebook could do this, and Facebook tunes the feed all the time.' That defense is now dead.
- On an open protocol, any lab can change what a few thousand people see in their feed, and there is a September 2026 methods paper telling you how.
- So the question on this slide, where is the line between an A/B test and human-subjects research, is now a question about us, not about Meta.
- The detail to land: the phrase "intervene on functional platform components.
- Ask: "If you could change the feed ranking for 5,000 Bluesky users tomorrow to test a hypothesis, what would you need before you were allowed to?"{B}**Course tie-in:** Respect for persons (consent at platform scale) and respect for law and public interest (open protocols have no ToS gate, so the only gate is us).
- Compared with Emotional Contagion: same intervention, different actor; compared with the LSE study: this is the next step from bots-as-users to researchers-as-platform.
- In the breakout, use it as the "what would you require before launching" prompt for whichever group finishes early.{B}**Also:** [LSE Reddit bot study (arXiv, Jul 2026)](https://arxiv.org/abs/2607.00854) — the concrete 2026 experiment that shows the pattern (full brief in the 2026 Lens row).

**Also for this slide:**

## 7 · A Framework, Not a Rulebook (divider)

Moor's "policy vacuum" formulation: [James H. Moor, "What Is Computer Ethics?", *Metaphilosophy* 16(4), 1985](https://onlinelibrary.wiley.com/doi/10.1111/j.1467-9973.1985.tb00173.x). This is the framing text for the entire ICT-ethics literature — worth naming for students who want to read the primary.

## 8 · Key Idea: Digital Is Different

**Original notes:**

The "database of ruin" line is [Paul Ohm, "Broken Promises of Privacy," *UCLA L. Rev.* 57 (2010)](https://www.uclalawreview.org/broken-promises-of-privacy-responding-to-the-surprising-failure-of-anonymization/). *"Social research in the digital age raises different ethical questions":* [Salganik, *Bit by Bit* Ch. 6](https://www.bitbybitbook.com/en/1st-ed/ethics/), one-line thesis. Tie to the [Sweeney re-identification work](https://dataprivacylab.org/projects/identifiability/paper1.pdf) and [Netflix Prize de-anonymization (Narayanan & Shmatikov, 2008)](https://www.cs.utexas.edu/~shmat/shmat_oak08netflix.pdf).

### Case: agentic-LLM re-identification (2026)

> **Read first:** [Li, "Agentic LLMs as Powerful Deanonymizers" (arXiv 2601.05918, Jan 9 2026)](https://arxiv.org/abs/2601.05918); then [Lermen et al., "Large-scale online deanonymization with LLMs" (arXiv 2602.16800, Feb 2026)](https://arxiv.org/abs/2602.16800).

**What to say:**

- "Ohm's 'database of ruin' was a warning about what could be linked if someone tried.
- In January 2026 someone tried with a chatbot and a search box, on an AI company's own anonymized interview release, and linked six of twenty-four interviews to named scientists; a month later a Zurich-and-Google team linked pseudonymous accounts across sites at 68% recall.
- The capability now outruns the rules by a wider margin than Moor could have imagined.
- Ask: "What in your own online footprint would survive an agent with a search box?"

**Course tie-in:**

- This is the slide's thesis with a timestamp: capabilities outrun rules.
- Beneficence (informational risk) is the principle; the Weld and Netflix cases below are the ancestors.
- Full brief (What happened, status, supporting links): see the **Beneficence and Justice in Practice** row.

## 9 · Salganik's Layered Approach

**Original notes:**

Direct from [Salganik, *Bit by Bit* Ch. 6](https://www.bitbybitbook.com/en/1st-ed/ethics/) — the frameworks→principles→rules figure. This is the diagram to return to whenever a student says "but is it legal?" — rules are the floor.

### Case: ethics flags do not change methods (Nishi, Sep 2026; Hantke, Jul 2026)

> **Read first:** [Nishi et al. (arXiv 2609.10740, Sep 9 2026)](https://arxiv.org/abs/2609.10740); [Hantke et al. (arXiv 2608.00282, Jul 31 2026)](https://arxiv.org/abs/2608.00282).

**What to say:**

- "This diagram says rules sit on principles sit on frameworks.
- Here is what happens when you keep only the top layer: 83% of ethics-flagged ICLR papers came back with the same method and better wording.
- A rule you cannot argue from is a rule you route around.
- Ask: "Which layer would have stopped Hypocrite Commits?"

**Course tie-in:**

- The empirical case for teaching principles rather than checklists; use it every time a student says "but the IRB approved it.
- Full brief (What happened, status, supporting links): see the **Why This Hits Close to Home** row.

## 10 · IRB, Belmont, Menlo

**Original notes:**

Primary sources: [Belmont Report (1979) — HHS](https://www.hhs.gov/ohrp/regulations-and-policy/belmont-report/index.html) · [Menlo Report (2012) — DHS S&T](https://www.dhs.gov/sites/default/files/publications/CSD-MenloPrinciplesCORE-20120803_1.pdf) · [Menlo Companion](https://www.caida.org/publications/papers/2013/menlo_report_companion/menlo_report_companion.pdf). Lineage: [Nuremberg Code (1947)](https://media.tghn.org/medialibrary/2011/04/BMJ_No_7070_Volume_313_The_Nuremberg_Code.pdf) → [Helsinki (1964)](https://www.wma.net/policies-post/wma-declaration-of-helsinki-ethical-principles-for-medical-research-involving-human-subjects/) → Tuskegee → NRA 1974 → Belmont 1979 → Common Rule → Menlo 2012. Related work: [Kenneally & Dittrich (Menlo authors) — "Applying the Menlo Report," *Communications of the ACM* (2015)](https://cacm.acm.org/magazines/2012/1/144826-toward-a-common-language-for-computer-security/fulltext).

### Case: OHRP's pending Common Rule revision (2026)

> **Read first:** [Advarra, "2026 DHHS Unified Agenda: Four Areas HRPP and IRB Leaders Should Watch" (Sep 28 2026)](https://www.advarra.com/blog/2026-dhhs-unified-agenda-four-areas-hrpp-and-irb-leaders-should-watch/) — the most current plain-language summary; the regulatory text itself does not exist yet.

**What happened:**

- The 2026 HHS Unified Agenda lists a planned Notice of Proposed Rulemaking from the Office for Human Research Protections to revise 45 CFR 46, the Common Rule.
- According to OHRP's own agenda entry, the proposal would expand the exemption categories to cover additional kinds of low-risk research, allow lighter-touch review of de minimis protocol changes rather than full-board reconsideration, and clarify terms such as "undue influence"; OHRP's stated goal is to let IRBs concentrate on higher-risk studies, and its entry acknowledges a risk of reduced oversight and inconsistent institutional implementation.
- The NPRM was scheduled for July 2026 but as of Advarra's September 28, 2026 write-up the text had not been published, so nobody yet knows which activities would become exempt or how the change interacts with FDA-regulated research.
- Separately, in March 2026 OHRP updated the Federalwide Assurance to implement burden-reducing provisions of the 2018 revised rule.
- Status as of Sept 30 2026: proposal pending, no text, no comment period open.{B}**What to say:** "The rules layer is moving under your feet.
- HHS wants to make more low-risk research exempt from IRB review, which sounds like good news for everyone in this room who scrapes public data or scans the Internet.
- But watch the trap: 'exempt' is a determination about the regulations, not about ethics, and most of the security research we will discuss this term is exempt or out of scope already.
- The IRB not looking at your study is not the same as your study being fine.
- Detail to keep: the NPRM was due in July and has not appeared.
- Ask: "If your scan or scrape is exempt, who is the reviewer?"{B}**Course tie-in:** This is the "rules" layer of Salganik's ladder and the reason Menlo exists: Belmont-era rules did not anticipate scanning or scraping, and an exemption expansion widens that gap. Compared with Tuskegee it is the pendulum swinging the other way (from too little oversight, to a full apparatus, to trimming it).
- In the breakout, ask each group whether their case would even reach an IRB under an expanded exemption regime.{B}**Also:** [Eto, Miller, Vidal & Lifson, "Streamlining IRB review of AI human subjects research: the three-stage framework" (Frontiers, Mar 6 2026)](https://www.frontiersin.org/journals/systems-biology/articles/10.3389/fsysb.2026.1804193/full) — how IRBs are trying to stage review for AI studies.
- Science, "Ethicists flirt with AI to review human research" (Sep 2025): no IRB has formally put an LLM in the loop yet, though pilots caught most reviewer-flagged problems (URL not verifiable this session).

## 11 · The Four Principles

**Live worked example to run all four on:** the [LSE Reddit bot study (arXiv, Jul 2026)](https://arxiv.org/abs/2607.00854) — respect for persons (no consent, mild deception), beneficence (paid awards, arguably minimal harm, but who judged?), justice (users of 12 unrelated subreddits bore the risk; who benefits?), respect for law and public interest (Reddit's bot norms; a post-hoc r/all debrief as "transparency"). Full brief in the **A 2026 Lens: AI Bots on Reddit** row. What to say: "Approval is not consent. Which principle does the approval number actually buy you?"

**Original notes:**

Text of the four principles is directly from [Belmont §B](https://www.hhs.gov/ohrp/regulations-and-policy/belmont-report/read-the-belmont-report/index.html) and [Menlo §II](https://www.dhs.gov/sites/default/files/publications/CSD-MenloPrinciplesCORE-20120803_1.pdf). Drill the *beneficence is not "do no harm"* point — students consistently misremember it. Cold-call: *"Give me a study that is beneficent but doesn't respect persons — and vice versa."*

## 12 · Respect for Persons: Informed Consent

**Original notes:**

The Zurich vignette explicitly fails this principle twice (undisclosed AI, fabricated identities). Related literature: [Nissenbaum, "Privacy as Contextual Integrity," *Wash. L. Rev.* 79 (2004)](https://digitalcommons.law.uw.edu/wlr/vol79/iss1/10/) — consent is not context-free. Bridge to the later dark-patterns thread (Lecture 11 / [Privacy Law](../11-PrivacyLaw/slides.qmd)).

### Case: the NeurIPS 2026 AI-assisted reviewing experiment (opt-in, IRB-exempt)

> **Read first:** [NeurIPS 2026, "AI-Assisted Reviewing Experiment" (official conference page)](https://neurips.cc/Conferences/2026/ai-reviewing-experiment) — the design, the IRB determination and the consent language are all on one page.

**What happened:**

- For its 2026 cycle NeurIPS is running a randomized experiment on its own peer review.
- For each paper, reviewers are independently assigned to one of three conditions: unassisted review with no LLM access, open-ended LLM assistance inside the OpenReview interface, or structured LLM assistance with proactive task suggestions.
- The stated purpose is to study how reviewers do and could use large language models during review, with the explicit line that "human judgement is augmented, not replaced.
- The University of Texas at Austin IRB determined the study exempt under the tests, surveys, interviews or observation category (Protocol STUDY00009083).
- Participation is opt-in on both sides: authors choose at submission whether to include their paper, reviewers volunteer through a recruitment form, and the page states participation "will have no bearing on paper decisions or other outcomes of the conference"; LLM providers are used under zero-data-retention terms.
- The conference is in December 2026, so results are not out as of Sept 30 2026, and the open question is whether opt-in produces a representative sample or just the reviewers who already like LLMs.{B}**What to say:** "Same year, same field, two answers to 'can we get consent.' NeurIPS wanted to know what happens when reviewers use an LLM, so it randomized reviewers, got an IRB determination, and made both authors and reviewers opt in, with a promise that it cannot affect your paper's fate.
- The LSE team wanted to know whether Reddit users pass on kindness, and decided realism required not asking.
- Neither is obviously wrong.
- But only one of them could have run with consent and chose not to.
- Ask: "Which of these two would you sign off on, and is 'consent would ruin the realism' ever enough on its own?"{B}**Course tie-in:** Respect for persons, in its positive form: this is what "obtain informed consent where possible" looks like at scale.
- Compared with Zurich and the LSE study it is the control case; compared with Emotional Contagion it answers the 2014 question ("could Facebook have asked?") with a yes.
- In the breakout, give it to the LLM-field-experiment group as the design they have to beat.{B}**Also:** [LSE Reddit bot study (arXiv, Jul 2026)](https://arxiv.org/abs/2607.00854) — the no-consent counterpart (full brief in the 2026 Lens row).

## 13 · Beneficence and Justice in Practice

**Original notes:**

Concepts to review: [de-identification failure — Sweeney (1997)](https://dataprivacylab.org/projects/identifiability/paper1.pdf); [Netflix Prize re-identification — Narayanan & Shmatikov (2008)](https://www.cs.utexas.edu/~shmat/shmat_oak08netflix.pdf); [Strava heatmap OPSEC failure (2018)](https://www.washingtonpost.com/world/a-map-showing-the-users-of-fitness-devices-lets-the-world-see-where-us-soldiers-are-and-what-they-are-doing/2018/01/28/86915662-0441-11e8-aa61-f3391373867e_story.html). Power analysis / underpowered studies: [Button et al., "Power failure," *Nature Reviews Neuroscience* (2013)](https://www.nature.com/articles/nrn3475) — the underpowered-study-as-ethics-problem framing.

### Case: agentic-LLM re-identification (January and February 2026)

> **Read first:** [Tianshi Li, "Agentic LLMs as Powerful Deanonymizers: Re-identification of Participants in the Anthropic Interviewer Dataset" (arXiv 2601.05918, Jan 9 2026)](https://arxiv.org/abs/2601.05918) — short, concrete, and the one students will remember.

**What happened:**

- On December 4, 2025 Anthropic released "Anthropic Interviewer," a tool for running qualitative interviews at scale, together with a public dataset of 1,250 interview transcripts with professionals, including 125 scientists, about how they use AI in their work.
- On January 9, 2026 Tianshi Li posted a preprint showing that off-the-shelf LLM agents with web search could take a sampled interview, extract the details a scientist gives about their own work, search for matching publications, and link six of twenty-four sampled interviews to specific papers, recovering the authors and in some cases uniquely identifying the interviewee; a broader pass reported by the paper identified nine of the 125 scientists after manual checking.
- The models' built-in refusals were bypassed simply by splitting the task into benign-looking steps (summarize, search, compare).
- The author reports notifying Anthropic.
- Then on February 18, 2026 Lermen, Paleka, Swanson, Aerni, Carlini and Tramèr posted "Large-scale online deanonymization with LLMs," a three-step pipeline (extract identifying features, retrieve candidates by embedding, verify) that linked pseudonymous accounts across platforms, Hacker News to LinkedIn and split Reddit histories, at up to 68% recall at 90% precision where the best non-LLM method was near zero.
- Neither paper has been peer-reviewed as of Sept 30 2026, and I have not seen a public response from Anthropic beyond the reported clarification that participants had consented to release of raw transcripts.{B}**What to say:** "Every de-identification story on this slide, Weld's hospital records, the Netflix Prize, the Strava heatmap, needed a clever researcher with an auxiliary dataset.
- In January somebody did it to an AI company's own 'anonymized' interview release with a chatbot and a search box, and the model's safety filter was defeated by asking three innocent questions instead of one bad one.
- So 'anonymized' is no longer a property of the file; it is a claim about what an agent can find.
- The detail to keep: six of twenty-four, by decomposition.
- Then ask: "You are releasing interview transcripts for your project.
- What is your threat model now, and what would you have to strip to survive it?"{B}**Course tie-in:** Beneficence (informational risk is the harm; open data increases benefit and risk at once, which is the slide's bullet) and justice (the interviewees bore a risk the releasing company did not).
- Compared with Tuskegee it is harm without intent, which is exactly the "violations occur even in benign studies" line on the consent slide.
- For the breakout, this is the mitigation prompt: k-anonymity, differential privacy and retention plans are the tools, and the group should say which one would have helped here.{B}**Also:** [Lermen et al., "Large-scale online deanonymization with LLMs" (arXiv 2602.16800, Feb 2026)](https://arxiv.org/abs/2602.16800) — the scale result (68% recall at 90% precision).

## 14 · Respect for Law and Public Interest

**Original notes:**

ToS-vs-ethics tension: the classic case is [ProPublica's 2016 Facebook ad discrimination audit](https://www.propublica.org/article/facebook-lets-advertisers-exclude-users-by-race), which arguably violated ToS but exposed genuine discrimination. Companion: [ACLU v. Clapper on ToS + research](https://www.aclu.org/cases/sandvig-v-barr-challenge-cfaa-prohibition-uncovering-racial-discrimination-online). "Transparency-based accountability" is a defined Menlo term — [Menlo §II.D](https://www.dhs.gov/sites/default/files/publications/CSD-MenloPrinciplesCORE-20120803_1.pdf).

### Case: DSA Article 40 vetted-researcher data access (2025 to 2026)

> **Read first:** [Jacob van de Kerkhof, "Unpacking the EU's Digital Services Act Delegated Regulation on Data Access" (Tech Policy Press, Jul 8 2025)](https://www.techpolicy.press/unpacking-the-eus-digital-services-act-delegated-act-on-data-access-/) — the clearest account of what the mechanism does and where it still fails.

**What happened:**

- Article 40 of the EU Digital Services Act (2022) requires very large online platforms and search engines to give vetted researchers access to internal data for studying systemic risks, and lets researchers using only public data collect it without platform permission.
- The European Commission adopted the delegated regulation spelling out the procedure in July 2025, and applications have been possible since late October 2025: a researcher applies through a national Digital Services Coordinator, the platform can object under Article 40(5) on grounds such as trade secrets or security, and the coordinator adjudicates.
- Van de Kerkhof's analysis identifies three unresolved problems: the "data stand-off" (researchers must specify what they need without seeing what exists, and there is little way to check a platform's objection), personal-data protection when data flows to institutions outside the EU, and uneven capacity and timelines across national coordinators.
- A 2026 Political Communication article, "Finally, Access: How Article 40 DSA Changes Platform Research in Practice," reports the first year of use: implementation has been inconsistent, narrow in scope and contested across member states.
- As of Sept 30 2026 the mechanism is live, but how many requests have been granted and against which platforms is not publicly tallied, so treat throughput as unknown.{B}**What to say:** "The Menlo principle on this slide says obey the terms of service, unless breaking them is defensible in the public interest, and for a decade the only way to audit a platform was to break its ToS and hope, like ProPublica did.
- Europe has now built the legal front door: a vetted researcher can demand the data and the platform has to argue to a regulator why not.
- It is slow and contested, but it changes the ethics: if a lawful route exists and you scrape anyway, 'defensible violation' is a harder argument.
- Detail to keep: the platform objects, the regulator decides.
- Ask: "If Article 40 existed in the U.S., would ProPublica's 2016 audit still be defensible?"{B}**Course tie-in:** Respect for law and public interest, both halves: compliance (a legal route now exists) and transparency-based accountability (applications are on the record).
- Compared with hiQ v. LinkedIn on the later slide, this is the non-U.S. counterpart: hiQ says scraping public data is not a crime, Article 40 says platforms must hand over non-public data.
- In the breakout, the privacy-regulation-compliance group should ask whether their scenario would go through Article 40 or around it.{B}**Also:** Brown, Gruen, Maldoff, Messing, Sanderson & Zimmer, "Web scraping for research: Legal, ethical, institutional, and scientific considerations," *Big Data & Society* (2025) — the U.S.-side framing for scraping decisions (URL not verifiable this session).
- [USENIX Security '26 CFP](https://www.usenix.org/conference/usenixsecurity26/call-for-papers) — transparency-based accountability made mandatory in the field's own venue (full brief in the Why Ethics row).

## 15 · Two Underlying Frameworks

**Live 2026 split to diagnose: Microsoft vs. "Nightmare Eclipse."** The researcher's defenders argue consequences (Microsoft closed the reporting channel, users are better off knowing, vendors only move under pressure), while Microsoft argues duty ("uncoordinated disclosures ... are never justifiable") and its critics argue duty too (a company must not threaten researchers). What to say: "Before you pick a side, name the framework each side is using. Consequentialists have to answer for the three exploited-in-the-wild bugs; deontologists have to say whether a vendor has a duty to keep the reporting channel open." Full brief in the **Ethics ≠ Law** row.

**Original notes:**

Consequentialism: [Bentham, *An Introduction to the Principles of Morals and Legislation* (1789)](https://www.econlib.org/library/Bentham/bnthPML.html); [Mill, *Utilitarianism* (1861)](https://www.utilitarianism.com/mill1.htm). Deontology: [Kant, *Groundwork of the Metaphysics of Morals* (1785)](https://www.earlymoderntexts.com/assets/pdfs/kant1785.pdf). The point isn't to pick a team — it's to notice which framework the *speaker* is using so debates become tractable.

## 16 · Ethics ≠ Law

**Original notes:**

The quoted definition is a paraphrase of the working definition in [Bynum, "Computer and Information Ethics" — Stanford Encyclopedia of Philosophy](https://plato.stanford.edu/entries/ethics-computer/). Historical case: [Aaron Swartz + CFAA overreach](https://www.eff.org/deeplinks/2013/01/aaron-swartz-and-computer-fraud-abuse-act-hackers-heroes-or-felons) — legal-but-not-ethical prosecution. Cold-call: *"Name a research practice that is currently legal that you think will be considered clearly unethical in 20 years."*

**Marquee 2026 case: Microsoft vs. "Nightmare Eclipse" (April to September 2026).**

> **Read first:** [TechCrunch, "Microsoft under fire for threatening security researcher with criminal investigation" (May 29 2026)](https://techcrunch.com/2026/05/29/microsoft-under-fire-for-threatening-security-researcher-with-criminal-investigation/) — the most complete single account of the threat and the backlash.

**What happened:**

- Beginning in early April 2026 an anonymous researcher posting as "Nightmare Eclipse" began publishing working exploit code for unpatched Windows vulnerabilities, mostly in Microsoft Defender and BitLocker, on GitHub and GitLab, typically timed to Patch Tuesday; by late May there were six (BlueHammer, RedSun, UnDefend, YellowKey, GreenPlasma, MiniPlasma), and The Register reported three were being exploited in the wild within days.
- The researcher's stated grievance is that Microsoft deleted their Microsoft Security Response Center reporting account and withheld bounties they had earned, which closed the coordinated-disclosure channel; Microsoft has not publicly confirmed or denied deleting the account.
- On May 28, 2026 Microsoft published a blog post saying "uncoordinated disclosures that put proof-of-concept code for unpatched vulnerabilities into the hands of bad actors are never justifiable" and pointing to its Digital Crimes Unit, warning of legal action and law-enforcement referral; Katie Moussouris, who built Microsoft's original bounty program, called the threat "over the top" and warned of a chilling effect, and Kevin Beaumont called it "a dumpster fire of its own making.
- On June 1 MSRC issued a clarification that it has "no intention to pursue action against individuals conducting or publishing their security research" and would escalate only against "malicious activity causing real harm to our customers.
- The drops did not stop: RoguePlanet (CVE-2026-50656) in July, then ShieldBreak (CVE-2026-69414) hours after the August Patch Tuesday bypassing the July fix, then ShieldCrash days after the September Patch Tuesday, per Dark Reading and TechRepublic reporting; roughly ten in total.
- Still unknown as of Sept 30 2026: the researcher's identity (they have claimed to be a former MSRC contractor; unverified), whether the bounty claims are accurate, and whether any legal action is actually contemplated.{B}**What to say:** "Here is a case where the law and the ethics point in different directions on both sides at once.
- A researcher, angry that Microsoft cut off the only channel for reporting bugs, dropped six working zero-days in six weeks; three were used against real people within days.
- Microsoft's response was to threaten criminal prosecution, then take it back four days later when the people who built its own bounty program said it would scare off every honest researcher.
- Was the threat legal?
- Probably.
- Was it ethical?
- The industry said no.
- Were the drops legal?
- Publishing a bug is speech.
- Were they ethical?
- Three of them got users hurt.
- Detail to keep: the four-day walk-back.
- Ask: "Assign the four principles to each side.
- Who violated what?"{B}**Course tie-in:** Respect for law and public interest cuts both ways (the researcher ignored the public-interest half; Microsoft used the law half as a weapon), and beneficence is the researcher's failure (users exposed to no research benefit).
- This is a disclosure case, not a human-subjects case, so it complements Zurich and Emotional Contagion rather than repeating them, and it connects directly to the CFAA debate later in the term.
- In the breakout it is the prompt for the coordinated-versus-full-disclosure group: what should each side have done differently, and at what point?{B}**Also:** [The Register, "Disgruntled 0-day hunter 'humiliated' by Microsoft pledges 'bone shattering drop' as Redmond calls cops" (May 28 2026)](https://www.theregister.com/security/2026/05/28/microsoft-0-day-feud-escalates-as-researcher-threatens-another-windows-exploit-dump/5248085) — the researcher's own framing and the in-the-wild exploitation detail.
- [Cybersecurity News, "Microsoft Clarifies It Won't Sue Security Researchers" (Jun 1 2026)](https://cybersecuritynews.com/microsoft-clarifies-nightmare-eclipse-controversy/) — the walk-back text.

## 17 · Laws Every Security Researcher Should Know

**Two 2026 anchors for this slide.** **Case: tenth triennial §1201 rulemaking.** Read first: [Copyright Office announcement (NewsNet 1088, Jun 9 2026)](https://www.copyright.gov/newsnet/2026/1088.html). What to say: "The DMCA line on this slide, 'long a threat to vulnerability research,' is managed by a temporary exemption that must be re-petitioned every three years; petitions for the next cycle were due August 24 and comments September 28, two days ago." Course tie-in: compliance is a moving target; full brief in the **The Law Is (Slowly) Catching Up** row.

Read first: [TechCrunch (May 29 2026)](https://techcrunch.com/2026/05/29/microsoft-under-fire-for-threatening-security-researcher-with-criminal-investigation/). What to say: "The chilling effect on this slide is not theoretical: in May a vendor's legal unit threatened a researcher with criminal referral over publishing bugs, and the person who built that vendor's own bounty program called it 'over the top' and said it would scare off honest reporters. Four days later the vendor took it back." Course tie-in: the fear of CFAA and DMCA liability (Mayer et al.) is what the walk-back was about; full brief in the **Ethics ≠ Law** row.

**Original notes:**

Primary text: [CFAA — 18 U.S.C. §1030](https://www.law.cornell.edu/uscode/text/18/1030) · [DMCA §1201 — 17 U.S.C. §1201](https://www.law.cornell.edu/uscode/text/17/1201) · [ECPA — 18 U.S.C. §§2510–2523](https://www.law.cornell.edu/uscode/text/18/part-I/chapter-119) · [FERPA — 20 U.S.C. §1232g](https://www2.ed.gov/policy/gen/guid/fpco/ferpa/index.html) · [HIPAA Privacy Rule](https://www.hhs.gov/hipaa/for-professionals/privacy/index.html). Chilling-effect literature: [Mayer et al., "Continuous Compliance," *Science* (2019)](https://www.science.org/doi/10.1126/science.aaw4045). Practical playbook: [EFF's "Coders' Rights Project" grey-hat guide](https://www.eff.org/issues/coders/reverse-engineering-faq). This slide sets up the [CFAA debate](../../debates/cfaa.md) that recurs in Lecture 7.

### Case: Microsoft's prosecution threat (May 2026)

## 18 · The Law Is (Slowly) Catching Up

**Original notes:**

Primary: [*Van Buren v. United States*, 593 U.S. 374 (2021) — opinion](https://www.supremecourt.gov/opinions/20pdf/19-783_k53l.pdf) · Wikipedia: [Van Buren v. United States](https://en.wikipedia.org/wiki/Van_Buren_v._United_States). [*hiQ Labs v. LinkedIn* — 9th Cir. remand (2022)](https://cdn.ca9.uscourts.gov/datastore/opinions/2022/04/18/17-16783.pdf). [DOJ Press Release, May 19, 2022 — "Department of Justice Announces New Policy for Charging Cases under the Computer Fraud and Abuse Act"](https://www.justice.gov/opa/pr/department-justice-announces-new-policy-charging-cases-under-computer-fraud-and-abuse-act). [DMCA §1201 security-research exemption — U.S. Copyright Office, 2024 rulemaking](https://www.copyright.gov/1201/2024/). EFF context on Van Buren: [EFF — "Victory! Supreme Court Rules Against Overbroad Interpretation of CFAA"](https://www.eff.org/deeplinks/2021/06/van-buren-victory-computer-fraud-abuse-act). Emphasize: narrower CFAA ≠ ethical clearance; **contract, copyright, and GDPR** claims are the current live risks (per the White & Case + Berkeley CLTC 2022–2026 write-ups).

### Case: the tenth triennial §1201 rulemaking (opened June 2026)

> **Read first:** [U.S. Copyright Office, "U.S. Copyright Office Announces Start of Tenth Triennial Rulemaking Proceeding Under Section 1201" (NewsNet 1088, Jun 9 2026)](https://www.copyright.gov/newsnet/2026/1088.html) — the official announcement with every deadline.

**What happened:**

- Section 1201 of the DMCA bans circumventing technical access controls, and every three years the Librarian of Congress, on the Register of Copyrights' recommendation, grants temporary exemptions.
- The ninth round (final rule October 2024) renewed the good-faith security-research exemption that researchers rely on to reverse-engineer devices and software; it also, per contemporaneous reporting, declined a proposed new exemption for research into AI system trustworthiness.
- On June 9, 2026 the Office published a notice of inquiry (Federal Register document 2026-11545) opening the tenth round: petitions to renew existing exemptions and petitions for new ones were due August 24, 2026, written comments responding to renewal petitions were due September 28, 2026, and any renewed exemption will run from October 2027 to October 2030.
- As in prior rounds the Office is using a streamlined renewal process: if no one meaningfully opposes a renewal petition, the exemption is expected to be recommended for renewal without a full evidentiary fight.
- So as of Sept 30 2026 the petition and renewal-comment windows have just closed; which petitions were filed, whether anyone opposed the security-research renewal, and whether expansions were requested are all on regulations.gov but not yet summarized by the Office, so treat the outcome as pending until the final rule in late 2027.{B}**What to say:** "Two days ago the comment window closed on whether you will still be allowed, in law, to pull apart a device to find its bugs after October 2027.
- That permission is not in the statute; it is a temporary exemption that has to be re-argued every three years, and it exists because people in this field filed petitions.
- The point of the slide is that the law is catching up, and this is what catching up looks like in practice: slowly, in triennial cycles, by petition.
- Detail to keep: it expires and must be renewed.
- Ask: "What would you have written in a petition for a new exemption this August, and for what kind of research?"{B}**Course tie-in:** Respect for law and public interest, compliance half; also the Ethics ≠ Law point in reverse, because here the community's norms (coordinated disclosure, good-faith research) are what the law is slowly encoding.
- Compared with Van Buren and hiQ on the same slide, this is the DMCA track rather than the CFAA track, and it is the one with a deadline.
- For the breakout, it is context for the Carna group: even a fully legal scan is not a fully ethical one, and vice versa.{B}**Also:** [Copyright Office, "Tenth Triennial Section 1201 Proceeding, 2027 Cycle"](https://www.copyright.gov/1201/2027/) — the docket page with the renewal petitions and links to public comments.
- CDT, "Security Research and the DMCA: The Copyright Office streamlines the exemption process" — why streamlined renewal matters for researchers (URL not verifiable this session).
- [Copyright Office, 2024 rulemaking page](https://www.copyright.gov/1201/2024/) — the ninth-round exemption that is up for renewal.

## 19 · Codes, Contracts, and Other Standards

**Original notes:**

[ACM Code of Ethics (2018 revision)](https://www.acm.org/code-of-ethics) · [IEEE Code of Ethics](https://www.ieee.org/about/corporate/governance/p7-8.html) · [Nuremberg Code (1947)](https://media.tghn.org/medialibrary/2011/04/BMJ_No_7070_Volume_313_The_Nuremberg_Code.pdf) · [Declaration of Helsinki (2013 revision)](https://www.wma.net/policies-post/wma-declaration-of-helsinki-ethical-principles-for-medical-research-involving-human-subjects/). EULA case study: [Vizio TV FTC consent decree (2017)](https://www.ftc.gov/enforcement/cases-proceedings/162-3024/vizio-inc) — an EULA can bind you to surveillance you didn't notice.

### Case: AMD's out-of-scope bounty denial and retroactive gag terms (February to June 2026)

> **Read first:** [TechSpot, "AMD changes rules, denies researcher $10,000 bounty after taking 124 days to patch security flaw" (Jun 12 2026)](https://www.techspot.com/news/112746-amd-changes-rules-denies-researcher-10000-bounty-after.html) — the fullest timeline including the rule change.

**What happened:**

- On February 6, 2026 a researcher known as MrBruh reported to AMD's bug-bounty program that AMD's software auto-updater fetched executables over unencrypted HTTP without proper signature verification, so a network attacker in a man-in-the-middle position could deliver arbitrary code; the flaw was later assigned CVE-2026-40677 with a CVSS 4.0 score of 7.7.
- AMD closed the report as "out of scope" because man-in-the-middle attacks were excluded by the program's rules and the affected tools were optional, declined the $10,000 bounty the program advertised for findings of that severity, and asked the researcher to take down a blog post, which he did.
- The embargo then ran 124 days, until June 9, 2026, against the customary 90.
- After the researcher published, AMD updated its bug-bounty terms so that non-disclosure obligations now also cover reports it deems ineligible, which critics read as removing the one lever researchers have when a vendor stalls.
- TechSpot also reports the patch may be incomplete (a CRC32 check rather than a cryptographic signature).
- Status as of Sept 30 2026: no bounty paid, terms changed, AMD has not publicly reversed; whether the fix is sufficient is disputed.{B}**What to say:** "Here is the small-print version of the law-and-public-interest principle.
- A researcher finds that a chip vendor's updater will run anything a coffee-shop attacker hands it.
- The vendor says that is out of scope, refuses the bounty, takes four months to fix it, and then rewrites its contract so the next researcher cannot even say that a report was refused.
- Nothing here is illegal.
- All of it is a contract you click through when you submit.
- Detail to keep: the terms were changed after the fact.
- Ask: "Should you sign a bounty agreement that can be amended retroactively?
- What is your alternative?"{B}**Course tie-in:** Contracts as the everyday form of respect for law and public interest, and beneficence from the vendor's side (users exposed for 124 days).
- Compared with the Microsoft case it is the quiet version: no zero-day drop, no prosecution threat, just a contract.
- In the breakout, pair it with Microsoft for the disclosure group and ask which vendor behavior is worse for the ecosystem.{B}**Also:** Tom's Hardware and SC Media covered the same dispute (URLs not verified this session).

### Case: curl ends its bug bounty over AI-generated reports (January 2026)

> **Read first:** [The Register, "Curl shutters bug bounty program to remove incentive for submitting AI slop" (Jan 21 2026)](https://www.theregister.com/security/2026/01/21/curl-shutters-bug-bounty-program-to-stop-ai-slop/5063039).

**What happened:**

- Daniel Stenberg, lead maintainer of curl, announced on January 21, 2026 that the project's six-year HackerOne bug bounty would end on January 31, 2026.
- He had been complaining publicly since early 2024 about AI-generated vulnerability reports that read plausibly and contain nothing; in the week before the announcement the project received seven submissions, none describing a real vulnerability, and the load on the volunteer security team had become unsustainable.
- Stenberg's stated aim was to remove the financial incentive for low-effort submissions while continuing to accept genuine reports, and he reserved the right to publicly criticize bad ones while acknowledging that submitters are often "ordinary misled humans.
- BleepingComputer's coverage put the program's lifetime output at 87 confirmed flaws and over $100,000 paid (figure from press, not verified here).
- As of Sept 30 2026 the bounty remains closed.{B}**What to say:** "Bounty programs are the contract layer of disclosure ethics, and here is one collapsing from the other side: not a vendor stiffing a researcher, but researchers, or people with a chatbot, drowning a volunteer maintainer in fake findings for money.
- The incentive that was supposed to make disclosure ethical made it worse.
- Ask: "Is submitting an AI-generated bug report you have not verified a research-ethics violation, and against whom?"{B}**Course tie-in:** Beneficence and respect for persons applied to maintainers as stakeholders, which is exactly what the USENIX appendix asks you to name.
- It is the 2026 echo of Hypocrite Commits: open-source maintainers as unconsenting subjects of other people's incentives.

### Case: ethics appendices become mandatory at security venues (2025 to 2026)

> **Read first:** [USENIX Security '26 Call for Papers, ethics section](https://www.usenix.org/conference/usenixsecurity26/call-for-papers) — read the "Ethical Considerations" requirements; they are the rubric your students will face.

**What happened:**

- Starting with the 2025 cycle, and hardened for the 35th USENIX Security Symposium (2026), every submission must include a separate appendix titled "Ethical Considerations" containing a stakeholder-based analysis: authors must name all potentially affected parties ("people, including the research team and society at large, and entities including companies"), state the ethical principles they applied, identify potential harms, describe mitigations, and explain why they decided to proceed and to publish.
- The CFP says the chairs may desk-reject papers for a missing or inadequate statement, including for naming the appendix incorrectly, and warns that the analysis must be done early rather than written retroactively to justify a decision already made.
- Help Net Security (Sep 8 2025) reported the Purdue and Carnegie Mellon framework behind the requirement and noted that IEEE S&P and ACM CCS have moved the same way; reporting at the time said more than a fifth of first-cycle 2025 rejections were for missing ethics sections (that figure is from press coverage, not USENIX).
- ACM CCS 2026 published a between-cycle transparency report on GitHub: 1,206 submissions, 981 reaching review, 191 accepted (15.8% including desk rejects), and 225 desk rejections, of which 122 were for missing open-science artifact sections, 59 for format, 41 for hallucinated references, 19 for anonymity breaches and 13 for missing ethics sections; the report says most were honest mistakes.
- ACM IMC 2026 (Oct 12 to 16, 2026) requires an ethics section in every accepted paper.
- Status as of Sept 30 2026: in force at all three venues; the open question, per the Hantke and Nishi papers, is whether it changes designs or only prose.{B}**What to say:** "If you publish in this field you will write one of these appendices, and the chairs can reject you without review if it is missing or if you named it wrong.
- So today is not a values lecture; it is the vocabulary for a document you will be required to produce.
- Note the numbers from CCS: 13 papers bounced for no ethics section, and 41 for citations that were hallucinated by an AI tool.
- Both are the same failure: nobody thought about who could be harmed by what they were submitting.
- Detail to keep: desk rejection.
- Ask: "Name three stakeholders of your term project that are not you and not the user."{B}**Course tie-in:** Respect for law and public interest, transparency-based-accountability half, institutionalized.
- Compared with the Encore signing statement (2015) this is the community moving from reviewers writing a protest note to venues requiring the analysis up front.
- In the breakout, the report-out template is literally the USENIX appendix: stakeholders, harms, mitigations, decision.{B}**Also:** [ACM CCS 2026 Between-Cycle Transparency Report (GitHub)](https://github.com/ACM-CCS-2026/Transparency-Report) — the desk-reject numbers.
- [Help Net Security, "Cybersecurity research is getting new ethics rules" (Sep 8 2025)](https://www.helpnetsecurity.com/2025/09/08/cybersecurity-research-ethics/) — the framework and the venue landscape.
- [ACM IMC 2026 CFP](https://conferences.sigcomm.org/imc/2026/cfp/) — dates and pointer to the ethics requirements.
- Then read the Nishi and Hantke briefs in the Close to Home row for whether any of this changes behavior.

## 20 · Breakout: Apply the Four Principles

**Fresh 2026 prompts (full briefs in the rows named).** Disclosure sub-breakout: Microsoft vs. "Nightmare Eclipse" ([TechCrunch, May 2026](https://techcrunch.com/2026/05/29/microsoft-under-fire-for-threatening-security-researcher-with-criminal-investigation/); **Ethics ≠ Law** row) and AMD's out-of-scope bounty denial with retroactive silence terms ([TechSpot, Jun 2026](https://www.techspot.com/news/112746-amd-changes-rules-denies-researcher-10000-bounty-after.html); **Codes, Contracts** row) — ask each group which vendor behavior is worse for the ecosystem and what the researcher should have done at day 90. LLM/bot field-experiment sub-breakout: contrast the [LSE Reddit study (Jul 2026)](https://arxiv.org/abs/2607.00854) (**2026 Lens** row) with the [NeurIPS 2026 opt-in experiment](https://neurips.cc/Conferences/2026/ai-reviewing-experiment) (**Informed Consent** row) — ask for the one design change that would make the LSE study acceptable, and whether opt-in would have ruined it. Report-out template for every group: the USENIX '26 appendix structure (stakeholders, harms, mitigations, decision).

**Original notes:**

Full prompts and prep reads: **[Ethics breakout doc](../../breakouts/ethics.md)** — two sub-breakouts: LLM field experiments (Zurich) and coordinated vs. full disclosure. Companion in-class exercise: **[IRB activity](../../activities/ethics.md)** (Carna / Emotional Contagion / Encore as case files). Related debates that recur later: [CFAA debate](../../debates/cfaa.md), [Backdoors debate](../../debates/backdoors.md). Give each group one scenario, ~10 minutes; push them past "it was bad" to *which principle* and *what specific design change* would have fixed it.

## 21 · Takeaways (divider)

Bridge: next lecture is **[Key Management and PKI](../03-KeyManagement/slides.qmd)** — the same "who do you trust?" question, now in the technical crypto plumbing. Recommended follow-on reading: [Salganik, *Bit by Bit* Ch. 6](https://www.bitbybitbook.com/en/1st-ed/ethics/) end-to-end; [Kenneally & Dittrich, "The Menlo Report" (IEEE S&P 2012)](https://www.caida.org/publications/papers/2012/menlo_report_actual/menlo_report_actual.pdf).
