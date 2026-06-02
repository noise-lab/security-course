# Grader Key — Authentication / API Lab

Pairs with `README.md` (same folder). Total **100 points**. Grade from `auth-report.md`
plus the pasted token JSON, request/response snippets, and any included code. See
`README.md` for the grading prompt and output format.

Submissions **vary by chosen service** (GitHub PAT, Spotify/Reddit OAuth, Google OAuth
Playground, or any other authenticated API). There is no single fixed answer. Grade
whether the analysis is **correct for the service the student chose** — e.g., a GitHub
PAT is a personal token with no refresh token, while Spotify's authorization-code flow
*does* issue a refresh token. Most evidence should be **pasted text**; screenshots
corroborate but don't replace it. **Tokens should be redacted** — do not penalize a
redacted token; *do* note (no points) if a student pasted a live secret.

---

## Item 1 — Access-Control Scheme (18 pts)

Maps to report heading **"1. Access-Control Scheme"**.

| Check | Pts |
|---|---|
| Identifies the mechanism: requests are authorized by a **token** (OAuth access token or personal access token), not a password per call | 6 |
| Explains how **scopes/permissions** attach to the token and bound what it can do | 6 |
| Describes the **grant flow** that issues the token for their service (correct for what they chose) | 6 |

**Expected/acceptable:** OAuth-based services (Spotify/Reddit/Google) describe the
authorization-code flow: user consents → authorization server returns a code → app
exchanges code at the token endpoint for an access token → token presented to the
resource server. GitHub PAT users correctly describe a self-minted long-lived token
scoped at creation time. **Diagram encouraged but not required for points.**
**Common errors:** describing password/basic auth as if it were the modern scheme;
conflating authentication (who you are) with authorization (what you may do) with no
mention of scopes; vague "it uses an API key" with no notion of scope or issuance.

## Item 2 — The App + Working Proof (17 pts)

Maps to **"2. The App"** and **"5. Proof It Works"** (proof may appear under either heading).

| Check | Pts |
|---|---|
| Describes a working app / authenticated call and which endpoint it hits | 7 |
| Pastes a **real JSON or text response** from the API consistent with their account/app | 10 |

**Acceptable variants:** any single authenticated endpoint (list repos, top tracks,
user profile, subreddit listing). **Common errors:** describing an app but pasting no
response, or pasting public/unauthenticated data that doesn't show the token was used
(cap at 7); a response that is clearly fabricated/generic rather than from their account.

## Item 3 — Auth-Flow Trace (22 pts) — *depth*

Maps to **"3. Auth-Flow Trace"**.

| Check | Pts |
|---|---|
| Correctly names the **grant type** (authorization-code / client-credentials / personal token) and how they can tell | 5 |
| Lists the **scopes** requested and justifies **why each** (mapped to their calls; least privilege) | 5 |
| Distinguishes **access vs. refresh** tokens correctly | 5 |
| States **where the token travels** — the `Authorization: Bearer <token>` header | 3 |
| Pastes a **redacted token-response JSON** and an authorized request showing the **Bearer header** | 4 |

**Expected answers:**
- **Access token** = short-lived credential, **sent on every API request** (in the
  `Authorization: Bearer` header), expires after `expires_in` seconds (e.g., Spotify
  3600s). **Refresh token** = long-lived credential, **not sent on normal requests**;
  exchanged at the token endpoint for a new access token when the access token expires.
- **Bearer scheme:** the token rides in the header `Authorization: Bearer <token>` —
  whoever bears it is granted access (hence "bearer"). Not in the URL/query, not a cookie.
- **GitHub PAT:** grant type = personal access token; **no refresh token** (it's
  long-lived itself). Accept this — do not dock for "missing" refresh token if the
  service doesn't issue one; full marks require noting *that* it doesn't.
- **client-credentials:** acceptable when there's no user (app-to-app); typically no
  refresh token.

**Common errors:** saying the token goes in the URL or a cookie (wrong for these APIs);
calling a PAT an "authorization-code" flow; swapping access and refresh roles (refresh
sent on every request — wrong); requesting broad scopes with no justification; no pasted
token JSON or no visible Bearer header (cap the last row).

## Item 4 — Token-Leak Threat Model (18 pts) — *depth*

Maps to **"4. Token-Leak Threat Model"**.

| Check | Pts |
|---|---|
| States **what an attacker can do** with a leaked token, tied to **their actual scopes** (correct blast radius) | 7 |
| Names **minimal scopes / least privilege** as a mitigation (and what they didn't request) | 4 |
| Names **short expiry + rotation/refresh** as a mitigation (leaked token soon dies; window closes) | 4 |
| Names **rate limiting** as a mitigation (caps extraction/damage before detection) | 3 |

**Expected answer:** a leaked **access token** lets the attacker **act as the app within
exactly the granted scopes, until the token expires** (or is revoked) — no password
needed, MFA bypassed, because the token *is* the credential. Tie this to their scopes:
e.g., `repo` → read/write private repos; `playlist-modify` → alter playlists; read-only
scope → exfiltrate data but not modify. **Mitigations:** minimal scopes shrink the blast
radius; short expiry + rotation/refresh shrink the *time window* (and a leaked refresh
token is worse — note revocation); rate limits cap how fast an attacker can extract or
destroy and aid detection. **Common errors:** "they can do anything / take over the
account" with no link to scopes (cap at ~7); listing mitigations generically without
connecting them to their own scopes/expiry; forgetting that the token bypasses the
password entirely.

## Item 5 — Reflection & AI-verification (15 pts) — *AI-resilience*

Maps to **"6. Reflection & Tinkering"**. This item rewards work that is demonstrably the
student's own. Graded on **specificity and grounding in their flow**, not prose quality.

| Check | Pts |
|---|---|
| Describes something they **tried that didn't work** and how they resolved it (a concrete dead end, not a platitude) | 5 |
| Notes something that **surprised them in their own flow**, referencing a specific token/scope/header/response | 5 |
| If AI was used: names **one claim they checked against the actual token/response** and the outcome. If AI was not used: a correct extra observation about their flow earns these points | 5 |

**This is the anti-bluff item.** Generic reflection that could describe *any* student's
run ("I learned OAuth is secure") earns ≤3 total. Look for detail that is only possible
if they actually did it: a specific 401 from a malformed header, a redirect-URI
mismatch, a scope they forgot, the actual `expires_in` value surprising them, an AI
claim that didn't match the field they found (e.g., model said token goes in the URL;
they verified it's in `Authorization: Bearer`).

## Item 6 — Clarity, diagram, naming (10 pts)

Maps to overall report quality across all headings.

| Check | Pts |
|---|---|
| Report named **`auth-report.md`** and follows the heading skeleton | 4 |
| Evidence pasted as **text** and **tokens redacted** (no live secrets) | 4 |
| A diagram (or equally clear structured explanation) clarifies the access-control scheme | 2 |

**Common errors:** wrong filename or scrambled headings (dock the first row); only
screenshots with no pasted text (dock the second row); **a live, unredacted secret** —
flag it prominently in feedback (it's a real security issue) though scoring stays here.

## Item 7 — Extra credit: least-privilege or refresh demo (+10) — *sophistication stretch*

Maps to **"7. (Extra credit) Scope/Refresh Demonstration"**. Award only with evidence.

| Check | Pts |
|---|---|
| **Insufficient-scope path:** pastes the API's real **`403` / `insufficient_scope`** error for an under-scoped action **OR** **refresh path:** pastes the failed (expired) request | +4 |
| Shows the **fix working:** adds the scope and re-runs successfully **OR** uses the **refresh token** to get a new access token (pastes both redacted token responses) | +4 |
| Explains *why* the demo proves least privilege / why refresh tokens exist (the boundary is real / the window closes) | +2 |

Cap total at 100 before extra credit; extra credit may push a strong submission above
100 per the instructor's policy, or offset losses elsewhere.

## Appendix — AI usage (no points, but affects others)

If the student used an LLM, they should include the prompt/output and **verify it
against their token/response**. **Reward verification:** if they caught the model in an
error (e.g., wrong header, wrong grant type, swapped access/refresh), award the related
item's points generously. **Penalize unverifiable assertions:** an explanation that
matches no pasted evidence and that they can't back up should lose the relevant item's
evidence points even if it happens to be correct.

---

### Scoring summary

| Item | Max |
|---|---|
| 1. Access-Control Scheme | 18 |
| 2. The App + Working Proof | 17 |
| 3. Auth-Flow Trace | 22 |
| 4. Token-Leak Threat Model | 18 |
| 5. Reflection & AI-verification | 15 |
| 6. Clarity, diagram, naming | 10 |
| **Total** | **100** |
| 7. Extra credit: least-privilege or refresh demo | +10 |
