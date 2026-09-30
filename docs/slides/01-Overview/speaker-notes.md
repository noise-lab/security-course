# Lecture 1 — Speaker Notes (Course Overview + Security Mindset + Trusting Trust)

Per-slide context + clickable links (one section per slide; case briefs are broken into Read first / What happened / What to say / Course tie-in / Also) for the opening half of Meeting 1: course logistics, the threat-modeling primer (assets / adversaries / capabilities), and Trusting Trust. In-deck notes (the `::: {.notes}` blocks) are also visible in reveal.js speaker view (press **S**). Every URL was verified this session or is a canonical org landing page. Pair this with the second half of the meeting: `../01-WhyCryptosystemsFail/speaker-notes.md`.

*Headings carry the slide number shown in the deck footer (title slide is 1 of 21).*

## 2 · Why This Course Exists

**Read first:** [FTC press release, Sep 24 2026 — "FTC Seeks Public Comment on Whether to Update Rule on Impersonation of Government and Businesses to Address Platforms' Role in Promoting Impersonation Scams"](https://www.ftc.gov/news-events/news/press-releases/2026/09/ftc-seeks-public-comment-whether-update-rule-impersonation-government-businesses-address-platforms).

The framing quote ("dearth of technologists in public policy") is Feamster's own; it's the reason the course exists. Give one concrete grounding story: e.g., the [BITAG](https://www.bitag.org/) working-group process (engineers writing consensus technical opinions that ISPs and regulators actually cite), or an FTC testimony where the argument turned on a technical detail the room was underpowered to evaluate. Cold-call prompt: *"Raise your hand if you're here mostly to learn how the tech works. Now raise your hand if you're here mostly to learn how the rules work. Look around — this whole course is why those two hands need to be up together."*

### Case: FTC impersonation-scam ANPRM (Sept 24, 2026)

**What happened:**

- On September 24, 2026 the FTC issued an Advance Notice of Proposed Rulemaking (ANPRM) — the earliest formal step in rulemaking — asking whether the ad-optimization tools that social-media platforms, search engines, and digital marketplaces sell to advertisers are helping scammers impersonate government agencies and legitimate businesses.
- The Commission's own numbers frame the docket: more than 1 million imposter-scam reports in 2025, roughly \$3.5 billion in reported losses, and nearly 30% of consumers who lost money say the first contact came through social media (about \$2.1 billion of the losses).
- The ANPRM asks about the financial incentives behind platform ad services, whether current practices are unfair or deceptive under Section 5, and what to do about it: amend the existing 2024 Rule on Impersonation of Government and Businesses, write a separate rule, or pursue non-regulatory measures such as advertiser vetting and faster ad removal.
- Comments are due 60 days after Federal Register publication, so the docket is open through roughly late November 2026.
- Status as of Sept 30: comment period open; no proposed rule text yet.
- Unknown: whether the Commission will extend liability to platforms at all (the 2024 rule covered impersonators, not intermediaries), and what evidence platforms will produce about how their targeting systems rank scam ads.{B}**What to say:** *"Two weeks ago the FTC asked a question that only a technologist can answer: does the machinery that decides which ad you see — the ranking model, the audience-targeting tools, the auto-optimization — make it easier for a fake IRS agent to find a 78-year-old with a checking account?
- Three and a half billion dollars in losses last year, and a third of the victims met the scammer on social media.
- The lawyers at the FTC can write the rule; they cannot tell you what an ad-optimization objective function actually rewards.
- That is the dearth on this slide.
- By the end of this course I want you to be able to write the comment that answers that docket."* Throw to the room: *"Who here could explain, today, how a platform decides which ad to show you?
- Who could explain what the FTC's legal authority to regulate that is?
- Look around — almost nobody has both hands up."*{B}**Course tie-in:** regulation as a security incentive (the FTC is trying to move platform economics, not patch code); adversary economics (scam ads are a marketplace with ROI); foreshadows the web tracking / ad-tech lectures and the content-moderation and consumer-protection weeks, and it is a live example of the debate skill — translating a technical mechanism into a policy recommendation.{B}**Also:** the FTC's [Privacy and Security Enforcement](https://www.ftc.gov/news-events/topics/protecting-consumer-privacy-security/privacy-security-enforcement) topic hub is the canonical place to find the agency's other 2026 actions.

## 3 · Who Am I?

Canonical bio: [people.cs.uchicago.edu/~feamster](https://people.cs.uchicago.edu/~feamster/). Neubauer Professor of CS, Director of the Network Operations and Internet Security Lab, Faculty Director of Research for the [Data Science Institute](https://datascience.uchicago.edu/people/nick-feamster/); ACM Fellow, PECASE, Sloan Research Fellow, 2026 Quantrell Award (undergraduate teaching). Policy roles: [BITAG](https://www.bitag.org/) (Broadband Internet Technical Advisory Group), FTC testimony, comments to FCC and USPTO. Keep this short — 60–90 sec.

## 4 · Learning Objectives

**Read first:** [European Commission, Jul 31 2026 — "Commission starts enforcing AI Act rules and new transparency requirements on 2 August"](https://digital-strategy.ec.europa.eu/en/news/commission-starts-enforcing-ai-act-rules-and-new-transparency-requirements-2-august).

Read the three bullets aloud, then say: *"The third one is the reason the debate is 35% of your grade — translation is a skill you build only by doing."* Anchor: the course pairs a technical spine (crypto, PKI, DoS/BGP, DNS/Web security) with policy (privacy laws, moderation, censorship, AI accountability).

### Case: EU AI Act enforcement goes live (Aug 2, 2026)

**What happened:**

- On August 2, 2026 the European Commission's AI Office and the national competent authorities began enforcing the AI Act.
- Two things switched on at once.
- First, the Commission's enforcement and penalty powers over providers of general-purpose AI (GPAI) models — the frontier-model developers — became applicable: the AI Office can now request documentation, run technical evaluations of a model, demand compliance and risk-mitigation measures, restrict or withdraw a model from the EU market, and fine up to 3% of global annual turnover or €15 million, whichever is higher (Article 101).
- GPAI providers must document their models and address systemic risks the Act names explicitly: chemical/biological/radiological/nuclear misuse, loss of control, cyber offence, harmful manipulation, and threats to fundamental rights.
- Second, the transparency duties took effect: chatbots and other interactive systems must tell users they are talking to a machine, deepfakes must be labelled, and AI-generated or altered content must carry machine-readable marks; more than 180 organisations signed the voluntary Code of Practice on transparency of AI-generated content.
- What did *not* switch on: the high-risk (Annex III) obligations, which the May 2026 Digital Omnibus deferred to December 2, 2027; bans on AI-generated non-consensual explicit content and child sexual-abuse material take effect December 2026.
- Enforcement is split among the AI Office, the national authorities, and the European Data Protection Supervisor.
- Status as of Sept 30: powers live for eight weeks, no public fine or model withdrawal yet.
- Unknown: how the AI Office will actually run a technical evaluation of a frontier model, and whether the first enforcement target will be a transparency case (easy) or a systemic-risk case (hard).{B}**What to say:** *"Since August 2nd there is a government office in Brussels whose job includes running evaluations on frontier AI models and, if it does not like what it finds, pulling that model off the European market and fining the company three percent of worldwide revenue.
- Think about who has to staff that office.
- Someone has to design the evaluation, read the model card, decide whether 'we red-teamed it' is evidence.
- Your third learning objective — translate technical ideas into policy — is now a job description in an EU regulator."* The detail they will remember: the fine is on *global* turnover, so a US company's non-EU revenue is in the base.
- Throw to the room: *"If you were the AI Office, what is the first document you would demand from a model provider, and what would you do if they said it was a trade secret?"*{B}**Course tie-in:** accountability of automated decision-making (objective two, verbatim); regulation as a security incentive; foreshadows the AI-and-privacy lecture and the copyright/fair-use-and-AI week; pairs with the *A 2026 Vignette* row, which tracks the Act alongside the US cases.{B}**Also:** [Help Net Security, Aug 4 2026 — "EU begins enforcing AI Act, putting AI models under the microscope"](https://www.helpnetsecurity.com/2026/08/04/eu-ai-act-enforcement-ai-models/) (the clearest one-page summary of what applies now vs. later); [European Commission AI Act policy page](https://digital-strategy.ec.europa.eu/en/policies/regulatory-framework-ai); [AI Act implementation timeline](https://artificialintelligenceact.eu/implementation-timeline/).

## 5 · Is This Course for You?

Set the "not a programming-heavy course" expectation early to avoid unnecessary self-selection. Labs use Python/JavaScript; students without a CS background have consistently done fine when paired. Cold-call: *"What's a technical topic you've read a policy piece about recently and thought 'they got it wrong'?"*

## 6 · Where This Can Take You

Four real career shapes: **FCC Commissioner** (e.g., [Jessica Rosenworcel](https://en.wikipedia.org/wiki/Jessica_Rosenworcel)), **U.S. Deputy CTO / FTC CTO** (e.g., [Ashkan Soltani](https://en.wikipedia.org/wiki/Ashkan_Soltani), CA Privacy Protection Agency ED; [Lorrie Cranor](https://lorrie.cranor.org/) served as FTC Chief Technologist), **civil-society NGO leader** (e.g., [Cindy Cohn](https://www.eff.org/about/staff/cindy-cohn) at EFF), **city/state data scientist** (e.g., [DataSF](https://datasf.org/), Chicago's [Mayor's Office of Public Safety](https://cityofchicago.org/)). The point isn't the specific people — it's that "technologist who understands policy" is a durable career, not a hobby.

**Read first:** [FTC press release, Sep 24 2026](https://www.ftc.gov/news-events/news/press-releases/2026/09/ftc-seeks-public-comment-whether-update-rule-impersonation-government-businesses-address-platforms).

### Case: what the job looks like this month — the FTC's ad-optimization ANPRM (Sept 24, 2026)

**What happened:**

- Full account in the *Why This Course Exists* row.
- Short version: the FTC opened a rulemaking docket asking whether platforms' ad-ranking and targeting tools are amplifying impersonation scams (\$3.5B in reported losses in 2025) and what obligations — advertiser vetting, ad removal, a new rule — should follow.
- The docket is open for 60 days after Federal Register publication.{B}**What to say:** *"Every one of the four people on this slide has written or read a document like this ANPRM.
- The questions in it are about ranking incentives, advertiser verification, and detection — the law is the easy part.
- An FTC or FCC technologist's job is to be the person in the building who can say 'here is what the optimization actually does, and here is what changing it would cost.'"* Throw to the room: *"Which of these four jobs would you want, and what technical question would land on your desk in week one?"*{B}**Course tie-in:** the career framing for the whole course; the same docket returns in the ad-tech/tracking and consumer-protection weeks as a worked example of writing a regulatory comment.

## 7 · What We Actually Cover

This slide is the actual delivered content from [`agenda.md`](../../agenda.md), not the aspirational syllabus. If a topic gets cut for time, update both files in sync. Companion resource: the [`readings/`](../../readings/) directory has the reading list per meeting.

## 8 · Course Components

Weights: **Midterm+Final 40% · Debate 35% · Labs 20% · Participation/quizzes 5%**. On labs: rubric published in each assignment; graded for thoughtful completion. **AI-tools policy:** allowed if you can defend the output — the "defend it" language matters, tell students you may cold-call about a specific choice. Debate format: Oxford-style, ~4 people per side, one debate per term. Format spec: [`../../debates/format.md`](../../debates/format.md). The Meeting 1 debate is on data breaches — [`../../debates/data-breach.md`](../../debates/data-breach.md).

**Read first:** [Krebs on Security, Sep 1 2026 — "FBI Probes Service Selling 153M+ Drivers Licenses"](https://krebsonsecurity.com/2026/09/fbi-probes-service-selling-153m-drivers-licenses/).

### Case for the Meeting 1 data-breach debate: IDScan (Sept 2026)

**What happened:**

- Full account in the *Meet the Adversary* row.
- For the debate, the load-bearing facts are: 153M+ US and Canadian driver's-license scans (170M+ identity documents in total) were offered on a dark-web lookup service on Aug 31, 2026; a journalist, not the company, discovered and reported it on Sept 1; the vendor, IDScan.net, only confirmed the breach publicly around Sept 8–10; the data sits with an intermediary the affected people never chose (Hertz, dispensaries, gun stores, and banks chose it); IDScan is offering free credit monitoring; the FBI is investigating; how the attacker got in and whether a ransom was demanded are not public.{B}**What to say:** *"Your first debate is about data breaches, and you have a perfect live case.
- A company you have never heard of had your license because a rental-car counter scanned it.
- A reporter found your data for sale before the company knew.
- Argue: who should be liable, what should notification law require, and is 'free credit monitoring' a remedy or a punchline?"*{B}**Course tie-in:** debate mechanics (Oxford style, graded on contribution); previews the privacy-law-and-compliance week (breach-notification statutes, vendor liability) and the threat-modeling frame introduced later in this deck.{B}**Also:** [The Record, Sep 10 2026](https://therecord.media/idscan-data-breach-notice-drivers-licenses) (the company's confirmation, in the outlet's words); [TechCrunch, Sep 10 2026](https://techcrunch.com/2026/09/10/id-verification-giant-idscan-confirms-data-breach-with-more-than-150-million-drivers-licenses-stolen/).

## 9 · A 2026 Vignette: Why This Is Timely

**Read first:** [European Commission, Jul 31 2026](https://digital-strategy.ec.europa.eu/en/news/commission-starts-enforcing-ai-act-rules-and-new-transparency-requirements-2-august).

**Case 2: *NYT v. OpenAI* reaches summary judgment (Sept 4, 2026).** **Read first:** [AI Lawsuit Tracker — NYT v. OpenAI & Microsoft, status reviewed Sep 27 2026](https://ailawsuittracker.com/cases/new-york-times-v-openai/).

**Read first:** [Authors Guild, Jul 21 2026 — "Court Grants Final Approval of \$1.5 Billion Anthropic Copyright Settlement"](https://authorsguild.org/news/court-grants-final-approval-anthropic-copyright-settlement/).

**Original source anchors for the slide text (kept for reference):** Anchor each phrase to a primary source: **20 states with comprehensive privacy laws in effect** — [MultiState 2026 tracker](https://www.multistate.us/insider/2026/2/4/all-of-the-comprehensive-privacy-laws-that-take-effect-in-2026) (Indiana, Kentucky, Rhode Island joined Jan 1, 2026); [IAPP US State Privacy Legislation Tracker](https://iapp.org/resources/article/us-state-privacy-legislation-tracker). **EU AI Act GPAI enforcement, Aug 2, 2026** — [European Commission AI Act page](https://digital-strategy.ec.europa.eu/en/policies/regulatory-framework-ai) and the [AI Act implementation timeline](https://artificialintelligenceact.eu/implementation-timeline/); Article 101 fines up to 3% of global turnover / €15M whichever is higher. Note the Digital Omnibus (May 2026) *deferred* high-risk Annex III obligations to Dec 2, 2027 but left GPAI enforcement in place. **Anthropic \$1.5B settlement** — see [law firm summary](https://www.apm.law/a-record-1-5-billion-compensation-for-copyright-infringement-in-a-i-training-agreed-in-a-settlement-approved-by-us-federal-court/) and [Norton Rose Fulbright 2026 update on AI copyright cases](https://www.nortonrosefulbright.com/en/knowledge/publications/ce8eaa5f/ai-in-litigation-series-an-update-on-ai-copyright-cases-in-2026); court found training was fair use but storing pirated copies was not, ~\$3K per work. *NYT v. OpenAI* still in discovery; NYT filed a sanctions motion July 9, 2026 ([Washington Times](https://www.washingtontimes.com/news/2026/jul/9/news-outlets-urging-judge-sanction-openai-high-stakes-ai-copyright/)). **Encrypted Client Hello (ECH) default-on** in Chrome/Firefox (since Oct 2023) and Safari 17+ (since Sept 2024) — [CDT rollout analysis](https://cdt.org/insights/do-not-stick-out-the-dynamics-of-the-ech-rollout/); [Cloudflare's ECH announcement](https://blog.cloudflare.com/announcing-encrypted-client-hello/). Cold-call: *"Name a tech-policy story from this week's news."* Point at the roadmap.

**Status check, Sept 30 2026 — the slide text dates from July; every phrase has moved. Cases in slide order, then the original source anchors.**

### Case 1: EU AI Act GPAI enforcement live (Aug 2, 2026)

**What happened:**

- Enforcement did switch on as the slide predicted: since August 2 the AI Office can request documentation, run technical evaluations, demand mitigations, restrict or withdraw a GPAI model, and fine up to 3% of global turnover / €15M; transparency duties (chatbot self-identification, deepfake labels, machine-readable marks on generated content) apply too; high-risk obligations remain deferred to Dec 2, 2027 by the Digital Omnibus.
- No public enforcement action yet as of Sept 30.
- Full account in the *Learning Objectives* row.{B}**What to say:** *"The slide said August 2nd; it happened.
- Eight weeks in, nobody has been fined, and the interesting question is what the first case looks like."*{B}**Course tie-in:** AI accountability; regulation as incentive; AI-and-privacy week.{B}**Also:** [Help Net Security, Aug 4 2026](https://www.helpnetsecurity.com/2026/08/04/eu-ai-act-enforcement-ai-models/).

**What happened:**

- The Times sued OpenAI and Microsoft in December 2023 (S.D.N.Y., Judge Sidney H. Stein), alleging its articles were used to train GPT models without permission and that ChatGPT and Copilot can reproduce them near-verbatim; it seeks billions in statutory and actual damages plus destruction of the models.
- In March 2025 Stein denied most of the motions to dismiss (narrowing the DMCA claims).
- In June 2026 the Times moved to amend to allege Microsoft encouraged OpenAI's use, dropping two trademark claims; on July 9, 2026 it filed a sanctions motion over discovery; an Aug 6, 2026 order resolved a fight over disclosure of ChatGPT conversation logs.
- On September 4, 2026 both sides filed cross-motions for summary judgment in the consolidated multidistrict litigation (25-md-03143); replies are due November 6, 2026, after which Stein decides whether the case, or parts of it, goes to trial next year.
- A September 2026 unsealed filing quotes a Microsoft official describing the scraping as "an astonishing theft of unprecedented proportions.
- OpenAI's defense is fair use and no market substitution.
- Status: pending; no trial date.
- Unknown: whether Stein rules on fair use as a matter of law or sends it to a jury.{B}**What to say:** *"The slide said 'headed toward trial.' Update: both sides asked the judge on September 4th to decide it without one.
- Replies land November 6th, so this term you will watch a judge decide whether training an LLM on the newspaper is fair use.
- The document students will remember: a Microsoft executive's own words, unsealed this month, calling it 'an astonishing theft of unprecedented proportions.'"* Throw: *"If the court says training is fair use but verbatim output is not, what does an engineer have to build?"*{B}**Course tie-in:** copyright, fair use, and AI week; translating a technical fact (memorization / regurgitation) into a legal argument.{B}**Also:** [Wikipedia — The New York Times v. Microsoft and OpenAI](https://en.wikipedia.org/wiki/The_New_York_Times_v._Microsoft_and_OpenAI) (procedural history); [Washington Times, Jul 9 2026 — sanctions motion](https://www.washingtontimes.com/news/2026/jul/9/news-outlets-urging-judge-sanction-openai-high-stakes-ai-copyright/); [Norton Rose Fulbright 2026 AI copyright update](https://www.nortonrosefulbright.com/en/knowledge/publications/ce8eaa5f/ai-in-litigation-series-an-update-on-ai-copyright-cases-in-2026).

### Case 3: Anthropic settlement gets final approval (July 20, 2026)

**What happened:**

- *Bartz v. Anthropic* (N.D. Cal.) is the case where the court held in 2025 that training on lawfully acquired books was fair use but that downloading and storing millions of pirated copies from Library Genesis and Pirate Library Mirror was not; Anthropic then agreed in September 2025 to a \$1.5 billion class settlement.
- On July 20, 2026 Judge Araceli Martínez-Olguín granted final approval, calling the benefits substantial "in light of the novel claims asserted.
- Terms: roughly \$3,000 per work (about four times the statutory minimum for ordinary infringement); attorneys' fees cut from the requested 20% to about 6.8% (\$101.56M); service awards for the three named plaintiffs trimmed from \$50,000 to \$15,000; Anthropic must destroy the pirated files.
- The settlement is now in its distribution phase; as of the Guild's July 21 note no payout date had been announced, and co-claimant disputes (authors vs. publishers over the same title) have to be resolved before contested works are paid.
- Unknown: the payout schedule and how many works end up contested.{B}**What to say:** *"The slide says Anthropic settled for a billion and a half.
- As of July 20th a judge has approved it, the lawyers got 6.8 percent instead of 20, and every author gets about three thousand dollars per book.
- The part to remember: the court said the training was fair use — the money is for how the books were acquired.
- Acquisition, not learning, was the tort."*{B}**Course tie-in:** copyright and AI; the difference between a technical act (training) and a legally salient one (piracy) — a translation problem.{B}**Also:** [law-firm summary of the settlement](https://www.apm.law/a-record-1-5-billion-compensation-for-copyright-infringement-in-a-i-training-agreed-in-a-settlement-approved-by-us-federal-court/).{B}**Case 4: Encrypted Client Hello becomes RFC 9849 (March 2026).** **Read first:** [IETF datatracker — RFC 9849, "TLS Encrypted Client Hello"](https://datatracker.ietf.org/doc/rfc9849/).

**What happened:**

- ECH encrypts the TLS ClientHello — including the Server Name Indication, the last plaintext field that tells a network observer which site you are visiting — under a server public key published in DNS (HTTPS/SVCB records), which is why it only works when DNS is itself encrypted (DoH).
- Browsers shipped it as a draft: Chrome and Firefox default-on since October 2023, Safari 17+ since September 2024, Cloudflare on by default for free zones.
- In March 2026 the IETF TLS working group published it as Standards Track RFC 9849, so 'ECH' is no longer a draft feature.
- The policy story is that censors noticed: Russia began blocking Cloudflare's ECH implementation in November 2024, and a July 2026 IETF deployment-considerations draft catalogues the network-operator objections.
- Unknown: how many non-Cloudflare origins actually publish ECH configs, i.e. how much traffic is really covered.{B}**What to say:** *"Every TLS connection you have ever made leaked one thing in plaintext: the hostname.
- As of March the fix is a full IETF standard, on by default in your browser.
- Russia's response was to block it.
- That is the whole course in one sentence: a privacy protocol, a deployment story, and a censorship reaction."*{B}**Course tie-in:** cryptography and PKI weeks (what TLS protects and what it leaks); DNS security; censorship week (SNI-based blocking and the response to ECH).{B}**Also:** [CDT rollout analysis](https://cdt.org/insights/do-not-stick-out-the-dynamics-of-the-ech-rollout/); [Cloudflare's ECH announcement](https://blog.cloudflare.com/announcing-encrypted-client-hello/).{B}**Case 5: the state-attorney-general enforcement wave (Sept 2026 roundup).** **Read first:** [MultiState, Sep 18 2026 — "How State AGs Are Policing Consumer Data Practices"](https://www.multistate.us/insider/2026/9/18/how-state-ags-are-policing-consumer-data-practices).

**What happened:**

- Twenty comprehensive state privacy laws are in effect (Indiana, Kentucky, and Rhode Island since Jan 1, 2026), and the enforcement is coming from attorneys general using both those statutes and older consumer-protection law.
- The roundup's ledger: 42 states settled with 23andMe for \$18M over the 2023 breach that exposed 6.9M customers; Connecticut took \$275,000 from TaxAct for sending taxpayer data to Meta and Google via tracking pixels; California AG Rob Bonta obtained \$12.75M from GM for selling drivers' location data to brokers; a New Mexico jury returned a \$375M verdict against Meta in March 2026 under the state Unfair Practices Act, alongside a \$567M public-nuisance order; a 47-state settlement with Meta over infinite scroll and autoplay features aimed at children is reported by MultiState at \$18 billion; Texas AG Ken Paxton sued Netflix under the Deceptive Trade Practices Act and settled with LG over television data collection.
- Status: this is the enforcement pattern for the fall — no federal privacy statute, twenty state ones, and AGs picking sensitive-data cases (genetic, financial, location, children).
- Unknown: whether the Meta multistate figure holds up on the final documents, and how the Digital Omnibus-style 'simplification' pressure in Europe plays out here.{B}**What to say:** *"The slide says twenty states.
- The update is who is enforcing them: not a privacy agency, but forty-two attorneys general in one settlement, a jury in New Mexico, and the Texas AG suing Netflix.
- Notice the pattern — genetic data, location data, children.
- That is a threat model, written by prosecutors."* Throw: *"Why did GM's location-data sale cost \$12.75M in California and nothing, yet, in most other states?"*{B}**Course tie-in:** privacy law and compliance week; regulation as a security incentive; the debate skill (state vs. federal preemption is a classic motion).{B}**Also:** [MultiState 2026 effective-dates tracker](https://www.multistate.us/insider/2026/2/4/all-of-the-comprehensive-privacy-laws-that-take-effect-in-2026); [IAPP US State Privacy Legislation Tracker](https://iapp.org/resources/article/us-state-privacy-legislation-tracker).{B}**Case 6: GDPR Digital Omnibus — Council talks resume (Sept 2026).** **Read first:** [Privacy Next, Sep 1 2026 — "Digital Omnibus (GDPR) Negotiations at the Council – September 2026 Update"](https://www.privacynext.eu/resources/digital-omnibus-gdpr-negotiations-at-the-council-september-2026-update/).

**What happened:**

- The Commission's Digital Omnibus package proposes to 'simplify' the GDPR, ePrivacy, NIS2, and DORA alongside the AI Act.
- The AI half was adopted by the Council on June 29, 2026 (that is what deferred the AI Act's high-risk rules to Dec 2027).
- The data half is still being negotiated: Council talks on the GDPR elements resumed in September under the Irish Presidency, with a fresh compromise text circulated in the first week of September ahead of an Antici Group meeting on September 11.
- Open fights: the definition of personal data (whether a proposed Article 29a 'Cyprus approach' delivers legal certainty), whether training AI 'may, in appropriate cases, constitute a legitimate interest' under Article 6, new definitions for scientific research, curbing 'abusive' data-subject requests, and the cookie/ePrivacy provisions.
- Civil-society groups (Amnesty, among others) call the package a rollback of rights; the EDPB and EDPS issued a joint opinion in February 2026.
- Status: final adoption not expected before late 2026 at the earliest.
- Unknown: whether the personal-data definition changes at all, which would ripple through every later lecture that mentions GDPR.{B}**What to say:** *"While the AI Act got stricter on August 2nd, the GDPR is being loosened in a Council working group in Brussels this month.
- The two headline questions — what counts as personal data, and whether training an AI model is a 'legitimate interest' — are technical questions wearing legal clothes."*{B}**Course tie-in:** privacy law and compliance; AI and privacy; an example of regulation moving in both directions at once.{B}**Case 7: FTC begins enforcing the TAKE IT DOWN Act (May 19, 2026).** **Read first:** [FTC press release, May 19 2026 — "FTC Begins Enforcing the TAKE IT DOWN Act"](https://www.ftc.gov/news-events/news/press-releases/2026/05/ftc-begins-enforcing-take-it-down-act).

**What happened:**

- The TAKE IT DOWN Act was signed May 19, 2025; its Section 3 gave covered platforms one year to build a notice-and-removal process for nonconsensual intimate imagery, including AI-generated deepfakes, and to remove qualifying images and known identical copies within 48 hours of a valid request.
- Enforcement began May 19, 2026: the FTC launched TakeItDown.ftc.gov for victims to report non-compliant platforms, sent reminder letters on May 11 to fifteen major platforms including Meta, TikTok, Amazon, Apple, and Discord, and published consumer and business guidance; Chairman Andrew Ferguson framed it as protecting minors.
- Civil penalties run up to \$53,088 per violation.
- Status as of Sept 30: no public enforcement action turned up in searches; the FTC is 'monitoring compliance.' Unknown: whether the 48-hour clock will be enforced against a large platform first, or against a smaller one that has no process at all.{B}**What to say:** *"This one is not on the slide because it took effect in May.
- Since then every big platform has had 48 hours to take down an intimate image once asked, real or AI-generated, with a fifty-three-thousand-dollar fine per miss.
- Four months in, no public cases.
- Is that compliance, or is the FTC waiting for a good test case?"*{B}**Course tie-in:** content moderation week (a statutory takedown regime alongside Section 230); AI and privacy (deepfakes); regulation as incentive.{B}**Also:** [FTC business-guidance blog, May 19 2026 — what TIDA requires of platforms](https://www.ftc.gov/business-guidance/blog/2026/05/take-it-down-act-enforcement-starts-now-what-know-about-ftc-tida).

## 10 · How a Typical Lecture Runs

3-hour block, mid-class break. Structure: vignette → key idea → thought question → breakout → debate portion where scheduled. Point students at the [`activities/`](../../activities/) directory for the hands-on activities we'll do (e.g., cert-chain inspection in Meeting 2). Feedback from last year's class: they wanted more explicit pacing — be transparent about the break.

## 11 · Logistics

Communication policy: **public channel first**, DMs have no response-time guarantee. Assignments have hard deadlines published day one. Readings drop the week before; if it isn't up, it isn't due. Sample syllabus: [`../../syllabus.md`](../../syllabus.md). Course landing: [`../../index.md`](../../index.md). Student disability services: [`../../sds.md`](../../sds.md).

## 12 · The Security Mindset (divider)

Section divider. Transition from logistics into the adversarial-thinking half of the lecture; the next slide (Meet the Adversary) carries the content.

## 13 · Meet the Adversary

**Second case: the 2026 breach ledger.** **Read first:** [TechCrunch, updated Sep 15 2026 — "Leaks, data breaches, and ransom notes: The worst hacks of 2026 so far" (Zack Whittaker)](https://techcrunch.com/2026/09/15/the-worst-hacks-and-breaches-of-2026-so-far/).

**Marquee case: IDScan / 'Nexus' (Sept 2026).** **Read first:** [Krebs on Security, Sep 1 2026 — "FBI Probes Service Selling 153M+ Drivers Licenses"](https://krebsonsecurity.com/2026/09/fbi-probes-service-selling-153m-drivers-licenses/) — the original investigation, with the timestamp analysis that pinned the source.

**What happened:**

- On August 31, 2026 a service calling itself 'Nexus' was advertised on the Russian-language Exploit crime forum: a searchable database of more than 153 million US and Canadian driver's-license scans, part of a 170-million-plus document trove that also held 10M+ ID cards, 3M travel documents, and 579,000 medical cards, indexed across about 11.5 million search-result pages.
- Brian Krebs, working with researcher Zach Edwards, authenticated samples — he found his own license, scanned at a car rental in June 2025 — and by matching record timestamps to rental and retail transactions traced the source to the customers of IDScan.net, a Louisiana identity-verification vendor that runs about 21 million ID checks a month for Hertz, cannabis dispensaries, gun stores, banks, and entertainment venues.
- Krebs published on September 1; the FBI's New Orleans field office opened an investigation the same day; Nexus went offline September 2.
- IDScan posted a notice on September 4 saying an 'unauthorized third party may have accessed and/or copied' customer information stored in customer accounts on its cloud platform, and confirmed the breach to press on September 8–10: exposed fields include full names, driver's-license numbers, and other government ID numbers such as passports.
- TechCrunch reported that Defense Secretary Pete Hegseth's license was among the records and that the Pentagon was also investigating.
- IDScan is offering free credit monitoring.
- Still unknown as of Sept 30: who runs Nexus, how the attacker got into the customer accounts, and whether a ransom was demanded.{B}**What to say:** *"Here is the adversary.
- Not a random disk failure — a group that looked at the ecosystem of places that scan your license, found the one vendor sitting behind Hertz and every dispensary in the country, and took 153 million scans in one go.
- Then they did something a reliability engineer would never model: they built a search engine and sold lookups.
- The detail you will remember is that the reporter found his own license — scanned at a rental counter a year earlier — before the company knew it had been breached."* Throw: *"Whose customer were you when your license got scanned?
- Whose customer was IDScan's?
- Who owes you notice?"*{B}**Course tie-in:** the adversary as *intelligence* (targets the aggregator, monetizes via a marketplace); adversary economics; sets up the four threat-model questions on the next slide; foreshadows the data-breach debate, privacy-law week (notification, vendor liability), and authentication week (why ID verification vendors exist at all).{B}**Also:** [TechCrunch, Sep 10 2026 — IDScan confirms breach, 150M+ licenses](https://techcrunch.com/2026/09/10/id-verification-giant-idscan-confirms-data-breach-with-more-than-150-million-drivers-licenses-stolen/); [The Record, Sep 10 2026 — the company's confirmation and the document counts](https://therecord.media/idscan-data-breach-notice-drivers-licenses); [Help Net Security, Sep 11 2026 — timeline summary](https://www.helpnetsecurity.com/2026/09/11/idscan-net-data-breach-153-million-drivers-licenses/).

**What happened:**

- A running list, first published June 8 and updated July 7 and September 15, 2026.
- The entries worth having in your pocket: the alleged DOGE upload of a Social Security Administration database to an unsecured server; Russian-attributed attacks on European energy and water infrastructure (Poland's grid, a Swedish thermal plant, a Norwegian dam, Polish water treatment); Iranian attacks on 100-plus US water providers over the summer; an August 2026 ransomware attack on the ATF; an August 2026 network disruption at Boston Scientific, a heart-implant manufacturer; the FBI surveillance-system breach in April that exposed phone numbers of surveillance targets; ShinyHunters' theft of 30 million Instructure/Canvas student and staff records, followed by a second intrusion that defaced login screens during finals; Iranian actors remotely wiping tens of thousands of Stryker employee devices in March; a Hasbro attack in late March that delayed SEC filings; healthcare breaches at DentaQuest (15M), Aesto Health (9.5M), and CareCloud (3.7M); and supply-chain compromises of security tooling that reached OpenAI and Vercel.{B}**What to say:** *"If IDScan feels like an outlier, here is this year's list.
- Water utilities, a heart-implant maker, the ATF, your learning-management system during finals.
- Every one of these has an adversary with a motive; pick any two and tell me the motive."*{B}**Course tie-in:** the 'someone trying, on purpose' line on the slide; a menu of cases to reuse in the DoS/botnet, routing, and web-security weeks.{B}**Underlying framing:** From the classic "security mindset" opening lecture (archived: `../ppt-archive/` and `archive/resources/lectures/ECE422-Spring2016-Lecture-01-Mindset.pptx`).
- The definitional move: security is the study of systems **in the presence of an adversary** — an intelligence, not entropy.
- Contrast with reliability engineering: a disk that fails randomly vs. an attacker who *chooses* the worst moment.
- Cold-call: *"Give me a failure that is a reliability problem but not a security problem — now flip it."*

## 14 · Threat Modeling: Vocabulary for the Whole Term

The four-question frame — **assets, properties (CIA), adversaries, capabilities** — is the vocabulary every later lecture reuses (PKI trust roots, BGP hijacks, DNS privacy, moderation pipelines). Say explicitly that this frame returns weekly. Canonical references if students want more: [OWASP Threat Modeling](https://owasp.org/www-community/Threat_Modeling), [Microsoft STRIDE](https://learn.microsoft.com/en-us/azure/security/develop/threat-modeling-tool-threats). Emphasize *limits*: a threat model that claims to cover everything covers nothing — deciding what you consciously ignore is part of the model.

**Worked case: IDScan through the four questions.** **Read first:** [Krebs on Security, Sep 1 2026](https://krebsonsecurity.com/2026/09/fbi-probes-service-selling-153m-drivers-licenses/) (full account in the *Meet the Adversary* row).

**What happened:**

- 153M+ license scans held in an ID-verification vendor's cloud customer accounts were exfiltrated and sold through a searchable dark-web service in Aug–Sept 2026; the people affected had no relationship with the vendor — a rental counter or a dispensary chose it for them; the initial access method is not public.{B}**What to say:** Walk the four questions on the board.
- *Assets:* your license image and number — held by a company you never chose.
- *Properties:* confidentiality obviously, but also integrity (an ID service that says 'valid' is an oracle for fraud).
- *Adversaries:* a criminal marketplace whose motive is resale, not you personally.
- *Capabilities:* access to the vendor's customer cloud accounts — how is still unknown, and that is a modeling gap you should state out loud.
- *Limits:* there is no individual countermeasure; you cannot 'lock your door' against a vendor three hops away — which is why the fix is policy (notification duties, vendor liability, data minimization at the point of scan).
- *"The threat model tells you where the countermeasure has to live.
- Here it cannot live with the victim."*{B}**Course tie-in:** this is the template every later lecture reuses (PKI trust roots, BGP hijacks, DNS privacy, moderation pipelines); foreshadows privacy-law week and the data-breach debate.

## 15 · Exercise: Should You Lock Your Door?

Classic mindset warm-up (from the archived Mindset deck). Two-minute pair discussion, then collect. Steer toward: different adversaries (burglar / roommate / landlord) have different capabilities and motives; countermeasure cost can rationally exceed risk; and the lock is a *deterrent*, not a guarantee — most residential locks are trivially picked, which is itself a nice threat-model point (what does the lock actually buy you?).

## 16 · Trusting Trust (divider)

Section divider. Introduces Thompson's 1984 lecture; the next three slides carry the content.

## 17 · Thompson's Question

The paper is short (~3 pages), the argument is simple, and it is *the* founding text of software supply chain security. **Ken Thompson, "Reflections on Trusting Trust"** — 1984 Turing Award lecture, CACM 27(8):761–763, [ACM DL](https://dl.acm.org/doi/10.1145/358198.358210); [Cambridge PDF](https://www.cl.cam.ac.uk/teaching/2223/R209/Reflections-Trusting-Trust.pdf); annotated at [Fermat's Library](https://fermatslibrary.com/s/reflections-on-trusting-trust). Cold-call: *"If a compiler binary lies about what its own source code compiles to, how could you ever prove it wasn't lying?"* Punchline in Thompson's own words: **"You can't trust code that you did not totally create yourself."** Partial defense: **David A. Wheeler's "Diverse Double-Compiling"** dissertation (2009) shows how compiling the same source with an independent, differently-compromised compiler can catch a Thompson attack — worth naming if a keener student asks whether the problem is unsolvable. Wheeler's [DDC paper](https://dwheeler.com/trusting-trust/) and [Reproducible Builds project](https://reproducible-builds.org/) are the modern partial answers.

## 18 · Why It Still Matters

The image is **[xkcd 2347 "Dependency"](https://xkcd.com/2347/)** (Randall Munroe, Aug 17, 2020); explainer: [explain xkcd](https://www.explainxkcd.com/wiki/index.php/2347:_Dependency). Alt-text: *"All modern digital infrastructure"* rests on *"a project some random person in Nebraska has been thanklessly maintaining since 2003."* Interactive Matter.js version: [nesbitt.io/xkcd-2347](https://nesbitt.io/2026/02/27/xkcd-2347.html). Cold-call: *"In your last programming project, how many dependencies did `npm install` or `pip install` pull in? How many did you actually read?"* Tie forward to PKI (Meeting 2): the "chain of trust must stop somewhere" — usually at a root CA the OS ships.

**Scale case: ChainDrop (Aug 4, 2026).** **Read first:** [Datadog Security Labs, Aug 4 2026 — "'ChainDrop' worm compromises hundreds of popular npm packages"](https://securitylabs.datadoghq.com/articles/npm-worm-compromises-popular-npm-packages/) (full account two rows down, in *Supply Chain as a Trust Problem*).

**What happened:**

- One compromised maintainer account on `keyv`, a small caching library, let a self-propagating worm republish 444 npm packages (2,212 versions) with a combined two billion monthly downloads in under four hours — the worm used the maintainer's own publish rights to poison everything else that account could publish.{B}**What to say:** *"This comic is not a joke anymore.
- In August the block at the bottom was a cache library called keyv.
- One stolen token, four hours, two billion downloads a month.
- Ask yourself how many of your projects are standing on it right now."*{B}**Course tie-in:** the transitive-dependency point on the slide; bridges to Thompson and to the PKI 'chain of trust must stop somewhere' thread.

## 19 · Trusting Trust, Realized: xz-utils

**Read first:** [Wikipedia — XZ Utils backdoor](https://en.wikipedia.org/wiki/XZ_Utils_backdoor) (the best consolidated timeline; read it end to end, ~15 min).

### Case: the xz-utils backdoor (CVE-2024-3094) — status as of Sept 2026

**What happened:**

- xz-utils is the compression library behind `.xz` and, via liblzma, a dependency of systemd on major Linux distributions — which is how it ends up linked into OpenSSH's `sshd` on Debian and Fedora builds.
- Beginning in late 2021 a contributor using the name 'Jia Tan' (GitHub JiaT75) made small, helpful contributions; sock-puppet accounts then pressured the sole maintainer, Lasse Collin, who had said he was struggling with burnout, into granting Jia Tan co-maintainer and release-manager rights during 2022–23.
- In February 2024 Jia Tan cut releases 5.6.0 and 5.6.1 whose *release tarballs* — not the git source — contained an obfuscated build-script stage that, on x86-64 Debian/RPM builds, spliced a payload into liblzma.
- The payload hooked RSA key checking in sshd so that a holder of a specific private key could execute arbitrary commands pre-authentication: a remote-code-execution backdoor on essentially every Linux server, rated CVSS 10.0.
- On March 29, 2024 Andres Freund, a Microsoft engineer benchmarking PostgreSQL on Debian Sid, noticed sshd logins took about 500 ms longer and Valgrind complained about liblzma; he pulled the thread and posted to oss-security the same day, days before the versions would have reached stable distributions.
- Status as of Sept 30, 2026: no public attribution — Jia Tan claimed to be in California but timestamp and language analysis pointed to Eastern Europe or Russia, and whether it was a state operation is unproven; Collin's canonical incident page at tukaani.org was last updated Jan 17, 2025 ("tarballs created by Jia Tan were signed by him"); and Binarly found backdoored Debian images still on Docker Hub in August 2025.
- Unknown: who Jia Tan is, how many other projects the same operators touched, and whether anyone was actually exploited.{B}**What to say:** *"This is Thompson's lecture, forty years later, in production.
- The malicious code was not in the source you could read; it was in the build tarball, unpacked only on the machines that mattered.
- The attacker did not exploit a bug — they spent two years becoming the maintainer.
- It was caught because one engineer thought half a second was too long for an SSH login.
- Nobody knows who Jia Tan is.
- Two and a half years later, that is still true."* Throw: *"You are Lasse Collin, burnt out, and a helpful stranger offers to share the load.
- What would you have done differently — and would any tool have told you?"*{B}**Course tie-in:** trust as the attack surface (Thompson); social engineering of maintainers; the AI-assisted-code question on the agenda (what happens when the 'helpful stranger' is an agent); foreshadows PKI (trusting a root you did not build) and the supply-chain slide that follows.{B}**Also, with the original detail:** **CVE-2024-3094**, CVSS **10.0** (max).
- Primary sources: [Wikipedia: XZ Utils backdoor](https://en.wikipedia.org/wiki/XZ_Utils_backdoor) — best consolidated reference; [Andres Freund's original disclosure on oss-security](https://www.openwall.com/lists/oss-security/2024/03/29/4) (Mar 29, 2024); the running community writeup / gist by "thesamesam": [`gist.github.com/thesamesam/223949d5a074ebc3dce9ee78baad9e27`](https://gist.github.com/thesamesam/223949d5a074ebc3dce9ee78baad9e27).
- Story detail: Freund was a **Microsoft principal engineer** benchmarking PostgreSQL on Debian Sid; he noticed sshd was ~500 ms slower than expected and Valgrind errors in liblzma — pure operational luck ([NPR](https://www.npr.org/2024/04/11/1244174104/one-engineer-may-have-saved-the-world-from-a-massive-cyber-attack)).
- "Jia Tan" (JiaT75) had spent ~2 years earning maintainer trust; sock-puppet accounts pressured original maintainer Lasse Collin into granting release-manager rights ([SentinelOne analysis](https://www.sentinelone.com/blog/xz-utils-backdoor-threat-actor-planned-to-inject-further-vulnerabilities/); [Akamai deep-dive](https://www.akamai.com/blog/security-research/critical-linux-backdoor-xz-utils-discovered-what-to-know)).
- Persistence angle (2025): [Binarly, "Persistent Risk: XZ Utils Backdoor Still Lurking in Docker Images"](https://www.binarly.io/) — backdoored Debian images still on Docker Hub in Aug 2025.
- Attribution remains **unresolved** as of mid-2026.
- Teaching point: SBOM and code review would have walked right past this — the exploit was a *trust* problem, not an artifact problem.
- Canonical maintainer statement: [tukaani.org/xz-backdoor](https://tukaani.org/xz-backdoor/).

## 20 · Supply Chain as a Trust Problem

**Background — the Shai-Hulud lineage (Sept 2025 → June 2026):**

**npm Shai-Hulud** — self-replicating worm named for the Dune sandworms after the `shai-hulud-workflow.yml` file it drops. Original outbreak Sept 2025 (500+ packages); CISA advisory: [Widespread Supply Chain Compromise Impacting npm Ecosystem](https://www.cisa.gov/news-events/alerts/2025/09/23/widespread-supply-chain-compromise-impacting-npm-ecosystem); Unit 42 running writeup (updated Nov 26): [`unit42.paloaltonetworks.com/npm-supply-chain-attack/`](https://unit42.paloaltonetworks.com/npm-supply-chain-attack/). **Shai-Hulud 2.0** (Dec 2025 – early 2026) added a destructive failsafe that can wipe `$HOME`: [Microsoft Security Blog, Dec 9, 2025](https://www.microsoft.com/en-us/security/blog/2025/12/09/shai-hulud-2-0-guidance-for-detecting-investigating-and-defending-against-the-supply-chain-attack/). **2026 waves:** May 11 hit TanStack, Mistral AI, UiPath, OpenSearch via CI cache-poisoning + npm OIDC abuse; May 19 hit the AntV data-viz ecosystem ([StepSecurity](https://www.stepsecurity.io/blog/shai-hulud-here-we-go-again-mass-npm-supply-chain-attack-hits-the-antv-ecosystem)); the worm code was **released publicly May 12, 2026** ([Akamai: "Mini Shai-Hulud: The Worm Returns and Goes Public"](https://www.akamai.com/blog/security-research/mini-shai-hulud-worm-returns-goes-public)). **June 1, 2026:** Red Hat's npm namespace (~80K downloads/week) compromised via a Red Hat employee's GitHub account ([The Register](https://www.theregister.com/security/2026/06/01/shai-hulud-malware-infects-red-hat-npm-packages-downloaded-80k-times-weekly/5249803)). Defense pointer: **npm trusted publishing** and **WebAuthn 2FA** for publish scopes. Debate seed (agenda-listed): *can trusting-trust ever be "solved" or only managed?* Point to [Reproducible Builds](https://reproducible-builds.org/) and Wheeler's [DDC](https://dwheeler.com/trusting-trust/) as partial answers.

**Marquee case: ChainDrop — the Aug 4, 2026 Shai-Hulud wave.** **Read first:** [Datadog Security Labs, Aug 4 2026 — "'ChainDrop' worm compromises hundreds of popular npm packages"](https://securitylabs.datadoghq.com/articles/npm-worm-compromises-popular-npm-packages/) — the most complete technical account, updated through Aug 5.

**What happened:**

- At 09:02:37 UTC on August 4, 2026 a malicious `keyv@6.0.0` appeared on npm.
- The maintainer's account had been compromised (the initial access is not detailed in the public writeups), and the new version carried two obfuscated files, `setup.mjs` and `Math_Symbol.js`, wired to a `preinstall` hook — so simply running `npm install` executed the payload before any test or review.
- Stage one is a small Node loader that downloads a Bun runtime; stage two is a heavily obfuscated credential harvester that sweeps the filesystem, shell configs, environment variables, cloud-provider credentials, CI variables, Kubernetes and Vault secrets, and — new this wave — AI-tool credentials for Claude and OpenAI, then exfiltrates over encrypted channels with GitHub repositories as a fallback and an Ethereum mainnet contract as command-and-control.
- Propagation is what earned it the name: with any npm token that has write rights, the worm republishes every package that token can publish, and it also commits startup hooks into `.claude/settings.json` and `.vscode/tasks.json` across branches of any GitHub repository it can reach, so developers re-infect themselves by opening a project; the malicious commits were authored as 'claude' with the message 'chore: update config.' Within four hours it had poisoned 444 packages and 2,212 versions (JFrog counts 400+ packages / 1,700+ versions; Singapore's CSA counts 1,300+ versions — the tallies differ by cutoff) including `keyv`, `flat-cache`, `file-entry-cache`, `cacheable`, `cacheable-request`, and `cache-manager`, together roughly two billion monthly downloads (Elastic's narrower count is 1.3B+).
- It also abused OpenSearch's npm trusted-publishing setup to sign malicious releases with legitimate OIDC tokens.
- Elastic's monitoring flagged it at 5:39 AM EST; Datadog, JFrog, and Elastic published the same or next day; Singapore's CSA issued a national advisory August 6; The Register's August 15 piece is the accessible summary.
- Status as of Sept 30: packages cleaned, credentials rotated industry-wide, no attribution.
- Unknown: who the operators are, how the keyv maintainer was first compromised, and how many downstream CI secrets were actually used.{B}**What to say:** *"Look at the third bullet on the slide — signing, SBOMs, trusted publishing.
- On August 4th a worm used trusted publishing to sign its own malicious releases, hid in the tarball rather than the source so code review saw nothing, and committed itself into your editor config under the author name 'claude' so the next engineer who opened the repo re-ran it.
- Four hours, four hundred forty-four packages, two billion downloads a month.
- The detail to remember: it specifically went looking for your Claude and OpenAI API keys."* Throw: *"Which of the three defenses on this slide would have stopped it?
- Argue for one."* (Answer you are steering toward: none of them alone — the token *was* the trust.){B}**Course tie-in:** trust extended to maintainers and registries as the attack surface; Thompson's regress made operational; the agenda's debate seed ('can trusting trust be solved or only managed?'); the AI-assisted-code question (an agent's config file is now an execution vector); foreshadows authentication (OIDC, tokens) and PKI.{B}**Also:** [JFrog Security Research, Aug 4 2026](https://research.jfrog.com/post/shai-hulud-is-back-august/) (Ethereum C2 and the OpenSearch trusted-publishing abuse); [Elastic Security Labs, Aug 6 2026](https://www.elastic.co/security-labs/shai-hulud-chaindrop-npm-supply-chain) (the 'claude' commits and per-package download counts); [Cyber Security Agency of Singapore advisory AD-2026-009, Aug 6 2026](https://www.csa.gov.sg/alerts-and-advisories/advisories/ad-2026-009/) (a national-CERT view: what to rotate); [The Register, Aug 15 2026](https://www.theregister.com/security/2026/08/15/chaindrop-worm-crawls-into-npm-supply-chain-evades-standard-defenses/5287958) (tarball propagation and the editor-config hooks).

## 21 · Up Next (divider)

Transition to the second deck: Anderson's [Why Cryptosystems Fail](https://www.cl.cam.ac.uk/~rja14/Papers/wcf.pdf) ([`../../readings/`](../../readings/)). Next deck: [`../01-WhyCryptosystemsFail/`](../01-WhyCryptosystemsFail/). Framing line: Thompson gave us the theory of misplaced trust; Anderson has the field data on where deployed systems actually break.
