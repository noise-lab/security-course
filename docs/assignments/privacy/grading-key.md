# Grader Key — Internet Privacy Lab

Pairs with `README.md` (same folder). Total **100 points**. Grade from `privacy-report.md`
plus the pasted captures' text. See `README.md` for the grading prompt and output format.

The submission is correct *for the student's chosen site*; there is no single fixed
answer. The set of domains, companies, and counts will vary by site and by when they
captured. Check that the analysis is right for what they did. Most evidence should be
**pasted text** copied from Wireshark (the query-name list, the domain→company table);
screenshots corroborate but don't replace it. Claude cannot open the `.pcap`, so an item
backed only by an un-pasted capture earns no evidence points.

---

## Item 1 — Setup & method (5 pts)

Maps to report heading **"1. Setup"**.

| Check | Pts |
|---|---|
| Names the specific site chosen and confirms a cold cache (cleared browser/OS cache or "not visited recently") | 3 |
| Describes capturing with Wireshark and exporting DNS-only (`dns` filter → Export Displayed) | 2 |

**Common errors:** no site named; no mention of clearing cache (a warm cache produces far
fewer queries and undermines Items 2–3).

## Item 2 — Unencrypted DNS Capture (12 pts)

Maps to **"2. Unencrypted DNS Capture"**.

| Check | Pts |
|---|---|
| Pastes a **list of distinct queried hostnames** (`dns.qry.name`) as text from the load | 8 |
| The `dns.pcap` is included and the pasted list is plausibly a real page load (multiple distinct hostnames, includes the site's own domain) | 4 |

**Acceptable variants:** any site; any plausible set of hostnames. A real popular site on
a cold cache typically yields well more than a handful of distinct names. **Common
errors:** asserting "I captured DNS" with no pasted list (cap at 4); only one or two
hostnames listed for a major site (suggests a warm cache or filtered-out packets — dock).

## Item 3 — Domain → Company → First/Third-Party Table (20 pts) — *depth*

Maps to **"3. Domain → Company → First/Third-Party Table"**.

| Check | Pts |
|---|---|
| Table maps each distinct domain to its **owning company** | 8 |
| Each domain is correctly classified **first-party vs third-party** | 6 |
| Reports the **count of distinct domains** and the **count of distinct companies** | 6 |

**Expected/acceptable answers:** the site's own domain (and its CDN) are **first-party**;
ad/analytics/tracker domains are **third-party**. Correct clustering examples:
`doubleclick.net`, `googlesyndication.com`, `google-analytics.com`,
`googletagmanager.com`, `gstatic.com`, `youtube.com` → **Google/Alphabet**;
`facebook.com` / `fbcdn.net` / `connect.facebook.net` → **Meta**; `amazon-adsystem.com` /
`cloudfront.net` → **Amazon**; `scorecardresearch.com` → **Comscore**; `criteo.com` →
**Criteo**; `adnxs.com` → **Xandr/Microsoft**. The distinct-domain count should match
their Item 2 list; the distinct-company count is that list rolled up to owners (smaller).
**Common errors:** listing domains without rolling them up to companies (miss the 8);
calling every domain "third-party" or every domain "first-party" without distinguishing;
not reporting either count; counts that contradict the pasted list.

## Item 4 — Who Can See Your Activity & Concerns (18 pts)

Maps to **"4. Who Can See Your Activity & Concerns"**.

| Check | Pts |
|---|---|
| Identifies the **on-path observers** of unencrypted DNS: the **ISP**, anyone on the same network/Wi-Fi, and the **resolver operator** | 7 |
| Explains **how** each company/observer gained visibility (a tracker domain was queried; the resolver answered the lookup; ISP saw plaintext port-53 traffic) | 5 |
| Gives concrete concerns that **differ by company** | 6 |

**Expected answer (who sees unencrypted DNS):** the queries are in plaintext on **port
53**, so the **ISP**, **anyone on-path / on the same Wi-Fi**, and **the DNS resolver
operator** all see every hostname looked up; in addition, the **companies behind the
queried domains** learn of the visit because their domains were contacted. **Differ-by-
company examples:** an **ad/tracking network** (Google, Meta, Criteo) builds a
cross-site behavioral profile for targeting; your **ISP** can log/sell browsing history;
a **CDN/font host** mainly sees an IP hit and is a lesser concern. **Common errors:**
naming only "hackers" with no ISP/resolver; treating all companies as equally concerning
with no differentiation (cap the 6).

## Item 5 — Encrypted DNS Repeat (12 pts)

Maps to **"5. Encrypted DNS Repeat"**.

| Check | Pts |
|---|---|
| Enabled DoH and recaptured the same site | 4 |
| Shows **evidence**: plain `dns` filter now shows nothing for the load, while `tcp.port == 443` (DoH) / `853` (DoT) traffic to the resolver appears | 4 |
| States **who can see your activity now** (the resolver operator, not the ISP, for the lookups) | 4 |

**Expected answer:** with DoH, the lookups ride inside TLS to the resolver, so the `dns`
filter is empty and you instead see encrypted traffic to the resolver IP (e.g.,
`1.1.1.1`) on 443. The ISP no longer sees the DNS names; the **resolver operator** does.
**Common errors:** claiming they still see `dns` packets after enabling DoH (suggests DoH
didn't actually take effect — note it); no evidence the second capture differs.

## Item 6 — Privacy Tradeoffs: ISP vs Resolver Trust, SNI, ECH (20 pts) — *depth*

Maps to **"6. Privacy Tradeoffs: ISP vs Resolver Trust, SNI, ECH"**. Full marks need the
trust-shift point **plus** the SNI point **plus** ECH; the IP point is the bonus detail.

| Point the student should make | Pts |
|---|---|
| **Trust shift**: visibility moves from the **ISP** to the **resolver operator** (e.g., Cloudflare), who now sees *every* lookup; centralization tradeoff discussed | 7 |
| **SNI** still leaks the hostname in plaintext in the TLS ClientHello, so an on-path ISP still learns the site | 7 |
| **Destination IP** in the IP header is never encrypted and often maps back to the site/CDN | 3 |
| **ECH (Encrypted Client Hello)** encrypts the SNI and would close that leak — but **not** the IP leak | 3 |

**Expected answer:** encrypted DNS does **not** make you anonymous — it relocates trust
to the resolver and leaves the **SNI** and **destination IP** exposed; **ECH** fixes SNI
but not the IP. **Common error (flag explicitly):** "encrypted DNS makes you anonymous"
or "now nobody can see what sites I visit" — **false**, because the resolver, the SNI, and
the destination IP still reveal the sites. Also wrong: claiming ECH hides the IP (it does
not). Penalize an answer that misses the trust shift or claims nothing leaks (cap at ~8).

## Item 7 — Reflection & AI-verification (13 pts) — *AI-resilience*

Maps to **"7. Reflection & Tinkering"**. This item rewards work that is demonstrably the
student's own. It is graded on **specificity and grounding in their capture**, not prose
quality.

| Check | Pts |
|---|---|
| Describes something they **tried that didn't work** and how they resolved it (a concrete dead end — a cached page, a DoH toggle that didn't apply, a filter that hid packets — not a platitude) | 4 |
| Notes something that **surprised them in their own capture**, referencing a specific domain/company/count | 4 |
| If AI was used: names **one claim they checked against their data** and the outcome (e.g., a domain→company mapping they confirmed or corrected). If AI was not used: a correct extra observation about their trace earns these points | 5 |

**This is the anti-bluff item.** Generic reflection that could describe *any* student's run
("I learned DNS can be tracked") earns ≤3 total. Look for detail only possible if they
actually did it: a specific unexpected tracker domain, the exact number of companies that
saw one load, a first-party-looking domain that turned out to be third-party-owned, an AI
domain attribution that didn't match their own check.

## Item 8 — Extra credit: two-resolver or cross-site comparison (+10) — *sophistication stretch*

Maps to **"8. (Extra credit) Two-Resolver or Cross-Site Comparison"**. Award only with
pasted evidence.

| Check | Pts |
|---|---|
| States which variant they did (two resolvers / cross-site / DoH-evidence) and pastes the second set of evidence | +5 |
| Analyzes **what differed and why** (who sees lookups changes by resolver; tracker footprint differs by site category; or why the lookups moved off port 53 under DoH) | +5 |

Cap total at 100 before extra credit; extra credit may push a strong submission above 100
per the instructor's policy, or offset losses elsewhere.

## Appendix — AI usage (no points, but affects others)

If the student used an LLM, they should include the prompt/output and **verify it against
their data**. **Reward verification:** if they caught the model in an error (e.g., a wrong
domain→company mapping), award the related item's points generously. **Penalize
unverifiable assertions:** an attribution that matches no pasted domain and that they
can't back up should lose the relevant item's evidence points even if it happens to be
correct.

---

### Scoring summary

| Item | Max |
|---|---|
| 1. Setup & method | 5 |
| 2. Unencrypted DNS Capture | 12 |
| 3. Domain → Company → First/Third-Party Table | 20 |
| 4. Who Can See Your Activity & Concerns | 18 |
| 5. Encrypted DNS Repeat | 12 |
| 6. Privacy Tradeoffs: ISP vs Resolver Trust, SNI, ECH | 20 |
| 7. Reflection & AI-verification | 13 |
| **Total** | **100** |
| 8. Extra credit: two-resolver or cross-site comparison | +10 |
