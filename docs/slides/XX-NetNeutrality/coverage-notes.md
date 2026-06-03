# XX-NetNeutrality — instructor notes

## Current-events updates made (point 2)
- **Headline hook (vignette):** Added the **Sixth Circuit's Jan 2, 2025 ruling** in
  *Ohio Telecom Ass'n v. FCC*, which vacated the FCC's 2024 Title II net-neutrality
  order. Verified via Davis Wright Tremaine, Gibson Dunn, and Congressional Research
  Service (LSB11264) summaries.
- **Loper Bright connection:** The court applied *Loper Bright Enterprises v. Raimondo*
  (2024, ended Chevron deference) and decided *itself* that broadband is a Title I
  "information service," not a Title II "telecommunications service." This is the most
  important conceptual update — it reframes net neutrality as a statutory-authority /
  administrative-law problem, and ties this deck to the same theme appearing in the
  privacy and AI lectures.
- **State patchwork:** Added the California **SB 822** story and the **Ninth Circuit's**
  *ACA Connects v. Bonta* decision upholding it (ISPs dropped their challenge). Framed
  states as the de facto national floor in the absence of federal rules.
- **History corrected to a clean timeline:** 2015 order → 2017/2018 repeal → 2024
  reinstatement → Jan 2025 vacatur. The old deck only knew the 2015 order ("invalidated").
- **International framing updated:** kept the India 2018 example (still accurate and a
  good zero-rating/Free Basics teaching case) and noted the EU's 2016 open-internet rules.

## Suggested missing coverage on broad themes (point 3)
- **Zero-rating** deserves its own slide. It's the most live consumer-facing issue
  (T-Mobile Binge On, carrier "free" video/music tiers, Free Basics) and the one place
  California went *beyond* the bright-line rules. Good for a debate.
- **Net neutrality vs. content moderation / censorship.** Students conflate "ISPs must
  carry all lawful traffic" with "platforms must carry all speech." Worth one slide
  distinguishing common-carriage of the pipe from First Amendment / Section 230 debates
  about edge platforms (ties to the content-moderation lecture).
- **Loper Bright / major-questions doctrine** as a cross-cutting mini-lecture. The same
  administrative-law shift is reshaping privacy, AI, and environmental regulation; a
  reusable 2-slide explainer would pay off across the course.
- **Measurement methodology.** The M-Lab interconnection data is a great chance to teach
  how you *measure* a neutrality violation (active measurement, NDT, DSCP markings) — a
  natural fit given the course's measurement/security framing.
- **5G network slicing and "specialized services."** A current technical wrinkle: slicing
  is paid-prioritization-by-design at the architecture level. Worth a forward-looking slide.
- **Privacy angle.** The 2015 Title II order also implied ISP **privacy** obligations
  (later undone by Congress via the CRA in 2017). Connects directly to the privacy-law deck.

## Next-year refresh notes

Refresh the dated content below per `../TEMPLATE.md` → "Annual current-events refresh" (web-verify; swap only for something fresher and confirmed). Items placed in prior refreshes that will age:

- Headline hook (vignette)
- Loper Bright connection
- State patchwork
- History corrected to a clean timeline
- International framing updated
- Flag any stronger alternative vignette you find but choose not to use yet.

## Curated images
- **Used:** `slide011_img012.png` (M-Lab throughput-across-Cogent plot — the empirical core);
  `slide012_img013.png` (two-theories interconnection diagram); `slide003_img001.png`
  (India open-internet news excerpt — international contrast).
- **Dropped:** `slide005_img009.png` and `slide014_img015.png` (John Oliver "Net
  Neutrality" video stills — decorative); `slide005`/Wikipedia "Criticism" text screenshot
  (unreadable wall of text); `slide009_img010.png` (duplicate of the Oliver still);
  `slide010_img011.png` (latency time-series, redundant with the cleaner throughput plot);
  `slide013_img014.png` (Cogent/M-Lab email screenshot — referenced verbally in notes
  instead); `slide004_*` / `slide016_*` (duplicate/clip-art image sets).

## Source
- Rebuilt from `_source-extract.md` (17 slides) + domain knowledge. `agenda.md` has no
  dedicated net-neutrality meeting (Topic 12 "Broadband Infrastructure" was removed per
  agenda.md line 902), so the deck leans on the source extract, the broadband/censorship
  course themes, and verified 2025–2026 current events.
