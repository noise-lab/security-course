# Reading Wireshark Output: A Field Guide
## How to make sense of a packet capture (and what it can — and can't — tell an eavesdropper)

This guide is for the **PKI** and **Internet Privacy** labs. Several students asked
to learn how to actually *interpret* a Wireshark trace rather than just collect one.
Use it as a reference while you work.

> **AI note.** You may use an LLM to help interpret a capture (e.g., paste a packet
> summary and ask what a field means). That is encouraged — but the point of the
> course is that you can *verify* the answer against the bytes in front of you. When
> a model tells you "this is a TLS ClientHello," confirm it: find the record, the
> handshake type, the SNI. Don't submit an explanation you can't defend.

---

## 1. The display filter bar (your most important tool)

The bar at the top of Wireshark filters which packets are *shown* (not which are
captured). A few you will use constantly:

| Filter | Shows |
|---|---|
| `http` | Plaintext HTTP requests/responses |
| `tls` | TLS records (the encrypted web traffic) |
| `dns` | DNS queries and responses |
| `tcp.port == 443` | All traffic to/from the HTTPS port |
| `ip.addr == 93.184.216.34` | Everything to/from one host |
| `tcp.stream eq 0` | One specific TCP connection (see §3) |
| `dns && ip.addr == 1.1.1.1` | DNS to/from Cloudflare's resolver |

Combine with `&&` (and), `||` (or), `!` (not). Example:
`tls.handshake.type == 1` shows only TLS ClientHello messages.

---

## 2. The TCP three-way handshake

Every TCP connection (and therefore every HTTP/HTTPS session) opens with three
packets. Spotting them tells you where a conversation *begins*:

```
Client → Server   SYN              "let's talk"
Server → Client   SYN, ACK         "sure, let's talk"
Client → Server   ACK              "great"
```

In the packet list, look at the **Info** column for `[SYN]`, `[SYN, ACK]`, `[ACK]`.
The connection closes with `[FIN, ACK]` packets (or an abrupt `[RST]`).

**What an eavesdropper learns just from this** — even before any data flows, and even
if the data is encrypted: the **client IP**, the **server IP**, the **port** (80 vs
443 → HTTP vs HTTPS), and the **timing** of the connection.

---

## 3. Following an HTTP stream (plaintext)

Right-click any HTTP packet → **Follow → HTTP Stream** (or **TCP Stream**). Wireshark
reassembles the whole conversation and color-codes it (client request in one color,
server response in another). With plain HTTP you will see, in the clear:

- The **request line**: `GET /secret-page.html HTTP/1.1`
- **Headers**: `Host:`, `User-Agent:`, `Cookie:`, `Referer:`
- The **full response body** — the actual HTML, images, JSON, etc.

This is the core lesson of the PKI lab: with HTTP, an eavesdropper on the path (your
ISP, someone on the same Wi-Fi, a compromised router) sees *exactly which resource you
requested and its entire contents*, including any cookies or credentials sent in the
clear.

Useful HTTP filters: `http.request.method == "GET"`, `http.host contains "example"`,
`http.cookie`.

---

## 4. The TLS handshake (what HTTPS adds)

Switch your capture to the HTTPS version of the site and filter on `tls`. A TLS 1.2/1.3
session opens with a handshake. The records you should be able to identify:

| Record | `tls.handshake.type` | What it carries |
|---|---|---|
| **ClientHello** | 1 | Cipher suites the client supports, **SNI** (the hostname!), supported TLS versions |
| **ServerHello** | 2 | The chosen cipher suite, server's TLS version |
| **Certificate** | 11 | The server's certificate chain *(visible in TLS 1.2; encrypted in TLS 1.3)* |
| **Key exchange / Finished** | — | Establishes the shared session key |
| **Application Data** | — | The actual HTTP request/response — **now encrypted** |

Try to **Follow → TLS Stream** on an HTTPS connection. Contrast it with §3: instead of
readable HTML you get **Application Data** records full of ciphertext. The eavesdropper
can no longer read the URL path, headers, cookies, or body.

---

## 5. What *still* leaks over HTTPS (the important part)

HTTPS encrypts the *content*, not the *fact* of the connection. Even with a perfect
TLS session, an on-path observer can still see:

1. **The server IP address** (from the IP header — never encrypted).
2. **The hostname via SNI.** In the ClientHello, the **Server Name Indication**
   extension carries the hostname (`www.example.com`) *in plaintext* so the server
   knows which certificate to present. Find it with `tls.handshake.extensions_server_name`.
   This is how an ISP can still tell *which sites* you visit even over HTTPS.
   - **ECH (Encrypted Client Hello)** is the fix — it encrypts the SNI. Most traffic
     does not use it yet. (Relevant to the Privacy lab's encrypted-DNS discussion.)
3. **The certificate** (in TLS 1.2) — which also names the host.
4. **Traffic metadata**: packet sizes, counts, and timing. These leak more than people
   expect — "website fingerprinting" attacks identify pages from size/timing patterns
   alone.
5. **DNS** — unless you use encrypted DNS, the lookup that *precedes* the connection
   reveals the hostname in plaintext (this is the entire premise of the Privacy lab).

So the honest summary: **HTTPS hides *what you said*, not *who you talked to*.**

---

## 6. DNS packets (for the Privacy lab)

Filter on `dns`. Each lookup is a **query** (`Standard query 0x1a2b A www.example.com`)
followed by a **response** with the answer records. Things to pull out:

- The **queried name** (`dns.qry.name`) — the hostname you're resolving.
- The **resolver** you're talking to (the destination IP of the query: your ISP's
  resolver, `8.8.8.8`, `1.1.1.1`, etc.).
- **Unencrypted DNS (port 53)**: the queried hostname is fully visible to anyone on
  path. To export only DNS for submission: filter `dns`, then **File → Export Specified
  Packets** with "Displayed" selected.
- **Encrypted DNS (DoH/DoT)**: you will *not* see `dns` packets at all — the lookups
  ride inside TLS to the resolver (DoH uses `tcp.port == 443` to a resolver like
  `1.1.1.1`; DoT uses port 853). The hostname is now hidden from your ISP — but the
  **resolver operator** (e.g., Cloudflare) sees every name you look up. That trust
  shift is the heart of the encrypted-DNS tradeoff.

---

## 7. A quick workflow checklist

1. Start the capture **before** you load the page; stop it right after.
2. Apply a display filter (`http`, `tls`, or `dns`) to cut the noise.
3. Use **Follow Stream** to read a whole conversation at once.
4. For HTTP: identify the request line, headers, and body.
5. For HTTPS: identify the handshake records and confirm the payload is encrypted, then
   list what metadata *still* leaks.
6. Export only the packets you need (**File → Export Specified Packets → Displayed**).
7. When you cite a packet in your write-up, give the **packet number** and the field
   you're pointing at so a grader can find it.

---

## Further reading

- Wireshark User's Guide: <https://www.wireshark.org/docs/wsug_html/>
- Wireshark display filter reference: <https://www.wireshark.org/docs/dfref/>
- RFC 8446 (TLS 1.3) §2 for the handshake overview
- The course readings on PKI and tracking
