# Modern Authentication and Access Control

**Format.** Break into groups of 4–5. Each group picks **one** of the two breakouts below (or takes both if time allows). Spend ~5 minutes skimming the prep reads, then ~10 minutes debating. A designated reporter brings the group's position — and any dissents — back to the full class for a ~3-minute report-back.

Lecture 4's opening claim — "attackers stopped stealing passwords" — is now backed by the Salesloft/Drift breach: UNC6395 replayed stolen OAuth *tokens* against 700+ orgs and bypassed MFA entirely. The industry is racing toward passkeys and zero-trust continuous authorization; both breakouts pick a fault line in that migration.

---

## Breakout A: Kill the Password — or Kill the Passkey?
<!-- breakout id="A" status="current" refreshed="2026-07-16" -->

**Motion.** *"Passkeys (FIDO2/WebAuthn) should be mandated as the default authenticator for consumer services by 2028. Continuing to allow password-only or SMS-OTP logins is negligent given the demonstrated failure modes of both."*

<!-- current-events:start topic="passkeys-fido2-mandate-passwords" -->
**Prep reads (5–10 min).**
- [NIST SP 800-63-4: Digital Identity Guidelines](https://nvlpubs.nist.gov/nistpubs/SpecialPublications/NIST.SP.800-63-4.pdf) — NIST, July 2025. The finalized federal identity guidance that codifies phishing-resistance as a required AAL2 option and mandates hardware-backed keys at AAL3 — the closest thing to a de facto passkey mandate for U.S. federal systems.
- [NIST SP 800-63-4: What the new phishing-resistant definition means for federal agencies](https://www.yubico.com/blog/nist-sp-800-63-4-what-the-new-phishing-resistant-definition-means-for-federal-agencies/) — Yubico, August 2025. Vendor-authored but useful breakdown of what "channel binding" vs. "verifier name binding" mean in practice, and which SMS/TOTP fallbacks are now non-compliant.
- [State-of-the-art phishing: MFA bypass](https://blog.talosintelligence.com/state-of-the-art-phishing-mfa-bypass/) — Cisco Talos, 2025. Empirical data on Tycoon 2FA and EvilProxy adversary-in-the-middle kits that defeat push and TOTP MFA — the failure mode passkeys are designed to eliminate.
- [Passwordless adoption moves from hype to habit](https://www.helpnetsecurity.com/2025/10/31/passkey-adoption-trends-2025/) — Help Net Security, October 2025. FIDO Alliance/Dashlane data: Microsoft made passkeys the default for new accounts in May 2025, Google reports 800M+ accounts using passkeys, but 93% of users still enter a password daily.
<!-- current-events:end -->

**Discussion prompts.**
- Passkeys are phishing-resistant by construction (origin-bound; no shared secret to phish). NIST SP 800-63-4 (finalized July 2025) formalizes phishing resistance as an authentication requirement. Is a *mandate* justified — or is default-on adoption (Apple, Google, Microsoft) with retained password fallback the right pace?
- Passkeys tie your login to a platform vendor's sync ecosystem (Apple iCloud Keychain, Google Password Manager, 1Password). Have we solved authentication or just centralized it into three vendors' account-recovery flows?
- SIM-swap attacks defeat SMS OTP; adversary-in-the-middle kits (Tycoon 2FA, EvilProxy) defeat TOTP; push-bombing defeats push MFA. In enterprises where passkeys aren't yet universal, which of these should regulators (FTC, CFPB, HHS) treat as *inadequate* MFA?
- The Salesloft/Drift breach bypassed MFA entirely by stealing valid OAuth tokens. Passkeys wouldn't have helped — the tokens were already minted. Does the "kill the password" framing distract from the real 2026 attack surface (session tokens, OAuth grants, refresh tokens)?

**Bring back.** Your group's timeline for phasing out password-only logins on consumer services, and the one class of service where you'd grant an indefinite exception.

---

## Breakout B: OAuth Was for Authorization — Everyone Uses It for Everything
<!-- breakout id="B" status="current" refreshed="2026-07-16" -->

**Motion.** *"The Salesloft–Drift breach (Aug 2025) proved that OAuth's 'authorize an app once, then it acts on your behalf forever' model is fundamentally broken for enterprise SaaS. Bearer tokens without continuous re-authorization must be regulated out of existence for any high-value data."*

<!-- current-events:start topic="oauth-token-breach-zero-trust" -->
**Prep reads (5–10 min).**
- [Widespread Data Theft Targets Salesforce Instances via Salesloft Drift](https://cloud.google.com/blog/topics/threat-intelligence/data-theft-salesforce-instances-via-salesloft-drift) — Google Threat Intelligence Group / Mandiant, August 2025. The primary-source technical writeup: UNC6395 stole Drift OAuth tokens (via a Salesloft GitHub compromise months earlier), ran SOQL exports against 700+ Salesforce tenants Aug 8-18, and deleted job records to cover tracks.
- [Cybersecurity Alert – Salesloft Drift AI Supply Chain Attack](https://www.finra.org/rules-guidance/guidance/salesloft-drift-AI-supply-chain-attack) — FINRA, September 2025. Regulator's guidance to member firms — a rare official document treating an OAuth-token supply-chain compromise as a foreseeable enterprise risk requiring due-diligence.
- [Reviewing the Salesforce–Salesloft Drift OAuth Supply Chain Breach](https://www.anomali.com/blog/salesloft-drift-breach-recap) — Anomali, September 2025. Named-victim list (Cloudflare, Google, PagerDuty, Palo Alto, Proofpoint, Zscaler, and others), scope of exfiltration, and the "MFA-doesn't-help" mechanics of stolen bearer tokens.
- [The Drift OAuth breach: A cybersecurity wake-up call](https://www.wtwco.com/en-us/insights/2025/09/the-drift-oauth-breach-a-cybersecurity-wake-up-call) — Willis Towers Watson, September 2025. Insurance-industry perspective on how the breach reshapes coverage for third-party SaaS integrations, useful counterweight to the technical write-ups.
<!-- current-events:end -->

**Discussion prompts.**
- UNC6395 stole Drift OAuth access tokens and exfiltrated Salesforce data from Cloudflare, Google, Palo Alto, Zscaler and 700+ others in days. A valid bearer token needs no second factor. Whose failure was this — Salesloft's, Salesforce's, or the OAuth spec's?
- The lecture distinguished OAuth (authorization) from OIDC (authentication) and warned that "log in with Google" conflates the two. In the wild, do users experience any difference? Should the two flows be visibly separated in the UX?
- Least-privilege / capability-URL / (object, rights) models sit at the theoretical core of the lecture. Real OAuth scopes are often coarse ("read all email," "post as user"). Is the gap between principle and practice a spec problem, a UX problem, or a vendor-incentive problem?
- Zero-trust "verify continuously, not once" is the marketed response. Does that actually mean re-authenticating every action (usability disaster), or continuously validating context (device posture, IP reputation, behavior)? Who decides what "context" is enough?

**Bring back.** The single OAuth scope your group would ban outright for consumer apps, and one enterprise change that would have blocked the Drift attack.

---

## Instructor notes

If students did the [OAuth](../activities/oauth.md) activity earlier in class, Breakout B has instant traction — they've just seen a token flow. Breakout A is more accessible to non-CS majors and produces livelier debate. Both benefit from the instructor pausing on one nuance: authentication (who are you?) vs. authorization (what can you do?) vs. session (are you still here?). Most real breaches confuse two of the three. Time-short: run B; the Salesloft story is a rare "everyone in the class has an OAuth token from that vendor" moment.

<!--
breakout-metadata:
  lecture: 4
  class: "Modern Authentication"
  last_refreshed: 2026-07-16
-->
