# Figure recovery: 03-KeyManagement

Source: `docs/slides/ppt-archive/03-KeyManagement.pptx`, 77 slides (26 and 27 hidden in the deck), rendered 2026-10-16 with `pptx-figures.py` (LibreOffice headless, 110 dpi contact sheet, 220 dpi captures). No slide in this deck animates, and none has pen ink.

The Quarto deck (31 slides before this pass) was rebuilt from the text extract and already embeds the useful media (`slideNNN_imgNNN.*`, see `coverage-notes.md`). The legacy-cipher and RSA-math block (pptx 6–17, 23–24, 42–47) is out of scope per the Meeting 2 agenda, so nothing from it is recovered.

| pptx slide | class | target Quarto slide | figure name | notes |
|---|---|---|---|---|
| 1 | skip | | | title |
| 2 | skip | | | Alice/Bob clip art with network cloud; decorative |
| 3 | skip | | | same picture with E(k,m) label; clip art, superseded by slide 4's drawn version |
| 4 | keep | new, "Confidentiality vs. Integrity, in Pictures" (after "The Setup") | symmetric-confidentiality-eve.png | Alice/Bob boxes, shared k at both ends, c := E_k(p), Eve tapping the wire |
| 5 | keep | same new slide | mac-integrity-mallory.png | Alice/Mallory/Bob, m with tag v := f_k(m), Bob checks f_k(m'); the "(Hash-based) MAC" prose below the group is cropped out |
| 6–17 | skip | | | encryption game, Caesar, Vigenère, Enigma, OTP, PRG/stream ciphers, block ciphers: cut per agenda |
| 18 | skip | | | divider |
| 19 | skip | | | "N people" broadcast model; clip-art people around a cloud, decorative |
| 20–22 | skip | | | text, D-H history photos (media not extracted; portraits, no teaching value beyond the names) |
| 23–24 | skip | | | multiplicative groups, mod-7 exercise: cut per agenda |
| 25 | keep | new, "Diffie-Hellman in One Picture" (after "How Diffie-Hellman Works") | dh-exchange.png | full exchange: secrets x/y, g^x and g^y crossing the dashed network line, both computations, HMAC-of-z box |
| 26 (hidden) | keep | new, "Eve vs. Mallory on the Same Exchange" (after "D-H's Big Weakness") | dh-passive-eavesdropper.png | Eve taps both values; "Eve knows: p, g, g^x, g^y" line kept; title descenders painted out |
| 27 (hidden) | keep | same new slide | dh-mitm.png | Mallory with secrets u and v, two independent exchanges |
| 28–33, 36–38 | skip | | | bullets |
| 34–35 | media | "Two Use Cases, One Idea" | | Stallings diagrams, already embedded |
| 39–41 | media | | | GCHQ aerial, RSA paper scan, RSA portrait; dropped in coverage-notes (RSA math cut) |
| 42–47 | skip | | | RSA derivation and modular exponentiation: cut per agenda |
| 48–53 | skip | | | bullets (49 is the Diffie–Hellman quote, already on "The Problem with Public Keys") |
| 54 | media | | | old deep CA hierarchy picture; deliberately dropped as superseded by the flat multi-root framing |
| 55–60, 63–67 | media | | | Keychain, cert chain, cert detail, lock screenshot, Bugzilla/CNNIC screenshots, Gogo headline; the useful ones are already embedded, the rest dropped per coverage-notes |
| 61–62, 68–70, 72–73, 75–76 | skip | | | bullets, EV guidelines scan, badssl list, divider |
| 71 | media | "Key Pinning and the SSH Model" | | SSH host-key warning, already embedded |
| 74 | media | "Expiration and Revocation" | | Heartbleed logo, already embedded |
| 77 | media | | | Apple/FBI news clipping; dropped, debate kept as text |

Captured:

- `images/symmetric-confidentiality-eve.png` (1551×272) — source: ppt-archive/03-KeyManagement.pptx slide 4, Group 23, no builds
- `images/mac-integrity-mallory.png` (1885×136) — source: ppt-archive/03-KeyManagement.pptx slide 5, Group 15 minus the "e.g." caption line, no builds
- `images/dh-exchange.png` (2326×1137) — source: ppt-archive/03-KeyManagement.pptx slide 25, steps 2–3 region incl. dashed connector and HMAC box, no builds
- `images/dh-passive-eavesdropper.png` (2263×492) — source: ppt-archive/03-KeyManagement.pptx slide 26 (hidden), Group 28 plus the "Eve knows" line; title descenders whited out
- `images/dh-mitm.png` (2569×274) — source: ppt-archive/03-KeyManagement.pptx slide 27 (hidden), Group 26, no builds
