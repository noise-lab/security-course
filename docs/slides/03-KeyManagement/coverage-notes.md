# 03-KeyManagement — instructor notes

## Current-events updates made (point 2)

- **CA/Browser Forum Ballot SC-081v3 (passed April 2025): 47-day cert lifetimes.**
  Added a dated `.vignette` on the revocation slide. Verified phase-in: max TLS lifetime
  drops from ~398 days to **200 days (Mar 15, 2026) → 100 days (Mar 15, 2027) → 47 days
  (Mar 15, 2029)**. All four major browser vendors voted in favor. Framed as the systems
  answer to broken revocation (shrink the exposure window instead of fixing OCSP).
  Sources: digicert.com/blog/tls-certificate-lifetimes-will-officially-reduce-to-47-days;
  theregister.com/2025/04/14/ssl_tls_certificates/.
- **Chrome distrust of Chunghwa Telecom + Netlock (Chrome 139, Aug 1, 2025).** Added to
  the "Browsers Are Still Pulling CAs" vignette. Verified: certs issued after
  2025-07-31 23:59:59 UTC are distrusted in Chrome 139; cited Google's "pattern of
  compliance failures" language; noted Edge/Firefox/Safari use separate trust stores.
  Sources: blog.google/security/sustaining-digital-certificate-security-chrome-root-store-changes/;
  bleepingcomputer.com (Chrome to distrust Chunghwa/Netlock).
- **DigiCert "Global Root CA" (G1) distrust, April 15, 2026.** Added to the same
  vignette as a forward-looking, dated example (Chrome + Mozilla). G2-chained certs
  unaffected. Source: hexssl.com DigiCert G1 distrust write-up.
- **EV "green bar" is gone.** Replaced the old EV-badge framing (slides 59–61 of the
  source) with the accurate current state: Chrome/Firefox removed the EV company-name UI
  (~2019–2020), so the lock icon now means "encrypted, DV-or-better," not "verified
  company."
- **TLS 1.3 + Encrypted SNI / ECH.** Updated the TLS-in-practice slide to reflect TLS 1.3
  as the default and ECH as the fix for the SNI privacy leak, per the agenda's note on
  TLS 1.2 vs 1.3 and encrypted SNI.
- **De-emphasized legacy ciphers per agenda.** The source pptx spent ~16 slides on
  Caesar/Vigenère/Enigma/OTP/stream ciphers and full RSA derivations/proofs. Meeting 2's
  agenda explicitly lists these (number theory, discrete-log computation, RSA details,
  legacy cryptosystems) as **NOT covered**, so they were cut to keep the deck lean and
  on-topic. D-H and RSA are presented conceptually only.

## Suggested missing coverage on broad themes (point 3)

- **Post-quantum migration.** The biggest live key-management story is the NIST PQC
  standards (ML-KEM/Kyber, ML-DSA) and "harvest now, decrypt later." Worth one slide:
  browsers/servers are already deploying hybrid X25519+ML-KEM key exchange. Ties D-H's
  discrete-log hardness assumption directly to "what happens when the assumption breaks."
- **Governance/accountability of root programs.** The deck raises that browser vendors
  are the de facto regulators; a follow-up could cover *how* the Chrome/Mozilla root
  programs and the CA/Browser Forum actually work, and the accountability gap (private
  governance of public infrastructure). Strong policy-class material.
- **ACME and the centralization trade-off.** Short-lived certs mandate automation, which
  pushes the web onto a few ACME issuers (Let's Encrypt). Worth making explicit: solving
  one fragility (revocation) can create another (issuer concentration / single points of
  failure).
- **DANE / DNSSEC as an alternative trust anchor.** Mentioned nowhere; a contrast to the
  CA model (anchor trust in DNS instead of ~hundreds of roots) would deepen the "where
  does trust stop?" discussion. Connects to the later DNS-security lecture.
- **Key storage / HSMs and key compromise mechanics.** The deck covers what happens when
  a CA misbehaves but not how private keys are actually protected (HSMs, key ceremonies)
  or how they leak (Heartbleed is the only example). One slide would round out "key
  management" as an operational discipline.
- **Concrete digital-signature applications.** The agenda notes software/OS update
  signing as an example; could expand to code signing, signed software supply chains
  (Sigstore), and document signing to make the integrity use case less abstract.

## Curated images

Used:
- `slide034_img025.png`, `slide035_img026.png` — Stallings encryption vs. authentication
  diagrams; clean illustration of the two public-key use cases.
- `slide056_img032.png` — real cert chain (USERTrust → Sectigo → nytimes.com); matches
  the in-class browser chain-inspection activity.
- `slide059_img036.png` — full certificate detail view; shows the real X.509 fields
  students inspect.
- `slide055_img031.png` — macOS Keychain showing ~200 trusted roots; concretizes the
  "trust is any-of-hundreds" weakness.
- `slide067_img046.png` — Gogo Inflight fake-cert headline; real MITM-in-the-wild.
- `slide071_img047.png` — SSH host-key-changed warning; pinning / MITM made visible.
- `slide074_img048.jpg` — Heartbleed logo; anchors the mass-revocation example.

Dropped:
- `slide002–003`, `slide019` Alice/Bob/Eve stick-figure clip art — decorative.
- `slide008` (Caesar), `slide009` (frequency plot), `slide011` (Enigma photos),
  `slide013/015` (XOR bitmaps), `slide039–041` (GCHQ/RSA paper scans, Rivest-Shamir-
  Adleman photo) — tied to the legacy-cipher/RSA-math content cut per the agenda.
- `slide054` (old deep CA hierarchy) — superseded by the accurate "flat, multi-root"
  framing in the trust-anchor slide.
- `slide058` (browser lock screenshot), `slide060/063/064/065/066` (Bugzilla/CNNIC
  process screenshots) — redundant with the case-study text or low teaching value.
- `slide076–077` (backdoor-debate clip art) — kept the debate as a text slide instead.

## Source

- Rebuilt from `_source-extract.md` (77 source slides → 24 rebuilt slides) +
  `agenda.md` Meeting 2 (Key Management and Public Key Infrastructure). Scoped to what
  was actually taught; legacy ciphers and crypto-math proofs cut per the agenda's
  explicit "NOT covered" list.
