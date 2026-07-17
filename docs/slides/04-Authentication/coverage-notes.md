# 04-Authentication — instructor notes

## Current-events updates made (point 2)

- **2026-07-16 refresh.** Verified/updated passkey adoption vignette against the FIDO
  Alliance State of Passkeys 2026 report (World Passkey Day, May 7, 2026): 5B passkeys
  in use, ~48% of top-100 sites, 75% of consumers with ≥1 passkey enabled, 68% of
  organizations deploying/piloting (revised down from earlier "87%" figure — 87% was
  from a 2025 enterprise-only survey that overstated the workforce number). Corrected
  the NIST SP 800-63-4 finalization date to **July 31, 2025** and clarified that AAL2
  requires offering a phishing-resistant option and AAL3 mandates it.
- **2026-07-16 refresh.** Replaced the generic 2026 follow-on framing on
  "Attackers Stopped Stealing Passwords" with the verified **Vercel/Context.ai
  April 2026** breach specifics — Lumma-Stealer-infected Context.ai employee → stolen
  OAuth grant into Vercel employee's Google Workspace → NPM/GitHub token theft → $2M
  ransom demand. Added AiTM phishing kits (Tycoon 2FA, EvilProxy, EvilTokens) with
  the Microsoft-reported 20M+ messages/month figure to make the "steal-the-token"
  playbook concrete.
- **Salesloft–Drift OAuth token breach (Aug 2025)** — retained as the central vignette on
  "Attackers Stopped Stealing Passwords." Threat actor UNC6395 stole and replayed OAuth
  *access + refresh tokens* from the Drift chatbot integration to exfiltrate Salesforce
  data from 700+ orgs (Cloudflare, Google, PagerDuty, Palo Alto Networks, Proofpoint,
  Tanium, Zscaler, etc.) Aug 9–17, bypassing MFA because a valid bearer token needs no
  second factor. Verified via Google Cloud Threat Intelligence, Mitiga, AppOmni.
- Modernized OAuth scenario to the **Slack + GitHub** integration and **GitHub PAT
  scoping** demo from the agenda; kept Strava as the worked real-flow example.

## Suggested missing coverage on broad themes (point 3)

- **Biometrics depth.** The deck names the three modes and the "can't revoke a
  fingerprint" problem but doesn't cover false-accept/false-reject trade-offs, liveness
  detection / presentation-attack detection, or the legal status of compelled biometric
  unlock (5th-Amendment "something you are" vs. "something you know"). Worth a slide given
  the agenda flags the three modes as exam material.
- **MFA failure modes.** Push-bombing/MFA fatigue, SIM-swap defeating SMS OTP, and
  adversary-in-the-middle phishing kits (Tycoon 2FA, EvilProxy) that proxy the session —
  directly relevant to why passkeys (phishing-resistant) matter.
- **OAuth vs. OIDC.** The deck correctly says OAuth is authorization, not authentication,
  but students conflate "Log in with Google" (OpenID Connect) with OAuth. A short
  clarification slide would prevent a common misconception.
- **Password storage on the defender side.** Salting, slow hashes (bcrypt/scrypt/
  Argon2), and credential-stuffing from breach corpuses — currently implied by
  "leaked/reused" but never made concrete.
- **PKCE.** Modern OAuth for public/mobile clients relies on PKCE to defend the
  authorization-code flow; deck stops at `state` + exact redirect matching.
- **VPNs / network access control.** The source pptx had a large VPN/IPsec block
  (slides 36–45). I deliberately scoped it out — it is closer to a network-security
  topic than authentication/access control, and the Meeting 3 agenda does not cover it.
  Flag for a possible standalone segment if VPNs are wanted in this course.
- **Zero Trust / continuous authorization.** The token-replay breaches motivate
  "verify continuously, not once" — a natural modern bookend to least privilege.

## Next-year refresh notes

Refresh the dated content below per `../TEMPLATE.md` → "Annual current-events refresh" (web-verify; swap only for something fresher and confirmed). Items placed in prior refreshes that will age:

- **Passkeys / FIDO vignette** — refresh against World Passkey Day 2027 (early May 2027); the 5B / 48% / 75% / 68% numbers will move. Prior year's 87% enterprise figure was a survey artifact — trust the FIDO/Sapio Research consumer + workforce studies as primary.
- **NIST SP 800-63-4 finalization date** — factually anchored (July 31, 2025); do not restate as "recent." Watch for 800-63-5 draft.
- **Salesloft–Drift OAuth breach (Aug 2025)** — still the canonical token-replay case; keep as anchor. Watch for legal outcomes (class-action / SEC disclosure) that would refresh the "consequences" angle.
- **Vercel/Context.ai (April 2026)** and **AiTM PhaaS kits** — refresh with the next-biggest OAuth-token-replay breach if one lands. Kali365 (April 2026) and Mamba 2FA are next-tier kits worth mentioning if EvilProxy/Tycoon fade.
- **Stronger alternative flagged, not yet used:** Microsoft's disclosure of the March 2026 Tycoon2FA law-enforcement disruption + post-takedown migration to Mamba 2FA/EvilProxy — a cleaner illustration of "session cookies are the new password" if the Salesloft story ages out.

## Curated images

- **Used:** `slide012_img004.png` (`ls -l` permissions — matches the live demo);
  `slide054_img018.png` (iOS "Uber would like to access your camera" just-in-time
  prompt); `slide032_img011.png` (OAuth 2.0 abstract flow); `slide035_img012.png`
  (Strava OAuth flow — concrete real-world example); `slide051_img017.png` (protection
  domains: (object, rights) pairs).
- **Dropped:** `slide003_img00{1,2,3}.jpg` (mainframe/PC/phone photos — decorative);
  `slide012_img005.png` (redundant second permissions screenshot);
  `slide015/016` Android permission/manifest screenshots (text on slide suffices);
  `slide017_img009.png` (system-layers clip art); `slide019_img010.png` (capability-URL
  screenshot — covered in prose); `slide039/041/047` VPN + TENEX diagrams (VPN section
  scoped out; TENEX timing attack described in notes).

## Source

- Rebuilt from `_source-extract.md` (58 original slides) + `agenda.md` Meeting 3
  (Authentication & Access Control; OAuth). Consolidated to 23 slides; dropped the VPN
  block as out-of-scope and added the three-modes / passwords-vs-passkeys material that
  the agenda taught but the old pptx omitted.
