# Key Management and PKI

**Format.** Break into groups of 4–5. Each group picks **one** of the two breakouts below (or takes both if time allows). Spend ~5 minutes skimming the prep reads, then ~10 minutes debating. A designated reporter brings the group's position — and any dissents — back to the full class for a ~3-minute report-back.

Lecture 3's central discomfort is that the Web PKI works by *any-of-hundreds* trust: any root in your OS/browser can vouch for any name, and revocation is functionally broken. The industry's answer in 2026 is to shrink the exposure window (47-day certs by 2029) rather than fix the trust model. Both breakouts push on whether the model itself can survive.

---

## Breakout A: Browsers as the Unelected CA Regulators
<!-- breakout id="A" status="current" refreshed="2026-07-16" -->

**Motion.** *"Chrome and Mozilla's root-store programs, the CA/Browser Forum, and the ability to distrust a CA by shipping a browser update have made *browsers*, not governments, the de facto global regulators of the certificate ecosystem. This is unaccountable private governance of public infrastructure and it needs a formal legal framework."*

<!-- current-events:start topic="ca-browser-forum-root-store-governance" -->
**Prep reads (5–10 min).**
- [Sustaining Digital Certificate Security — Chrome Root Store changes](https://blog.google/security/sustaining-digital-certificate-security-chrome-root-store-changes/) — Google Security Blog, May 2025. Google's own announcement distrusting Chunghwa Telecom (Taiwan) and Netlock (Hungary) in Chrome 139 (August 1, 2025), citing "patterns of concerning behavior" — the archetypal browser-as-regulator action.
- [Ballot SC-081v3: Introduce Schedule of Reducing Validity and Data Reuse Periods](https://cabforum.org/2025/04/11/ballot-sc-081v3-introduce-schedule-of-reducing-validity-and-data-reuse-periods/) — CA/Browser Forum, April 2025. The passed ballot text and voting record for the 398→47 day certificate lifetime reduction (final: March 2029); four browsers voted yes, five CAs abstained citing subscriber cost.
- [Chrome to Distrust Chunghwa Telecom and Netlock Certificates](https://www.securityweek.com/chrome-to-distrust-chunghwa-telecom-and-netlock-certificates/) — SecurityWeek, June 2025. Third-party reporting on why two national-scale CAs lost trust, plus the enterprise override mechanism and how Apple/Mozilla/Microsoft are responding independently.
- [TLS Certificate Lifetimes Will Officially Reduce to 47 Days](https://www.digicert.com/blog/tls-certificate-lifetimes-will-officially-reduce-to-47-days) — DigiCert (CA industry perspective), April 2025. The largest commercial CA's public-facing acknowledgement of SC-081v3 and the automation-forcing effects that concentrate issuance further onto ACME-native providers.
<!-- current-events:end -->

**Discussion prompts.**
- Chrome distrusted Chunghwa Telecom and Netlock (Chrome 139, Aug 2025) citing "a pattern of compliance failures." Mozilla and DigiCert have made similar calls historically (Symantec, WoSign, CNNIC). Are these decisions more like *editorial* choices or *regulatory* enforcement — and should the legal framework track the answer?
- CA/Browser Forum Ballot SC-081v3 (2025) cut TLS cert lifetimes to 47 days by 2029. Four browser vendors voted yes; CAs mostly voted no. Who *should* have won that vote — the parties who trust or the parties who issue? What does that say about who "owns" the ecosystem?
- Consider the Chinese counter-move: a state CA whose certificates are trusted only in browsers distributed inside the country. Is the fact that Chrome and Firefox can (and do) exclude such CAs *good* (they protect users globally) or *bad* (they're one country's browsers making trust decisions for the world)?
- The 47-day rule forces ACME automation, which pushes issuance onto Let's Encrypt and a handful of ACME providers. Solving revocation created issuer concentration. Is that a fair trade, or did we just move the single point of failure?

**Bring back.** Whether your group would formalize browser root-store decisions as public regulation, and one specific accountability mechanism you'd require.

---

## Breakout B: What Do You Actually Do When a Root Compromises?
<!-- breakout id="B" status="current" refreshed="2026-07-16" -->

**Motion.** *"Given that revocation is broken (OCSP is slow, unreliable, and privacy-leaking; CRLs are enormous; browsers implement soft-fail), and given that 47-day certs won't be universal until 2029, users have effectively no protection today against a compromised private key on a still-valid cert. The right answer is DNSSEC + DANE — anchor trust in DNS, not in ~150 roots."*

<!-- current-events:start topic="revocation-dane-post-quantum" -->
**Prep reads (5–10 min).**
- [Ballot SC-085v2: Require Validation of DNSSEC (when present) for CAA and DCV Lookups](https://cabforum.org/2025/06/18/ballot-sc-085v2-require-validation-of-dnssec-when-present-for-caa-and-dcv-lookups/) — CA/Browser Forum, June 2025. A quietly consequential ballot: WebPKI issuers must now validate DNSSEC when the domain publishes it — the first structural convergence of the CA and DNSSEC trust models.
- [State of the post-quantum Internet in 2025](https://blog.cloudflare.com/pq-2025/) — Cloudflare, March 2025. Measurement data on X25519+ML-KEM hybrid deployment (~38% of Cloudflare HTTPS traffic by March 2025), the "harvest now, decrypt later" threat model, and why hybrid rather than replace.
- [Google Chrome Switches to ML-KEM for Post-Quantum Cryptography Defense](https://thehackernews.com/2024/09/google-chrome-switches-to-ml-kem-for.html) — The Hacker News, September 2024. Reporter-side coverage of Chrome 131's move from Kyber-draft to the finalized NIST FIPS 203 (ML-KEM) — the shipped code that makes the debate concrete.
- [Internet PKI to Integrate DNSSEC](https://www.feistyduck.com/newsletter/issue_126_internet_pki_to_integrate_dnssec) — Feisty Duck (Ivan Ristić), 2025. Sober analysis of why browsers still won't deploy DANE despite decades of theoretical elegance, and why "the CA industry annexes DNSSEC" is the more likely 2026-2029 path.
<!-- current-events:end -->

**Discussion prompts.**
- Heartbleed (2014) forced mass revocation and made OCSP's brokenness public: OCSP outages caused soft-fail behavior, and users kept trusting revoked certs. If Heartbleed happened tomorrow, would the response be materially better?
- DANE anchors TLS trust in DNSSEC — one hierarchy instead of hundreds of roots. But DNSSEC deployment is <40% globally and the U.S. government controls the DNS root zone. Have we improved trust or just changed *whom* we distrust?
- "Harvest now, decrypt later" — adversaries recording encrypted traffic today to decrypt after post-quantum breaks Diffie-Hellman. Browsers are already deploying hybrid X25519+ML-KEM. Does this change the calculus on cert *lifetime* (why bother with 47-day certs if the underlying key exchange breaks?) or reinforce it?
- Encrypted SNI / ECH closes the last plaintext leak in TLS 1.3. But the destination IP is still visible, and in a CDN-consolidated web, that IP maps to Cloudflare. Is the trust anchor *actually* the CA now, or is it Cloudflare?

**Bring back.** The single mechanism your group thinks would most improve everyday web security in 2026, and one honest reason it hasn't happened.

---

## Instructor notes

Breakout A is the policy-forward version; Breakout B is the technical-forward version. If your class has done the [Certificate Chains](../activities/cert.md) or [Key Signing](../activities/gpg.md) activity that day, Breakout B lands harder — students have just seen a real cert chain. If they haven't yet, run A: it previews the browser-as-regulator theme that recurs in Lectures 9, 16, and 18. Both benefit from a running whiteboard tally of "who trusts whom" so students see the transitive-trust problem visually.

<!--
breakout-metadata:
  lecture: 3
  class: "Key Management"
  last_refreshed: 2026-07-16
-->
