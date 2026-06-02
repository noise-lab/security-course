## Internet Privacy

The goal of this assignment is to understand how your web activity can be
tracked using your DNS queries — and what does and does not change when you
turn on encrypted DNS. To do so, you will visit a website of your choice and
log all DNS queries made by your browser. Try to pick a popular website
(nytimes, facebook, reddit, etc.) that you have **not visited in a while**, so
your caches are cold and you see the full set of lookups a fresh page load
triggers. For simplicity, assume that all browser caches are empty; you can
also clear your browser cache manually (and flush the OS resolver cache).

> **New:** A companion [Wireshark Interpretation Guide](../../notes/wireshark-interpretation-guide.md)
> walks through how to read the traces you'll collect here — how to apply the
> `dns` display filter, pull out the queried name (`dns.qry.name`), see which
> resolver you're talking to, export *only* the DNS packets, and (in §5) what
> still leaks over HTTPS even when DNS is encrypted. Read it alongside this
> assignment.

### Grading & Rubric (100 points)

This rubric is shown up front so you know where to invest your effort. Labs are
graded primarily for thoughtful completion; points reward *understanding*, not polish.

| Component | Points | What earns full marks |
|---|---|---|
| **Setup & method** | 5 | You name the site you chose, confirm a cold cache, and describe how you captured (Wireshark `dns` filter, exported DNS-only pcap). |
| **Unencrypted DNS capture (with pasted queries)** | 12 | You capture real DNS traffic loading the page and **paste the list of distinct queried hostnames** (`dns.qry.name`) as text; the `dns.pcap` is included. |
| **Domain → company → first/third-party table (depth)** | 20 | You build a table mapping each distinct domain to its **owning company** and **first- vs third-party**, and report the **count of distinct domains** and **count of distinct companies** that saw a query. |
| **Who can see your activity & concerns** | 18 | You identify who sees unencrypted DNS (ISP / resolver / anyone on-path), explain *how* each company gained visibility, and give concrete privacy concerns that **differ by company**. |
| **Encrypted DNS repeat (with evidence)** | 12 | You enable DoH, repeat the load, and show the evidence (e.g., `dns` filter now shows nothing while 443/853 traffic to the resolver appears), and state who can see your activity now. |
| **Privacy tradeoffs: ISP-vs-resolver trust, SNI, ECH (depth)** | 20 | You analyze the **trust shift** to the resolver operator, explain that the hostname still leaks via **TLS SNI** (and the destination **IP**), and identify **ECH** as the fix for the SNI leak. |
| **Reflection & AI-verification** | 13 | You report what you *tried* (including dead ends), what surprised you in **your own** capture, and — if you used an LLM — at least one place you checked its claim against your data and what you found. |
| **Extra credit: two-resolver or cross-site comparison** | +10 | You go deeper with a second comparison and paste the evidence. See the stretch task below. |

Cite evidence by **pasted text** (the query-name list, the domain→company table) so a
grader can check it without opening your pcap. The reflection must be grounded in *your*
specific capture — generic prose that could describe anyone's run earns little credit.

### Tasks

1. **Set up and capture (cold cache).**
Pick a popular site you haven't visited recently. Clear your browser cache (and flush
the OS DNS cache if you can). Start Wireshark capturing **before** you load the page,
load the site once, then stop. Apply the `dns` display filter and **export only the DNS
packets** (File → Export Specified Packets → "Displayed") to `dns.pcap`. See
the [Wireshark Interpretation Guide](../../notes/wireshark-interpretation-guide.md) §6
for the exact filter and export steps.

2. **Capture the unencrypted DNS queries.**
With unencrypted DNS (port 53), the queried hostname is visible to anyone on path.
**Paste, as a text list, every distinct hostname you see in the `dns.qry.name` field**
during the page load. (Copy from Wireshark's packet detail or the `dns.qry.name`
column.) This list is the raw evidence for the rest of the lab — screenshots are welcome
but do not replace the pasted text.

3. **Build the domain → company → first/third-party table (depth).**
Take the distinct domains from Task 2 and group them by the **company that owns them**
(e.g., `doubleclick.net`, `googlesyndication.com`, `google-analytics.com`, and
`fonts.gstatic.com` all roll up to **Google/Alphabet**). For each domain, record whether
it is **first-party** (the site you actually visited, e.g. its own domain and CDN) or
**third-party** (trackers, ad networks, analytics, embedded widgets). Then report:
   - the **count of distinct domains** queried while loading the page, and
   - the **count of distinct companies** that saw at least one query.

   Present it as a table:

   | Domain | Owning company | First- or third-party |
   |---|---|---|
   | `www.example.com` | Example Inc. | first |
   | `doubleclick.net` | Google/Alphabet | third |
   | ... | ... | ... |

4. **Who can see your activity, and what concerns follow?**
Based on your unencrypted capture:
   - **Who can see** that you visited the site? Name the on-path observers (your **ISP**,
     anyone on the same Wi-Fi, the **resolver operator**) *and* the companies behind the
     queried domains. Explain *how* each gained visibility (a tracker domain was queried,
     the resolver answered the lookup, the ISP saw plaintext port-53 traffic, etc.).
   - What **different types of concerns** might you have about each — and why do they
     **differ by company** (e.g., an ad network building a profile vs. your ISP selling
     browsing data vs. a CDN that just serves fonts)?

5. **Enable encrypted DNS and repeat.**
[Enable encrypted DNS (DoH) in your browser](https://developers.cloudflare.com/1.1.1.1/encrypted-dns/dns-over-https/encrypted-dns-browsers),
clear caches again, and recapture the same site. Show your **evidence**: with DoH on, the
plain `dns` filter should show **nothing** for the page load, while traffic to the
resolver on `tcp.port == 443` (DoH) or `853` (DoT) appears instead. Paste a short note of
what you observed. Then state **who can see your activity now**.

6. **Privacy tradeoffs: trust shift, SNI, and ECH (depth).**
Encrypted DNS does **not** make you anonymous. Analyze the tradeoff carefully:
   - **Trust shift.** Your ISP no longer sees your DNS lookups — but the **resolver
     operator** (e.g., Cloudflare for `1.1.1.1`) now sees **every** name you look up. Who
     gained visibility, who lost it, and is centralizing all your lookups at one resolver
     a net win? Discuss.
   - **SNI still leaks.** Even with encrypted DNS, the hostname is sent **in plaintext**
     in the TLS **ClientHello** as the **SNI** extension, so an on-path observer (your
     ISP) still learns which site you're visiting. See the
     [Wireshark Interpretation Guide §5 "What still leaks over HTTPS"](../../notes/wireshark-interpretation-guide.md#5-what-still-leaks-over-https-the-important-part).
   - **Destination IP.** The server IP in the IP header is never encrypted and often maps
     back to the site (or its CDN). Explain what that still reveals.
   - **ECH.** What is **Encrypted Client Hello**, which of the leaks above does it close,
     and which does it *not* (the IP)?

7. **Reflection & tinkering (required).**
This is where you show the work is *yours*. In a short reflection (a few paragraphs):
   - What did you **try that didn't work** at first (a capture that caught nothing because
     the page was cached, a DoH setting that didn't take effect, a filter that hid the
     packets)? How did you fix it?
   - What **surprised you** in *your own* capture specifically — a tracker domain you
     didn't expect, how many distinct companies saw one page load, a first-party domain
     that turned out to be third-party-owned?
   - If you used an LLM anywhere, name **one claim you checked against your data** and say
     whether it held up (e.g., the model said `X.net` belongs to company Y — did your own
     check confirm it?).

8. **Stretch — go deeper on the tracker footprint (extra credit, +10).**
Anyone can capture one site once; show you can reason comparatively. Do **one** of these
and paste the evidence:
   - **Two resolvers.** Capture the same site's DNS twice — once on your **ISP's default
     resolver** and once on `1.1.1.1` (or `8.8.8.8`) — and analyze what changes about who
     sees your lookups.
   - **Cross-site comparison.** Capture two sites from **different categories** (e.g., a
     news site vs. a privacy-focused or government site) and compare their domain sets:
     how does the **third-party tracker footprint** differ, and what explains it?
   - **DoH evidence.** Demonstrate that with DoH enabled, a plain `dns` filter shows
     **nothing** for the load while traffic to the resolver on `443`/`853` appears —
     paste both filtered views as evidence and explain why the lookups moved.

> **Using AI (encouraged, with verification).** You may use an LLM to help map a domain
> to its owning company or interpret a packet you don't understand. If you do, **include
> the exchange in the appendix** and then **verify the model's claim against your own
> data** — point to the queried name, the WHOIS/ownership fact, or the packet that
> confirms (or contradicts) it. Submitting an attribution you can't defend will lose
> points; catching the model in an error (e.g., a wrong domain→company mapping) will earn
> full marks for that item.

> **Be ready to defend it.** Per the syllabus, we may ask you to reproduce or explain any
> part of this lab live (office hours, a pop quiz, or the exam) — e.g., "open this capture
> and show me the third-party domains," or "with DoH on, where did the lookups go?" Do the
> work so you can.

### Submission Instructions

Submit a single markdown report named **`privacy-report.md`** plus your DNS capture.
**Because your report is graded from its text, paste the required evidence *as text*
directly into the report** — the grader cannot open your `.pcap`. In particular, paste
the **list of distinct queried hostnames** and the **domain → company → party table**.
Screenshots are welcome but are corroboration, not a substitute for the pasted text.

Your report **must contain these headings, in this order** (they map one-to-one to the
rubric above):

```
# Internet Privacy Lab — <your name>

## 1. Setup
   (site you chose; confirmation of cold cache; how you captured and exported DNS-only)

## 2. Unencrypted DNS Capture
   - Pasted list of distinct queried hostnames (dns.qry.name) from the page load

## 3. Domain → Company → First/Third-Party Table
   - The table (domain | owning company | first/third party)
   - Count of distinct domains; count of distinct companies that saw a query

## 4. Who Can See Your Activity & Concerns
   - On-path observers (ISP, resolver, same-Wi-Fi) and the companies behind the domains
   - How each gained visibility; concerns that differ by company

## 5. Encrypted DNS Repeat
   - What you enabled (DoH); your evidence (plain `dns` shows nothing; 443/853 to resolver)
   - Who can see your activity now

## 6. Privacy Tradeoffs: ISP vs Resolver Trust, SNI, ECH
   - Trust shift to the resolver operator
   - Hostname still leaks via SNI; destination IP; ECH as the SNI fix (not the IP)

## 7. Reflection & Tinkering
   - What you tried that didn't work; what surprised you in YOUR capture;
     one AI claim you verified against your data

## 8. (Extra credit) Two-Resolver or Cross-Site Comparison
   - Which variant you did; pasted evidence; what differed and why

## Appendix: AI usage (if any)
   - Prompts, model output, and your verification against your data
```

Also include:

- `dns.pcap` — a capture containing **only** your DNS queries (filter `dns`, then export
  Displayed packets)

Push the report and the capture to your private GitHub repository (do not push a zip file).
