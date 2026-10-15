## Agenda — Autumn 2026 (Chicago)

One three-hour meeting per week, Wednesday evenings. Notes are reconstructed from the class recordings after each meeting; where a recording was partly inaudible the entry says so rather than guessing. Items marked **Midterm flag** were called out in class as likely exam material.

### Meeting 1 (Wed Sep 30)

No debate this week. First half: course mechanics. Second half: threat modeling, *Reflections on Trusting Trust*, *Why Cryptosystems Fail*, and the start of ethics.

* **Course mechanics (syllabus walk-through)**
    * Everything lives on the course web page (a GitHub page, also embedded in Canvas). Canvas is otherwise used as little as possible. The repository can be cloned for a local copy of slides, readings, and past exams
    * Past midterms and finals are all posted with solutions, along with the prompt used to draft each exam. Exams are drafted from the prompt plus this agenda file, so you can generate your own practice exams the same way
    * This agenda file is the record of what was actually covered. There is more in the slides than we will get through, and exams do not ask about material that is not here. Debates are not captured in the recording but may still be asked about
    * Meeting format ("a lecture in six acts"): housekeeping and reading questions, first topic, break, Oxford-style debate, break, second topic
    * No prerequisites
    * **Lab assignments:** four, possibly five (decision to be announced). Due Fridays; dates are in the pinned sheet in Slack and will not move. Weighted lightly on purpose: do them and understand them, because the exams ask about them
        * Assignment 1: stand up a web server with a certificate (public key infrastructure) and capture packet traces
        * Assignment 2: build an app that uses OAuth
        * Assignment 3: web tracking and privacy, what data is collected as you browse
        * Later assignments: how platforms detect copyrighted material in uploads; how large language models decide which prompts to accept and what to return
    * **Debates:** one per week from next week on, Oxford style, done in teams, and a large share of the grade. Sign-up sheet is linked in Slack
        * A resolution is read, the room votes, both sides argue, there is a back-and-forth and audience questions, then the room votes again to see whether anyone changed their mind. About 45 to 60 minutes
        * Next week's resolution: *Companies should be liable for damages incurred from data breaches if there was a known vulnerability in the software used by the company that led to the breach*
    * **Midterm: Wednesday November 4 (week 6), in class.** Typically covers Meetings 1 through 5. Final is in week 9 and focuses on the later topics
    * Exams are not timed. They are written for about an hour and you may take the whole period; a debate usually runs in the second half of the midterm meeting
    * Accommodations page: `sds.html` on the course site
    * **Late policy:** 96 late hours for the term, tracked from commit timestamps, no need to ask. Deadlines are not extended. Real emergencies (medical, family) are handled separately; talk to me. If an assignment turns out to be broken, everyone gets additional late hours rather than a moved deadline
    * **Readings:** read before class when you can; nothing is collected. A Slack channel will take reading questions to steer the lecture
    * In-class activities (for example a key-signing party) are planned for some weeks and may be dropped for time
    * **Course staff:** TAs are Kyle MacMillan, Tajveer Singh Dhesi, and Lan Gao. Grading is largely automated, so TA time goes to office hours; use them
    * **Communication:** post in the public Slack channels first. For private matters, DM the whole staff rather than one person. Email is the fastest way to reach me for something urgent
    * **Collaboration and AI policy:** work with whoever and whatever helps you learn, including coding agents, and **acknowledge what you did**. Do not submit work you do not understand. Unacknowledged copying is the one thing that leads to a conversation
    * **Debate norms:** respect differing viewpoints and approach your own and others' opinions with curiosity. The instructor does not offer personal opinions on contested questions, to avoid putting a thumb on the scale

* **Why this course exists**
    * A security course that crosses into law and public policy; originally created for the computer science and public policy overlap
    * First half is classic systems and network security. Second half moves up the stack to privacy, policy, and law
    * Motivation from the instructor's own work: policymakers often lack technical grounding, and expert testimony in litigation (for example *Sony v. Cox*, decided by the Supreme Court this year; revisited in the copyright unit)
    * Career paths that use this material: regulators (Federal Communications Commission, Federal Trade Commission), state and city technology policy, public-interest advocacy, law

* **Threat modeling (Overview)**
    * An attacker is anything that actively tries to make a system misbehave; attacks are frequent, large-scale, and increasingly automated and agent-based
    * Running example: the IDScan breach, in which about 153 million driver's license scans held by a data aggregator were compromised and sold on the dark web. Leads directly into next week's debate
    * The four questions of a threat model:
        * **Assets:** what is being protected? Data, money, reputation, availability of a service
        * **Properties:** what must hold? *Confidentiality* (only authorized parties can read it; example: end-to-end encrypted messages) and *integrity* (it has not been altered or forged; example: a fake "midterm canceled" announcement in Slack). A bank transaction needs both
        * **Adversaries:** who is the attacker and what do they want? A classmate, a criminal, a nation-state have different motives
        * **Capabilities:** what can the attacker do, and what is in scope? Stolen credentials, a software vulnerability, insider access
    * AI agents change the threat model. Example from class: an agent, not a person, posted the TA announcement to Slack using stored authorization tokens. That is a new attack surface: whoever obtains the tokens can act as the instructor
    * Costs and benefits: every design choice (including using agents at all) trades risk for utility
    * Security mindset: to defend a system, think like the person trying to break it
    * **Midterm flag:** given a described attack, model the threat (assets, properties, adversaries, capabilities)
    * **Midterm flag:** how does a threat model change once AI agents hold credentials and act on a user's behalf?

* **Reading: Thompson, "Reflections on Trusting Trust" (1984)**
    * Ken Thompson wrote Unix; this was his Turing Award lecture. Two pages; the one reading to read if you read only one
    * Question: how much do you have to trust to claim a program has no backdoor?
    * The construction: a compiler that inserts a backdoor into a target program, and also inserts that same behavior into any new compiler it compiles. Delete the malicious source. Every line of source you can read is now clean, and the backdoor still ships in the binary
    * "You can't trust code that you did not totally create yourself," and nobody creates all of their own code. The same argument continues downward through the operating system, the hardware, and the supply chain
    * Chain of trust: for any system the chain stops somewhere, at a root of trust you simply accept. Certificates in Assignment 1 are the same idea
    * Modern instances: a widely used library nobody thinks about (the xkcd "dependency" picture); the backdoor slipped into build scripts of a compression library used by SSH. Reading the source is not enough; the build process is part of what you trust
    * **Midterm flag:** for a given system, what is the chain of trust and where does it stop?

* **Reading: Anderson, "Why Cryptosystems Fail" (1993)**
    * When a secure system fails it is almost never the math. It is the implementation, the operations, or the people
    * 1990s UK banking: the customer had to prove fraud, so banks had no incentive to look for their own weaknesses. The burden has since shifted toward providers, which changes behavior. Same incentive question as next week's debate
    * Failure modes from the paper and class:
        * **Insider attacks:** a clerk issues an extra card. Related term: lateral movement, using one foothold inside to gain more
        * **Outsider attacks:** shoulder-surfing a PIN; copying magnetic-stripe data to a blank card
        * **Replay attacks:** capture a valid authorization message and send it again. The same concern applies to authorization tokens (OAuth, Assignment 2)
        * **Fake terminals and skimmers:** complete fake ATMs; a keypad overlay that records the PIN while the real keypad still works
        * **Weak PINs:** schemes that reduce the number of possible PINs; issuing the same PIN to many customers
        * **Key management:** secret keys committed to public repositories (a recent Stripe key leak was discussed); passwords on sticky notes
        * **Operations:** procedures are the weakest link, and now that includes procedures carried out by agents
        * **Usability:** vendors overestimate users' patience and sophistication. Passwords are the classic case; locking yourself out of two-factor authentication because the backup codes were never saved is a current one
    * A vocabulary for reading about any breach: was it a software vulnerability, a dependency or infrastructure problem, a credential or key-management failure, a human-factors attack such as phishing, or an insider?
    * **Midterm flag:** take a breach from the news and identify what actually failed

* **Vulnerabilities and exploits (Equifax, 2017)**
    * Equifax ran web software (Apache Struts) with a publicly known vulnerability and did not patch it. Not a cryptographic failure
    * A **vulnerability** is a flaw that could let an attacker do something they should not. An **exploit** is the working attack that uses it. Many known vulnerabilities never get an exploit; it depends on attacker cost and benefit
    * Vulnerabilities vary in severity. A **remote** vulnerability can be used over the network without prior access to the machine, which is why it is the most dangerous kind
    * Known vulnerabilities are catalogued publicly (the CVE database)
    * Patching is not free, especially for critical systems, which is part of why known vulnerabilities stay unpatched
    * A **zero-day** is an exploit for a vulnerability that was not publicly known beforehand, so defenders had zero days to fix it
    * The Federal Trade Commission has warned that failing to remediate known vulnerabilities can violate the law; the trend is toward a duty of care for companies and developers. More in next week's debate

* **Ethics (Lecture 2, begun)**
    * Motivating problem, vulnerability disclosure: you find a flaw. Whom do you tell, and when? A common approach is to withhold public disclosure until a patch exists. What if the vendor will not fix it? (Example: university researchers who found remotely exploitable flaws in cars.)
    * **Midterm flag:** the ethics of vulnerability disclosure
    * Tuskegee: participants were not told they had syphilis and treatment was withheld. Exposed in the 1970s; the reason institutional review boards exist
    * Cases in computing:
        * "Hypocrite commits": researchers submitted deliberately flawed patches to the Linux kernel to test its review process
        * Carna botnet (2012): an anonymous researcher logged into home routers that still had default passwords, installed measurement software, and published the resulting data set. Was collecting it acceptable? May others use data they did not collect? **Midterm flag**
        * The instructor's own measurement study that caused browsers to request third-party content, including from sites that may be blocked in the user's country; now a case study in the Salganik reading
        * Facebook emotional contagion (2014): news feeds were altered to study mood without asking users. Where is the line between routine product testing and manipulating people?
    * The purpose of an ethical framework is not to reach one correct answer. It is to give a shared way to reason toward a decision; two people can use the same framework and disagree
    * Two broad philosophical approaches: **consequentialism** (judge an action by its outcomes; the ends can justify the means) and **deontology** (judge an action by duties and rules, regardless of outcome)
    * **The four principles** (three from the Belmont Report, one added by the Menlo Report):
        * **Respect for persons:** people are autonomous; hence informed consent, meaning asked beforehand and actually told the risks
        * **Beneficence:** weigh risks against benefits. Not "do no harm," which would rule out surgery
        * **Justice:** risks and benefits should be distributed fairly across groups. Tuskegee put the risk on one group for the benefit of others
        * **Respect for law and public interest:** added for computer security research. Flagged in class as the awkward one: security research often requires breaking terms of service or risking the Computer Fraud and Abuse Act, and not every law is a good law. Has appeared on past midterms
    * Not finished. Remaining ethics material, including AI bots on Reddit, is held for next meeting if time allows

* **For next week**
    * Read Thompson and Anderson if you have not, and the ethics chapter from Salganik, *Bit by Bit*
    * Create your private GitHub repository, add `feamster` as a collaborator, and fill out the intake form
    * Sign up for a debate. Next week's debate is on data breach liability

### Meeting 2 (Wed Oct 7)

*Both lecture segments written from their recordings. The debate is not recorded (it is the students' session) and is logged by resolution, format, and the one twist raised from the floor.*

* **Housekeeping**
    * Assignment 1 (PKI) is out. **Do the version on the course website**, not the one in the public GitHub template, which is older and shorter; the website version asks you to reflect on what a coding agent produces. The GitHub copy will be updated to match
    * Dates are pinned in Slack as the "assignment deadlines" sheet; the first deadline is **Fri Oct 23**, and dates will not move. A calendar (ICS) file may follow
    * Office hours: the instructor's are by sign-up, Tuesday evenings from next week (this week, Wednesday evening). TAs will announce theirs now that there is an assignment; a TA channel will be created
    * Expect exam questions about the assignments; today's first hour is the background for Assignment 1
* **Lecture: Key Management and Public Key Infrastructure** (topic 3)
    * Review of the two properties from Meeting 1: confidentiality (keeping messages unreadable to others) and integrity (an adversary cannot alter a message in transit). **Midterm flag:** these definitions
    * The math has been settled since the 1970s; managing keys is the hard, unsolved part of security, and its inventors also won the Turing Award
    * Cast: Alice and Bob, Eve the eavesdropper (passive), Mallory the active attacker
    * **Symmetric cryptography:** one shared key encrypts and decrypts. Fast, and what carries almost all real traffic eventually. The catch is that both sides must already share the key without Eve learning it: that is the key-distribution problem. Also pairwise keys do not scale (n² keys for n parties). Related questions: distribution, revocation, knowing a key really belongs to its claimed owner
    * **Midterm flag (true/false style):** a browser connecting to a web site uses *both* symmetric and asymmetric cryptography. Algorithm names will not be asked
    * **Diffie-Hellman (1976):** public generator and large prime; Alice raises the generator to her secret exponent modulo the prime and sends the result, Bob does the same; each raises the other's value to their own secret, and both arrive at the same shared key. Eve sees both transmitted values but cannot recover the secrets because the discrete-logarithm problem is hard with well-chosen numbers. Worked example of modular exponentiation on the board. The math will not be on the exam
    * Quantum computing makes discrete log and factoring easy, which is what "quantum breaks crypto" and "post-quantum crypto" refer to
    * **Man-in-the-middle:** Mallory on the path replaces each side's transmitted value with her own, ends up sharing one key with Alice and another with Bob, and neither notices. **Correction: the diagram drawn on the board was wrong.** The box read K = g^(x'y') mod p, which is a value only Mallory could form. There are two keys: Alice ends up with g^(xy') mod p (her x, Mallory's y') and Bob with g^(x'y) mod p (Mallory's x', his y). Mallory knows both; Alice and Bob each think theirs is shared with the other. The conclusion is unchanged: Mallory decrypts, reads, and re-encrypts everything. Example in practice: the first-connection host-key prompt in SSH, which only works if you can confirm the fingerprint out of band. MITM is itself a key-management problem: you need some trusted channel to know who is on the other end. Trusting Trust again. **Midterm flag:** given a different protocol, explain how a man-in-the-middle attack would work
    * **Asymmetric (public-key) cryptography** (RSA, 1977, correction: "early 1980s" was said in class; its inventors also won the Turing Award): a key pair, one published, one secret. Door analogy: anyone can lock, only the owner can unlock
        * Confidentiality: encrypt with the recipient's public key; only the private key decrypts
        * Integrity: sign with your private key; anyone verifies with your public key
        * **Midterm flag (multiple choice):** which key does Alice use to encrypt to Bob, and which does she use to sign
    * Public-key crypto is slow and does not replace symmetric crypto, and it does not solve distribution: how do you know whose public key this is? Posting "here is my public key" anywhere can be impersonated. **Midterm flag:** what is wrong with publishing a public key on a web page or in a chat
    * **Certificates:** a signed statement binding an identity to a public key, with subject, issuer, and validity period. Self-signed certificates prove nothing by themselves (Assignment 1 has you make one). A certificate authority signs the server's certificate; the chain runs up to a root; roots ship with the operating system or browser, hundreds of them, and any one malicious root breaks the whole chain. **Midterm flag:** what is a certificate
    * Live demo: a news site's certificate (domain validation: only the domain name is attested), its issuer, the issuer's public key, and the matching root certificate found in the operating system's keychain. Then a bank's certificate (extended validation: the organization's legal identity and registration number, traceable to a state business registry)
    * Why certificates expire: limits the damage from a compromised key. Subject alternative names let one certificate cover many related hostnames
    * **When roots go bad:** compromised or shady certificate authorities, a rogue root once shipped in a browser, an in-flight Wi-Fi provider that intercepted TLS with its own certificate, and corporate laptops with a company root installed (assume the company can read your traffic; use a VPN)
    * Defenses: certificate transparency (public append-only logs of every issued certificate; detects, does not prevent); key pinning (remember the key you saw before, as SSH does with `known_hosts`); expiration and revocation; much shorter-lived certificates
    * Anecdote: intercepting a device's encrypted traffic with a man-in-the-middle proxy requires installing your own root on the device; that used to be routine and some apps now detect it and refuse. Possible future assignment
    * Not covered: the key-signing (web of trust) hands-on, for time
* **Break** (15 minutes)
* **Debate: Data Breaches** (not recorded)
    * Resolution: *Companies should be held liable for damages incurred from data breaches if there was a known vulnerability in the software used by the company that led to the breach*
    * Oxford style: opening poll (thumbs up/down on the resolution posted in Slack), affirmative opening, negative response, affirmative reply, audience questions, closing poll. Six students signed up, three per side
    * The debate took place as scheduled. One twist raised from the floor by the instructor: **how does liability shift when an AI agent is in the loop?** If an agent introduces the vulnerability (writes the code, misconfigures the system) or takes the action that leads to the breach, who is liable: the company that deployed it, the agent's vendor, the person who prompted it, or nobody? **Midterm flag:** apply the resolution to a breach caused by an autonomous agent
* **Break** (10 minutes)
* **Lecture: Modern Authentication and Access Control** (topic 4, first part; about 20 minutes)
    * What access control is for: protecting users from each other (shared servers, shared documents), applications from each other (your browser should not touch your music app), and the system from the network (firewalls)
    * The hard part is that you want the walls to be porous: apps that talk to each other (chat to code hosting, video calls to calendars, an instructor's software agent reading a sign-up sheet and posting to Slack) but with specific, limited permissions. That is where OAuth comes in (Assignment 2)
    * **Three concepts to keep apart.** *Identification:* who do you claim to be? *Authentication:* prove it. *Authorization:* now that you are proven, what are you allowed to do? Then access control enforces it, and logging records what happened. Example: the agent that posts agendas authenticates with a token and is authorized to read a sheet but not write it; in OAuth those permissions are called scopes. **Midterm flag:** these definitions and the sequence identify, authenticate, authorize
    * **The three modes of authentication**, each with weaknesses, which is why multi-factor exists
        * Something you know (password, PIN, security questions): guessable, phishable, reused across sites, leaked
        * Something you have (a phone receiving a code, an authenticator app, a hardware token): the campus two-factor login as the example; lost or stolen devices, backup codes nobody saves
        * Something you are (fingerprint, face, iris): hard to revoke, can be spoofed, and a phone held up to a sleeping parent's face unlocks it
    * **How a passkey works** (worked through on the spot, using the morning's public-key material): your device creates a key pair *per site*; the site stores the public key where it used to store a password; the private key stays on the device. To sign in, the site sends a random challenge, the device signs it with the private key, and the site verifies the signature with the stored public key. The private key is unlocked with a biometric, so a passkey is something you have plus something you are. The secret never leaves the device, the server holds only public keys (nothing to steal), and every site gets a different key (nothing to reuse). Adoption is widening. *The two passkey slides in the deck were rewritten after class to say exactly this; see slides 7 and 8*
    * **Subject, verb, object:** who may do what to which thing. Classic Unix permissions as the example: read, write, execute bits for the owner, the group, and everyone, shown on a real directory listing. Will not be asked on the exam. **Midterm flag:** more likely, a modern app or website and the question of what its subjects, verbs, and objects should be
    * **OAuth, motivation only:** budgeting apps used to need your bank password to read your balances; OAuth exists so a third party can be given limited, read-only access without your password. Assignment 2 is OAuth
* **Not covered, carried to Meeting 3:** the rest of OAuth (roles, the flow, tokens and scopes, what goes wrong), then topics 5 and 6 (botnets and denial of service)

### Meeting 3 (Wed Oct 14)

*Both lecture segments written from their recordings. The debate is not recorded (it is the students' session) and is logged by resolution and format.*

* **Housekeeping**
    * Assignment 1 (PKI) is due **Fri Oct 23**. Assignment 2 is about OAuth and opens shortly after, around Oct 25–26; today's OAuth lecture is its background, and the draft on the course site can be read ahead
    * **Midterm: Wed Nov 4**, in class, three weeks away
    * TA office hours were announced in Slack last night. The instructor's Zoom office-hour sign-up will be pinned in Slack. Reading assignments are all posted on the website
    * Waitlist: anyone still attending in week three is welcome to stay; tell the instructor and you will be enrolled
* **Lecture: OAuth** (finishing Modern Authentication, topic 4)
    * Review of Meeting 2: identification (which user, process, or app), then authentication (prove it, by something you have, know, or are), then authorization (what that identity may do), then logging for accountability; passkeys, subject-verb-object, and the Unix access-control model
    * **The problem OAuth solves: delegated access.** How do you let a third-party application act on your behalf without handing it your password? Examples: an app asking for your Google contacts or Docs; a desktop AI assistant asking for your Dropbox or local files; Slack connectors to GitHub, Google Docs, or your calendar
    * Life before OAuth: budgeting apps (Mint and its successors) required your bank username and password. That gives the app full control with no way to scope it (can it also withdraw money or trade?), no way to revoke it short of changing your password, and no way to audit it, since every action it takes looks like you
    * OAuth is a delegation protocol that gives a third-party application *limited* access to resources on your behalf. It separates authentication (you log in to the authorization server) from authorization (the consent screen where you choose what the app may do). The app only ever holds a **token**, which can be scoped, expired, and revoked
    * **The four roles**, using Slack opening a GitHub issue as the running example: the **resource owner** (you, who own the repository); the **client** (Slack, the third-party app); the **authorization server** (GitHub's, which issues a token after you consent); and the **resource server** (the GitHub API, which receives the token from the client and validates it). **Midterm flag:** given a scenario, identify which party is the resource owner, client, authorization server, and resource server
    * **The flow:** (1) the client asks the resource owner for access and bounces you to the provider's login page; (2) you log in and approve, and the client receives a short **authorization grant**; (3) the client sends the grant plus its own client credentials (every registered app has its own) to the authorization server; (4) the authorization server returns an **access token** limited to what you allowed; (5) the client presents the token to the resource server; (6) each request is allowed or denied according to the token's scopes
    * **Principle of least privilege:** grant only the minimum privileges needed for the task and no more. Giving a third-party app your username and password is a clear violation, because the app can then act as you in every way, far beyond the one task you wanted done. **Midterm flag:** explain why handing an app your credentials violates least privilege
    * **Access tokens** are delegated rights bounded by **scope** (the set of permitted actions) and **duration**. A token is a capability: a bearer string the client cannot inspect, it just presents it. Least privilege in practice means picking the narrowest scope that works and a short validity period; a **refresh token** lets the app obtain a new access token when the old one expires, which is why you are not re-authorizing every hour
    * **Where it goes wrong:** token theft or leakage (tokens in logs, URLs, browser history, or checked into a repository can be replayed for as long as they are valid, which is why short lifetimes matter) and over-broad scope (requesting more than the app needs, often for convenience when getting something working)
    * **Live demo.** Connecting Slack to Zoom: the consent page at zoom.us listed the scopes in English ("app can access and manage this even when not using the app") with no option to uncheck any, but the integration failed after consent, probably blocked by campus IT. Connecting Slack to Google Drive worked: log in to Google (authentication), then a consent screen listing scopes including viewing, editing, and creating files and "view the activity history of all your Google apps" (so much for least privilege), then Slack reported Google Drive ready and authenticated as the instructor. The grant and the client credentials never appeared on screen; the token exchange happened in the background
    * **Assignment 2 preview:** build your own third-party app against a service of your choice (GitHub, Spotify, Reddit, Google, and so on): register the app and get client credentials, implement the flow, and write up which scopes you requested and why, arguing that the app follows least privilege. The write-up has more questions than before; expect to look at a packet capture from your own machine to find where the token travels. Building a Model Context Protocol server for an AI agent will likely be added as a strongly suggested option, since agents are third-party apps that need exactly these tokens
* **Lecture: Denial of Service** (topic 5, first part)
    * Denial of service is an attempt to **exhaust a limited resource** so that legitimate users cannot reach a service. It has been going on for almost thirty years: a simple class of attack that is very hard to defend against
    * Scale today: the largest recorded attack is **31.4 terabits per second**, short, driven by compromised Internet-of-things devices, about three thousand times the roughly 10 Gbps connecting this campus to the Internet (correction: "about 1,000 times" was said in class). Recent botnets have had around three million hosts sending attack traffic
    * **What gets exhausted**
        * The network: the campus link is on the order of 10 Gbps; send 20 Gbps in, or have compromised devices inside send more than that out, and the link is gone. One laptop cannot do it, but a thousand devices each sending a thousandth of it can, which is why IoT matters so much to this attack
        * Connection state on a server: every connection allocates memory. Thousands of machines each opening one connection costs each of them little and exhausts the server. That is the **TCP SYN flood**
        * Any finite resource: CPU, memory, processing, and storage (fill the disk)
    * **The firewall irony.** Putting a firewall in front of the campus to inspect and remember traffic gives the attacker a new target: the firewall's own memory and CPU, and when it falls over nobody gets through. **Midterm flag (yes/no, why or why not):** campus IT deploys a firewall to drop attack connections from a region; has it introduced a new denial-of-service vulnerability? Yes: the firewall has limited resources and all the attack traffic now passes through it. The general lesson is that deploying an appliance to fix a security problem makes the appliance the next target
    * **What gets targeted:** web, file, and software-update servers, and above all **authentication and DNS**, which are force multipliers. Example: rather than flooding Canvas, attack the authentication service everything depends on. An authentication attempt makes the server do real work (identify you, generate a challenge, send it back), so it can be cheaper to take down, and if it falls, Canvas, Zoom, and the mail suite go with it. The 2016 **Mirai** attack on **Dyn**, a DNS provider for Reddit, Twitter, the New York Times, and many others, took all of them down at once without touching their web servers: their names simply stopped resolving
    * **Three characteristics of every denial-of-service attack. Midterm flag.**
        * **Asymmetry:** the attacker does little work and the victim does a lot. One SYN packet makes the server allocate memory; one "hello" makes a TLS server do expensive public-key operations to set up a session (largely fixed now); a tiny DNS query asking for everything about a name produces a large answer (**amplification**), and with a spoofed source address the answer goes to the victim instead of the attacker (**reflection**)
        * **Indistinguishability:** attack traffic looks like legitimate requests. One host sending thousands of requests a second is easy to block, which is why attacks are **distributed**: thousands of compromised devices each sending a request or two, exactly as a real user would
        * **Attribution is hard:** spoofed sources, and reflected traffic that arrives from innocent open resolvers
    * **Mirai and Dyn (2016):** roughly 100,000 security cameras with default passwords, small by today's standards. What was new was that it exhausted the query-processing capacity of the DNS servers rather than the network. Then the death spiral: legitimate lookups of those names began failing, and well-behaved software responds to failure by retrying, so legitimate devices were recruited into the attack and the two kinds of traffic became even harder to separate
    * **Open resolvers:** historically many servers would answer a DNS query from anyone (public resolvers such as 8.8.8.8 and 1.1.1.1 are the deliberate version). Attackers use them for reflection: spoof the victim's address as the query source, and multiply by a thousand machines. Locking them down is a misaligned-incentives problem: the operator does the work and someone else gets the protection
    * **TCP SYN flood in detail:** the client's SYN says "I want a connection"; the server allocates a transmission control block (memory) and waits: a half-open connection. SYNs with spoofed, non-existent sources fill the table and legitimate clients are refused. The fix is the **SYN cookie**: the server remembers nothing on the first packet and instead puts something in its reply that lets it recognize the client when it comes back, like a web cookie. The cryptographic mechanics will not be covered in class. **Midterm flag:** you could be asked to design a defense in this spirit for a system you have not seen: spot where an attacker's cheap action forces the recipient to spend memory or compute, then redesign so the recipient does no work until the client proves it is real by returning
    * **Summary:** denial of service targets availability by exhausting a finite resource; security mindset means asking what the limited resources of a system are. Defense means restoring symmetry: pushing work back onto the requester. Incentives and the Internet of things keep coming up
    * The instructor's own example of restoring symmetry: a flood of individually legitimate, cheap-to-send enrollment and waitlist emails is a distributed denial of service on one person. The defense is a one-line reply that costs nothing (the SYN cookie) and the rule that anyone still attending in week three is admitted: the real clients come back, the rest disappear
    * Not covered: the slides on amplification factors, BCP 38 ingress filtering, scrubbing, and the Great Cannon. Power went out in the room at the end of this block
* **Debate: Encryption Backdoors** ([resolution and readings](../debates/backdoors.md), [format](../debates/format.md)): *It should be legal to compel tech companies to provide a backdoor to law enforcement*. Ten students signed up. Opening and closing polls were taken in Slack. Not recorded
    * Logistics raised afterwards: the debate resolutions are linked from the third column of the syllabus table, mixed in with other activities, which makes them hard to find. The instructor will reorganize the site so each week's resolution is easy to locate
* **Lecture: Routing Security** (topic 6, first part). The classroom projector failed after the debate, so the deck was posted to Slack as a PDF and narrated by slide number. The second half of Denial of Service was not resumed; routing was started instead
    * Framing: the next two modules are infrastructure security, in three parts: routing (today and next week), naming (DNS), and the web. Routing is the least familiar of the three and the ordering would have been better the other way round
    * The Internet is an inter-network: a network of networks, each independently operated (UChicago's network staff, Google's). Each such network is an **autonomous system (AS)** with an **AS number**, and the **Border Gateway Protocol (BGP)** is how they tell each other which destinations they can reach. Border routers at the boundaries between networks are what talk BGP, hence the name
    * Worked example from the new overview slide: UChicago (AS 160) advertises its **prefix** 128.135.0.0/16 to its transit provider; the provider (Cogent, AS 174) passes the same prefix on to Google with the **AS path** 174 160. A /16 is a group of 2^16 addresses; prefix arithmetic will not be asked. The first AS in the path is the **origin**. A **route advertisement** says "I can reach this prefix, and here is the path"; traffic then flows back along that path toward the destination. That is BGP in a nutshell
    * Analogy: driving directions to the state line, then asking again. Each network only knows how to get you to its boundary; it works this way for scalability
    * **BGP has no security.** When it was deployed thirty to forty years ago, nothing checked whether a network was allowed to announce what it announced: neighboring routers simply believe. By accident this is a **route leak**; on purpose it is a **route hijack**
    * **Case studies:** the 1997 leak, where one small network announced it could reach the whole Internet and its neighbors believed it; China Telecom in April 2010, which announced about 50,000 prefixes it did not own, from 170 countries, less disruptive than it sounds because networks prefer the shorter AS path; and Pakistan Telecom in February 2008, which announced YouTube's addresses to block YouTube inside Pakistan and leaked the announcement to the rest of the Internet, pulling other networks' YouTube traffic into Pakistan. The last is a censorship action that became a global outage
    * **What a hijacker can do** with another network's addresses: capture the traffic meant for them and eavesdrop on it, drop it (a denial of service), or, if the attacker can also put itself on a path back to the real destination, pass it through as a **man-in-the-middle**. Doing this takes real infrastructure: you need routers and providers willing to accept your announcements. It still happens: about a year ago attackers set up fake Internet service providers to do exactly this (the case study on the deck's "What Attackers Can Do" slide)
    * **The two problems to solve,** teed up for next week: **origin authentication** (is the announcing network the rightful holder of that address space?) and **path authentication** (is the AS path real, or forged?). Origin is the critical one. Both are solved with public-key cryptography: every AS gets a public key tied to its identity through a public key infrastructure, the same shape as the web PKI from Meeting 2
    * Not covered: RPKI, path validation, the FCC proceeding, and the rest of the Routing deck from "Origin Authentication With RPKI" onward
* **Next week (Wed Oct 21):** a slower review of how BGP works, then the routing-security defenses, then DNS security, which uses its own public key infrastructure to do the same thing for DNS records that RPKI does for routes. Assignment 2 (OAuth) opens Mon Oct 26
