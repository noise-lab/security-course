# Grader Key — PKI Lab

Pairs with `README.md` (same folder). Total **100 points**. Grade from `pki-report.md` plus the two
pasted captures' text. See `README.md` for the grading prompt and output format.

The submission is correct *for the student's chosen server/site*; there is no single
fixed answer. Check that the analysis is right for what they did. Most evidence should
be **pasted text** copied from Wireshark; screenshots corroborate but don't replace it.

---

## Item 1 — Web Server Setup (10 pts)

Maps to report heading **"1. Web Server Setup"**.

| Check | Pts |
|---|---|
| Describes a working local server (Python `http.server`, nginx, Apache, etc.) | 5 |
| Makes clear a client actually fetched a resource from it (so there's traffic to capture) | 5 |

**Common errors:** describing the server but never serving/fetching anything; no
indication a request was made.

## Item 2 — Why HTTP Is Insecure (18 pts)

Maps to **"2. Why HTTP Is Insecure"**.

| Check | Pts |
|---|---|
| Pastes a real HTTP **request line** (`GET /... HTTP/1.1`) and headers from their capture | 7 |
| Shows response **body content** visible in cleartext (snippet or screenshot of Follow Stream) | 5 |
| Explains in their own words that an on-path eavesdropper sees the URL, headers (incl. cookies), and body | 6 |

**Acceptable variants:** any path/host; any cleartext body. **Common errors:** asserting
"HTTP is unencrypted" with no pasted evidence (cap at 7); confusing TCP metadata with payload.

## Item 3 — HTTPS Upgrade (18 pts)

Maps to **"3. HTTPS Upgrade"**.

| Check | Pts |
|---|---|
| Generated a self-signed cert and added it to locally trusted roots; server restarted on HTTPS | 9 |
| Correctly answers **why a public CA won't issue a cert** for a local server | 9 |

**Expected answer (why no CA cert):** a CA validates **control of a public domain
name** (DNS/HTTP/email challenge) before issuing; a local server has no public domain
the CA can validate (it's `localhost` / a private IP / not internet-reachable), so the
CA cannot perform domain validation. Accept any answer capturing "CA must verify you
control a public domain and you don't / it isn't reachable." **Common error:** "because
it's not secure" or "it costs money" — these miss the validation point (≤3 pts).

## Item 4 — HTTP vs. HTTPS Comparison (14 pts)

Maps to **"4. HTTP vs. HTTPS Comparison"**.

| Check | Pts |
|---|---|
| Shows the HTTP payload was readable | 4 |
| Shows the HTTPS payload is **TLS Application Data** (ciphertext) — pasted or screenshotted | 6 |
| States the contrast: same content, now unreadable to an eavesdropper | 4 |

**Common errors:** claiming HTTPS hides *everything* (it doesn't — see Item 6); no
evidence the second capture is actually TLS.

## Item 5 — Handshake Interpretation (15 pts) — *depth*

Maps to **"5. Handshake Interpretation"**.

| Check | Pts |
|---|---|
| Pastes the **TCP three-way handshake** (`SYN` / `SYN, ACK` / `ACK`) with packet numbers | 5 |
| Pastes **ClientHello** and **ServerHello** detail, including the **SNI / `server_name`** in the ClientHello | 6 |
| Correctly explains what each packet does (handshake sets up the connection / negotiates cipher + keys) | 4 |

**Common errors:** mislabeling Application Data as part of the handshake; missing SNI;
no packet numbers (the rubric asks for them — dock 1–2).

## Item 6 — What Still Leaks Over HTTPS (10 pts) — *depth*

Maps to **"6. What Still Leaks Over HTTPS"**. Award up to the cap for correctly covering
each; full marks need at least the SNI/IP point plus two others.

| Leak the student should identify | Pts |
|---|---|
| **Hostname** via **SNI** (plaintext in ClientHello) and/or **destination IP** | 4 |
| **Packet sizes/timing** → traffic analysis / website fingerprinting | 2 |
| **DNS** leaks the hostname *before* TLS (unless encrypted) | 2 |
| **ECH** encrypts the SNI and would close the SNI leak (not the IP) | 2 |

**Common errors:** claiming nothing leaks; saying ECH hides the IP (it does not).

## Item 7 — Reflection & AI-verification (15 pts) — *AI-resilience*

Maps to **"7. Reflection & Tinkering"**. This item rewards work that is demonstrably the
student's own. It is graded on **specificity and grounding in their capture**, not prose
quality.

| Check | Pts |
|---|---|
| Describes something they **tried that didn't work** and how they resolved it (a concrete dead end, not a platitude) | 5 |
| Notes something that **surprised them in their own capture**, referencing a specific packet/field/domain | 5 |
| If AI was used: names **one claim they checked against the bytes** and the outcome. If AI was not used: a correct extra observation about their trace earns these points | 5 |

**This is the anti-bluff item.** Generic reflection that could describe *any* student's
run ("I learned HTTPS is more secure") earns ≤3 total. Look for detail that is only
possible if they actually did it: a specific wrong cipher, a filter that hid packets, a
surprising third-party domain, an AI claim that didn't match the SNI they found.

## Item 8 — Extra credit: decrypt your own TLS (+10) — *sophistication stretch*

Maps to **"8. (Extra credit) Decrypted TLS"**. Award only with evidence.

| Check | Pts |
|---|---|
| Describes using `SSLKEYLOGFILE` + Wireshark TLS key-log setting | +4 |
| Pastes the **recovered plaintext** HTTP request/response from the decrypted capture | +4 |
| Explains why holding the key log lets *them* read what an on-path eavesdropper cannot | +2 |

Cap total at 100 before extra credit; extra credit may push a strong submission above 100
per the instructor's policy, or offset losses elsewhere.

## Appendix — AI usage (no points, but affects others)

If the student used an LLM, they should include the prompt/output and **verify it
against the packets**. **Reward verification:** if they caught the model in an error,
award the related item's points generously. **Penalize unverifiable assertions:** an
explanation that matches no pasted packet and that they can't back up should lose the
relevant item's evidence points even if it happens to be correct.

---

### Scoring summary

| Item | Max |
|---|---|
| 1. Web Server Setup | 10 |
| 2. Why HTTP Is Insecure | 18 |
| 3. HTTPS Upgrade | 18 |
| 4. HTTP vs. HTTPS Comparison | 14 |
| 5. Handshake Interpretation | 15 |
| 6. What Still Leaks Over HTTPS | 10 |
| 7. Reflection & AI-verification | 15 |
| **Total** | **100** |
| 8. Extra credit: decrypt own TLS | +10 |
