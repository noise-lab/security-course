# XX-Vulnerabilities — instructor notes

## Current-events updates made (point 2)
- **Lead vignette (May 2026, verified):** Replaced the dated Felten/Sklyarov-only framing
  of the disclosure conflict with the live **"Chaotic Eclipse" vs. Microsoft** dispute —
  a researcher dumped PoCs for unpatched Windows zero-days (*BlueHammer* CVE-2026-33825,
  *RedSun*, *UnDefend*), several were exploited in the wild within days, Microsoft
  condemned the uncoordinated disclosure and GitHub removed the account; Microsoft later
  said it would not pursue the researcher. Sources: The Hacker News (2026-05),
  Security Affairs, and The Record (therecord.media). This is the modern restatement of
  the 25-year-old Felten/SDMI fight and makes the disclosure spectrum + incentives
  concrete.
- **Added a zero-day / exploit-market slide** (not in the original deck) to introduce the
  vocabulary and the grey/black-market economics that motivate bug bounties.
- **Modernized the CFAA case law:** kept the historical Drew/Facebook/hiQ progression but
  added a dedicated **Van Buren v. United States (2021)** and **Sandvig v. Barr (2020)**
  slide — the pro-researcher counterweight that postdates the original slides. Sources:
  EFF (Van Buren), Columbia Global Freedom of Expression (Sandvig v. Barr).
- Reframed "responsible disclosure" as **coordinated disclosure** (current preferred term)
  and noted the de facto 90-day norm.

## Suggested missing coverage on broad themes (point 3)
- **CVE / CVSS / the vulnerability-management pipeline.** The deck title promises "CVE" but
  the source slides never define it. Add one slide: CVE IDs, the CVE/NVD ecosystem, CVSS
  scoring, and the recent **CVE program funding/governance scare (2025)** plus the rise of
  EUVD and other alternatives. Ties directly to the pentest-severity tables already shown.
- **CISA KEV catalog and coordinated disclosure infrastructure.** Mention CISA's Known
  Exploited Vulnerabilities catalog and CERT/CC's coordination role — the institutional
  plumbing behind "coordinated disclosure."
- **The exploit-broker / government market in depth.** NSO Group, Zerodium-style brokers,
  and the policy question of governments stockpiling vs. disclosing (the "equities
  process," EARN/VEP). Strong debate material adjacent to the existing CFAA debate.
- **Bug-bounty platforms as institutions:** HackerOne / Bugcrowd, safe-harbor language,
  and `security.txt` / `/.well-known` and ISO/IEC 29147 (disclosure) + 30111 (handling) as
  the standards that now formalize what used to be ad hoc.
- **Supply-chain and dependency vulnerabilities:** Log4Shell-style transitive bugs, SBOMs,
  and why "who is responsible for disclosure" gets murky across a dependency tree.
- **AI-assisted vulnerability discovery (2025–2026):** LLM fuzzing/agents finding bugs at
  scale, and the new disclosure-flood problem (low-quality AI-generated reports swamping
  maintainers and bounty programs) — directly relevant and very current.
- **DMCA Section 1201 research exemptions:** the triennial Library of Congress exemptions
  that now partially shield good-faith security research — the legal relief valve the
  Felten/Sklyarov era lacked.

## Curated images
- **Used `slide021_img023.png`** — Google VRP payout table; a genuine teaching artifact for
  bounty tiering and the zero-day-market economics.
- **Used `slide024_img024.png`** — Cure53 Mozilla VPN penetration-test report excerpt; real
  artifact showing severity-ranked, actionable findings.
- **Dropped** the headline/screenshot images (Nest leak headline `slide003_img001`,
  Zuckerberg-Facebook-hack headline `slide018_img017`, Sandvig/Van Buren title banners
  `slide013_img009`/`slide015_img013`, court-opinion footnote `slide016_img016`, Sklyarov
  headshot `slide007_img004`, and the various logo/decorative images) — these are text or
  decoration and are better conveyed as slide text per the template's image-curation rule.

## Source
- Rebuilt from `_source-extract.md` (25 slides) consolidated to ~22 slides + `agenda.md`
  ("Debate: CFAA"; the agenda has no detailed lecture record for this meeting, so the deck
  relies on the source extract + domain knowledge + verified June 2026 web research).
