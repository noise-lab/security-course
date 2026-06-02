# 04-Authentication — instructor notes

## Current-events updates made (point 2)

- **Salesloft–Drift OAuth token breach (Aug 2025)** — added as the central vignette on
  "Attackers Stopped Stealing Passwords." Threat actor UNC6395 stole and replayed OAuth
  *access tokens* from the Drift app to exfiltrate Salesforce data from 700+ orgs
  (Cloudflare, Google, Palo Alto Networks, Zscaler, etc.), bypassing MFA because a valid
  bearer token needs no second factor. Verified via The Hacker News, Google Cloud Threat
  Intelligence, and Arctic Wolf. This replaces the dated, generic "tokens can leak"
  framing and ties directly to capabilities/least-privilege/revocation.
- **2026 follow-ons** (same slide): the Vercel/Context.ai breach via a compromised
  Google Workspace OAuth token, and the EvilTokens phishing-as-a-service campaign hitting
  340+ Microsoft 365 tenants — shown as evidence the "steal the token, not the password"
  playbook is now standard. Verify exact figures before lecturing; these are recent.
- **Passkeys / FIDO2 vignette** — added on the passwords slide. World Passkey Day
  (May 2026) reporting: passkeys on ~48% of top-100 sites, ~87% of enterprises
  deploying/piloting, and NIST SP 800-63-4 (finalized July 2025) endorsing
  phishing-resistant auth. Grounds the "passwords are losing" claim with dated facts.
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
