## Authentication / API Access Control

The goal of this assignment is to understand API access control by building a
small third-party application against a real web service and then tracing —
concretely, with bytes — how the service decides what your app is allowed to do.
Modern APIs gate access with tokens (OAuth 2.0 access/refresh tokens, or personal
access tokens). You'll obtain such a token, use it, and reason about what happens
when it leaks.

> **New:** This lab now goes deeper than "make an API call." You will trace the
> full auth flow (grant type, scopes, access vs. refresh tokens, and the
> `Authorization: Bearer ...` header), and build a token-leak threat model.
> The evidence is text you paste into your report.

### Grading & Rubric (100 points)

This rubric is shown up front so you know where to invest your effort. Labs are
graded primarily for thoughtful completion; points reward *understanding*, not polish.

| Component | Points | What earns full marks |
|---|---|---|
| **Access-control scheme** | 18 | You explain how *your chosen service* decides access — tokens/scopes/grant flow — accurately and in your own words. A diagram is encouraged. |
| **The app + working proof** | 17 | You describe a working app (even a one-endpoint script) and paste a **real JSON/text response** from the API that proves it ran. |
| **Auth-flow trace (depth)** | 22 | You identify the **grant type**, the **scopes** requested *and why*, **access vs. refresh** tokens, and **where the token travels** — and you paste a **redacted token-response JSON** plus one authorized request showing the `Authorization: Bearer ...` header. |
| **Token-leak threat model (depth)** | 18 | You explain what an attacker can do with a leaked token *given your scopes*, and give concrete mitigations: minimal scopes, short expiry + rotation/refresh, rate limiting. |
| **Reflection & AI-verification** | 15 | You report what you *tried* (including dead ends), what surprised you in **your own** flow, and — if you used an LLM — at least one place you checked its claim against the actual token/response and what you found. |
| **Clarity, diagram, naming** | 10 | Report is named correctly, headings follow the skeleton, evidence is pasted as text, tokens are redacted, and (ideally) a diagram clarifies the scheme. |
| **Extra credit: least-privilege or refresh demo** | +10 | You empirically demonstrate scopes or refresh — e.g., trigger a real **403 / insufficient-scope** error, or expire and refresh a token. See the stretch task. |

Paste evidence **as text** so a grader can read it. Redact secrets (see below). The
reflection must be grounded in *your* specific service and flow — generic prose that
could describe anyone's run earns little credit.

> **Redaction rule.** Never paste a live, valid secret. Replace the bulk of every
> token, client secret, and code with `...` or `<REDACTED>`, leaving only enough
> (e.g., the first few characters, the `token_type`, `expires_in`, `scope`) to make
> the structure clear. A leaked token in your repo is itself a security incident —
> and these labs go to a **private** repo for that reason.

### Tasks

1. **Choose a service and get authenticated access.**
   Twitter/X's API is no longer free or practical for this lab. Use one of these
   currently-free, token-bearing options (or **choose any web service with
   authenticated access** you prefer):
   - **GitHub REST API** — [personal access tokens](https://docs.github.com/en/rest/authentication/authenticating-to-the-rest-api) (easiest; a fine-grained or classic PAT, no OAuth dance).
   - **Spotify Web API** — [OAuth 2.0](https://developer.spotify.com/documentation/web-api) (authorization-code flow with scopes).
   - **Reddit API** — [OAuth 2.0](https://www.reddit.com/dev/api/) (script or web app).
   - **Google OAuth 2.0 Playground** — [oauthplayground](https://developers.google.com/oauthplayground/) (great for *seeing* the token exchange and scopes explicitly).

   **Note: approval and API keys can take time** (hours to days for some services).
   **Request access as early as possible.**

2. **Describe the service's access-control scheme.**
   Explain how *your* service decides what a request is allowed to do: what a token
   represents, how scopes/permissions attach to it, and how the grant flow issues it.
   Some schemes are simple to explain; some are not — **a diagram can make this much
   easier** (e.g., the OAuth box-and-arrow flow: user → authorization server →
   redirect with code → token endpoint → access token → resource server).

3. **Build the app and prove it works.**
   The app does **not** need to be complicated — a single authenticated endpoint call
   is fine (list your repos, fetch your top tracks, read a subreddit's posts, get your
   user profile). Describe what it does, then **paste a real JSON or text response**
   from the API that proves it actually ran against your account.

4. **Trace the auth flow (depth).**
   Pin down, for your service, the following — and back each with evidence:
   - **Grant type.** Which one did you use: **authorization-code** (user consents,
     you exchange a code for a token), **client-credentials** (app-to-app, no user),
     or a **personal access token** (a long-lived token you minted yourself)? Say how
     you can tell.
   - **Scopes.** Which scopes/permissions did you request, and **why each one**? Map
     each scope to the specific call your app makes (least privilege: don't request
     `repo` if you only read public data).
   - **Access vs. refresh tokens.** Identify the **access token** (short-lived, sent on
     every request) and, if your flow issues one, the **refresh token** (long-lived,
     exchanged at the token endpoint for a new access token). Note `expires_in` /
     `token_type` from your response.
   - **Where the token travels.** Show that the token rides in the
     **`Authorization: Bearer <token>`** request header (not the URL, not a cookie, for
     these APIs).
   - **Paste evidence:** a **redacted token-response JSON** (showing `access_token` (redacted),
     `token_type`, `expires_in`, `scope`, and `refresh_token` if present) **and** one
     example authorized request showing the `Authorization: Bearer ...` header (token redacted).

5. **Token-leak threat model (depth).**
   Suppose your access token leaks (committed to a public repo, captured from a log,
   phished). Answer concretely *for your scopes*:
   - **What can the attacker do** with it? Tie this to the exact scopes you requested —
     e.g., a token with `playlist-modify` lets them edit your playlists; a GitHub PAT
     with `repo` lets them read/write your private repos. Be specific about the blast radius.
   - **What can't they do** (scopes you deliberately didn't request)?
   - **Mitigations.** Explain how each of these limits the damage: **minimal scopes**
     (least privilege), **short expiry + rotation/refresh** (the window of abuse closes,
     and the leaked token soon dies), and **rate limiting** (caps how much an attacker
     can extract or destroy before detection). Connect each mitigation to *your* setup.

6. **Reflection & tinkering (required).**
   This is where you show the work is *yours*. In a short reflection (a few paragraphs):
   - What did you **try that didn't work** at first (a 401 from a malformed header, a
     scope you forgot to request, a redirect URI mismatch, a token that expired
     mid-test)? How did you fix it?
   - What **surprised you** in *your own* flow specifically — how short the access
     token's life was, a scope that granted more than you expected, a header you didn't
     anticipate, a rate-limit response you hit?
   - If you used an LLM anywhere, name **one claim you checked against the actual token
     or response** (e.g., it said the token goes in the URL; you found it goes in the
     `Authorization` header) and say whether it held up.

7. **Stretch — prove least privilege or refresh (extra credit, +10).**
   Anyone can *say* scopes and expiry matter; demonstrate it empirically. Do **one** of:
   - **Least-privilege / insufficient-scope.** Have your app attempt an action that
     requires a **broader** scope than the one your token holds, and **paste the API's
     `403` / `insufficient_scope` (or equivalent) error**. Then add the scope, re-run,
     and show it now succeeds. This proves the access-control boundary is real, not theoretical.
   - **Token refresh.** Let an access token **expire** (or revoke it), show the failed
     request, then **use your refresh token to obtain a new access token** and paste
     **both token responses** (old and new, redacted) plus the now-successful request.

   This requires real tinkering and is self-evidently done or not — a good way to go
   beyond a one-shot answer.

> **Using AI (encouraged, with verification).** You may use an LLM to help you
> understand a scope, a grant type, or an error response. If you do, **include the
> exchange in the appendix** and then **verify the model's claim against your actual
> token/response** — point to the field that confirms (or contradicts) it. Submitting
> an explanation you can't defend against your own evidence will lose points; catching
> the model in an error will earn full marks for that item.

> **Be ready to defend it.** Per the syllabus, we may ask you to reproduce or explain
> any part of this lab live (office hours, a pop quiz, or the exam) — e.g., "show where
> your token travels," "which scope authorizes this call," or "what would an attacker
> do with this token?" Do the work so you can.

### Submission Instructions

Submit a single markdown report named **`auth-report.md`**. **Because your report is
graded from its text, paste the required evidence *as text* directly into the report**
(redacted token JSON, the `Authorization` header, request/response snippets).
Screenshots are welcome but are corroboration, not a substitute for the pasted text.
You may also include your app code.

Your report **must contain these headings, in this order** (they map one-to-one to the
rubric above):

```
# Authentication / API Lab — <your name>

## 1. Access-Control Scheme
   (how your chosen service decides access: tokens, scopes, grant flow; diagram encouraged)

## 2. The App
   (what it does; which endpoint it calls and why)

## 3. Auth-Flow Trace
   - Grant type (authorization-code / client-credentials / personal token) and how you can tell
   - Scopes requested and WHY each one (mapped to your calls)
   - Access vs. refresh tokens (which is short- vs. long-lived; expires_in / token_type)
   - Where the token travels (the Authorization: Bearer header)
   - Pasted REDACTED token-response JSON
   - Pasted authorized request showing the Authorization: Bearer header (redacted)

## 4. Token-Leak Threat Model
   - What an attacker can do with a leaked token, tied to YOUR scopes (and what they can't)
   - Mitigations: minimal scopes, short expiry + rotation/refresh, rate limiting

## 5. Proof It Works
   - Pasted real JSON/text response from the API

## 6. Reflection & Tinkering
   - What you tried that didn't work; what surprised you in YOUR flow;
     one AI claim you verified against the actual token/response

## 7. (Extra credit) Scope/Refresh Demonstration
   - 403/insufficient-scope error then success, OR expired+refreshed token (both responses, redacted)

## Appendix: AI usage (if any)
   - Prompts, model output, and your verification against the token/response
```

Push the report (and any app code) to your **private** GitHub repository. **Do not push
a zip file, and do not push live secrets** — redact all tokens, secrets, and codes.
