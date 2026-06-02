# XX-Election — instructor notes

## Current-events updates made (point 2)
- **AI deepfake robocall (Jan 2024, NH primary)** as the freshest hook (vignette on the
  disinformation slide): AI clone of President Biden's voice told Democrats not to vote;
  cost the creator ~$1 and 20 minutes; FCC ruled AI-voiced robocalls illegal under the
  TCPA and pursued a multi-million-dollar penalty. Verified via NPR, electioninnovation.org,
  Vermont SOS.
- **2024 paper-ballot adoption**: replaced the 2016 Verified Voting map's "still many
  paperless states" framing with the 2024 reality — ~98% of votes on voter-verifiable
  paper-based systems (Verified Voting / Brennan Center).
- **Risk-limiting audits, 2024–2025**: added a dated, concrete RLA slide — Georgia's
  statewide RLA across all 159 counties at a 5% risk limit after the Nov 2024 general
  election; Virginia RLAs after 2024 and 2025 elections. Verified via Georgia SOS,
  Virginia Dept. of Elections, NCSL, Brennan Center.
- **"Apocalypse that wasn't" nuance** (in speaker notes): post-2024 analysis (Harvard Ash
  Center) found the dominant 2024 misinformation narratives were not AI-driven —
  positions AI as an accelerant, not the whole threat. Keeps the deck from overstating.
- Dropped/contextualized dated artifacts: punch cards (none in federal elections since
  2014), lever machines (none since ~2010), the 2016 recount framing — kept as history,
  not current state.

## Suggested missing coverage on broad themes (point 3)
- **End-to-end verifiable (E2E-V) voting**: ElectionGuard, STAR-Vote, Benaloh-style
  cryptographic receipts — the serious answer to "can I verify my vote counted?" that the
  blockchain slide gestures at but doesn't develop. Strong contrast with blockchain.
- **Voter registration & election-infrastructure security**: the 2016 attacks were largely
  against *registration databases and election websites*, not tabulators. CISA's role,
  designation of election systems as critical infrastructure (2017), and EI-ISAC deserve a
  slide — arguably the higher-likelihood threat than vote-flipping.
- **Do voters actually verify BMD printouts?** Appel/DeMillo/Stark research showing most
  voters don't check; implications for whether a BMD trail is truly software-independent.
- **Mail/absentee voting at scale**: signature verification, ballot tracking, drop boxes —
  became dominant in 2020 and is a major attack/availability surface barely touched here.
- **The legitimacy/contestation problem**: 2020 false-fraud claims, Jan 6, and the gap
  between "technically auditable" and "politically accepted." Connects the audit material
  to the disinformation material.
- **Foreign influence operations** beyond deepfakes: coordinated inauthentic behavior,
  platform takedowns (Meta/Google/OpenAI threat reports), and the role of content
  moderation — links this deck to the course's content-moderation lecture.
- **Coercion-resistance / remote voting tradeoffs**: vote-by-phone for disabled and
  overseas (UOCAVA) voters; the unresolved tension between accessibility and the secret
  ballot.

## Curated images
- **Used:** `slide005_img003.png` (Dewey Defeats Truman — motivates evidence-based
  elections); `slide012_img013.png` (Florida 2000 butterfly ballot — HAVA backstory);
  `slide041_img033.png` (Diebold "vote-stealing control panel" demo — memorable attack);
  `slide048_img041.png` (ballot-marking devices); `slide044_img034.png` (Verified Voting
  paper-vs-DRE map, updated verbally to 2024).
- **Dropped:** generic candidate/headline photos (slides 2,3,6,7,8,10,11), lever-machine
  and punch-card photos (slides 29–33,37,38 — covered in the timeline bullet without
  decorative duplicates), DRE/VVPAT and audit photos that were redundant with the chosen
  attack and BMD images (slides 45,46,47,49,50,51), and the Augur/blockchain logo
  (slide57 — concept covered in text). All clip-art and decorative headshots dropped per
  template.

## Source
- Rebuilt from `_source-extract.md` (57 slides) consolidated to 21 slides. No matching
  Meeting in `agenda.md` (election security was not an indexed agenda topic), so built
  from the source extract + domain knowledge + 2024–2025 web-verified current events.
