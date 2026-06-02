## Public Key Infrastructure

The goal of this assignment is to understand why unencrypted HTTP is not
secure and how HTTPS addresses some of the vulnerabilities of HTTP. To
this end, complete the following tasks and answer the accompanying
questions. 

> **New:** A companion [Wireshark Interpretation Guide](../../notes/wireshark-interpretation-guide.md)
> walks through how to read the traces you'll collect here — the TCP handshake,
> following an HTTP stream, the TLS handshake records, and what metadata still
> leaks over HTTPS. Read it alongside this assignment.

### Grading & Rubric (100 points)

This rubric is shown up front so you know where to invest your effort. Labs are
graded primarily for thoughtful completion; points reward *understanding*, not polish.

| Component | Points | What earns full marks |
|---|---|---|
| **Local web server + HTTP capture** | 10 | Server runs; you capture real HTTP traffic between client and server and include the pcap. |
| **Why HTTP is insecure (with trace evidence)** | 18 | You explain eavesdropping *and* point to specific packets — the request line, headers, and body visible in your HTTP stream. |
| **HTTPS upgrade (self-signed cert)** | 18 | Certificate generated, added to trusted roots, server restarted on HTTPS; HTTPS pcap included. You answer why a CA won't issue a cert for your local server. |
| **HTTP vs. HTTPS trace comparison** | 14 | You contrast the two traces and show the payload is encrypted under TLS. |
| **Wireshark interpretation (depth)** | 15 | You correctly identify the TCP handshake and the TLS handshake records (ClientHello / ServerHello / Certificate), citing packet numbers. |
| **Metadata-leakage analysis (depth)** | 10 | You identify what an eavesdropper *still* learns over HTTPS (server IP, SNI, certificate, packet sizes/timing) and how that connects to DNS and ECH. |
| **Reflection & AI-verification** | 15 | You report what you *tried* (including dead ends), what surprised you in **your own** capture, and — if you used an LLM — at least one place you checked its claim against the bytes and what you found. |
| **Extra credit: decrypt your own TLS** | +10 | Using `SSLKEYLOGFILE`, decrypt your own HTTPS capture in Wireshark and paste the now-readable application data. See the stretch task below. |

Cite packets by **number and field** so a grader can find your evidence. The reflection
must be grounded in *your* specific capture — generic prose that could describe anyone's
run earns little credit.

### Tasks

1. **Host a local web server**.  
There are many services for this. If you\'ve done this before, you\'re free to
use the service/software that you\'re comfortable with. If you\'re feeling
adventurous, try setting up an [nginx](https://www.nginx.com/) or
[Apache](https://httpd.apache.org/). Both are used extensively in enterprise
and professional settings. Another option is to use Python's [HTTP server
class](https://docs.python.org/3/library/http.server.html)


2. **Identify why HTTP is not secure**.  
(spoiler: it is unencrypted). In your write-up, explain how an
eavesdropper can \"sniff\" web traffic between a client and HTTP server
to see what is being communicated (including which resources are being
fetched and the contents of the resources). In addition, use
[Wireshark](https://www.wireshark.org/)
to capture network traffic between your local web server
and a local client**. **Feel free to include screenshots from Wireshark
in your explanation. 

3. **Create a self-signed certificate and upgrade your web server to
HTTPS**.  
(a) Why can\'t you obtain an SSL certificate for your local web
server from a certificate authority? 
Generate an SSL certificate for your web server, add the certificate to
your list of locally trusted roots, and restart the web server with the
certificate. All communications with your server should now be secured.
Once again, include a network trace (captured using Wireshark) and
comment on the difference between the contents of HTTP and HTTPS (TLS)
traffic. 

4. **Interpret the handshakes (depth)**.  
Using the [Wireshark Interpretation Guide](../../notes/wireshark-interpretation-guide.md):
   - In your **HTTP** capture, find and **paste the text of the TCP three-way
     handshake** (the `[SYN]`, `[SYN, ACK]`, `[ACK]` lines from the Info column,
     with packet numbers).
   - In your **HTTPS** capture, find the TLS handshake and **paste the packet-detail
     text** for the **ClientHello** and **ServerHello** (the lines naming the
     handshake type and, for the ClientHello, the `server_name` / SNI extension).
   - Briefly explain, in your own words, what each of these packets does.

5. **What still leaks over HTTPS? (depth)**.  
Even after the upgrade, an on-path eavesdropper still learns several things.
Using evidence from your HTTPS trace, answer:
   - Which fields reveal the **hostname** even though the payload is encrypted?
     (Point to the SNI in the ClientHello, and the destination **IP** in the IP header.)
   - What does the eavesdropper learn from **packet sizes and timing** alone?
   - What role does **DNS** play in leaking the hostname *before* the TLS connection
     even starts? (This connects directly to the Internet Privacy lab.)
   - What is **ECH (Encrypted Client Hello)**, and which of the leaks above would it
     close?

6. **Reflection & tinkering (required)**.  
This is where you show the work is *yours*. In a short reflection (a few paragraphs):
   - What did you **try that didn't work** at first (a capture that caught nothing, a
     cert the browser rejected, a filter that hid the packets)? How did you fix it?
   - What **surprised you** in *your own* capture specifically — a header you didn't
     expect, how much (or little) TLS hid, a domain you didn't realize you contacted?
   - If you used an LLM anywhere, name **one claim you checked against the bytes** and
     say whether it held up.

7. **Stretch — decrypt your own TLS (extra credit, +10)**.  
Anyone can *say* TLS is encrypted; prove you can pierce it when you hold the keys. Set
the `SSLKEYLOGFILE` environment variable before launching your browser/client, point
Wireshark at that key log file (Preferences → Protocols → TLS → *(Pre)-Master-Secret log
filename*), and re-open your HTTPS capture. Wireshark will now decrypt the session.
**Paste the recovered, now-readable HTTP request/response** and explain *why* having the
key log lets you read traffic an on-path eavesdropper cannot. This requires real
tinkering and is self-evidently done or not — a good way to go beyond a one-shot answer.

> **Using AI (encouraged, with verification).** You may use an LLM to help interpret a
> packet you don't understand. If you do, **include the exchange in the appendix** and
> then **verify the model's claim against the actual packet** — point to the field that
> confirms (or contradicts) it. Submitting an explanation you can't defend against the
> bytes will lose points; catching the model in an error will earn full marks for that
> item.

> **Be ready to defend it.** Per the syllabus, we may ask you to reproduce or explain any
> part of this lab live (office hours, a pop quiz, or the exam) — e.g., "open this capture
> and find the SNI." Do the work so you can.

### Submission Instructions

Submit a single markdown report named **`pki-report.md`** plus your two packet
captures. **Because your report is graded from its text, paste the required evidence
*as text* directly into the report** (copy from Wireshark's Follow-Stream and
packet-detail panes). Screenshots are welcome but are corroboration, not a substitute
for the pasted text.

Your report **must contain these headings, in this order** (they map one-to-one to the
rubric above):

```
# PKI Lab — <your name>

## 1. Web Server Setup
   (what you ran; how the client reached it)

## 2. Why HTTP Is Insecure
   - Pasted HTTP request line + headers + a snippet of the body (from Follow HTTP Stream)
   - Your explanation of what an eavesdropper sees

## 3. HTTPS Upgrade
   - How you generated and trusted the cert
   - Why a public CA won't issue a cert for your local server

## 4. HTTP vs. HTTPS Comparison
   - Side-by-side: readable HTTP payload vs. encrypted TLS Application Data

## 5. Handshake Interpretation
   - Pasted TCP three-way handshake (with packet numbers)
   - Pasted ClientHello + ServerHello detail (with SNI)
   - Your explanation of each

## 6. What Still Leaks Over HTTPS
   - Hostname (SNI + IP), sizes/timing, DNS, and ECH

## 7. Reflection & Tinkering
   - What you tried that didn't work; what surprised you in YOUR capture;
     one AI claim you verified against the bytes

## 8. (Extra credit) Decrypted TLS
   - How you set up SSLKEYLOGFILE; the recovered plaintext; why the key log defeats encryption

## Appendix: AI usage (if any)
   - Prompts, model output, and your verification against the packets
```

Also include:

- `http.pcap` — a capture containing your HTTP traffic
- `https.pcap` — a capture containing your HTTPS traffic

Push the report and both captures to your private GitHub repository (do not push a
zip file).
