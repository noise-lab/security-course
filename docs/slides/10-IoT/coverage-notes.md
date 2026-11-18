# 10-IoT — instructor notes

## Status: mirrors the original pptx slide for slide

The Quarto deck now follows `ppt-archive/10-IoT.pptx` (146 slides) in order,
with the same claims, numbers, examples, and figures. Animation builds are
collapsed to one slide showing the final state, with the build order in the
`::: {.notes}` block. The pptx speaker notes are in the matching notes blocks
(lightly cleaned; the "More relax" self-reminders and pure to-do notes such as
"Add table of crawls" were not carried). 106 Quarto positions from the pptx, plus the 11 slides kept from the earlier
teaching-arc rebuild (framing, synthesis, the 2026 ACR vignette, discussion),
117 in all plus the YAML title slide. Per the instructor (Nov 18 2026) the
rule is additive: every pptx slide's content is present, and the existing
good material and current-events updates stay, integrated where they belong.

The archive is two talks back to back: the 2018 workshop talk on web attacks
plus the TV-tracking study (pptx 1–92) and a later job-talk retelling of IoT
Inspector and the TV crawler (pptx 93–146). Both are kept; the job-talk
framing slides (93–97, 117) and the cybercrime slide (96) are the obvious
cuts if the deck is too long for one meeting.

### pptx → Quarto mapping

| pptx | Quarto slide | note |
|---|---|---|
| 1 | IoT Inspector | whole slide as image |
| 2 | Initial Work: Connect and Monitor | |
| 3 | divider: Attack 1 | |
| 4 | Attack Steps: 1. Get Local IP | |
| 5–7 | Attack Steps: 2. Find Active Local Devices | build collapsed |
| 8–9 | Attack Steps: 3. Identify IoT Devices | build collapsed |
| 10–12 | Attack Steps: 3. What the MediaError Says | three browser slides as one table |
| 13 | Implications | |
| 14 | divider: Attack 2 | |
| 15 | DNS Rebinding | |
| 16–18 | Attack Steps: Rebinding, Steps 1–2 | build collapsed |
| 19–22 | Attack Steps: Rebinding, Steps 3–5 | build collapsed |
| 23 | Attack on Devices | |
| 24 | Demo: A User Visits a Site with a Malicious Script | video poster frame |
| 25 | Implications | |
| 26 | Moving Forward... | |
| 27 | divider: Privacy Challenges | |
| 28 | Difficult to Study Security/Privacy Systematically | |
| 29 | What Is IoT Inspector | |
| 30–31 | Download and Run IoT Inspector | two screenshots side by side |
| 32–33 | Bandwidth Graph for Each Device | two screenshots side by side |
| 34 | IoT Inspector Works Through ARP Spoofing | |
| 35 | Insight: IoTs Communicate with Whom | |
| 36 | Insight: Trackers/Ads on Roku TV | |
| 37 | Insight: Trackers/Ads on Roku TV (Bloomberg and CBSN) | |
| 38 | Insight: A Samsung Fridge Talks to Trackers | untitled in pptx; title from its note |
| 39 | Naming a Device in IoT Inspector | untitled in pptx |
| 40 | Summary of Insights | |
| 41 | Summary | |
| 42 | Streaming Devices | |
| 43 | Cord-Cutting: Two Primary Options | |
| 44 | Cord-Cutting: Household Penetration by Device | |
| 45 | Cord-Cutting: New Privacy Concerns | |
| 46 | Cord-Cutting: Device Share Among OTT Streaming Devices | |
| 47 | Hidden Data Flows | |
| 48 | Research Questions | |
| 49 | Results | |
| 50 | Challenges | Selenium icon not reproduced |
| 51 | Overview of Method | |
| 52–55 | System Design of Crawler | build collapsed |
| 56, 59, 60, 62 | Intercepting Traffic | build collapsed |
| 57–58 | Best-Effort Traffic Interception | identical slides |
| 61 | Rooting Fire TV | |
| 63–65, 67–69, 72 | Automatically Interacting with Channels | one screenshot set (65) stands for the per-step screenshots |
| 66, 70–71 | Automatically Interacting with Channels: Navigation and Playback | |
| 73 | (not reproduced) | stock photo with no text; its note is on Platform Privacy Options |
| 74 | Overview of Method: Collect Data | |
| 75–76 | Channel Lists | |
| 77 | Overview of Method: Analyze Data | |
| 78 | Tracking Domains | |
| 79 | 3rd-Party Trackers | |
| 80 | Previously Unknown Trackers | |
| 81 | Previously Unknown Trackers: Roku | |
| 82 | Device and Location Identifiers | |
| 83 | Device and Location Identifiers: Roku and Amazon | |
| 84 | Video Titles Shared with 3rd-Party Trackers | |
| 85 | Video Titles Shared with 3rd-Party Trackers: Roku | |
| 86 | Platform Privacy Options | |
| 87 | Platform Privacy Options: Roku and Amazon | drawn table rebuilt as Markdown |
| 88 | Implications | |
| 89 | Contributions | |
| 90 | Future Work | |
| 91 | Crawler and Data Released | |
| 92 | CBS Watches Me Watching CBS | |
| 93 | Consumers Face a Large Variety of Security and Privacy Threats | job-talk framing |
| 94 | Challenges for Empirically Studying Security & Privacy Threats | job-talk framing |
| 95 | Smart Home IoT Security & Privacy | job-talk framing |
| 96 | Studying the Cyber-Criminal Ecosystem | job-talk framing, not IoT |
| 97 | Focus of the Talk | job-talk framing |
| 98 | divider: Discovering Smart Home IoT Security & Privacy Threats in the Wild | |
| 99 | Many Smart Home IoT Devices, but Few Systematic Insights | |
| 100 | Challenges of Identifying IoT Security & Privacy Threats at Scale | |
| 101 | Crowdsourcing IoT Network Traffic at Scale | |
| 102–103 | IoT Inspector: A System to Crowdsource IoT Traffic at Scale | |
| 104–106 | IoT Inspector Uses ARP Spoofing to Capture Traffic | build collapsed |
| 107 | IoT Inspector Uses TCP Ack Numbers to Infer Traffic Rate | |
| 108 | IoT Inspector: Usage Statistics | |
| 109 | Design Goal: Generates Insights | |
| 110 | Screenshot of IoT Inspector from a User: Science Friday | |
| 111 | Screenshot of IoT Inspector from a User: The Washington Post | |
| 112 | Features of IoT Inspector | |
| 113 | Findings: Ineffective Encryption on IoT Devices | |
| 114 | Finding: Smart TVs Communicate with 3rd-Party Ad/Tracking Services | |
| 115 | Opportunities for Further Research | |
| 116 | Summary of IoT Inspector | |
| 117 | Summary of the Talk | |
| 118 | divider: Analyzing Tracking on Smart TVs | |
| 119 | Recap: Using IoT Inspector to Watch CBS | |
| 120–121 | Challenges of Analyzing Smart TV Traffic in Lab | build collapsed |
| 122 | Building a Smart TV Crawler | icon layout rebuilt as a table |
| 123 | Our Contributions | |
| 124 | Automating Interactions with Smart TVs | |
| 125 | TV Crawler Interacting with a Single Channel | |
| 126 | (not reproduced) | video |
| 127–128 | Challenges of Automatic Interactions with Channels | build collapsed |
| 129 | Detecting Video Playback | |
| 130–131 | Detecting Privacy Leaks | transition slide folded in |
| 132 | Man-in-the-Middling Traffic | |
| 133–134 | Findings: Ad/Tracking Companies | drawn tables rebuilt as Markdown |
| 135–136 | Findings: Sensitive Data Shared with Ad/Tracking Services | drawn tables rebuilt as Markdown |
| 137 | Privacy for Children? | |
| 138 | Findings: Privacy Leaks in Child-Directed Channels | |
| 139 | Examples of Persistent IDs in Child-Directed Channels: Amazon | |
| 140 | Examples of Persistent IDs in Child-Directed Channels: Roku | |
| 141 | DNS-Based Block Lists May Cause Some Channels to Crash | |
| 142 | Limited Ad Tracking (Roku) / No Interest-Based Ads (Amazon) | |
| 143–145 | Finding: Channels Still Shared Persistent IDs Under "Limited Ads" | build collapsed |
| 146 | Summary of Tracking on Smart TVs | |
| 72 | Automatically Interacting with Channels: Uninstall | the uninstall screenshot |

## Kept from the earlier teaching-arc rebuild (not in the pptx)

Slides: Why the Smart Home Is Hard; Two Questions That Drive the Lecture; Many
IoT Devices Run an Unauthenticated Web Server; Why These Attacks Matter;
Studying IoT Is Genuinely Hard; Findings from 50,000 Devices; The Opt-Outs
Don't Really Work; States Go After ACR: 2025–2026; Putting It
Together (EU CRA / AI Act / Cyber Trust Mark in its notes); Discussion. The
earlier rebuild's other slides duplicated pptx slides (same figure or same
bullets); their narration was merged into the matching pptx slide's notes
block, and the "Almost Every Channel Talks to a Known Tracker" bullets sit
under the 3rd-Party Trackers table. Nothing from the earlier version was
dropped.

### Graphics checklist (every pptx slide with pictures)

| pptx | what it shows | images/ file | note |
|---|---|---|---|
| 1 | abstract text + house photo | iot-inspector-abstract-house.png | |
| 2 | 2015 testbed diagram | initial-work-testbed.png | |
| 4 | attacker browser, local IP | webrtc-local-ip.png | |
| 5–7 | LAN scan timing diagram | lan-scan-timing.png | final state (7) |
| 8–9 | GET /setup.xml probe | get-setup-xml-probe.png | final state (9) |
| 10–12 | Chrome, Firefox, Safari, Edge logos | (skipped) | logos; strings are in the table |
| 16–22 | DNS rebinding exchange | dns-rebinding-short-ttl.png, dns-rebinding-rebound.png | short-TTL answer (17) and final state (22) |
| 23 | Google Home, Chromecast | google-home-chromecast.png | |
| 24 | demo video poster | web-attack-demo.png | |
| 28 | WaPo and Gizmodo clippings | anecdotal-reports-clippings.png | |
| 30, 31 | first-launch dialog, Discover Devices | iot-inspector-open-dialog.png, iot-inspector-discover-devices.png | |
| 32, 33 | bandwidth graph, endpoints table | iot-inspector-bandwidth-graph.png, iot-inspector-endpoints-table.png | |
| 34 | ARP-spoofing diagram (2018) | arp-spoofing-2018.png | |
| 35 | Orvibo socket endpoints | insight-communicate-with-whom.png | |
| 36, 37 | Roku Bloomberg / CBSN dashboards | roku-tv-trackers-bandwidth.png, roku-bloomberg-cbsn.png | |
| 38 | Samsung fridge dashboard | samsung-fridge-dashboard.png | |
| 39 | device-naming screen | iot-inspector-name-device.png | |
| 40 | database/bulb/camera icons | (skipped) | decorative |
| 42 | Fire TV and Roku | fire-tv-roku-devices.png | |
| 43 | paid-TV subscribers chart | paid-tv-subscribers-chart.png | |
| 44 | household penetration chart | household-penetration-by-device.png | |
| 46 | OTT device-share pie | ott-device-share.png | |
| 47 | Vizio / Roku headlines | hidden-data-flows-headlines.png | |
| 50 | crossed-out Selenium icon | (skipped) | decorative |
| 52–55 | crawler system diagram | crawler-system-design.png | final state (55) |
| 61 | Fire TV Stick board | fire-tv-stick-board.png | |
| 63 | Roku channel store | roku-home-screen.png | same screen as 125 |
| 64, 67, 68, 69 | launch and playback screenshots | (represented) | per-step illustrations; 65 and 72 stand for the set |
| 65 | navigation screenshots | channel-navigation-screens.png | |
| 72 | Roku remove-channel menu | roku-uninstall-screen.png | |
| 73 | stock photo | (skipped) | no content |
| 75 | Roku channel store | channel-store-screenshot.png | |
| 76 | Roku/Amazon privacy screens (small) | (covered) | same screens larger on 86 and 142; crop kept as channel-list-privacy-screens.png |
| 79 | tracker-domain tables | slide079_img142.png | |
| 81 | unknown-tracker table | previously-unknown-trackers-roku.png | |
| 83 | identifier leak tables | identifier-leak-counts.png | |
| 85 | video-title leak table | video-title-leaks-roku.png | |
| 86 | privacy option screens | platform-privacy-screens.png | |
| 87 | drawn counts table | (Markdown table) | same numbers |
| 92 | CBS on Roku dashboard | cbs-watching-cbs.png | |
| 93 | threat icons | consumer-threats-icons.png | |
| 94–97 | wild/lab framing diagrams | measurement-wild-lab.png, smart-home-wild-lab.png, cybercrime-wild-lab.png, talk-focus-wild-lab.png | |
| 99 | vendor logos + box | many-devices-few-insights.png | |
| 100 | approaches table | iot-study-approaches.png | |
| 101 | houses | crowdsourcing-vision-houses.png | |
| 102, 103, 108 | house diagram | iot-inspector-house.png | |
| 104–106 | ARP spoofing house | arp-spoof-house.png | final state (105); 106's router photo decorative |
| 107 | TCP ack diagram | tcp-ack-inference.png | |
| 109, 111 | Samsung TV activities | samsung-tv-device-activities.png | |
| 110 | Roku activities | slide110_img182.png | |
| 112 | callouts | (text) | |
| 113 | TLS table | weak-tls-by-vendor.png | |
| 114 | tracker shares | smart-tv-tracker-shares.png | |
| 115 | research icons + logos | research-opportunities.png | |
| 116 | summary icons | iot-inspector-summary-icons.png | |
| 117 | talk focus | talk-focus-wild-lab.png | |
| 119 | CBS dashboard + questions | cbs-roku-dashboard-questions.png | |
| 120–121 | tcpdump + SpotX capture | smart-tv-lab-tcpdump-spotx.png | final state (121) |
| 122, 123 | tool icons, logos | (Markdown table / text) | |
| 124 | crawler rig | tv-crawler-rig.png | |
| 125 | Roku home | roku-home-screen.png | |
| 126 | video | (skipped) | video |
| 127 | channel screenshot + play icon | (covered) | same screenshot as 121 |
| 129 | playback detection tree | audio-playback-oracle.png | |
| 130 | goals | (text) | |
| 131 | MITM icons | mitm-fake-account.png | |
| 132 | opportunistic MITM | mitm-opportunistic.png | |
| 133–136 | drawn tables | (Markdown tables) | same numbers |
| 137 | FTC headline | slide137_img234.png | |
| 138 | child-channel counts | child-channel-leaks.png | |
| 139, 140 | PBS Kids / Roblox / Nick leaks | child-channels-amazon-leaks.png, child-channels-roku-leaks.png | |
| 141 | Pi-hole crash | pihole-crash.png | |
| 142 | settings screens | platform-privacy-settings-screens.png | |
| 143–145 | limited-ads table | limited-ads-table.png | final state (145) |

## Next-year refresh notes

Only the 2026 vignette and the Putting It Together notes date. Check the Sony, Hisense, and TCL ACR cases, any new
state ACR statutes beyond Kentucky, EU CRA enforcement after the September
2026 reporting date, AI Act deadline changes, and whether the U.S. Cyber Trust
Mark has been mandated anywhere.
