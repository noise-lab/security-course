# Lecture 1 — Speaker Notes (Why Cryptosystems Fail)

Per-slide context + clickable links (one section per slide; case briefs are broken into Read first / What happened / What to say / Course tie-in / Also) for the second half of Meeting 1 (the Trusting Trust segment now lives at the end of the overview deck — see [`../01-Overview/speaker-notes.md`](../01-Overview/speaker-notes.md)). In-deck notes (the `::: {.notes}` blocks) are also visible in reveal.js speaker view (press **S**). Every URL was verified this session or is a canonical org landing page. Follows the course-overview deck: [`../01-Overview/speaker-notes.md`](../01-Overview/speaker-notes.md).

## Where Does It Actually Break?

Both readings are canonical: **Ken Thompson, "Reflections on Trusting Trust"** — 1984 Turing Award lecture, CACM 27(8):761–763, [ACM DL](https://dl.acm.org/doi/10.1145/358198.358210); [Cambridge PDF](https://www.cl.cam.ac.uk/teaching/2223/R209/Reflections-Trusting-Trust.pdf); annotated at [Fermat's Library](https://fermatslibrary.com/s/reflections-on-trusting-trust). **Ross Anderson, "Why Cryptosystems Fail"** — 1st ACM CCS 1993, pp. 215–227, [ACM DL](https://dl.acm.org/doi/10.1145/168588.168615); [Cambridge PDF](https://www.cl.cam.ac.uk/~rja14/Papers/wcf.pdf); Anderson's own page: [`cl.cam.ac.uk/archive/rja14/wcf.html`](https://www.cl.cam.ac.uk/archive/rja14/wcf.html). Anderson died in March 2024; [Bruce Schneier's tribute](https://cacm.acm.org/news/in-memoriam-ross-anderson-1956-2024/) is a good one-line pointer if a student asks. Two papers, one lesson: the failure is almost never the math.

### Case: the ChainDrop npm worm (Aug 4, 2026)

> **Read first:** [Microsoft Security Blog — "ChainDrop supply chain compromise: Anatomy of a self-propagating worm" (Aug 4, 2026)](https://www.microsoft.com/en-us/security/blog/2026/08/04/chaindrop-supply-chain-compromise-anatomy-self-propagating-worm/) — the most complete technical account, with the propagation loop and the editor-config persistence spelled out.

**What happened:**

- On the morning of Aug 4, 2026 (Elastic's first alert was ~5:39 AM ET), a malicious release of `keyv` — a key-value storage shim with roughly 150M weekly / 600M+ monthly downloads — appeared on npm, published with the maintainer's own credentials.
- The package carried a `preinstall` lifecycle hook that ran before installation finished: it fetched the Bun runtime, executed a large obfuscated JavaScript payload, and harvested credentials on the developer machine or CI runner against 300+ patterns (npm, GitHub, AWS/GCP/Azure, Vault, Kubernetes, AI-tool keys).
- Whenever it found an npm publish token with write rights — preferring tokens flagged `bypass_2fa: true`, the CI-convenience setting — it enumerated every package that identity could publish, downloaded the latest tarball, inserted itself plus the hook, bumped the patch version, and republished.
- Because it rebuilt the *published tarball* and never touched a git commit, the source repositories stayed clean.
- Within about four hours it had poisoned 444 packages and 2,212 versions across more than a dozen organisations, including `flat-cache`, `file-entry-cache`, `cache-manager`, and `cacheable-request` — roughly 2B monthly downloads in aggregate.
- With stolen GitHub tokens it also committed hooks into `.claude/settings.json` and `.vscode/tasks.json` across repository branches, so simply opening an infected branch in VS Code or Claude Code re-ran the payload with no `npm install` at all.
- Command-and-control addresses were published via an Ethereum smart contract so infrastructure could rotate without new code, and a dead-man switch executed attacker-supplied code if the stolen tokens were revoked.
- Microsoft, Elastic, Unit 42, JFrog, StepSecurity and Datadog all classify it as a "Mini Shai-Hulud" variant in the TeamPCP lineage (Shai-Hulud, Sept 2025; TanStack/Mistral/UiPath wave, May 2026, tracked as CVE-2026-45321, CVSS 9.6).
- Status as of Sept 30, 2026: the malicious versions were pulled and tokens rotated; attribution remains unconfirmed, and no one has published a count of downstream builds that consumed the bad versions during the window.

**What to say:**

- "Thompson told you in 1984 that you can't trust code you didn't write, and the comeback for forty years has been 'fine, I'll read the source.' On August 4th this year that comeback died.
- A worm got one maintainer's npm token — one person — and within four hours it had rewritten 444 packages that two billion installs a month depend on.
- Here's the detail I want you to remember: it never touched GitHub.
- It rebuilt the *tarball* that npm ships.
- If you had opened the repo and read every line, it would have looked perfect.
- And then the part that should make you sit up: it wrote itself into `.claude/settings.json` and `.vscode/tasks.json`, so the next developer who opened the branch in their editor got infected without installing anything.
- Your coding assistant is now part of the trusted computing base.
- So — question for the room — where does your trust actually stop?
- Your compiler?
- Your package manager?
- Your editor?
- Your AI agent?
- Pick one and defend it."

**Course tie-in:**

- Misplaced trust, first and foremost — Thompson's compiler regress transplanted into the build-and-distribute pipeline; secondarily key management (a long-lived publish token with 2FA bypassed) and operational (a `preinstall` hook is a design choice the ecosystem accepted).
- Echoes Anderson's ATM insiders: one trusted identity, no second check.
- Foreshadows Meeting 2 (keys and tokens as the crown jewels), the software-supply-chain material later in the term, and the AI-trust discussion prompt on the Food for Thought slide.

**Also:**

- [Elastic Security Labs — "Shai-Hulud strikes again: CHAINDROP worm hits 400+ npm packages" (Aug 6, 2026)](https://www.elastic.co/security-labs/shai-hulud-chaindrop-npm-supply-chain) — timeline, the `bypass_2fa` detail, the Ethereum C2.
- [The Register — "ChainDrop worm crawls into npm supply chain, evades standard defenses" (Aug 15, 2026)](https://www.theregister.com/security/2026/08/15/chaindrop-worm-crawls-into-npm-supply-chain-evades-standard-defenses/5287958) — why source review, provenance and scanners all missed it.
- Lineage back to Sept 2025 is summarized in `coverage-notes.md` in this directory.

## Anderson's Surprise

The paper's central claim: in the 1990s UK banking system, **customers bore the fraud burden**, so banks had structurally weak incentives to hunt for their own bugs; meanwhile, **cryptology got little public feedback** because governments (the main users) never disclosed how their systems failed. Contrast this with modern breach-notification laws (state laws in the US, GDPR Art. 33 in the EU) that *force* public feedback. Cold-call: *"If your bank told you 'the ATM never makes mistakes; if there's a discrepancy, it's your fault,' what would that do to their patch cycle?"* Ties to the agenda's discussion question on how GDPR/CCPA shape crypto implementation.

### Case: the UK flipped Anderson's incentive — and fraud fell (PSR evaluation, Jul 1, 2026)

> **Read first:** [Regulation Tomorrow (Norton Rose Fulbright) — "Payment fraud falls by £73m following PSR reimbursement scheme" (Jul 1, 2026)](https://www.regulationtomorrow.com/2026/07/payment-fraud-falls-by-73m-following-psr-reimbursement-scheme/) — a clean summary of the independent evaluation's numbers and its incentive finding.

**What happened:**

- Since Oct 7, 2024 the UK Payment Systems Regulator (PSR) has required payment firms to reimburse victims of authorised-push-payment (APP) scams — the case where the customer is tricked into sending the money themselves — with liability split 50/50 between the sending and receiving bank, up to a per-claim cap. Before that, reimbursement was voluntary under an industry code and, as Anderson described for the 1990s, the customer usually ate the loss.
- On Jul 1, 2026 the PSR published an independent third-party evaluation of the first year: APP fraud losses sent over Faster Payments fell about 21%, roughly £73M a year; the share of losses reimbursed rose from 54% to 65% (89% for in-scope claims); individual scam cases fell by nearly 35,000; and even after counting firms' new detection spend and payouts, the net short-term economic benefit was put at £17M–£29M.
- The report explicitly credits the mechanism Anderson predicted: mandatory reimbursement "strengthened incentives for PSPs to invest in fraud prevention.
- It also notes outcomes for victims remain inconsistent because of scope limits and exceptions.
- UK Finance's annual fraud report (Jun 15, 2026) gives the wider picture for 2025: £1.28B total payment fraud (+4%), of which unauthorised fraud £703.4M (−5%) and APP fraud £576.4M (+19%), with £354.3M (61%) reimbursed across all account types.
- Status as of Sept 30, 2026: PSR stakeholder engagement over summer 2026, formal consultation on changes scheduled for Dec 2026; the two reimbursement percentages differ because PSR counts only in-scope claims while UK Finance counts everything.

**What to say:**

- "Anderson's most important sentence isn't about cryptography at all.
- It's that in 1990s Britain, if your card was cloned, *you* had to prove the bank was wrong — so the bank had no reason to look for its own bugs.
- Fast-forward: in October 2024 the UK made banks reimburse push-payment scam victims by law.
- It's the cleanest natural experiment we have.
- One year later fraud through the main payment rail is down a fifth, seventy-three million pounds, and the regulator's own evaluators say the reason is that banks finally had a reason to invest in detection.
- Nothing about the cryptography changed.
- The only thing that changed is who pays.
- The number to remember: 21%.
- The question: if we did the same thing for data breaches in the US — you leak my data, you pay — what would Equifax's patch cycle have looked like in 2017?
- We debate exactly that later tonight."

**Course tie-in:**

- Operational / organizational failure in Anderson's taxonomy — the incentive structure, not the mechanism — and the direct answer to the slide's "legal burden fell on customers" bullet.
- Foreshadows the data-breach liability debate (`../../debates/data-breach.md`) and the regulatory half of the course (FTC reasonable-security theory, GDPR Art. 33 breach notification as forced public feedback).

**Also:**

- [UK Finance — "Fraud remains a national security threat as criminals steal almost £1.3 billion" (Jun 15, 2026)](https://www.ukfinance.org.uk/news-and-insight/press-release/fraud-report-2026-press-release) — the 2025 headline numbers.

## How ATM Fraud Actually Happened

None of the failure modes Anderson catalogs is a break of DES. Contemporary analog: [Krebs on Security's ATM skimmer archive](https://krebsonsecurity.com/all-about-skimmers/) — the physical version is alive and well in 2026, especially at gas pumps. The image on the slide is a real skimmer overlay. Teaching move: give students the story of the clerk issuing an extra card and the customer whose complaint was stonewalled — this is a human-factors + institutional-power failure, not a cryptography failure.

### Case: malware jackpotting — FBI FLASH (Feb 19, 2026) and the Tren de Aragua prosecutions

> **Read first:** [FBI FLASH-20260219-001, "Increase in Malware Enabled ATM Jackpotting Incidents Across United States" (PDF, Feb 19, 2026)](https://www.ic3.gov/CSA/2026/260219.pdf) — the primary source; four pages, with the numbers, the XFS explanation and the infection methods.

**What happened:**

- The FBI's Feb 19, 2026 FLASH reports 1,900 ATM jackpotting incidents in the US since 2020, more than 700 of them in 2025 alone, with 2025 losses above $20M.
- The method: crews surveil a target (photograph it, test whether opening the hood trips an alarm), preferring standalone machines in rural locations, and hit several ATMs of the same institution within a day or two.
- They open the ATM face with widely available generic keys, then either pull the hard drive and copy malware onto it, swap in a pre-loaded drive, or plug in a thumb drive.
- The malware family is **Ploutus**, which speaks directly to XFS (eXtensions for Financial Services) — the software layer that tells the hardware what to physically do.
- Normally the ATM application sends a withdrawal through XFS only after bank authorization; Ploutus issues its own XFS commands, so, in the FBI's words, it can "bypass bank authorization entirely" and dispense on demand with no card, account or authorization, then delete itself.
- The prosecutions: DOJ's investigation into an international jackpotting scheme run by members of Tren de Aragua (a Venezuelan gang designated a Foreign Terrorist Organization) produced a Dec 9, 2025 indictment of 22 people and, on Jan 26, 2026, a further indictment of 31, for 87 total charged defendants on bank-fraud, money-laundering and material-support counts.
- The FBI's mitigations are all operational: change the default locks, add hood sensors and cameras, encrypt the hard drive, allowlist USB devices, auto-shutdown on indicators of compromise.
- Status as of Sept 30, 2026: trials pending in several districts; the FBI says incidents are still rising in 2026.

**What to say:**

- "Look at Anderson's outsider list: replay the bank's 'pay' response and the machine jackpots.
- That was 1993.
- Here is 2026: seven hundred jackpotting incidents in the US last year, twenty million dollars, and the tool is a piece of malware called Ploutus.
- How does it get in?
- Not through the network.
- The crew opens the front of the ATM with a generic key you can buy online, swaps the hard drive, and reboots.
- Ploutus then talks straight to the layer that moves the cash drawer — below the layer where the bank ever gets asked.
- The detail to remember: the FBI's number-one recommendation is *change the locks*.
- Not upgrade the crypto — change the locks.
- Thirty-three years after Anderson, the failure is still physical access plus a component that trusts anything on the bus.
- Question for the room: what is the ATM's threat model missing — and who at the bank owns that gap, the security team or facilities?"

**Course tie-in:**

- Implementation and operational failure — an unauthenticated hardware-control layer (XFS trusts local commands) plus default physical keys — with zero cryptanalysis.
- It is the literal modern form of the slide's "replaying the bank's pay response.
- Foreshadows Meeting 2's threat-modelling discussion (physical adversary, insider-equivalent access) and the later embedded/IoT material.

**Also:**

- [DOJ — Tren de Aragua jackpotting investigation, 87 charged defendants (Jan 26, 2026)](https://www.justice.gov/opa/pr/investigation-international-atm-jackpotting-scheme-and-tren-de-aragua-results-additional) — the reconnaissance-to-cash-out playbook in the indictment.
- [ABA Banking Journal — "FBI: Malware-enabled ATM jackpotting crimes on the rise" (Feb 25, 2026)](https://bankingjournal.aba.com/2026/02/fbi-malware-enabled-atm-jackpotting-crimes-on-the-rise/) — the banking industry's summary.
- [FDIC OIG — ATM Jackpotting explainer](https://www.fdicoig.gov/atm-jackpotting) — one-page description for students.

## And the Crypto-Adjacent Mistakes

This is the crux for Meeting 2: the **PIN-derivation key** had to be both secret *and* widely distributed *and* available at all times. That contradiction is exactly why key management gets its own lecture. Modern echo: **hardcoded API keys and cloud credentials in public GitHub repos** — same class of failure, different decade. Reference point: [GitGuardian's "State of Secrets Sprawl"](https://www.gitguardian.com/state-of-secrets-sprawl-report-2024) reports millions of leaked secrets/year.

### Case 1: the Stripe merchant secret-key dump (Aug 18, 2026)

> **Read first:** [Security Affairs — "50,000 Stripe Secrets Leaked in Public Code" (Aug 19, 2026)](https://securityaffairs.com/197504/cyber-crime/50000-stripe-secrets-leaked-in-public-code.html) — the fullest write-up of both the forum dump and the wider public-code survey.

**What happened:**

- On Aug 18, 2026 a seller using the alias "Satanic" posted, free rather than for sale, a ~35GB archive (17,654 files) on a data-trading forum containing what researchers at Ransomnews verified as live Stripe API credentials for 659 merchant accounts — 650 live secret keys and nine restricted keys — together with 688,363 customer and payment records pulled from those accounts across 42 countries.
- Ransomnews reviewed the material offline and notified Stripe before publishing.
- Separately, the same investigation counted more than 50,000 unique Stripe keys sitting in public places: hard-coded in GitHub repositories, in committed `.env` files and code comments, in GitHub Actions build logs, and on misconfigured web servers; a meaningful share were still active.
- The researchers demonstrated with a single active key that they could list a merchant's customers, create fraudulent payment links and execute a test charge within 17 hours.
- Nothing indicates Stripe's own infrastructure was breached; every one of the 659 merchants leaked its own key, and the attacker simply used the API the way any developer would.
- Still unknown as of Sept 30, 2026: the exact provenance of the dump (infostealer logs vs. scraped repos vs. exposed backups) and whether Stripe force-rotated the affected keys — Stripe has not issued a public statement I could verify.

**What to say:**

- "Anderson's PIN-derivation key had to be secret, and widely distributed, and always available — pick two, you can't have three.
- Here's the same contradiction in August.
- A Stripe secret key is full API access to a merchant's money and customers.
- It has to live wherever the merchant's code runs, so it ends up in a `.env` file, and the `.env` file ends up in a repo, and the repo ends up public, and a CI log prints it.
- On August 18th somebody gave away six hundred and fifty live ones — plus the customer records they'd already pulled with them — for free.
- Stripe wasn't hacked.
- Six hundred and fifty merchants each leaked their own key.
- The detail to remember: from one leaked key to a fraudulent charge took the researchers seventeen hours.
- Question: what's the difference between this and a customer writing their PIN on the card?
- Is there one?"

**Course tie-in:**

- Key management, purely — Anderson's secret-and-ubiquitous contradiction reappearing as an API secret; with a human-factors layer (developers treating a bearer credential as configuration).
- Foreshadows Meeting 2 (key management and PKI) and the later material on secrets management, scoped/short-lived credentials and vaults.

### Case 2: 9,300 leaked AWS keys that still worked (Truffle Security, Aug 21, 2026)

> **Read first:** [BleepingComputer — "Hundreds of leaked AWS keys give full control over corporate accounts" (Aug 21, 2026)](https://www.bleepingcomputer.com/news/security/hundreds-of-leaked-aws-keys-give-full-control-over-corporate-accounts/) — the numbers and methodology in one place.

**What happened:**

- Truffle Security (makers of TruffleHog) scanned public sources for AWS credentials leaked between Aug 2022 and Aug 2026 and found 431,875 AWS secrets, 64,024 unique access keys, and 50,654 distinct AWS accounts.
- Of the 10,616 keys for which a complete credential pair was available to test, 88% still authenticated as of Aug 10, 2026 — more than 9,300 live keys. 817 of those were tied to identifiable companies; 526 were **root** keys (unrestricted, un-scopable account owners) and 242 belonged to IAM users carrying the `AdministratorAccess` policy; 768 in total gave full control of the account.
- The single largest leak source was not GitHub but Hugging Face — 8,482 unique key leakages, about 17.9% of them root — i.e., model and dataset repos with credentials committed alongside notebooks.
- Truffle's point is about lifecycle: the keys were not new, they were years old and never rotated.
- Unknown as of Sept 30, 2026: how many were abused before disclosure; AWS has not published an account of remediation.

**What to say:**

- "Same slide, second act.
- Truffle Security went looking for AWS keys that had leaked publicly over four years — and then, crucially, tested whether they still worked.
- Eighty-eight percent did.
- Five hundred and twenty-six of them were root keys — the master key to the account, which AWS itself tells you never to create.
- And the number-one place they were leaking from wasn't GitHub — it was Hugging Face, in machine-learning notebooks.
- The detail to remember: these keys are *years* old.
- Nobody broke anything.
- Nobody rotated anything either.
- Anderson's 'sloppy ops: open files, shared keys' — that bullet is thirty-three years old and it just described 2026."

**Course tie-in:**

- Key management (generation without scope, no rotation, no expiry) and operational failure; the root-key point ties directly to Meeting 2's discussion of key hierarchies and least privilege.

**Also:**

- Pre-existing pointer below: GitGuardian's secrets-sprawl report for the annual leaked-secret baseline.

## The Takeaway

The quote *"The vast majority of security failures occur at the level of implementation detail"* is from Anderson's 1993 paper (CCS Proceedings, p. 226); read straight from the [Cambridge PDF](https://www.cl.cam.ac.uk/~rja14/Papers/wcf.pdf). The "seven-month tenure of US-agency security managers" figure is from Anderson quoting a Peter Neumann *ACM SIGSOFT Software Engineering Notes* observation — still directionally true; today the [ISACA "State of Cybersecurity" report](https://www.isaca.org/state-of-cybersecurity) tracks turnover. Put this line on the exam.

### Case 1: Cisco ISE authentication bypass, CVE-2026-76460 (Sept 2026)

> **Read first:** [Help Net Security — "Unauthenticated attackers are bypassing Cisco ISE's management interface (CVE-2026-76460)" (Sept 17, 2026)](https://www.helpnetsecurity.com/2026/09/17/cisco-ise-vulnerability-exploited-cve-2026-76460/) — versions, patches, exploitation status, no-workaround note.

**What happened:**

- Cisco Identity Services Engine (ISE) is the network-access-control and identity product that large enterprises use to decide who and what may join the network — it is, itself, the authentication system.
- In mid-September 2026 Cisco disclosed CVE-2026-76460, rated CVSS 10.0: an API endpoint in the web-based management interface had "insufficient authentication control," so an unauthenticated remote attacker could send a crafted request and bypass authentication to the management plane entirely; Cisco warns that follow-on command execution with root privileges is possible.
- Cisco confirmed active exploitation at disclosure; CISA added the CVE to its Known Exploited Vulnerabilities catalog with a federal patch deadline of Sept 19, 2026.
- Affected: ISE and ISE-PIC releases 3.0 through 3.5; fixes are 3.1 Patch 12, 3.2 Patch 11, 3.3 Patch 12, 3.4 Patch 7, and 3.5 Patch 4; there is no workaround, and 3.0 is out of support.
- It follows a string of Cisco ISE unauthenticated RCEs in 2025.
- Unknown as of Sept 30, 2026: who is exploiting it and at what scale; Cisco has not published indicators of compromise or a victim count.
- Citrix NetScaler had two unpatched zero-days under active exploitation the same fortnight (CISA KEV, Sept 9, 2026), so the pattern is not vendor-specific.

**What to say:**

- "Anderson: 'the vast majority of security failures occur at the level of implementation detail.' Here's this month's example, and it's almost too on-the-nose.
- Cisco ISE is the box that decides whether *you* are allowed on the corporate network.
- It is the authentication system.
- And in September it turned out one of its own management API endpoints didn't check authentication.
- CVSS ten out of ten, exploited in the wild before the patch, no workaround, federal agencies given four days.
- Not a crypto bug.
- Not a cryptanalytic breakthrough.
- A missing check on one endpoint in the product whose entire job is checking.
- The detail to remember: the highest possible severity score, on the identity product.
- The question for the room: Anderson says application-level security functions get neglected — but this *is* the security function.
- So what got neglected?"

**Course tie-in:**

- Implementation — the "application-level security functions get neglected" bullet on the slide, made literal; also operational (CISA's deadline shows patching-as-duty).
- Foreshadows the web-security and authentication lectures and the later discussion of KEV-driven patch obligations.

### Case 2: wolfSSL 5.9.4 — three high-severity certificate-validation bypasses (Sept 25, 2026)

> **Read first:** [SecurityWeek — "High-Severity Vulnerabilities Patched in OpenSSL, WolfSSL" (Sept 30, 2026)](https://www.securityweek.com/high-severity-vulnerabilities-patched-in-openssl-wolfssl/) — covers both libraries in one piece; today's news.

**What happened:**

- wolfSSL is the small-footprint TLS library used in embedded, automotive and IoT devices.
- Its 5.9.4 release (Sept 25, 2026) fixed eleven CVEs: three high-severity (CVE-2026-93302, CVE-2026-89102, CVE-2026-89136), four medium and four low.
- The three high ones are all authentication bypasses in certificate validation and peer authentication — improper checks that let an attacker present a forged certificate or impersonate a server to a wolfSSL client.
- In other words, the math (signatures) was fine; the code that decides whether to *believe* the signature had gaps.
- Unknown as of Sept 30, 2026: whether any are exploited in the wild; because wolfSSL ships inside firmware, the long tail of unpatched devices is the real exposure.

**What to say:**

- "And five days before Cisco, the same lesson in a TLS library that lives inside cars and thermostats.
- Three high-severity bugs in wolfSSL, and all three are the same shape: the certificate check is wrong, so a client accepts a forged certificate.
- RSA didn't break.
- ECDSA didn't break.
- The `if` statement that decides whether to trust the signature was wrong.
- One-liner to remember: the crypto verified the signature; the code forgot to ask whose it was."

**Course tie-in:**

- Implementation, shading into misplaced trust — a sound primitive wrapped in flawed validation logic; direct setup for Meeting 2 (certificates, chains, what "validation" actually has to check) and for the DigiNotar/Entrust discussion on the next slide.

**Also:**

- (No additional links; the OpenSSL half of the SecurityWeek piece is covered on the next slide.)

## A Taxonomy of Failure

Run the in-class activity: give students a headline breach and ask which bucket it fits. Seed examples with primary sources: **[Heartbleed (CVE-2014-0160)](https://heartbleed.com/)** — implementation (missing bounds check in OpenSSL); [OpenSSL advisory Apr 7, 2014](https://www.openssl.org/news/secadv/20140407.txt). **[Debian OpenSSL PRNG bug (CVE-2008-0166)](https://www.debian.org/security/2008/dsa-1571)** — key management (2 lines removed left PID as sole entropy source; only 32,767 possible RSA keys per architecture). **[DigiNotar (2011)](https://en.wikipedia.org/wiki/DigiNotar)** — key/CA trust (Iran-linked MITM on 300K Gmail users; Chrome cert pinning caught it; [EFF post-mortem](https://www.eff.org/deeplinks/2011/09/post-mortem-iranian-diginotar-attack)). Default passwords / Mirai — human factors. Cold-call: *"When was the last time cryptanalysis actually broke a real system?"* (Almost never — MD5/SHA-1 collisions are the rare exceptions, and they took decades and academic effort.)

### Case 1: OpenSSL CVE-2026-84782 — DTLS retransmit leaks heap memory (Sept 29, 2026)

> **Read first:** [OpenSSL Library — Vulnerabilities page (advisory entries dated Sept 29, 2026)](https://openssl-library.org/news/vulnerabilities/) — the primary advisory text for all four new CVEs.

**What happened:**

- On Sept 29, 2026 the OpenSSL project shipped 4.0.3, 3.6.5, 3.5.9 and 3.4.8, fixing 14 issues, one rated High: CVE-2026-84782 (CVSS 8.2), "DTLS retransmits handshake messages from a stale buffer offset.
- The mechanism: when OpenSSL suspends writing a DTLS handshake message because the transport is not ready (it returns `WANT_WRITE`), and the retransmission timer fires while that write is still paused, vulnerable versions fail to reset the read offset, so the retransmitted message starts from a stale position — reading past the intended buffer (an out-of-bounds read, CWE-125).
- A remote peer can thereby receive fragments of adjacent heap memory in plaintext, or crash the process.
- It affects every supported line and the old 1.1.1 / 1.0.2 lines.
- The same release fixed CVE-2026-84783 (Moderate, a use-after-free in the X.509 extension cache under concurrent use — crashes multi-threaded TLS clients), CVE-2026-84784 (Low, unbounded QUIC `RETIRE_CONNECTION_ID` backlog, ~400MB memory) and CVE-2026-75806 (Low, an undersized unauthenticated DTLS 1.2 AEAD record terminating an association).
- Status as of Sept 30, 2026: no known in-the-wild exploitation and no public proof-of-concept; distributions are rolling packages today.

**What to say:**

- "Yesterday — literally yesterday — OpenSSL patched a bug that should sound familiar.
- Heartbleed in 2014 was a missing bounds check that let a remote peer read server memory.
- This one is a DTLS retransmission that starts from the wrong offset and, again, sends a remote peer chunks of heap memory in plaintext.
- Twelve years apart, same library, same *shape* of bug, same bucket.
- Which bucket?
- Not cryptanalysis — AES and the handshake are fine.
- Implementation.
- The detail to remember: the trigger is a timer firing while a write is paused.
- Nobody attacked the cipher; they attacked a state machine.
- For the activity, this is your freebie: I'll take a hand — which bucket?"

**Course tie-in:**

- Implementation, the bucket most students under-pick; it is the direct descendant of the Heartbleed seed already in this row.
- Foreshadows the TLS lecture (handshake state machines, why DTLS is harder than TLS) and memory-safety discussions.

### Case 2: Entrust distrusted by Chrome and Mozilla (Nov–Dec 2024) — the modern DigiNotar

> **Read first:** [Cloudflare docs — "Entrust distrust by major browsers" (updated Apr 17, 2026)](https://developers.cloudflare.com/ssl/reference/migration-guides/entrust-distrust/) — the dates and the practical consequence in one page.

**What happened:**

- Entrust was one of the oldest commercial certificate authorities.
- Through 2023–2024 it accumulated a run of publicly tracked incidents — mis-issued certificates, missed revocation deadlines required by the CA/Browser Forum baseline requirements, and incident responses the root programs judged inadequate.
- On Jun 27, 2024 Google's Chrome Security Team announced Chrome would stop trusting new TLS certificates chaining to Entrust and AffirmTrust roots; the change shipped in Chrome 131 on Nov 12, 2024, applying to certificates whose first Signed Certificate Timestamp was after Nov 11, 2024 23:59:59 UTC.
- On Jul 31, 2024 Mozilla set a distrust-after date of Nov 30, 2024 for Firefox.
- Existing certificates kept working until expiry; new ones would throw browser errors.
- Entrust responded by issuing under SSL.com roots, then sold its public certificate business to Sectigo (Jan 2025); Sectigo completed migrating Entrust's public-certificate customers on Sept 29, 2025.
- Nothing was cryptographically broken at any point: the private keys were never known to be compromised.
- Entrust lost the browsers' trust for *organizational* reasons — how it handled its own mistakes.

**What to say:**

- "DigiNotar in 2011 was a CA that got hacked and issued a fake Google certificate that was used against Iranians.
- Entrust in 2024 is the same bucket without the hack.
- Nobody stole Entrust's keys.
- Entrust simply kept mis-issuing certificates, kept missing the revocation deadlines it had agreed to, and kept responding to incident reports in ways Google and Mozilla found unserious — and so, on November 12th 2024, Chrome stopped believing anything Entrust signed from then on.
- Think about what that means: the math was flawless, the keys were safe, and the whole business evaporated because the *organization* couldn't be trusted to run it.
- The detail to remember: a CA got fired for its incident-response habits, not its cryptography.
- The question: who in this system is the 'customer bearing the loss' — Entrust, or the thousands of sites that had to re-issue?"

**Course tie-in:**

- Misplaced trust / key-management (CA trust) with an organizational root cause — Anderson's argument that a security metaphor must address organizational issues, applied to the PKI.
- Foreshadows Meeting 2 (PKI, root programs, Certificate Transparency — the very SCT timestamps used to enforce the cut-off).

**Also:**

- [SecurityWeek — "High-Severity Vulnerabilities Patched in OpenSSL, WolfSSL" (Sept 30, 2026)](https://www.securityweek.com/high-severity-vulnerabilities-patched-in-openssl-wolfssl/) — press summary of the OpenSSL release.
- Cross-references: the Stripe/AWS key dumps (Aug 2026) are the *key management* seed — full write-up in the "And the Crypto-Adjacent Mistakes" row; IDScan.net (Sept 2026) is the *human factors / operations* seed — full write-up in the "Food for Thought" row.

## Case in Point: Equifax (2017)

The clean case study: Apache Struts patch shipped **March 7, 2017** (CVE-2017-5638); Equifax ran a vulnerability scan Mar 15 that missed the unpatched instance; attackers were inside **May 13–July 30**; ~**147.9M** consumers affected. Primary sources: [Wikipedia: 2017 Equifax data breach](https://en.wikipedia.org/wiki/2017_Equifax_data_breach); [FTC Equifax Settlement page](https://www.ftc.gov/enforcement/refunds/equifax-data-breach-settlement); [CFPB settlement page](https://www.consumerfinance.gov/equifax-settlement/). July 2019 global settlement with FTC/CFPB/50 state AGs: up to **\$700M** total (\$425M consumer fund, \$175M states, \$100M CFPB civil penalty). Judge Thrash: "the largest and most comprehensive recovery in a data breach case in U.S. history by several orders of magnitude." Feb 2020: DOJ indicted **four PLA (Unit 54398)** officers for the attack ([DOJ press release](https://www.justice.gov/opa/pr/chinese-military-personnel-charged-computer-fraud-economic-espionage-and-wire-fraud-hacking)). 2026 status: settlement in wind-down; identity-restoration services free until **Jan 2029**; 7 free Equifax credit reports/yr through 2026 via [annualcreditreport.com](https://www.annualcreditreport.com/). Directly seeds the meeting's debate: [`../../debates/data-breach.md`](../../debates/data-breach.md) — *"Companies should be held liable for damages incurred from data breaches if there was a known vulnerability."*

**2026 counterpoint on "just patch" — the Sept 2026 Windows Server Remote Desktop regression.** Full write-up (Read first / What happened / What to say) is in the "Specifications Should Plan for Failure" row below; use it here in one sentence: Microsoft's Sept 8 security updates froze Remote Desktop on Windows Server 2019/2022/2025, admins uninstalled the *security* fixes to get back in, and Microsoft needed an out-of-band patch on Sept 14 ([BleepingComputer, Sept 14 2026](https://www.bleepingcomputer.com/news/microsoft/microsoft-releases-emergency-windows-updates-to-fix-rds-failures/); [Cybersecurity News, Sept 11 2026](https://cybersecuritynews.com/remote-desktop-services-failures/)). Patching has real operational cost, which is why patch *management* (inventory, staging, testing) is the discipline, not the click — and why Equifax's ten-week miss on a known-exploited critical is still indefensible.

## When Regulators Treat Patching as a Duty

**FTC Log4j warning, January 4, 2022** (CVE-2021-44228) — primary source: [FTC blog post](https://www.ftc.gov/policy/advocacy-research/tech-at-ftc/2022/01/ftc-warns-companies-remediate-log4j-security-vulnerability). Legal hooks: FTC Act §5 ("unfair or deceptive acts") and Gramm-Leach-Bliley Safeguards Rule. Key quote: *"When vulnerabilities are discovered and exploited, it risks a loss or breach of personal information… The FTC intends to use its full legal authority to pursue companies that fail to take reasonable steps to protect consumer data from exposure as a result of Log4j, or similar known vulnerabilities in the future."* Cited Equifax explicitly as the cautionary example. Modern counterpart to name: **CISA Secure by Design pledge** — [cisa.gov/securebydesign/pledge](https://www.cisa.gov/securebydesign/pledge); ~367 signatories as of mid-2026 (up from 68 at May 2024 launch). The regulator's message: fixing implementation and ops failures is now a legal duty, not just hygiene. Directly answers the agenda discussion question on GDPR/CCPA impact.

### Case 1: FTC v. Illusory Systems (Nomad bridge) — secure development as a legal duty (Dec 16, 2025)

> **Read first:** [FTC press release — "FTC Will Require Illusory Systems to Return Money Stolen by Hackers and Implement an Information Security Program" (Dec 16, 2025)](https://www.ftc.gov/news-events/news/press-releases/2025/12/ftc-will-require-illusory-systems-return-money-stolen-hackers-implement-information-security-program) — the agency's own statement of the theory and the order terms.

**What happened:**

- Illusory Systems, a Utah company doing business as Nomad, ran a cross-chain "bridge" that let users move crypto assets between blockchains.
- In June 2022 it deployed a routine upgrade to its Replica contract that had not been adequately tested; the change marked a zero-value trusted root as valid, so any message passed verification.
- On Aug 1, 2022 an attacker noticed, and then hundreds of copycats simply replayed the first exploit transaction with their own addresses — one of the first "crowd-sourced" hacks — draining about $186M (the FTC's figure) in hours; after partial recoveries and returns, users were still out more than $100M.
- On Dec 16, 2025 the FTC announced a proposed consent order alleging violations of Section 5 of the FTC Act: unfair conduct through failure to use secure coding practices (no adequate unit tests, no process for receiving and handling third-party vulnerability reports, no written information-security plan, no use of readily available technologies to limit loss), plus deception in representing its secure-development practices.
- The order bars misrepresenting security, requires a comprehensive information-security program with independent assessments, requires a capability to pause irreversible actions, requires returning recovered assets to users, carries annual CEO certifications, and runs 10 years rather than the traditional 20.
- The notice was published in the Federal Register on Dec 19, 2025 for comment; crypto-industry trade groups filed objections.
- Status as of Sept 30, 2026: I could not verify whether the Commission has voted to finalize the order.

**What to say:**

- "The slide says the FTC warned in 2022 that failing to patch Log4j could be an unfair practice.
- Here's how far that theory has travelled.
- Nomad was a crypto bridge.
- In June 2022 they pushed an upgrade that, in effect, set the trusted root to zero, so every message was 'proven.' Somebody noticed in August, and then hundreds of people copied that person's transaction and helped themselves — a hundred and eighty-six million dollars gone in an afternoon.
- Three years later the FTC didn't say 'you got hacked.' It said: you had no unit tests for that change, no way for outsiders to report bugs, no written security plan, and you told your users you did — that's *unfair and deceptive*.
- The detail to remember: the FTC is now enforcing software development practice, not just patching.
- Question for the room: is a missing unit test a consumer-protection violation?
- Where does that stop?"

**Course tie-in:**

- Specification and implementation failure (an untested change to a trust root) turned into regulatory precedent — the arc from Anderson's "specifications should plan for failure" to the FTC's reasonable-security theory.
- Foreshadows the consumer-protection lectures (FTC Act §5 unfairness and deception) and tonight's data-breach liability debate.

### Case 2: FTC v. Illuminate Education — plaintext student data and ignored warnings (Jan 2026)

> **Read first:** [Covington Inside Privacy — "FTC Announces 10-Year Information Security Consent Orders with Illuminate Education and Illusory Systems" (Jan 2, 2026)](https://www.insideprivacy.com/united-states/federal-trade-commission/ftc-announces-10-year-information-security-consent-orders-with-illuminate-education-and-illusory-systems/) — both orders side by side, with the allegation lists.

**What happened:**

- Illuminate Education is a K-12 ed-tech vendor holding records on millions of US students.
- Between Dec 2021 and Jan 2022 an attacker used a former employee's credentials to access its network and exfiltrated records on more than 10 million students.
- The FTC's complaint alleges that until Jan 2022 Illuminate stored student data in plaintext, lacked reasonable access controls and account auditing (the ex-employee's account still worked), retained data it no longer needed, delayed notifying school districts, and had ignored security warnings from its own vendors since 2020.
- The order, announced with the Nomad order, requires a comprehensive security program with multi-factor authentication, a data inventory and classification scheme, deletion of unnecessary personal data, a publicly posted retention schedule, periodic independent assessments, and annual CISO compliance certifications, for 10 years.
- Nothing cryptographic failed; the failures are Anderson's operational list almost verbatim — open files, stale credentials, no one reading the warnings.

**What to say:**

- "And the companion order the same month is even more Anderson-shaped.
- Ed-tech company, ten million kids' records.
- How did it get out?
- A *former* employee's login still worked.
- Where was the data?
- Plaintext.
- Had anyone told them?
- Their own vendors had been warning them since 2020.
- Read Anderson's 'sloppy ops' bullet again — open files, shared keys — and then read this complaint.
- The detail to remember: an account for someone who no longer worked there.
- That's not a cryptography problem; that's an HR-to-IT handoff problem.
- And the FTC now treats it as a legal violation."

**Course tie-in:**

- Operational / human-factors failure (access-control hygiene, data minimisation, ignored warnings) — Anderson's "operating procedures are the weakest link," enforced by regulator.
- Foreshadows the privacy-regulation lectures (data minimisation, retention, breach notification) and the FTC-enforcement material.

**Also:**

- Both orders' 10-year terms (vs. the FTC's traditional 20) are themselves a policy shift worth one sentence.

## What Good Vendors Owe Customers

(Full incident write-up is in the "Where Does It Actually Break?" row; this block is the angle for *this* slide.)

npm, as the vendor, offers maintainers two-factor authentication on publishing — and also a token setting that bypasses it, because CI pipelines cannot answer a 2FA prompt. It also runs `preinstall` lifecycle scripts by default, because some packages need native builds. ChainDrop's worm logic explicitly looked for publish tokens with write rights and `bypass_2fa: true`; when it found one, it reinfected every package that token could publish, using a `preinstall` hook so the payload ran before installation finished. The May 2026 wave of the same lineage (TanStack, Mistral AI, UiPath; CVE-2026-45321) had already shown that packages carrying valid SLSA Build Level 3 provenance could be poisoned by harvesting OIDC tokens from a GitHub Actions runner — the provenance control attested that the malicious build was genuine. Each defence was real; each shipped with an escape hatch that a non-expert would leave open. Status as of Sept 30, 2026: npm has been tightening trusted publishing and token lifetimes across 2026, but `preinstall` and long-lived bypass tokens still exist.

Anderson's three-part vendor prescription (build for real-world skill / train customers / provide own operators) reads today as an argument against shipping "expert-required" security tooling to non-experts. Modern echo: **CISA's [Secure by Design](https://www.cisa.gov/securebydesign) principles** — take ownership of customer security outcomes, embrace radical transparency, build organizational structure that makes security a business decision. The [Secure by Design Pledge](https://www.cisa.gov/securebydesign/pledge) has 7 goals (MFA, no default passwords, reduced vuln classes, patch adoption, VDPs, CVE quality, intrusion evidence).

### Case: ChainDrop and the `bypass_2fa` escape hatch (Aug 2026) — the vendor-side view

> **Read first:** [Elastic Security Labs — "Shai-Hulud strikes again: CHAINDROP worm hits 400+ npm packages" (Aug 6, 2026)](https://www.elastic.co/security-labs/shai-hulud-chaindrop-npm-supply-chain) — the write-up that documents the worm activating on tokens carrying `bypass_2fa: true` and the `preinstall` execution path.

**What happened (vendor angle):**

**What to say:**

- "Anderson says a vendor owes you one of three things: a product your real staff can run safely, or training, or their own operators.
- Now look at npm as the vendor.
- It gave maintainers 2FA — good — and a flag to turn it off for CI, because CI can't type a code.
- It runs install scripts automatically, because some packages need it.
- Both are reasonable engineering choices.
- And the worm's first move was: find me a token with the 2FA-bypass flag.
- The detail to remember: the security control and the hole in it shipped in the same box, and the customer — a volunteer maintainer — was expected to know which one they'd turned on.
- Question: whose fault is that?
- The maintainer who set the flag, or the vendor who made the flag?"

**Course tie-in:**

- Anderson's vendor-obligation argument and "suppliers overestimate customers' sophistication"; the CISA secure-by-default framing on this slide is the modern statement of the same duty.
- Foreshadows the supply-chain lecture (provenance, trusted publishing, SLSA) and Meeting 2 (token lifetimes as key management).

**Also:**

- [Microsoft Security Blog — ChainDrop anatomy (Aug 4, 2026)](https://www.microsoft.com/en-us/security/blog/2026/08/04/chaindrop-supply-chain-compromise-anatomy-self-propagating-worm/) — the full incident.
- [The Register (Aug 15, 2026)](https://www.theregister.com/security/2026/08/15/chaindrop-worm-crawls-into-npm-supply-chain-evades-standard-defenses/5287958) — "evades standard defenses."

## Specifications Should Plan for Failure

This is **threat modeling avant la lettre**. Point to Meeting 2 (formal threat models / STRIDE) but tie the intuition to today. Named methodology: [Microsoft STRIDE](https://learn.microsoft.com/en-us/azure/security/develop/threat-modeling-tool-threats), [OWASP threat modeling](https://owasp.org/www-community/Threat_Modeling). Contemporary case for "spec that plans for failure": the **CrowdStrike outage of July 19, 2024** — a Rapid Response Content update pushed globally with no staged rollout crashed ~8.5M Windows systems; the postmortem [RCA (Aug 6, 2024)](https://www.crowdstrike.com/wp-content/uploads/2024/08/Channel-File-291-Incident-Root-Cause-Analysis-08.06.2024.pdf) is a textbook enumeration of what a real spec should have caught. Also [Wikipedia: 2024 CrowdStrike-related IT outages](https://en.wikipedia.org/wiki/2024_CrowdStrike-related_IT_outages) — losses >\$5B.

### Case: the September 2026 Windows Server Remote Desktop regression

> **Read first:** [BleepingComputer — "Microsoft releases emergency Windows updates to fix RDS failures" (Sept 14, 2026)](https://www.bleepingcomputer.com/news/microsoft/microsoft-releases-emergency-windows-updates-to-fix-rds-failures/) — the resolution piece, with every affected build and out-of-band KB listed.

**What happened:**

- On Sept 8, 2026 (Patch Tuesday) Microsoft shipped cumulative security updates KB5122876 (Windows Server 2019), KB5122882 (Server 2022) and KB5122871 (Server 2025).
- Within days administrators worldwide reported that Remote Desktop Services session hosts became unstable hours after boot: RDP connections hung at "Connecting…", users could not sign in, disconnect or log off cleanly, some servers hung at "Please wait for the Remote Desktop Configuration," and the TerminalServices log filled with Event ID 20498 ("Remote Desktop Services has taken too long to complete the client connection").
- Windows 10 and 11 clients were also affected.
- The only field workaround was to uninstall the cumulative update with DISM — which restored Remote Desktop and removed the month's security fixes.
- Microsoft added the known issue to the KB articles on Sept 12, published a Group Policy-based Known Issue Rollback, and on Sept 14 released out-of-band fixes (KB5129238 for Server 2019, KB5129237 for Server 2022, KB5129235 for Server 2025, plus client builds).
- Microsoft's public statement says only that the September updates "caused Remote Desktop Services to become unstable"; no root cause has been published as of Sept 30, 2026, and it is not known how many organisations ran unpatched for the week.

**What to say:**

- "Anderson wants a specification that lists every plausible failure mode and tests that real operators can actually run the thing.
- Here's what happens without it.
- Three weeks ago Microsoft's monthly security update went out to every Windows Server on earth.
- Hours after reboot, Remote Desktop froze.
- Think about what that means for an admin: the fix for this month's vulnerabilities just locked you out of the box you'd need to log into to fix it.
- The only workaround for a week was to *remove the security update* — go back to being vulnerable so you can get to work.
- Microsoft needed an emergency patch six days later.
- The detail to remember: 'the patch breaks the remote access you'd use to fix the patch' is a failure mode any spec should have listed.
- And here's the tension with the Equifax slide: we just said not patching for ten weeks is indefensible.
- Now — how fast *should* you patch, and what would you need in place to do it safely?
- That's not a crypto question.
- That's an operations question."

**Course tie-in:**

- Specification failure — Anderson's "list all plausible failure modes" and "test that real people can operate it" — plus the organizational point that patch management needs staging, canaries and rollback (the CrowdStrike lesson below, in miniature).
- Foreshadows the incident-response / operations material and the software-liability discussion.

**Also:**

- [Microsoft Support — KB5122882 release notes with the known-issue entry added Sept 12, 2026](https://support.microsoft.com/en-us/servicing/os/windows-server/2026/09/kb5122882-windows-server-2022-security-update) — the vendor's own record.
- [Cybersecurity News — "Remote Desktop Services Failures on Windows Servers Following September Update" (Sept 11, 2026)](https://cybersecuritynews.com/remote-desktop-services-failures/) — the symptom report from before the fix.

## Two Paradigms for Safety

Anderson's contrast of **signalling/interlocks** (system in control, formal verification) with **aviation** (constant feedback, incremental improvement, pilot in control) is worth debating explicitly. Good debate seed: *"Which paradigm is a better model for modern software security — hard interlocks or feedback-driven aviation-style culture?"* Contemporary hook: post-incident review culture at large tech companies (SRE/Google-style blameless postmortems) is an "aviation" borrowing; regulated healthcare/embedded is more "signalling."

(Full incident write-up is in the "When Regulators Treat Patching as a Duty" row; this block is the angle for *this* slide.)

Among the Nomad order's terms is a requirement to build a system-pause capability for irreversible actions — in bridge terms, a circuit breaker that halts transfers when something anomalous is happening. On Aug 1, 2022 the exploit ran for hours while hundreds of copycats replayed it; a working pause would have bounded the loss. The FTC's complaint also faults the absence of a channel for outside vulnerability reports — the *feedback* half of Anderson's aviation paradigm.

### Case: a regulator mandating an interlock — the FTC's Nomad order (Dec 2025 / Jan 2026)

> **Read first:** [Covington Inside Privacy (Jan 2, 2026)](https://www.insideprivacy.com/united-states/federal-trade-commission/ftc-announces-10-year-information-security-consent-orders-with-illuminate-education-and-illusory-systems/) — lists the order's requirement that Nomad implement a capability to pause irreversible actions.

**What happened (this angle):**

**What to say:**

- "Anderson gives you two ways engineers keep things safe: railway signalling, where interlocks make the unsafe state impossible and the *system* is in control; and aviation, where pilots stay in control but every incident feeds back into training and design.
- Here's a regulator picking one.
- The FTC ordered a crypto bridge to build a pause button — an interlock — because on the day it was drained there was no way to stop the machine.
- But read the complaint again and the *other* paradigm is there too: no way for outsiders to report a bug, no learning loop. So the question I want you to argue: which would have saved Nomad — the interlock, or the feedback culture?
- And is that the right split for the systems you'll build?"

**Course tie-in:**

- The organizational half of Anderson's argument: a safety metaphor must say who is in control and how the organisation learns.
- Foreshadows the incident-response and secure-development-lifecycle material.

**Also:**

- [FTC press release (Dec 16, 2025)](https://www.ftc.gov/news-events/news/press-releases/2025/12/ftc-will-require-illusory-systems-return-money-stolen-hackers-implement-information-security-program) — the agency's own statement.

## Food for Thought

(Full write-up in the "Where Does It Actually Break?" row; this is the angle for the second prompt.)

With stolen GitHub tokens, ChainDrop committed startup hooks into `.claude/settings.json` and `.vscode/tasks.json` across repository branches. Opening an infected branch in VS Code or Claude Code executed the hook — no `npm install` needed — creating a developer-to-developer infection path through the tooling itself. It also harvested AI-tool API keys among its 300+ credential patterns.

Three prompts, all live in 2026: **(1) identity verification pushed to production fast** — see the [UK Online Safety Act age-assurance enforcement wave 2025–2026](https://ico-newsroom.prgloo.com/) and various US state age-verification laws; the human-factors failures Anderson described repeat. **(2) AI writes and reviews code** — does that shrink or grow trusting-trust? Point at [GitHub Copilot autofix](https://github.blog/2024-03-20-found-means-fixed-introducing-code-scanning-autofix-powered-by-github-copilot-and-github-advanced-security/) and the emerging risk of models re-introducing known CVEs; poisoned training data; agentic coding tools installing dependencies autonomously. **(3) who bears the loss** — modern anchor: **Salt Typhoon** PRC breach of US telecoms (2024, ongoing), which compromised **CALEA lawful-intercept systems** ([CRS IF12798](https://www.congress.gov/crs-product/IF12798); [FBI PSA](https://www.ic3.gov/PSA/2025/PSA250424-2)). Anderson's lesson lands hard: telcos built lawful-intercept as a legal compliance obligation, not a defended attack surface.

### Case 1: IDScan.net — a year-long live feed of 153M ID scans (Sept 2026)

> **Read first:** [TechCrunch — "ID verification giant IDScan confirms data breach with more than 150 million driver's licenses stolen" (Sept 10, 2026)](https://techcrunch.com/2026/09/10/id-verification-giant-idscan-confirms-data-breach-with-more-than-150-million-drivers-licenses-stolen/) — the confirmation piece, with the notice dates and what is still unknown.

**What happened:**

- IDScan.net is a Louisiana-based identity-verification vendor whose scanners and cloud platform check IDs for bars, entertainment venues, cannabis dispensaries and other businesses that must verify age or identity.
- Around Sept 1, 2026 the company "received information" that data in its clients' cloud accounts may have been accessed; on Sept 2 Brian Krebs and TechCrunch reported that a Russia-linked dark-web marketplace, Nexus, was offering a searchable trove of roughly 153 million driver's-licence scans of US and Canadian residents, with photos where available, plus about 10 million ID cards, 3+ million travel documents and 579,000 medical cards — and that the feed was still growing by roughly 400,000 records a day, implying the attackers had been reading the platform for over a year.
- Named victims in the trove included Krebs himself and the US Secretary of Defense.
- Nexus went offline shortly after the coverage.
- IDScan.net posted a notice dated Sept 4 and confirmed the breach on Sept 10: an unauthorized third party may have accessed or copied customer information held in clients' IDScan.net cloud accounts — full names, driver's-licence numbers, and other government-ID numbers such as passports; it engaged outside specialists, and the FBI's New Orleans field office opened an investigation.
- Multiple class actions were filed within days.
- Still unknown as of Sept 30, 2026: how initial access was obtained (client credentials? platform flaw?), the true number of affected people, whether a ransom was demanded, and why a year of exfiltration went undetected.
- The wider context is the Mysterium VPN tally (Case 2 below).

**What to say:**

- "First prompt on the slide: identity-verification systems pushed into production fast.
- Three weeks ago we got the case.
- IDScan.net makes the scanner the bouncer waves your licence under.
- Every scan went to the cloud.
- Someone was reading that cloud for *over a year* — 153 million licences, photos included, four hundred thousand new ones a day still arriving when it was discovered.
- Brian Krebs found his own licence in it.
- The company found out because a reporter called.
- The detail to remember: the breach wasn't detected — it was *reported*.
- Anderson's point about feedback: the system had none.
- Now the policy question.
- Every age-verification law passed in the last two years creates another one of these databases.
- Is there a version of 'prove you're over 18' that doesn't build a target like this?
- Argue it."

**Course tie-in:**

- Human factors and operational failure — a system built to satisfy a compliance requirement, not to defend the data it collected (the Salt Typhoon / CALEA point below is the same shape); zero cryptography involved.
- Foreshadows the privacy lectures (data minimisation, age assurance, biometrics) and the breach-liability debate.

### Case 2: the Mysterium VPN tally — 88 identity-verification breaches since 2011 (Aug 26, 2026)

> **Read first:** [Security Affairs — "88 ID Verification Breaches Show the Cost of Collecting Identity Data" (Aug 26, 2026)](https://securityaffairs.com/197855/reports/88-id-verification-breaches-show-the-cost-of-collecting-identity-data.html) — summary of the report and its headline numbers.

**What happened:**

- A research team at Mysterium VPN compiled every documented incident since 2011 in which data collected specifically to verify someone's identity or age was breached, exposed or sold: 88 incidents, 2.15 billion records confirmed by researchers or the companies themselves, with attackers and sellers claiming another 4.54 billion on top. 37 of the 88 (42%) occurred between Jan 2024 and Aug 2026 — the period in which mandatory identity and age checks spread fastest — and in 41 incidents what leaked was the source material itself: ID scans, verification selfies, fingerprints or biometric templates, none of which can be rotated like a password.
- Caveat when teaching: the compiler is a VPN vendor with a commercial interest in the conclusion; the incident list is what is useful, not the framing.

**What to say:**

- "Zoom out from IDScan.
- One tally counts eighty-eight of these since 2011, two billion confirmed records — and almost half of the incidents happened in the last two and a half years, which is exactly when governments started mandating ID checks online.
- The detail to remember: in forty-one of them, what leaked was the selfie or the fingerprint.
- You can change a password.
- Tell me how you change your face."

**Course tie-in:**

- Operational / organizational — the aggregate consequence of the human-factors failures Anderson described, at policy scale.
- Foreshadows the biometrics and age-assurance material.

### Case 3: ChainDrop and the AI coding agent (Aug 2026)

> **Read first:** [The Register — "ChainDrop worm crawls into npm supply chain, evades standard defenses" (Aug 15, 2026)](https://www.theregister.com/security/2026/08/15/chaindrop-worm-crawls-into-npm-supply-chain-evades-standard-defenses/5287958) — the piece that spells out the editor-config infection path.

**What happened (this angle):**

**What to say:**

- "Second prompt: does AI writing and reviewing code extend or shrink the trusting-trust problem?
- ChainDrop gives you a data point.
- The worm didn't just poison packages — it wrote itself into the config files your editor and your coding agent read on startup. Open the branch, you're infected.
- Your agent is now inside Thompson's loop. So: when your AI assistant reviews a pull request and says it's clean — what, exactly, did it trust to reach that conclusion?"

**Course tie-in:**

- Misplaced trust, extended to the AI toolchain.
- Foreshadows the AI-security discussion later in the term.

**Also:**

- [TechCrunch — "It sure looks like hackers breached a major ID card verification service" (Sept 2, 2026)](https://techcrunch.com/2026/09/02/it-sure-looks-like-hackers-breached-a-major-id-card-verification-service/) — the first report.
- [The Record — "IDScan confirms breach after hackers offer 153 million driver's license scans for sale" (Sept 10, 2026)](https://therecord.media/idscan-data-breach-notice-drivers-licenses) — record-type breakdown and the lawsuits.
- [Techdirt — "Hackers Had A Live Feed Of Every ID This Verification Company Scanned. For Over A Year." (Sept 3, 2026)](https://www.techdirt.com/2026/09/03/hackers-had-a-live-feed-of-every-id-this-verification-company-scanned-for-over-a-year/) — the policy argument that no centralized age-verification store is safe.

## The Through-Line

The one-line summary of both papers. Close with the agenda's transition to Meeting 2 (Key Management & PKI): *the reason we spend a whole lecture on keys is precisely because they are the single hardest implementation-and-operations problem in the field.* Related activities coming up: [`../../activities/`](../../activities/); the data-breach debate: [`../../debates/data-breach.md`](../../debates/data-breach.md).
