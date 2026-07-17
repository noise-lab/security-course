# 01-WhyCryptosystemsFail — instructor notes

## Current-events updates made (point 2)

- **2026-07-16 refresh:**
  - Updated the xz-utils vignette with two verified additions: (a) attribution
    to "Jia Tan" is still unresolved as of mid-2026 (Wikipedia, SentinelOne,
    Akamai reporting); (b) Binarly's Aug 2025 finding that backdoored xz binaries
    still lurk in Debian images on Docker Hub (persistent supply-chain hygiene
    problem, not a closed case). Added an operational speaker-note detail: Freund
    was a Microsoft principal engineer benchmarking PostgreSQL and noticed sshd
    was ~500 ms slower than usual (NPR, Wikipedia).
  - Refreshed the Shai-Hulud slide with the 2026 wave timeline: original Sept 2025
    outbreak; Shai-Hulud 2.0 in Dec 2025 / early 2026 (destructive failsafe);
    TanStack/Mistral AI/UiPath (May 11, 2026); AntV (May 19, 2026); **Red Hat**
    npm namespace (~80K downloads/week, June 1, 2026); public release of the
    weaponized worm code on May 12, 2026. Verified via Microsoft Security Blog,
    Unit 42, CISA advisory, StepSecurity, Akamai, The Register.
- **xz-utils backdoor (CVE-2024-3094) as the headline vignette.** Replaced the
  abstract Thompson framing with the most exact real-world realization of
  "Reflections on Trusting Trust": a contributor ("Jia Tan") spent 2+ years
  earning maintainer trust, then hid an RCE backdoor in the *build scripts*
  (not the source) of a library that OpenSSH loads transitively. Discovered
  March 29, 2024 by Andres Freund; CVSS 10.0; caught by luck before reaching
  stable distros. Verified via Wikipedia and multiple security vendor writeups.
- **npm "Shai-Hulud" worm (Sept 2025, recurring waves into spring 2026)** added
  to frame supply chain as a *trust* problem and to modernize the xkcd-2347
  dependency point. Self-replicating malware that compromised maintainer
  accounts and republished popular packages; one phishing email poisoned
  packages with billions of downloads.
- **Equifax framed precisely** (Apache Struts patch shipped March 7, 2017;
  breach May–July 2017; ~147M records; 2019 FTC/CFPB/states settlement up to
  $700M incl. $300M consumer fund) — kept because it is the cleanest
  "implementation/operations, not crypto" case study and bridges to the policy
  half of the course.
- **FTC Log4j warning (Jan 2022, CVE-2021-44228)** retained and tied explicitly
  to Anderson's thesis: regulators now treat *fixing* implementation/ops
  failures as a legal duty (FTC Act, Gramm-Leach-Bliley). Directly answers the
  agenda's discussion question on how GDPR/CCPA-style regimes shape crypto
  implementation.

## Suggested missing coverage on broad themes (point 3)

- **Reproducible builds / diverse double-compiling** as the concrete partial
  answer to Thompson's regress — worth one slide or a debate pointer; the deck
  currently asserts trust "must stop somewhere" without naming the mitigation.
- **Threat modeling as a discipline** (STRIDE, attack trees, defining adversary
  capabilities) — the deck gestures at it via Anderson's "list all failure
  modes," but Meeting 2 formally introduces threat models; a one-slide bridge
  would help.
- **AI-specific trusting-trust angle** is raised as discussion only. Could be
  expanded: model/weight provenance, prompt-injection and poisoned training
  data, AI-generated code that reintroduces known CVEs, agentic coding tools
  installing dependencies autonomously.
- **Modern key-management failures** (hardcoded secrets in repos, leaked cloud
  keys, KMS misconfigurations) would update Anderson's PIN-key contradiction
  for a cloud-native audience and set up the PKI lecture.
- **Heartbleed / Debian OpenSSL RNG** as named examples for the failure-
  taxonomy activity — currently only seeded in speaker notes.
- **Secure-by-design / CISA pledge** as the modern, named counterpart to
  Anderson's vendor-obligations slide.

## Next-year refresh notes

Refresh the dated content below per `../TEMPLATE.md` → "Annual current-events refresh" (web-verify; swap only for something fresher and confirmed). Items likely to age by next term:

- **xz-utils backdoor (CVE-2024-3094)** remains the freshest exact realization of
  Thompson's argument. Refresh only if (a) formal attribution finally lands, or
  (b) a comparable maintainer-trust exploit with equivalent CVSS 10.0 lands in
  the intervening year. Docker Hub persistence note (Aug 2025) is now the
  living example of "the incident isn't over."
- **npm Shai-Hulud** — the 2026 wave list will keep growing (June 2026 Red Hat is
  the current "big brand" anchor; July 2026 AsyncAPI/jscrambler are smaller but
  show OIDC-provenance-abuse). Recount at term start; if a *different* worm
  family displaces Shai-Hulud, swap.
- **Equifax** — still the cleanest legal-liability worked example; the Struts
  patch was March 7, 2017. Docket now in "wind-down phase" (2026); identity-
  restoration services free until Jan 2029; 7 free credit reports/yr through 2026.
- **FTC Log4j warning (Jan 2022, CVE-2021-44228)** — still the canonical
  "reasonable security" statement. If a specific FTC enforcement action tied
  explicitly to failure-to-patch lands in the coming year, swap that in for the
  warning itself.
- Alternative vignettes flagged but not used: **Salt Typhoon** PRC breach of US
  telecom lawful-intercept systems (crypto-adjacent, spectacular scope); **UK
  Post Office / Horizon** miscarriages of justice as a modern "Anderson-style"
  human-factors-plus-legal-burden case; **CrowdStrike July 2024 outage**
  (implementation-detail failure at global scale).
- **CISA Secure by Design pledge** — as of mid-2026, ~367 signatories (up from 68
  at May 2024 launch, 200+ by Aug 2025). Worth naming as the modern named
  counterpart to Anderson's vendor-obligations slide.
- Flag any stronger alternative vignette you find but choose not to use yet.

## Curated images

- **Used:** `slide002_img001.png` (xkcd 2347 "Dependency" — the modern
  trusting-trust/supply-chain image); `slide007_img006.png` (ATM skimmer
  overlay — physical human-factors attack that still works today);
  `slide003_img002.png` (FTC Log4j warning screenshot — ties Anderson to
  regulatory duty).
- **Dropped:** `slide010_img009/010`, `slide014_img011`, `slide017_img014`,
  `slide018_img015` and other Anderson-paper *text screenshots* — low teaching
  value as images; their content was folded into bullets/quotes instead.
  Dropped `slide019_img016/017`, `slide020_img018/019` (Equifax logo and
  settlement-page screenshots — decorative; facts stated in text). Dropped
  `slide003_img003/004/005`, `slide008`, `slide009`, `slide016`, `slide021`,
  `slide022` as redundant or decorative.

## Source

- Rebuilt from `_source-extract.md` (22 slides) + `agenda.md` Meeting 1
  ("Trusting Trust" and "Why Cryptosystems Fail" lecture coverage and reading
  discussions). Consolidated to 19 slides.
