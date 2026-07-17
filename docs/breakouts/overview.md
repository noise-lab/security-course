# Course Overview: Why Cryptosystems Fail and Trusting Trust

**Format.** Break into groups of 4–5. Each group picks **one** of the two breakouts below (or takes both if time allows). Spend ~5 minutes skimming the prep reads, then ~10 minutes debating. A designated reporter brings the group's position — and any dissents — back to the full class for a ~3-minute report-back.

Lecture 1 pairs Anderson's "Why Cryptosystems Fail" (the crypto rarely breaks — the *implementation* and the *humans* do) with Thompson's "Reflections on Trusting Trust" (you cannot trust code you did not totally create yourself). The two breakouts below take one motion from each — because both remain painfully load-bearing in 2026.

---

## Breakout A: Should Regulators Treat Implementation Failure Like a Product Defect?
<!-- breakout id="A" status="current" refreshed="2026-07-16" -->

**Motion.** *"Anderson was right: the vast majority of security failures are boring implementation and operations bugs, not cryptographic weaknesses. Regulators (FTC, CISA, state AGs) should therefore treat unpatched CVEs and misconfigured systems as strict-liability product defects, the same way we treat exploding batteries."*

<!-- current-events:start topic="ftc-cisa-cve-liability" -->
**Prep reads (5–10 min).**
- [FTC warns companies to remediate Log4j security vulnerability](https://www.ftc.gov/policy/advocacy-research/tech-at-ftc/2022/01/ftc-warns-companies-remediate-log4j-security-vulnerability) — Federal Trade Commission, January 2022. The FTC's blog post that first put unpatched Log4j on the "unfair practices" enforcement radar under Section 5 and GLBA, citing the Equifax precedent.
- [Equifax to Pay $575 Million as Part of Settlement with FTC, CFPB, and States Related to 2017 Data Breach](https://www.ftc.gov/news-events/news/press-releases/2019/07/equifax-pay-575-million-part-settlement-ftc-cfpb-states-related-2017-data-breach) — Federal Trade Commission, July 2019. The settlement that made "failure to patch a critical known CVE" a concrete Section 5 violation, at ~$575M base plus contingent funds up to $700M.
- [CISA Secure by Design Pledge](https://www.cisa.gov/securebydesign/pledge) — Cybersecurity and Infrastructure Security Agency, May 2024 (256+ signatories by December 2024). CISA's voluntary alternative to strict liability: seven measurable goals (MFA defaults, vuln-class reduction, VDPs, CVE hygiene) that vendors self-attest to within a year.
- [How the EU Cyber Resilience Act Transforms Cybersecurity Into Product Liability Law](https://www.law.berkeley.edu/research/bclt/bclt-legal-analysis/how-the-eu-cyber-resilience-act-transforms-cybersecurity-into-product-liability-law/) — UC Berkeley Law BCLT, 2025. Analysis of the EU CRA (in force December 2024, full compliance December 2027) as the world's first legal regime that ties cybersecurity failure directly to CE-marking and PLD product liability.
<!-- current-events:end -->

**Discussion prompts.**
- Anderson's ATM data showed that PIN losses came from procedural failures (mailed PINs, insider fraud, buggy verification) — not broken crypto. The Equifax breach (147M records, Apache Struts patch shipped March 2017, exploited May–July) fits the same pattern. If the failure is *always* implementation and ops, is the FTC's Section 5 "unfair practices" theory the right instrument, or does it need statutory backup?
- The FTC's 2022 Log4j warning treated *failure to patch* as a legal duty under GLBA and Section 5. Under a strict-liability regime, would small vendors (open-source maintainers, one-person shops) go out of business, or would insurance and vulnerability-management markets absorb the risk?
- The lecture's threat-modeling primer asks: assets, adversaries, capabilities. If regulators only punish *outcomes* (breach happened → penalty), do they get the incentives right — or do they push vendors toward defensive paperwork rather than actual hardening?
- Consider the counter-model: safe-harbor regimes (like some state data-breach laws) that shield companies who followed "reasonable security practices." Which framing — strict liability or safe harbor — better tracks Anderson's argument?

**Bring back.** Your group's one-sentence rule for when a CVE-driven breach should trigger regulator action, and one edge case where your rule breaks.

---

## Breakout B: xz-utils and the Limits of Open-Source Trust
<!-- breakout id="B" status="current" refreshed="2026-07-16" -->

**Motion.** *"The xz-utils backdoor (CVE-2024-3094) proved Thompson right in the worst possible way: no amount of code review saves you from a maintainer who spent years earning your trust. The correct response is to move critical infrastructure off individually-maintained OSS onto vendor-supported forks — even at the cost of the OSS ecosystem."*

<!-- current-events:start topic="xz-utils-supply-chain-oss-maintainers" -->
**Prep reads (5–10 min).**
- [xz-utils backdoor situation (CVE-2024-3094)](https://gist.github.com/thesamesam/223949d5a074ebc3dce9ee78baad9e27) — Sam James (community-maintained reference), March 2024 onward. The canonical timeline and technical dissection of Jia Tan's 2+ year social-engineering campaign, the sockpuppet pressure on the original maintainer, and Andres Freund's 500ms-latency accident that caught it.
- [XZ Utils Backdoor — Everything You Need to Know](https://www.akamai.com/blog/security-research/critical-linux-backdoor-xz-utils-discovered-what-to-know) — Akamai Security Research, April 2024. Vendor-side write-up covering the IFUNC hijack of RSA_public_decrypt, why the malicious build-to-host.m4 evaded source review, and the near-miss with Debian/Fedora stable.
- [Widespread Supply Chain Compromise Impacting npm Ecosystem](https://www.cisa.gov/news-events/alerts/2025/09/23/widespread-supply-chain-compromise-impacting-npm-ecosystem) — CISA, September 2025. Official alert on the self-propagating "Shai-Hulud" worm that compromised hundreds of npm packages via maintainer phishing — the same trust-in-a-maintainer failure at ecosystem scale.
- [Sustaining Digital Certificate Security — Chrome Root Store changes](https://blog.google/security/sustaining-digital-certificate-security-chrome-root-store-changes/) — Google Security Blog, May 2025. Not xz per se, but the same institutional pattern: when a single trusted actor stops being trustworthy, downstream users have almost no recourse except distrust-and-fork.
<!-- current-events:end -->

**Discussion prompts.**
- "Jia Tan" spent 2+ years contributing to xz-utils before hiding the backdoor in build scripts, not source. Andres Freund caught it by accident, days before it would have shipped in stable Debian/Fedora. Thompson's compiler-in-a-compiler regress has an obvious answer here: nobody was auditing the build system. What *would* have caught this, and would you actually deploy it?
- The npm "Shai-Hulud" worm (Sept 2025 and recurring) compromised maintainer accounts and republished popular packages via one phishing email. Is this a Thompson problem, an Anderson problem, or both — and does that classification change the fix?
- Reproducible builds and "diverse double-compiling" are the standard partial answers to trusting-trust. If your employer told you tomorrow that every dependency must be reproducibly built, would that be feasible, and what would you *lose*?
- The lecture asks whether AI code-generation tools reintroduce this problem at machine speed (poisoned training data, hallucinated dependencies, agentic installers). Does "trust" mean something different when the code was suggested by an LLM than when it was suggested by a stranger on GitHub?

**Bring back.** The one class of software your group would *never* trust to an individually-maintained OSS project, and the one where you think the OSS model still wins.

---

## Instructor notes

Breakout A works well as the framing debate — it foregrounds the "policy is inseparable from technique" thread that runs through the whole course. Breakout B is punchier for a technical audience but assumes students have skimmed the Thompson paper. If time is short, run A: it previews the FTC/CISA/state-AG through-line that recurs in Lectures 11, 12, and 15. If your class has more systems folks than policy folks, flip and run B — the xz-utils dissection lands and produces stronger report-backs.

<!--
breakout-metadata:
  lecture: 1
  class: "Overview + Why Cryptosystems Fail + Trusting Trust"
  last_refreshed: 2026-07-16
-->
