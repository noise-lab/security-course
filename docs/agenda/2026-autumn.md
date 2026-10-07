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

*First segment written from the recording. The debate is not recorded (it is the students' session) and is logged by resolution and format only. The post-debate segment will be added from its recording.*

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
    * **Man-in-the-middle:** Mallory on the path replaces each side's transmitted value with her own, ends up sharing one key with Alice and another with Bob, and neither notices. Example in practice: the first-connection host-key prompt in SSH, which only works if you can confirm the fingerprint out of band. MITM is itself a key-management problem: you need some trusted channel to know who is on the other end. Trusting Trust again. **Midterm flag:** given a different protocol, explain how a man-in-the-middle attack would work
    * **Asymmetric (public-key) cryptography** (RSA, early 1980s, also a Turing Award): a key pair, one published, one secret. Door analogy: anyone can lock, only the owner can unlock
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
* **Post-debate segment:** to be added from the recording (planned: OAuth / Modern Authentication, which is also the background for Assignment 2)
