# 14-Copyright — instructor notes

## Current-events updates made (point 2)
- **2026-07-16 refresh.** Extended the Anthropic vignette with the **May 14, 2026**
  final fairness hearing (Judge Martínez-Olguín, N.D. Cal.), the **92.77% claims rate**,
  and the **August 2026** estimated initial-payment window (verified via Publishing
  Perspectives, Authors Alliance, Publishers Weekly, Authors Guild). Named the parallel
  Meta ruling as **Kadrey v. Meta (June 25, 2025)** — Chhabria — and added his
  **"market dilution"** framing as the direction future plaintiffs are being pushed
  (verified via Goodwin, Jackson Walker, Skadden). Noted NYT v. OpenAI still in discovery
  (no fair-use merits ruling yet). Speaker notes rewritten in compact table format (see
  `speaker-notes.md`); dropped the per-URL glosses appendix in favor of per-slide
  clickable citations.
- **New lead vignette: Bartz v. Anthropic (verified, dated).** Judge William Alsup
  (N.D. Cal.) ruled **June 23, 2025** that training an LLM on books is "exceedingly
  transformative" / fair use, *but* that downloading 7M+ pirated books for a permanent
  library was **not** fair use. Anthropic agreed to a reported **~$1.5B** settlement
  (notice filed Sept 2025), described as the largest U.S. copyright settlement. Sources:
  ArentFox Schiff, Norton Rose Fulbright, Kluwer Copyright Blog, Authors Guild.
- **Teaching thread surfaced:** Alsup is the *same* judge who first ruled APIs
  uncopyrightable in Google v. Oracle (2012) — used to connect the Oracle case to the
  2025 AI case via the single idea of transformative use.
- **AI-training slide grounded in real rulings:** added the Meta parallel fair-use ruling
  (June 2025) and framed the open question as Supreme-Court-bound rather than decided.
  Deliberately did NOT assert a NYT v. OpenAI outcome (not verified; that case had no
  fair-use merits ruling at time of writing) — kept general.
- **Replaced the old "$2B annually / 98% of claims" Content-ID statistics** with
  qualitative claims ("100M+ reference files," "vast majority of actions," "billions to
  rights holders") to avoid stating figures I could not re-verify for 2026.
- **Softened the NASA Mars-landing example** into a general "government/public-domain
  footage re-claimed by a broadcaster" pattern in a notes block, rather than asserting a
  specific dated incident, since the precise mechanism is easy to misstate.

## Suggested missing coverage on broad themes (point 3)
- **AI-generated output and authorship.** The deck covers copying *into* AI (training) but
  not copyright *of* AI output. The U.S. Copyright Office position (human-authorship
  requirement; AI-as-tool vs. pure AI output) is a natural and current addition — and a
  good contrast with the training debate.
- **Licensing markets as the emerging "answer."** Many rights holders are now signing
  paid licensing deals with AI companies. Worth a slide: if a licensing market exists,
  Factor 4 (market harm) gets stronger for plaintiffs — a feedback loop between law and
  business model.
- **The data-provenance / piracy distinction deserves its own beat.** Bartz shows that
  *lawful acquisition* may matter more than *use*. Students should see that "fair use of
  the use" and "lawful source of the copy" are separable questions.
- **EU contrast (DSM Directive Art. 17 + the text-and-data-mining exception with opt-out).**
  The deck is U.S.-centric; a short comparison would show how upload filters and a
  rights-holder opt-out regime diverge from U.S. fair use.
- **DMCA §1201 anti-circumvention** (separate from §512 takedowns) — relevant to security
  research and the course's broader security theme; currently absent.
- **Empirical grounding on fair use.** Beebe's empirical study (Factor 1 is the strongest
  predictor) would let students see that "transformative wins" is data, not just doctrine.
- **Statutory damages mechanics.** The "billions in jury verdicts" claim would land harder
  with the actual $750–$150,000-per-work statutory range and why class certification (as in
  Bartz, ~500k works) creates existential exposure.

## Next-year refresh notes

Refresh the dated content below per `../TEMPLATE.md` → "Annual current-events refresh" (web-verify; swap only for something fresher and confirmed). Items placed in prior refreshes that will age:

- **Anthropic vignette** — after final approval (expected 2026), swap in the entered
  order + first-round payments (target date August 2026 or later). Track any appellate
  activity from opt-outs; the 28-author non-class action (3:26-cv-04482 N.D. Cal.) and
  the Kwon v. Anthropic follow-on are the ones to watch.
- **NYT v. OpenAI** — should produce its first substantive fair-use ruling in 2026–27
  (summary judgment briefing concluded April 2, 2026); watch for a merits decision and
  swap it into the AI-training slide when it lands. The July 9, 2026 sanctions motion
  may reshape the record.
- **Kadrey v. Meta** — appellate posture likely by 2026–27; "market dilution" theory
  will be tested in later cases (music publishers v. Anthropic, artists v. Stability).
- **Content ID statistics** — currently qualitative to avoid staleness. If YouTube
  publishes fresh 2026 figures worth citing (e.g., annual payouts to rights holders),
  add them back.
- Flag any stronger alternative vignette you find but choose not to use yet.

## Curated images
- No images used. This deck is text-driven; there is no images/ folder for it (per task).
  The two code blocks (declaring vs. implementing) and four tables (four-factor test,
  Oracle timeline, Oracle factor-by-factor, Court's findings) carry the visual load. If a
  diagram is ever added, the highest-value one is a Content-ID pipeline flow
  (reference upload → fingerprint → scan → block/monetize/track).

## Source
- Rebuilt from the existing Marp `slides.md` (33 slides) + `speaker-notes.md`, aligned to
  `agenda.md` Meeting on "Copyright Law and Fair Use" (lines ~1158–1264). Consolidated to
  **22 slides** (incl. 3 section dividers). Prioritized the agenda's flagged midterm items:
  four-factor test, transformative use, and the for/against AI fair-use case-study drill.

## 2026-11-18 graphics pass (deck-graphics skill)

Deck went from 23 headings (22 slides + title) to 30 rendered slides. No legacy
clippings exist for this topic (no pptx), so every picture is new; the
dated-vs-landmark rule applied only to captures, all of which are live refreshes
of the primary source and should be re-captured at the next annual pass.

**Graphviz diagrams (8):** idea/expression split (slide 4); four-factor weighing
diagram (new slide 8, "Weighing the Four Factors"); Oracle ruling ping-pong strip
under the timeline table (slide 16); Content ID pipeline, reference → fingerprint
→ compare → policy → block/monetize/track (slide 19); DMCA §512 notice,
takedown, counter-notice, 10–14 days, suit-or-restore flow with repeat-strike
box (slide 21); AI-training decision flow, acquisition → transformative →
market dilution (new slide 25); human-control spectrum for AI output (new slide
27); licensing-market feedback loop (new slide 28).

**Live captures (6, all clickable, captured Nov 18 2026):** Authors Alliance
final-approval post (slide 3); 17 U.S.C. §107 at Cornell LII (slide 6); Google
v. Oracle opinion page at Cornell LII (slide 14); YouTube Copyright Transparency
Report summary (new slide 20, "Content ID by the Numbers"); U.S. Copyright
Office AI page (new slide 26). Also captured and kept in `images/captures/` but
linked from the notes rather than placed on a slide: 17 U.S.C. §512 at LII
(`s512.png`; the slide links the statute in text) and YouTube's Content ID
help page (`contentid.png`). Dropped: `anthropiccopyrightsettlement.com`
returned "The request is blocked" (linked in the notes instead); Oyez's case
page captured fine but duplicated the LII capture; AI Lawsuit Tracker's NYT page
captured fine but there was no room on the AI-training slide (linked in the
notes). `copyright.gov/ai` hung headless Chrome on the first attempt (no
timeout in `deck-graphics.py capture`); it captured on a second run with a
per-page timeout.

**Current-events verification (web, Nov 18 2026):**
- Bartz v. Anthropic: final approval **July 20, 2026** (Judge Martínez-Olguín),
  fees cut to ~$101.5M, >91% of authors claimed, appeals of the final judgment
  filed; first payments expected the **week of Nov 23, 2026** at ~70% of each
  claim pending the Sept 2026/Sept 2027 installments (Authors Guild page updated
  Nov 16 2026; Authors Alliance; JURIST; Writer Beware). Vignette rewritten to
  replace the May 14 fairness-hearing/August-payment text.
- Kadrey v. Meta: no Ninth Circuit appeal pending; Chhabria **denied interlocutory
  appeal July 8, 2026** ("tidy package" after final judgment); remaining claims in
  discovery. Added to slide 24.
- NYT v. OpenAI: cross-motions for summary judgment on fair use filed **Sept 4,
  2026**, oppositions Oct 23, replies due Nov 20; **no ruling** (AI Lawsuit
  Tracker, reviewed Nov 16 2026). Slide 24 updated from "still in discovery".
  A DOJ statement of interest backing OpenAI's fair-use defense was reported but
  only by secondary trackers; not placed on the slide.
- Content ID statistics restored with a primary source: YouTube Copyright
  Transparency Report, calendar 2025 (2.5B claims, >99% of actions, >99%
  automated, >90% monetized, 0.51% disputed, 67% of disputes to the uploader,
  $12B+ cumulative to rights holders by Dec 2024; TorrentFreak Jun 6 2026 for
  the exact figures).

**Missing coverage now added (two of the point-3 items):**
- *AI output and authorship* (slides 26–27): Copyright Office *Copyright and AI,
  Part 2* (Jan 29, 2025) and Thaler v. Perlmutter (D.C. Cir. 2025; **cert denied
  March 2, 2026**, No. 25-449; Holland & Knight, Finnegan, Baker Donelson).
- *Licensing markets* (slide 28): News Corp–OpenAI ($250M+/5 yr, 2024),
  Reddit–Google (~$60M/yr, 2024), Wiley $49M FY2026 (CASRAI roundup citing
  Wiley's results), Press Gazette tracker's four-in-five-undisclosed count (via
  secondary summaries; the tracker URL itself 404'd on fetch). Framed as a
  Factor 4 feedback loop.

**Type:** `.smaller` dropped from the Anthropic vignette (slide 3), which now has
a capture beside it. Every other `.smaller` slide carries a table, a code block,
two columns, or a figure.

**Still missing (unchanged from the July list):** data-provenance beat as its own
slide (now partly covered by the decision flow), EU DSM Art. 17 / TDM opt-out,
DMCA §1201, statutory-damages mechanics, Beebe chart as a generated figure.

**Next refresh:** re-capture all six pages; swap in the Bartz payment outcome and
any appellate ruling; check for a NYT v. OpenAI summary-judgment decision and a
Ninth Circuit Kadrey appeal; refresh the 2025 Content ID numbers with the 2026
report; re-check the licensing figures (Wiley FY2027, new disclosed deals).
