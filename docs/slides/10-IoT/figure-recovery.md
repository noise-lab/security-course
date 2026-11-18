# Figure recovery: 10-IoT

Source: `docs/slides/ppt-archive/10-IoT.pptx`, 146 slides, rendered 2026-10-16
(headless LibreOffice, 110 dpi contact sheet, 220 dpi captures). The archive
is two talks back to back: the 2018 workshop version (slides 1–91, serif
"Attack Steps" layout) and a later job-talk version (92–146, blue title bars)
that redraws most of the same diagrams more cleanly. Where both exist, the
redraw was captured. No pen-ink parts in this deck. Budget was about ten
figures, so the triage below is deliberately selective.

| pptx slide | class | target Quarto slide | figure name | notes |
|---|---|---|---|---|
| 1 | skip | | | abstract text with a house photo |
| 2 | media | | | device product shots arranged around a hub; dropped by the earlier curation |
| 3 | skip | | | divider "Attack 1" |
| 4–6 | skip | | | build-up steps of the slide-7 diagram |
| 7 | keep | new, after "Attack 1: Discover Local Devices from a Web Page" | lan-scan-timing.png | step text (shape 327) stripped; no animation |
| 8–9 | skip | | | build steps toward the GET /setup.xml probe; text slide covers it |
| 10–12 | skip | | | per-browser MediaError strings with browser logos; already in bullets and notes |
| 13 | skip | | | implications bullets |
| 14–15 | skip | | | divider and DNS-rebinding definition text |
| 16 | skip | | | bare browser and device, build base |
| 17 | keep | new, after "Attack 2: DNS Rebinding to Control Devices" | dns-rebinding-short-ttl.png | HTTP overlay (shapes 443, 447, 448) stripped so the short-TTL answer is visible |
| 18–21 | skip | | | intermediate build states of the same exchange |
| 22 | keep | same new slide as 17 | dns-rebinding-rebound.png | final state: GET /setup.xml straight to the device, HTTP 200 |
| 23 | media | | | Google Home and Chromecast photos; attack list already in bullets |
| 24 | skip | | | dated demo screenshot |
| 25–27 | skip | | | bullets and dividers |
| 28 | media | | | Gizmodo clippings, someone else's |
| 29–33 | skip | | | bullets; dated 2018 IoT Inspector preview screenshots |
| 34 | skip | | | ARP-spoofing diagram, superseded by the redraw on 105 |
| 35–39 | media | | | dashboard screenshots; the deck already embeds slide110_img182 |
| 40–41 | skip | | | summary bullets |
| 42 | media | | | Fire TV and Roku product shots |
| 43–44 | skip | | | cord-cutting charts (comScore, Nielsen), third-party figures |
| 45 | skip | | | bullets |
| 46 | skip | | | Parks Associates pie chart, third-party |
| 47 | skip | | | Vizio and Roku news headlines, dated |
| 48–51 | skip | | | research questions, results and challenge bullets |
| 52–55 | skip | | | crawler system diagram, superseded by the redraw on 124 |
| 56–62 | skip | | | interception bullets; 61 is a Fire TV board photo (media) |
| 63–72 | skip | | | per-step crawler screenshots, consolidated into one text slide by the rebuild |
| 73 | skip | | | stock photo |
| 74–78 | skip | | | method bullets, channel-list screenshots |
| 79 | media | | | tracker table, already embedded as slide079_img142 |
| 80–81 | skip | | | previously-unknown-tracker list; covered in notes |
| 82–85 | skip | | | identifier and video-title leak counts; the percentage versions on 135–136 are the better tables and the bullets already carry the headline numbers |
| 86 | skip | | | platform settings screenshots |
| 87 | skip | | | limited-ads counts, superseded by the percentage version on 145 |
| 88–91 | skip | | | implications, contributions, future work, release pointers |
| 92 | media | | | CBS-on-Roku dashboard screenshot |
| 93–97 | skip | | | job-talk framing loop (in the wild / in the lab), no mechanism |
| 98 | skip | | | blank |
| 99 | skip | | | vendor logos |
| 100 | keep | new, after "Studying IoT Is Genuinely Hard" | iot-study-approaches.png | final build state (all marks visible) |
| 101–103 | skip | | | vision and design-goal versions of the house diagram |
| 104 | skip | | | same as 105 with the camera as the spoofed device |
| 105 | keep | new, after "How It Sees the Traffic: ARP Spoofing" | arp-spoof-house.png | final state, both callouts |
| 106 | skip | | | 105 plus a router photo for the caveat already in the bullets |
| 107 | keep | new, after the ARP slide | tcp-ack-inference.png | final state, both braces |
| 108 | skip | | | usage statistics text |
| 109–111 | media | | | dashboard screenshots with press quotes; slide110_img182 already embedded |
| 112 | skip | | | design-goal callouts |
| 113 | keep | new, after "Findings from 50,000 Devices" | weak-tls-by-vendor.png | no animation; vendor logos are row labels in our own table |
| 114 | skip | | | smart-TV tracker percentages with tracker logos; the 14.9% is already in the notes |
| 115–118 | skip | | | future-work icons, university logos, framing, blank |
| 119–121 | media | | | CBS dashboard and SpotX capture screenshots |
| 122–123 | skip | | | design goals and contributions |
| 124 | keep | new, after "Building a Smart-TV Crawler" | tv-crawler-rig.png | "Content Placeholder 2" (design-goals text) stripped |
| 125–128 | skip | | | channel screenshots and key-sequence text |
| 129 | keep | new, second slide after "Building a Smart-TV Crawler" | audio-playback-oracle.png | final state |
| 130–131 | skip | | | goals; MITM icons without mechanism |
| 132 | skip | | | per-platform MITM text with small icons; content already in the crawler bullets |
| 133–136 | skip | | | tracker and identifier percentage tables; 133 duplicates the embedded slide079_img142, 136's numbers are in the bullets. Would be the next to add if the budget grows |
| 137 | media | | | FTC headline, already embedded as slide137_img234 |
| 138 | keep | new, after "Children's Privacy: COPPA Enters the Picture" | child-channel-leaks.png | no animation |
| 139–140 | media | | | PBS Kids and Nick listings with leaked-ID callouts; dropped as screenshots |
| 141 | skip | | | Pi-hole crash icon diagram, little content |
| 142 | media | | | Roku and Amazon settings screenshots |
| 143–144 | skip | | | build-up of 145 |
| 145 | keep | new, after "The Opt-Outs Don't Really Work" | limited-ads-table.png | no animation |
| 146 | skip | | | summary |

## Captured images

- `images/iot-study-approaches.png` (2720×1356) — source: ppt-archive/10-IoT.pptx slide 100, final build state
- `images/lan-scan-timing.png` (1957×778) — source: ppt-archive/10-IoT.pptx slide 7, shape "Google Shape;327;p52" (step text) stripped
- `images/dns-rebinding-short-ttl.png` (1949×984) — source: ppt-archive/10-IoT.pptx slide 17, shapes 443, 447, 448 (HTTP exchange overlay) stripped
- `images/dns-rebinding-rebound.png` (1949×984) — source: ppt-archive/10-IoT.pptx slide 22, final build state
- `images/arp-spoof-house.png` (1797×1053) — source: ppt-archive/10-IoT.pptx slide 105, final build state
- `images/tcp-ack-inference.png` (2833×1144) — source: ppt-archive/10-IoT.pptx slide 107, final build state
- `images/weak-tls-by-vendor.png` (2736×1182) — source: ppt-archive/10-IoT.pptx slide 113
- `images/tv-crawler-rig.png` (1883×1041) — source: ppt-archive/10-IoT.pptx slide 124, "Content Placeholder 2" stripped
- `images/audio-playback-oracle.png` (2203×724) — source: ppt-archive/10-IoT.pptx slide 129, final build state
- `images/child-channel-leaks.png` (2393×1198) — source: ppt-archive/10-IoT.pptx slide 138
- `images/limited-ads-table.png` (2688×927) — source: ppt-archive/10-IoT.pptx slide 145

## Captured 2026-11-18 for the slide-for-slide conform (whole-content crops at 220 dpi, downscaled to 1500 px wide)

- `images/iot-inspector-abstract-house.png` (1500×833) — source: ppt-archive/10-IoT.pptx slide 1, final state, title and slide number excluded
- `images/initial-work-testbed.png` (1500×674) — source: ppt-archive/10-IoT.pptx slide 2, final state, title and slide number excluded
- `images/webrtc-local-ip.png` (477×552) — source: ppt-archive/10-IoT.pptx slide 4, final state, title and slide number excluded
- `images/get-setup-xml-probe.png` (1500×467) — source: ppt-archive/10-IoT.pptx slide 9, final state, title and slide number excluded
- `images/google-home-chromecast.png` (975×471) — source: ppt-archive/10-IoT.pptx slide 23, final state, title and slide number excluded
- `images/web-attack-demo.png` (1500×844) — source: ppt-archive/10-IoT.pptx slide 24, final state, title and slide number excluded
- `images/anecdotal-reports-clippings.png` (1127×983) — source: ppt-archive/10-IoT.pptx slide 28, final state, title and slide number excluded
- `images/iot-inspector-open-dialog.png` (1500×1034) — source: ppt-archive/10-IoT.pptx slide 30, final state, title and slide number excluded
- `images/iot-inspector-discover-devices.png` (1500×850) — source: ppt-archive/10-IoT.pptx slide 31, final state, title and slide number excluded
- `images/iot-inspector-bandwidth-graph.png` (1500×891) — source: ppt-archive/10-IoT.pptx slide 32, final state, title and slide number excluded
- `images/iot-inspector-endpoints-table.png` (1500×807) — source: ppt-archive/10-IoT.pptx slide 33, final state, title and slide number excluded
- `images/arp-spoofing-2018.png` (1500×662) — source: ppt-archive/10-IoT.pptx slide 34, final state, title and slide number excluded
- `images/insight-communicate-with-whom.png` (1500×446) — source: ppt-archive/10-IoT.pptx slide 35, final state, title and slide number excluded
- `images/roku-tv-trackers-bandwidth.png` (1500×757) — source: ppt-archive/10-IoT.pptx slide 36, final state, title and slide number excluded
- `images/roku-bloomberg-cbsn.png` (1500×605) — source: ppt-archive/10-IoT.pptx slide 37, final state, title and slide number excluded
- `images/samsung-fridge-dashboard.png` (1500×844) — source: ppt-archive/10-IoT.pptx slide 38, final state, title and slide number excluded
- `images/iot-inspector-name-device.png` (1500×847) — source: ppt-archive/10-IoT.pptx slide 39, final state, title and slide number excluded
- `images/fire-tv-roku-devices.png` (1500×674) — source: ppt-archive/10-IoT.pptx slide 42, final state, title and slide number excluded
- `images/paid-tv-subscribers-chart.png` (1482×883) — source: ppt-archive/10-IoT.pptx slide 43, final state, title and slide number excluded
- `images/household-penetration-by-device.png` (1500×648) — source: ppt-archive/10-IoT.pptx slide 44, final state, title and slide number excluded
- `images/ott-device-share.png` (1500×1139) — source: ppt-archive/10-IoT.pptx slide 46, final state, title and slide number excluded
- `images/hidden-data-flows-headlines.png` (1500×577) — source: ppt-archive/10-IoT.pptx slide 47, final state, title and slide number excluded
- `images/crawler-system-design.png` (1500×786) — source: ppt-archive/10-IoT.pptx slide 55, final state, title and slide number excluded
- `images/fire-tv-stick-board.png` (1050×671) — source: ppt-archive/10-IoT.pptx slide 61, final state, title and slide number excluded
- `images/channel-navigation-screens.png` (1500×868) — source: ppt-archive/10-IoT.pptx slide 65, final state, title and slide number excluded
- `images/channel-store-screenshot.png` (948×579) — source: ppt-archive/10-IoT.pptx slide 75, final state, title and slide number excluded
- `images/previously-unknown-trackers-roku.png` (1244×1091) — source: ppt-archive/10-IoT.pptx slide 81, final state, title and slide number excluded
- `images/identifier-leak-counts.png` (1500×779) — source: ppt-archive/10-IoT.pptx slide 83, final state, title and slide number excluded
- `images/video-title-leaks-roku.png` (1500×470) — source: ppt-archive/10-IoT.pptx slide 85, final state, title and slide number excluded
- `images/platform-privacy-screens.png` (1500×428) — source: ppt-archive/10-IoT.pptx slide 86, final state, title and slide number excluded
- `images/cbs-watching-cbs.png` (1500×849) — source: ppt-archive/10-IoT.pptx slide 92, final state, title and slide number excluded
- `images/consumer-threats-icons.png` (1500×1036) — source: ppt-archive/10-IoT.pptx slide 93, final state, title and slide number excluded
- `images/measurement-wild-lab.png` (1500×772) — source: ppt-archive/10-IoT.pptx slide 94, final state, title and slide number excluded
- `images/smart-home-wild-lab.png` (1500×779) — source: ppt-archive/10-IoT.pptx slide 95, final state, title and slide number excluded
- `images/cybercrime-wild-lab.png` (1500×781) — source: ppt-archive/10-IoT.pptx slide 96, final state, title and slide number excluded
- `images/talk-focus-wild-lab.png` (1500×459) — source: ppt-archive/10-IoT.pptx slide 97, final state, title and slide number excluded
- `images/many-devices-few-insights.png` (1500×692) — source: ppt-archive/10-IoT.pptx slide 99, final state, title and slide number excluded
- `images/crowdsourcing-vision-houses.png` (1479×800) — source: ppt-archive/10-IoT.pptx slide 101, final state, title and slide number excluded
- `images/iot-inspector-house.png` (1500×1162) — source: ppt-archive/10-IoT.pptx slide 102, final state, title and slide number excluded
- `images/samsung-tv-device-activities.png` (1500×775) — source: ppt-archive/10-IoT.pptx slide 109, final state, title and slide number excluded
- `images/smart-tv-tracker-shares.png` (1500×806) — source: ppt-archive/10-IoT.pptx slide 114, final state, title and slide number excluded
- `images/research-opportunities.png` (1500×658) — source: ppt-archive/10-IoT.pptx slide 115, final state, title and slide number excluded
- `images/iot-inspector-summary-icons.png` (1500×573) — source: ppt-archive/10-IoT.pptx slide 116, final state, title and slide number excluded
- `images/cbs-roku-dashboard-questions.png` (1500×849) — source: ppt-archive/10-IoT.pptx slide 119, final state, title and slide number excluded
- `images/smart-tv-lab-tcpdump-spotx.png` (1500×805) — source: ppt-archive/10-IoT.pptx slide 121, final state, title and slide number excluded
- `images/roku-home-screen.png` (1500×1006) — source: ppt-archive/10-IoT.pptx slide 125, final state, title and slide number excluded
- `images/mitm-fake-account.png` (1318×945) — source: ppt-archive/10-IoT.pptx slide 131, final state, title and slide number excluded
- `images/mitm-opportunistic.png` (1500×771) — source: ppt-archive/10-IoT.pptx slide 132, final state, title and slide number excluded
- `images/child-channels-amazon-leaks.png` (1500×758) — source: ppt-archive/10-IoT.pptx slide 139, final state, title and slide number excluded
- `images/child-channels-roku-leaks.png` (1500×759) — source: ppt-archive/10-IoT.pptx slide 140, final state, title and slide number excluded
- `images/pihole-crash.png` (907×1078) — source: ppt-archive/10-IoT.pptx slide 141, final state, title and slide number excluded
- `images/platform-privacy-settings-screens.png` (1500×712) — source: ppt-archive/10-IoT.pptx slide 142, final state, title and slide number excluded
