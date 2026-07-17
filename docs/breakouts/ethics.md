# Research Ethics for Security and Privacy

**Format.** Break into groups of 4–5. Each group picks **one** of the two breakouts below (or takes both if time allows). Spend ~5 minutes skimming the prep reads, then ~10 minutes debating. A designated reporter brings the group's position — and any dissents — back to the full class for a ~3-minute report-back.

Lecture 2 traces the Belmont → Menlo lineage and lands on the awkward reality that the *legal* line (CFAA, DMCA §1201, ToS) and the *ethical* line (respect for persons, beneficence, justice) rarely coincide. Both breakouts pick a live case where the community is arguing about where those lines should sit.

---

## Breakout A: LLM Field Experiments Without Consent
<!-- breakout id="A" status="current" refreshed="2026-07-16" -->

**Motion.** *"The University of Zurich r/changemyview experiment (~1,700 AI-generated comments under fabricated personas, no consent) was worse than Facebook's Emotional Contagion study, and IRBs should treat any LLM-driven deception of online communities as human-subjects research requiring full review — full stop."*

<!-- current-events:start topic="llm-field-experiments-irb-reddit" -->
**Prep reads (5–10 min).**
- ['Unethical' AI research on Reddit under fire](https://www.science.org/content/article/unethical-ai-research-reddit-under-fire) — Science (AAAS), May 2025. The clearest reporter-driven account of the four-month r/changemyview study, the fake-persona methodology (rape survivor, trauma counselor, Black anti-BLM voice), and moderators' complaint to the UZH IRB.
- [AI-Reddit study leader gets warning as ethics committee moves to 'stricter review process'](https://retractionwatch.com/2025/04/29/ethics-committee-ai-llm-reddit-changemyview-university-zurich/) — Retraction Watch, April 2025. UZH's admission that IRB recommendations are "not legally binding" and that the PI received only a formal warning — with the researchers voluntarily withholding publication.
- [Experiment using AI-generated posts on Reddit draws fire for ethics concerns](https://retractionwatch.com/2025/04/28/experiment-using-ai-generated-posts-on-reddit-draws-fire-for-ethics-concerns/) — Retraction Watch, April 2025. Companion piece with the full mod-team complaint, including the contrast with OpenAI's earlier, consent-based use of the same subreddit's public data.
- [Editorial Expression of Concern: Experimental evidence of massive-scale emotional contagion through social networks](https://www.pnas.org/doi/10.1073/pnas.1412469111) — PNAS, July 2014. The rare "editorial expression of concern" attached to Facebook's 2012 study — the exact precedent Zurich's defenders and critics both cite.
<!-- current-events:end -->

**Discussion prompts.**
- The Zurich team argued their work was low-risk public-data research and that their IRB approved a protocol. Reddit's counsel and the r/changemyview mods disagreed. Walk through the four Belmont/Menlo principles (respect for persons, beneficence, justice, respect for law/public interest) — which ones does the study fail, and how badly?
- The 2012 Emotional Contagion study manipulated real users' News Feeds without notice and triggered a global backlash. Zurich's study also manipulated real users but with *synthetic* personas. Does the shift from "manipulating what humans post" to "posting as humans" change the ethical analysis, or is it the same problem?
- "IRB exempt" is doing a lot of work in security research (network scans, public-data scraping, model probing). If you were on an IRB, how would you decide whether an LLM red-teaming study on a live community is exempt, expedited, or full-board? Where's your bright line?
- The lecture's "law is (slowly) catching up" slide mentioned Van Buren and hiQ narrowing CFAA. Do those rulings make things *better* for ethical researchers (safer to scrape) or *worse* (less legal pressure means fewer institutional guardrails)?

**Bring back.** Your group's proposed one-paragraph rule for whether an LLM-driven online experiment needs consent — and one case that would trip your rule.

---

## Breakout B: Coordinated Disclosure vs. Full Disclosure vs. No Disclosure
<!-- breakout id="B" status="current" refreshed="2026-07-16" -->

**Motion.** *"Security researchers have an ethical obligation to publish exploit code publicly after a coordinated disclosure window expires, even when the vendor has not patched — the alternative gives vendors indefinite leverage to keep users at risk."*

<!-- current-events:start topic="vulnerability-disclosure-coordinated-full" -->
**Prep reads (5–10 min).**
- [Project Zero: Reporting transparency policy](https://googleprojectzero.blogspot.com/2025/07/reporting-transparency.html) — Google Project Zero, July 2025. The updated disclosure policy that publishes vendor + CVE metadata within one week of report (technical details withheld until Day 90) — a live experiment in shortening the "upstream patch gap."
- [Project Zero disclosure policy change puts vendors on early notice](https://cyberscoop.com/project-zero-google-zero-day-vulnerability-disclosure/) — CyberScoop, July 2025. Reporter-side context on Google's shift, including Bruce Schneier's objection that Google isn't a neutral disclosure party when its policies pressure competitors' products.
- [Exploits for unauthenticated FortiWeb RCE are public, so patch quickly! (CVE-2025-25257)](https://www.helpnetsecurity.com/2025/07/14/exploits-for-unauthenticated-fortiweb-rce-are-public-so-patch-quickly/) — Help Net Security, July 2025. The concrete FortiWeb case: watchTowr Labs published a technical write-up on July 11, mass exploitation began the same day, and CISA added the CVE to KEV within days.
- [U.S. CISA adds Fortinet FortiWeb flaw to its Known Exploited Vulnerabilities catalog](https://www.cisa.gov/news-events/alerts/2025/07/18/cisa-adds-known-exploited-vulnerability-catalog) — CISA, July 2025. The government-side data point on how fast a public PoC translates into "in-the-wild" — 77 compromised appliances tracked by Shadowserver within five days.
<!-- current-events:end -->

**Discussion prompts.**
- Google Project Zero's 90-day (+30 for patch adoption) policy is the de facto industry norm. Is 90 days a principled number, a bureaucratic compromise, or both? What would you change and why?
- The Menlo Report's "respect for law and public interest" principle asks researchers to weigh third-party harm. In a world of automatic exploit weaponization (metasploit modules, PoCs weaponized within hours per Shadowserver), does publishing PoCs help defenders more than attackers, or the reverse?
- The FortiWeb SQLi (CVE-2025-25257) had public PoC from watchTowr on 2025-07-11 and dozens of appliances compromised within days. If watchTowr had held the PoC for another 30 days, would net harm have been lower — or would slow-patching vendors just have taken 30 more days?
- Dual-use publications (offensive ML weights, exploit chains, novel attack techniques): when does *publishing* itself become the ethical question, independent of any target? Is there a version of the Belmont "beneficence" principle that says "some knowledge should not be published"?

**Bring back.** Your group's disclosure timeline (in days) for a critical unpatched vulnerability affecting consumer devices, and the one condition that would make your timeline change.

---

## Instructor notes

Breakout A gets the loudest engagement — students have strong intuitions about being manipulated online. Push them to distinguish the ethics from the legality (nothing Zurich did was clearly illegal). Breakout B is where the CS students shine; the disclosure debate has fewer easy answers. If time is short, run A as the whole-class discussion and hold B for the CFAA-focused Lecture 7 breakout day. Both benefit from a quick reminder that the Menlo Report is the field's answer to the fact that most computer science research is not obviously "human-subjects."

<!--
breakout-metadata:
  lecture: 2
  class: "Ethics"
  last_refreshed: 2026-07-16
-->
