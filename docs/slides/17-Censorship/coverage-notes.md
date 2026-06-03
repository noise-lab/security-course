# 17-Censorship — instructor notes

## Current-events updates made (point 2)
- **Fresh vignette (Access Now #KeepItOn, March 2026):** 2025 was the worst year on
  record for deliberate internet shutdowns — **313 shutdowns across 52 countries** (up
  from 304 in 2024 and 289 in 2023), with an estimated **$19.7B** in global economic
  losses; **75 shutdowns in 33 countries** were still ongoing entering 2026. Verify
  against the report PDF before class:
  https://www.accessnow.org/internet-shutdowns-2025/ and
  https://www.accessnow.org/wp-content/uploads/2026/03/KeepItOn-Internet-Shutdowns-2025-Annual-Report.pdf
- **Blacklisting → whitelisting pivot (Iran, Russia):** added as the key conceptual
  update. Whitelisting inverts the default (block everything, allow only approved
  "socially significant" services) — a censor's structural answer to circumvention.
- **Measurement tools modernized:** replaced the dated Herdict reference (project has
  ended) with the now-standard OONI, Censored Planet, Google Transparency Report, and
  Access Now/#KeepItOn.
- **Protocol updates:** noted SNI-based filtering and the erosion of the SNI/DNS vantage
  point by encrypted DNS (DoH/DoT) and Encrypted Client Hello (ECH) — links to the
  DNS-security lecture.
- **Generative-AI flooding:** added a note that LLMs make plausible sock-puppet/astroturf
  content nearly free, scaling the "flooding" tactic.
- Kept the historical timeline (Great Firewall, Egypt 2011, Great Cannon 2015, Cloudflare/
  Daily Stormer 2017) as teaching history rather than "current" examples.

## Suggested missing coverage on broad themes (point 3)
- **The China case study in depth:** Great Firewall mechanics (RST injection, DNS
  poisoning, active probing of circumvention servers) and the Great Cannon as an
  offensive injection weapon (GitHub/GreatFire 2015). Source deck only names these.
- **VPN crackdowns and the circumvention arms race:** 2024–2025 tightening of VPN access
  (Russia app-store removals, Apple removing VPN apps in Russia; periodic China/India
  pressure). Good concrete "friction" example.
- **Platform-as-censor and Section 230 vs. moderation:** sharpen the "is moderation
  censorship?" question and connect explicitly to the Content Moderation debate listed in
  agenda.md (Meeting 7) — the deck currently only gestures at it.
- **Domestic / democratic-context control:** age-verification mandates, "lawful but
  awful" takedown pressure, and platform deplatforming as soft censorship in the US/EU —
  the source leans heavily on authoritarian examples.
- **Encrypted transport vs. filtering:** a slide pairing ECH/DoH adoption against SNI
  filtering would make the technical arms race concrete and tie to the DNS/web lectures.
- **Empirical pushback on filter bubbles:** the deck cites the Zuckerberg quote; worth
  noting the mixed empirical evidence (e.g., 2023 Science papers) so students don't
  overstate the effect.
- **Note:** agenda.md has no standalone censorship lecture section — it appears as a
  theme (Overview) and via the Content Moderation debate. This deck is rebuilt from the
  source extract + domain knowledge; if censorship is taught as its own meeting, add a
  matching agenda section.

## Next-year refresh notes

Refresh the dated content below per `../TEMPLATE.md` → "Annual current-events refresh" (web-verify; swap only for something fresher and confirmed). Items placed in prior refreshes that will age:

- Fresh vignette (Access Now #KeepItOn, March 2026)
- Blacklisting → whitelisting pivot (Iran, Russia)
- Measurement tools modernized
- Protocol updates
- Generative-AI flooding
- Flag any stronger alternative vignette you find but choose not to use yet.

## Curated images
- **Used:** `slide007_img005.png` (Roberts information pyramid — core teaching figure);
  `slide012_img015.png` (Google Transparency Egypt-2011 traffic plot — real data);
  `slide027_img033.png` (VPN tunnel schematic — instructive despite clip-art styling);
  `slide030_img036.png` (decoy/refraction routing diagram — clean attack/defense flow);
  `slide029_img035.png` (Weibo homophone substitution diagram — excellent concept figure).
- **Dropped:** generic person/clip-art avatars (`slide014_img016/017/018`,
  `slide009_*`, `slide020_*`); `.wmf` censor icons (`slide014_img019/020`, not renderable);
  decorative news-screenshot clutter (`slide021_*`, `slide034_*`, `slide036_*`,
  `slide037_*`, `slide039_*`, `slide041_img047`, `slide046_img048`, `slide048_img049`) —
  low-resolution or redundant with text; `slide005/006/011/018/026` map/screenshots were
  redundant given the live OONI/Access Now framing now in the vignette.

## Source
- Rebuilt from `_source-extract.md` (49 slides) + domain knowledge. agenda.md has no
  dedicated censorship meeting (theme appears in Overview and the Meeting 7 Content
  Moderation debate); consolidated to a lean deck on the friction/flooding/fear thesis.
