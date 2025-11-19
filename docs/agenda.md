## Agenda

### Meeting 1

* Overview
  * Course Objectives and Context
  * Format
  * Debates
  * Labs
* Lecture Coverage: Trusting Trust
* Reading Discussions: Reflections on Trusting Trust
  * How does this concept apply beyond the specific example he gives about compilers and backdoors?
  * How can we protect against similar threats in today’s highly interconnected and complex systems?
  * How would the concerns addressed in this paper extend to AI-based systems?
* Lecture Coverage: Why Cryptosystems Fail
* Reading Discussion: Why Cryptosystems Fail
  * How can these failures be mitigated through better design and operational practices?
  * How do regulatory frameworks, like GDPR and CCPA, impact the development and implementation of cryptosystems?

### Meeting 2

* Lecture Coverage: Key Management and Public Key Infrastructure
  * **Encryption Fundamentals**
    * Threat models and adversary capabilities
    * Encryption algorithms (encryption function E)
    * Properties: Correctness and Security
    * Security definition: Indistinguishability (one-bit perfect security intuition)
  * **Symmetric Key Cryptography**
    * Key exchange problem
    * Shared keys between Alice and Bob
    * Scalability challenges
    * Use in practice: Fast encryption/decryption for bulk data transfer
  * **Diffie-Hellman Key Exchange**
    * Public key exchange without prior shared secret
    * Based on discrete logarithm problem (hardness assumption)
    * Modular exponentiation basics
    * How Alice and Bob derive shared secret from public exchange
    * NOT covered: Mathematical proofs, number theory details, computing discrete logs
  * **Public Key (Asymmetric) Cryptography**
    * Key pairs: Public key and private key
    * Different keys for encryption vs. decryption
    * Public key can't be derived from private key (hardness assumption)
    * RSA algorithm (mentioned, not detailed)
  * **Two Use Cases for Public Key Cryptography**
    * **Confidentiality**: Encrypt with public key, decrypt with private key
    * **Integrity/Authentication**: Sign with private key, verify with public key
    * Digital signatures for message integrity
    * Examples: Software updates, OS patches (Apple example)
  * **Certificates and Trust**
    * Problem: How to know a public key belongs to a specific entity
    * Certificates bind entities to public keys
    * Self-signed certificates vs. CA-signed certificates
    * **Certificate Chains** (Hands-on Activity)
      * Inspecting certificate chains in browser (Firefox example)
      * Walking up the certificate hierarchy
      * Example chain: course website → Let's Encrypt → ISRG Root X1
      * Root certificates in operating systems and browsers
      * Trust anchor: Where does trust ultimately stop?
  * **Certificate Validation Levels**
    * **Domain Validation (DV)**: Proves control over domain (Let's Encrypt example)
      * How it works: Placing specific content on website as proof
    * **Extended Validation (EV)**: Proves legal entity identity (Bank of America example)
      * Additional verification requirements
      * Visual indicators in browsers
  * **Security Case Studies**
    * DigiNotar breach (2011): Compromised CA issuing fake Google certificates
    * China Internet Network Information Center (CNNIC) root certificate controversy
    * Gogo inflight internet issuing fake certificates (2015)
    * Bad SSL website for testing certificate validation
  * **TLS/HTTPS in Practice**
    * Wireshark packet capture demo
    * TLS handshake: Certificate exchange, key exchange, session establishment
    * Session keys for symmetric encryption after handshake
    * TLS 1.2 vs TLS 1.3 (Encrypted SNI for privacy)
    * Information leakage in unencrypted handshake (SNI)
  * **Key Concepts Students Should Understand** (NOT Math Details)
    * Why key exchange protocols are important
    * Threat models and adversary capabilities
    * Difference between symmetric and asymmetric cryptography
    * What certificates do (bind identity to public key)
    * Certificate chains and roots of trust
    * Domain validation vs. extended validation
    * Confidentiality vs. Integrity as security properties
    * Where trust ultimately resides (OS, browser, certificate authorities)
  * **Topics NOT Covered in Detail**
    * Number theory and mathematical proofs
    * Computing discrete logarithms or factoring
    * RSA algorithm details
    * Specific cipher implementations
    * Legacy cryptosystems
* Assignment 1: Public Key Infrastructure and Certificates
  * Generate self-signed certificate
  * Set up web server with HTTPS
  * Capture and analyze TLS handshake with Wireshark
  * Examine certificate chains
  * Due: Two weeks from Friday (Feb 9, 2024)
* Hands-on Activity: Certificate Chain Inspection
  * Students inspect certificate chains in their own browsers
  * Trace certificates to root CAs in operating system
  * Understand trust hierarchy in practice
* Debate: Data Breaches
* Modern Authentication: OAuth (Topic deferred to next week due to time)


### Meeting 3

* Lecture Coverage: Authentication and Access Control
  * **Goals of Access Control**
    * Protecting users from one another
    * Protecting applications from each other
    * Protecting systems on the network from other systems
    * Allowing information to be shared across boundaries
  * **Threat Models**
    * Honest but curious adversary
    * Insider attacks
    * Financial motives and espionage
  * **Authentication Basics**
    * Identification vs. Authentication vs. Authorization
    * **Three Modes of Authentication** (Important for midterm)
      * Something you know (passwords)
      * Something you have (keys, ID cards, UB keys, 2FA tokens)
      * Something you are (biometrics: fingerprints, facial recognition, iris scans)
  * **Operating System Access Control**
    * Unix/Linux file permissions model
    * File ownership: user and group
    * Permission bits: read (r), write (w), execute (x)
    * Three permission sets: owner, group, world
    * Live demo: `ls -l`, file permissions, `whoami`, `groups`
  * **Processes and Privileges**
    * Processes run as users (`ps` command)
    * Operating system mediates access based on process user privileges
    * Example: PowerPoint process running as user accessing files
  * **Special Users and Privilege Escalation**
    * Root/superuser (ultimate privileges)
    * `sudo` command (super user do)
    * Principle of least privilege
      * Definition: Only grant minimum privileges needed to perform a task
      * Example: Web servers running as limited users (not root)
      * Example: OAuth scope limiting permissions
    * Privilege escalation attacks
      * Definition: Vulnerability allowing process to gain higher privileges
  * **Web Server Security Model**
    * Historical: Web servers ran as root (security risk)
    * Modern: Web servers run as limited users (e.g., "nobody", "www-data")
    * World-readable files for public access
  * **Logging and Auditing**
    * Tracking who has accessed what
    * Forensics after breaches or unauthorized access
* Lecture Coverage: OAuth (Modern Authentication and Authorization)
  * **Problems with Credential Sharing**
    * Sharing passwords with third-party apps (insecure)
    * Example: Banking apps requesting username/password
    * No delegation, just impersonation
    * Hard to revoke access
    * Poor auditability
  * **OAuth Solution**
    * Access delegation without credential sharing
    * Framework (not protocol): doesn't specify cryptography or token format
    * Common implementation: JSON Web Tokens (JWT)
  * **OAuth Roles**
    * Resource owner: User who owns the protected data
    * Client: Third-party application requesting access
    * Authorization server: Issues tokens (e.g., GitHub)
    * Resource server: Hosts protected resources
  * **OAuth Flow** (Live demo: Slack + GitHub integration)
    * Step 1: Client requests authorization from resource owner
    * Step 2: Resource owner logs in and approves request
    * Step 3: Resource owner grants authorization code to client
    * Step 4: Client presents authorization code to authorization server
    * Step 5: Authorization server issues access token
    * Step 6: Client uses access token to access resource server
  * **Access Token Scoping**
    * Tokens encode specific permissions (scope)
    * Examples: read-only, issues access, repository access
    * Principle of least privilege applies to token scope
    * Live demo: GitHub personal access token creation
  * **Key Concepts**
    * Authorization grant: Temporary code proving user consent
    * Access token: Credential representing delegated permissions
    * Scope: Set of permissions associated with token
    * Token expiration and revocation
  * **Possible Midterm Questions**
    * Three modes of authentication (know, have, are) - examples
    * Given a scenario (e.g., Slack + GitHub), identify OAuth roles
    * Unix file permissions interpretation
    * Principle of least privilege examples
    * OAuth flow steps
* Assignment 2 Preview: Build OAuth Application
  * Write third-party app using OAuth
  * Choose any service with OAuth API
  * Examples: Google Calendar, Nest thermostat, GitHub
  * Must use OAuth for authentication/authorization
  * Due: ~2 weeks (not yet officially assigned)
* Debate: Encryption Backdoors
* Lecture Coverage: Denial of Service Attacks and Botnets
  * **Theme Shift**: From System Security to Internet Security
  * **Definition of DoS Attacks**
    * Attempt to exhaust limited resources in a system
    * Network-based attacks
    * Goal: Deny service to legitimate users
  * **Types of Limited Resources that can be Exhausted**
    * **Network resources**: Bandwidth/capacity (e.g., 1 Gbps link saturation)
    * **Transport/Connection resources**: Maximum simultaneous connections
    * **Server resources**: CPU, memory, processing (e.g., TLS handshake computation)
  * **Common Targets**
    * Web servers (most common)
    * File servers
    * Authentication services (e.g., Duo two-factor authentication)
    * Update servers
    * Domain Name System (DNS) servers
    * Network infrastructure devices (less common, harder to attack)
  * **Three Common Characteristics of DoS Attacks** (Important for midterm)
    * **1. Asymmetry**
      * Attacker's cost << Victim's cost
      * Examples:
        * Single packet triggers server to allocate memory/state
        * Small hello message forces server to generate keys (old TLS)
        * Small query generates large response (amplification)
      * Amplification: Small input generates large output
      * Botnets: Many compromised machines send small amounts, victim sees large aggregate
    * **2. Difficulty of Distinguishing Legitimate from Attack Traffic**
      * Attack traffic looks like normal requests
      * Hard to filter without blocking legitimate users
      * Example: Botnet traffic from many different sources
      * Can't simply block one IP address or subnet
    * **3. Difficulty of Attribution**
      * IP address spoofing common
      * Attacker doesn't care about receiving response
      * Makes it harder to trace attack source
      * Forged source addresses in packets
  * **Case Study: Mirai Botnet Attack on Dyn (October 2016)**
    * Major outages: Twitter, Netflix, Spotify, Reddit, and many others
    * Target: Dyn (DNS infrastructure provider, not the end services)
    * Attack vector: DNS servers hosting domain resolution for major sites
    * Key insight: Attack DNS infrastructure to take down multiple services at once
    * **Botnet Composition**
      * Mirai malware targeting IoT devices (smart cameras, home devices)
      * Estimated 100,000 compromised endpoints (relatively small for botnets)
      * "Army of vulnerable gadgets"
    * **Why Effective Despite Small Size**
      * Application-level attack (server resource exhaustion)
      * Not purely bandwidth exhaustion
      * Targeted DNS query processing capacity
      * Relatively low total traffic volume
    * **Death Spiral Effect**
      * Attack traffic overloads DNS servers
      * Legitimate users can't resolve domains
      * Applications retry automatically (by design for resilience)
      * Legitimate retries amplify the attack
      * "Storm of legitimate retry activity"
      * Impossible to distinguish attack from legitimate retries
    * **Attribution Challenges**
      * Attack and legitimate traffic from millions of IPs
      * Can't filter by source
      * Attack traffic looks like normal DNS queries
    * **Lessons**
      * Critical infrastructure dependencies create cascading failures
      * Easier to attack infrastructure than individual services
      * Legitimate traffic patterns can amplify attacks
  * **DNS Reflection and Amplification Attack**
    * **How it Works**
      * Attacker sends small DNS query to open DNS resolver
      * Query has spoofed source IP (victim's address)
      * DNS server generates large response
      * Large response sent to victim (not attacker)
      * Amplification factor: 60x to 3,000x possible
    * **Key Techniques**
      * Reflection: Bounce traffic off third party (DNS server)
      * Amplification: Small query → large response
      * IP spoofing: Victim receives response they never requested
    * **Why Effective**
      * Satisfies asymmetry: Attacker sends small queries, victim receives large responses
      * Satisfies IP spoofing: Source address forged
      * Attacker doesn't do the work; DNS server generates traffic
      * Can use many DNS servers simultaneously (distributed)
    * **Partial Distinguishability**
      * Victim receives responses without sending requests
      * Could be detected/filtered
    * **Defense: Stateful Firewall**
      * Track outgoing DNS queries
      * Drop incoming responses that don't match outgoing queries
      * **New Vulnerability Introduced**
        * Firewall must maintain state (memory)
        * State storage = limited resource
        * Attacker can exhaust firewall memory
        * Attack vector: Send spoofed queries through firewall
        * Firewall remembers queries, runs out of memory, crashes
      * **Defense Against Firewall Attack**
        * Ingress filtering: Check if packet source matches expected direction
        * Drop packets claiming to be from inside network but arriving from outside
    * **Open Resolvers**
      * Definition: DNS servers that answer queries from anyone
      * Examples: Google (8.8.8.8), Cloudflare (1.1.1.1)
      * Vulnerability: Can be used for reflection attacks
      * Historical problem: Many insecure open resolvers
      * Misaligned incentives: Secure your server to protect others
  * **Key Security Principles Illustrated**
    * Any defense requiring state introduces new attack surface
    * Stateful systems = limited memory = potential DoS target
    * Tradeoff: Security features vs. new vulnerabilities
    * Always ask: "Have I introduced new vulnerabilities?"
  * **Possible Midterm Questions**
    * Analyze recent DoS attack, identify characteristics, propose mitigations
    * Given a reflection attack diagram, explain how it works
    * Propose defenses for specific attack scenarios
    * Identify new vulnerabilities introduced by defenses
    * Example: "How would you attack the stateful firewall? What traffic would you send?"
* Topics NOT Covered in Detail
  * TCP SYN Flood attacks
  * TCP handshake details
  * TCP SYN cookies
  * Technical details of TCP-based attacks
  * Traffic injection attacks (Great Cannon)

### Meeting 4

* **Administrative Updates**
  * Midterm scheduled for Week 6 (two weeks out)
  * Midterm will be generated using LLM (Claude) based on:
    * Previous three midterms (available in GitHub docs/midterm directory)
    * Agenda file tracking topics covered
    * Manual editing for quality and accuracy
  * Prompt will be shared for students to generate practice exams
  * Exam designed for 45-60 minutes, but no time limit enforced
  * Students can stay as long as needed (accommodations available)
  * Structure similar to past years: sections on public infrastructure, web security, ethics, etc.
  * Goal: Not adversarial, want students to succeed and learn
* Lecture Coverage: Internet Routing Security
  * **Three Categories of Internet Infrastructure Security**
    * Security of internet routing infrastructure (BGP)
    * Security of naming infrastructure (DNS)
    * Security of the web
  * **Internet Routing Background**
    * **Purpose**: Distributed system that tells routers where to send traffic
    * **Internet = "Inter-network"**: Network of networks
    * **Autonomous System (AS)**: Independently operated network
      * Examples: University of Chicago network, Google network, Netflix network
    * **Border Gateway Protocol (BGP)**: Protocol that connects autonomous systems
      * Border routers on edges of autonomous systems use BGP to exchange routing information
    * **Routing Analogy**: Like Google Maps for traffic
      * Instead of full directions, internet routing works in chunks
      * Example: Get directions to Wisconsin border, then ask again at next network
      * Each autonomous system only knows how to get to its boundaries
  * **Security Problems in Internet Routing**
    * **Lack of Security in BGP**: No security when initially deployed
    * **Fundamental Problem**: Routers believe whatever neighboring networks tell them
    * **Two Types of Incidents**
      * **Route Leak** (Accidental): Misconfiguration causes bad routing information to spread
      * **Route Hijack** (Intentional): Deliberate advertising of incorrect routing information
    * **Case Study: 1997 Virginia ISP Outage**
      * Small ISP in Virginia misconfigured router
      * Accidentally advertised routes to entire internet
      * Information propagated to Sprint (large ISP)
      * All traffic routed to small Virginia ISP, which couldn't handle load
      * Major outage lasting over 2 hours
    * **Case Study: China Telecom Hijacking (2010)**
      * China Telecom advertised 50,000+ IP prefixes from hundreds of countries
      * Traffic between US providers (AT&T, Verizon) routed through China
      * Unexpected routing path with poor performance
      * Security concern: Traffic routed through potentially adversarial country
  * **How BGP Hijacking Works**
    * **Autonomous System Path (AS Path)**: List of networks to traverse
      * Example legitimate path: Verizon → Level 3 → Verizon Wireless
    * **Hijacking Mechanism**
      * Attacker advertises same IP prefix with shorter AS path
      * BGP selects routes based on shortest AS path (fewest ASes)
        * Note: This is illogical (like choosing interstate route by number of states, not miles)
      * Networks prefer "shorter" route, sending traffic to attacker
    * **Example Attack**
      * Legitimate path: 4 autonomous systems
      * China Telecom advertises same prefix with 3 autonomous systems (lie)
      * Networks choose China Telecom route (appears shorter)
      * Traffic flows through China Telecom instead of legitimate path
  * **Two Security Problems to Solve**
    * **1. Origin Authentication**
      * **Problem**: How to verify which AS is allowed to advertise a specific IP prefix?
      * Like verifying Toronto is in Ontario, not Kentucky
      * **Solution: Resource Public Key Infrastructure (RPKI)**
        * Certificates bind IP prefixes to autonomous systems
        * Similar to web PKI binding domains to entities
        * Certificate contains:
          * AS number (e.g., 22394)
          * IP prefix (e.g., 66.174.161.0/24)
          * Public key for that AS
        * Certificates signed by Internet registries (e.g., ARIN - American Registry for Internet Numbers)
      * **How Origin Authentication Works**
        * Originating AS signs routing message with its private key
        * Message contains: IP prefix + originating AS number
        * Receiving router:
          1. Verifies signature using AS's public key (from RPKI certificate)
          2. Checks certificate to confirm AS is authorized to advertise that prefix
        * Prevents unauthorized AS from claiming ownership of IP prefix
      * **Deployment Status**: Actually deployed (took over a decade)
      * **Incentive Alignment**: Networks want to protect their own routes from hijacking
    * **2. Path Authentication**
      * **Problem**: How to verify the AS path hasn't been modified?
      * Prevents attackers from shortening or changing the path
      * **Path Shortening Attack Example**
        * Legitimate path: AS100 → AS6167 → AS22394 → Verizon Wireless
        * Attacker (AS100) removes AS6167 from path
        * Advertises shorter path: AS100 → AS22394 → Verizon Wireless
        * Attracts more traffic for surveillance/interception
      * **Solution: Route Attestations with Signatures**
        * Each AS signs not just the current message, but also:
          * The AS path so far
          * The AS number it's sending the message TO (critical detail)
        * Example: AS6167 signs message containing:
          * Path: 6167 → 22394
          * Recipient: AS100 (or Level 3, etc.)
        * Prevents path shortening because signature includes destination AS
        * Each AS passes along chain of signed attestations
      * **Deployment Status**: NOT deployed after 30 years
      * **Why Not Deployed: Misaligned Incentives**
        * Requires ALL autonomous systems to participate
        * Network must upgrade routers (expensive: Cisco equipment, complexity, etc.)
        * Cost/effort to protect OTHER networks, not yourself
        * Classic coordination problem / prisoner's dilemma / tragedy of the commons
        * If any AS doesn't deploy, protection fails for everyone
        * Article assigned: "Why is it taking so long to secure internet routing?"
  * **Key Technical Concepts** (Pedagogical emphasis)
    * Real-world application of public key infrastructure
    * Understanding what signatures guarantee
    * Man-in-the-middle attacks (AS100 acting as intermediary mangling messages)
    * What must be signed to prevent specific attacks
    * Thinking critically about security guarantees
  * **Possible Midterm Questions**
    * **Understanding public key infrastructure in routing context** (tests PKI knowledge)
    * **How signatures prevent path shortening attacks** (critical thinking about what to sign)
    * **Difference between origin authentication and path authentication**
    * **Why origin authentication is simpler than path authentication** (similar to base case in induction)
    * Path shortening attack is a good topic to understand for testing knowledge of signatures
    * Understanding this example helps with any secure system using PKI
  * **Topics NOT Covered in Detail**
    * Technical BGP protocol details other than IP prefixes and AS paths
    * Complete technical specification of route advertisements
    * Why some AS numbers repeat in paths
    * Specific standards names (S-BGP vs BGPsec naming)
* Debate: CFAA
* Lecture Coverage: DNS Security and Privacy
  * **DNS Background and Review**
    * **Primary Purpose**: Translate human-readable names (e.g., uchicago.edu) to IP addresses
    * **Hierarchical System**
      * Stub resolver: On local machine, launches DNS queries
      * Local recursive resolver: On campus/network, caches commonly looked up domains
      * Root servers → Top-Level Domain (TLD) servers → Authoritative name servers
    * **DNS Resolution Process** (Slide 5)
      1. Stub resolver sends query to local recursive resolver
      2. If not cached, recursive resolver queries root server
      3. Root refers to TLD server (e.g., .com)
      4. TLD refers to authoritative name server for domain (e.g., foo.com)
      5. Authoritative name server returns answer
      6. Local recursive resolver caches result and returns to client
    * **Referrals**: Each level refers query to next level down the hierarchy
    * **Why Caching Matters**: Typical webpage requires hundreds of DNS lookups (scripts, trackers, images, etc.)
  * **DNS Security: Integrity and DNSSEC**
    * **Security Problem**: Until ~7-8 years ago, DNS had no signatures or encryption
    * **Threat**: Malicious resolver could lie about DNS records
    * **Solution: DNSSEC (DNS Security Extensions)**
      * Uses public key infrastructure with signatures
      * Each level signs messages with its private key
    * **DNSSEC Public Key Hierarchy**
      * Authoritative name server signs DNS response with its private key
      * Name server's public key certificate is signed by TLD server
      * TLD server's public key certificate is signed by root server
      * Root is the trust anchor (installed in resolver software)
      * Similar structure to web PKI and RPKI for BGP
    * **How to Trust the Root?**
      * Root public key installed in resolver software
      * Trust whoever you got the software from
      * "Trusting Trust" problem again - chain of trust must stop somewhere
    * **Focus on Concepts, Not Protocol Details**
      * Understand the hierarchy and how signatures work
      * Use DNSSEC as test of understanding public key infrastructure
      * Won't be quizzed on specific DNSSEC record types or protocol mechanics
  * **DNS Privacy: Confidentiality Concerns**
    * **Problem 1: Eavesdropping**
      * DNS queries sent in the clear (unencrypted)
      * Any eavesdropper on path can see queries
    * **Problem 2: Local Resolver Surveillance**
      * Local recursive resolver sees both:
        * Your identity (IP address)
        * What you're looking up (domain names)
      * Do you trust your university/ISP with all your DNS queries?
    * **Privacy Leakage from DNS Metadata** ("It's just metadata" - antenna should go up!)
      * **Websites you visit**: Direct correlation to DNS lookups
      * **Devices you own**: IoT devices make specific lookups (Nest, Echo, thermostats)
      * **Activity patterns**: DNS lookups indicate browsing activity
      * **Website Fingerprinting**
        * Each webpage loads unique set of objects (hundreds of DNS lookups)
        * Different pages on same site have different lookup patterns
        * Machine learning can classify specific pages visited based on DNS fingerprint
        * Even without seeing content, can infer what page you're viewing
  * **DNS-over-HTTPS (DoH)**
    * **Mozilla's 2018 Solution**
      * Browser does DNS lookups instead of passing to OS stub resolver
      * Encrypts DNS queries using HTTPS (already built into browsers)
      * Sends encrypted queries to resolver over HTTPS
    * **How It Works**
      * DNS query embedded in HTTPS request
      * Protects against eavesdropping on query/response
      * Encrypted channel from browser to resolver
    * **Default Deployment**
      * Firefox: Cloudflare as default resolver partner
      * Chrome: Google Public DNS as default resolver
      * Now enabled by default (users may not even get warning)
      * Can be configured in browser settings: Security → Secure DNS
    * **The Trust Trade-off**
      * **Before DoH**: Local ISP/university sees queries (unencrypted on path)
      * **After DoH**: Cloudflare or Google sees ALL your queries (encrypted on path)
      * Solves eavesdropping problem but centralizes trust
      * Changed who you trust, not whether you trust someone
    * **User Awareness Problem**
      * Most users don't know DoH exists or is enabled
      * Research by Ranya (student in class) on user understanding and interface design
    * **Centralization Concerns**
      * All DNS queries going to small number of providers (Cloudflare, Google)
      * Single point of failure (relates to AWS outage discussion)
      * DNS denial of service attack on these providers would be catastrophic
  * **Oblivious DNS-over-HTTPS (ODoH)**
    * **Goal**: Decouple DNS query content from client IP address
    * **Core Problem with DoH**: Resolver sees both identity AND queries
    * **ODoH Solution**: Split information between two servers
      * **Recursive resolver**: Sees client IP address but NOT query content
      * **ODoH authoritative server**: Sees query content but NOT client IP address
      * Neither server has both pieces of information
    * **How ODoH Works** ("Add a layer of indirection")
      1. Stub encrypts query with public key of ODoH authoritative server
      2. Appends fake TLD suffix (.odns) in the clear
      3. Sends to recursive resolver (can't decrypt query)
      4. Recursive resolver sees fake TLD, generates referral to ODoH authoritative
      5. ODoH authoritative decrypts query, resolves it normally
      6. Response encrypted and returned through chain
      7. ODoH authoritative acts as "masking proxy"
    * **Encryption Detail**: Query encrypted with ODoH server's public key (NOT recursive's key)
    * **Invented by Professor's Research Group**
      * Presented at IETF DNS Privacy working group
      * Initially opposed by Cloudflare (Nick Sullivan: "horrible, too much latency, too complex")
      * Later implemented by Cloudflare as "Oblivious DoH"
      * Lesson: Strong opposition often indicates threatening/valuable idea
    * **Centralization Research Story**
      * 2021 paper: ~25% of top 10,000 websites hosted only on Amazon
      * Paper warned about single point of failure
      * Initially rejected by reviewers as bad methodology
      * AWS outage (Monday) validated the concerns
      * Lesson: If you have a good idea, run with it; if people get angry, keep running
  * **Key Technical Concepts** (Pedagogical emphasis)
    * Understanding DNS hierarchy and resolution process
    * Public key infrastructure applied to DNS (DNSSEC)
    * Chain of trust and roots of trust
    * Privacy vs. security (confidentiality vs. integrity)
    * Metadata privacy concerns
    * Trade-offs in trust models (who do you trust?)
    * Centralization risks in Internet infrastructure
  * **Possible Midterm Questions**
    * **DNS resolution process** (walk through the steps)
    * **DNSSEC public key hierarchy** (who signs what, similar to web PKI and RPKI)
    * **What DNSSEC protects against** (integrity, not confidentiality)
    * **DNS privacy concerns** (what can be learned from DNS metadata)
    * **Website fingerprinting** (how it works at high level)
    * **DoH trust model** (who sees what before vs. after)
    * **ODoH architecture** (how it splits information between servers)
    * **Centralization concerns** (risks of all queries going to few providers)
  * **Topics NOT Covered in Detail**
    * DNSSEC record types and protocol specifications
    * Kaminsky DNS cache poisoning attack mechanics
    * DNS-over-TLS (DoT) vs DNS-over-HTTPS (DoH) technical differences
    * Machine learning techniques for website fingerprinting
    * Specific IETF standards documents

# Meeting 5

* **Administrative Updates**
  * **Midterm Scheduled for Week 6 (Meeting 6)**
    * Past midterm examples available in GitHub docs/midterm directory
    * Midterm will be generated using Claude (LLM) based on:
      * Agenda file (complete record of topics covered)
      * Past three midterms
      * Manual editing for images, quality control
    * Prompt will be shared with students
      * Students can generate unlimited practice exams using same prompt
      * Provides clear description of format, topics, point distribution
    * **Philosophy**: No surprises, testing understanding not speed
      * Not a timed race - take as long as needed
      * Focus on understanding concepts
      * Preparation/studying is most valuable part
    * Structure similar to past years
  * **Assignment Submission Clarification**
    * Push to GitHub repository (private repos now)
    * Commits have timestamps - full record available
    * No need for separate zip files or Canvas uploads
* **Lecture Coverage: Web Security**
  * **SQL Injection Attacks**
    * **Core Problem**: Code expects data, gets code instead (recurring theme in web security)
    * **Classic Example**: xkcd "Little Bobby Tables" comic
      * Student name: `Robert'); DROP TABLE students;--`
      * Web form expects name (data)
      * Instead receives SQL command (code)
      * Code executes with privileges of web application
    * **How It Works**
      * Web form input inserted into SQL query
      * Example: `SELECT * FROM students WHERE name='[USER_INPUT]'`
      * Malicious input: `Robert'; DROP TABLE students;--`
      * Result: Two commands executed (query + destructive command)
      * Single quote breaks out of data context
      * Semicolon starts new SQL command
    * **Why Dangerous**
      * Attacker executes code with web application's database privileges
      * Can delete data, read sensitive information, modify records
      * Access control bypassed
    * **Defenses**
      * **Sanitize/Escape Control Characters**
        * Remove or escape special characters (quotes, semicolons)
        * Why some forms don't allow special characters in input
      * **Parameterized Types/Prepared Statements**
        * Declare types on data (e.g., password type)
        * Tell database: "treat this as data, never execute"
        * Type casting to prevent code execution
      * **Input Validation**
        * Restrict allowed characters (alphanumeric only for names)
        * Prevent special SQL characters from being submitted
    * **For Midterm**: May give code snippet and ask to write injection attack or identify vulnerable variable
  * **Same Origin Policy (SOP)**
    * **Purpose**: Browser security model preventing cross-site data theft
    * **Definition of Origin**
      * Protocol + Hostname + Port (e.g., https://amazon.com:443)
      * Typically just hostname in practice (HTTPS/443 standard)
    * **Core Principle**: JavaScript/code can freely interact with same origin, but NOT read data from different origins
    * **Key Question**: "What origin is my script running under?"
      * Critical for understanding what's allowed vs blocked
    * **Four Key Takeaways**
      * **1. SOP prevents cross-site data reading**
        * Facebook script cannot read Gmail data
        * Browser checks origin before allowing data access
      * **2. Loading vs Reading (Important Distinction)**
        * Third party CAN cause browser to load cross-origin resources
        * Third party CANNOT read the data that was loaded
        * Example: Cross-origin images can be displayed but pixel data cannot be read
      * **3. Scripts take origin of embedding page**
        * Script loaded from google.com but embedded in facebook.com
        * Script runs under facebook.com origin (NOT google.com)
        * Allows loading libraries (jQuery, Bootstrap) from CDNs
        * jQuery from Google CDN can't send data to Google
      * **4. iframes maintain their own origin**
        * iframe acts as separate page with separate origin
        * Parent page cannot read iframe content (and vice versa)
        * Example: Gmail inbox embedded in Facebook page
          * Gmail iframe keeps its own origin
          * Facebook cannot read Gmail iframe content
    * **Examples Covered**
      * Simple case: gmail.com script reading gmail.com data (allowed)
      * Blocked case: facebook.com script trying to fetch gmail.com data (blocked by browser)
      * Images: facebook.com can display image from third party, but cannot read pixel data
      * Script tags: Can load cross-origin scripts, but script runs under embedding page's origin
  * **Cross-Site Scripting (XSS) Attacks**
    * **How Same Origin Policy Gets Bypassed**
      * SOP still in effect, but attack tricks the browser
      * Gets malicious code to run in trusted origin (first party)
    * **Attack Mechanism**
      * Web form expects data (e.g., user name)
      * Attacker injects script tag instead: `<script>malicious code</script>`
      * Vulnerable code echoes input back into HTML without sanitization
      * Example PHP: `echo "Hello " . $_GET['name'];`
      * Browser renders attacker's script as part of trusted page
    * **Why Dangerous**
      * Malicious script runs with origin of vulnerable site (e.g., Gmail)
      * Can steal cookies, session tokens, authentication credentials
      * Can perform actions as the user
      * Can exfiltrate private data
    * **Progression Example**
      * Harmless: User types "Robert" → Page displays "Hello Robert"
      * Formatting: User types `<b>Robert</b>` → Page displays "Hello **Robert**" (bold)
      * Attack: User types `<script>steal_cookies()</script>` → Malicious script executes
    * **Two Types of XSS**
      * **Reflected XSS**: Attack happens in real-time
        * Victim clicks malicious link
        * Link contains script in URL parameters
        * Vulnerable site reflects script back immediately
        * Example: Evil site embeds iframe with malicious URL to Gmail
      * **Stored XSS**: Attack persists on server
        * Attacker posts script in comment field, forum post, etc.
        * Script stored in database
        * Every visitor loads page → script executes
        * Common on old WordPress sites with vulnerable comment sections
    * **Attack Flow (Reflected XSS)**
      1. Attacker creates malicious page (evil.com)
      2. Page contains iframe with URL: `gmail.com/?user=<script>malicious</script>`
      3. Victim visits evil.com
      4. Browser makes request to Gmail with script in parameter
      5. Gmail echoes back the parameter without sanitization
      6. Script executes in Gmail's origin
      7. Script can now access Gmail data and send to attacker
    * **Key Insight**: Browser has no way to know script was injected
      * Sees HTML from Gmail containing script tag
      * Executes it normally under Gmail's origin
      * SOP doesn't break - attack works around it by polluting trusted origin
    * **Defenses**
      * **Content Security Policy (CSP)**
        * Browser configuration to block inline scripts
        * Only execute scripts from same origin
        * Block `eval()` and inline script tags
        * Trade-off: May break legitimate site functionality
      * **Input Sanitization/Escaping**
        * Treat all input as data, never code
        * Escape HTML special characters (`<`, `>`, quotes)
        * Remove script tags from input
        * Modern frameworks (Python web frameworks) do this automatically
      * **No-Script Browser Plugins**
        * Block all JavaScript execution
        * Breaks most modern websites (heavy client-side JavaScript usage)
        * Extreme but effective defense
    * **Relationship to SQL Injection**: Same fundamental problem - data vs code
  * **Cross-Site Request Forgery (CSRF)**
    * **Different Goal**: Not about reading data, about executing unwanted actions
    * **Attack Mechanism**
      * User logged into trusted site (e.g., bank)
      * Visits malicious site or clicks malicious link
      * Malicious site causes browser to make request to trusted site
      * Trusted site sees authenticated session, executes request
    * **Example Scenarios**
      * Bank transfer initiated by malicious link
      * Social media post made without user consent
      * Settings changed on user account
    * **Live Demo: Search History Pollution**
      * Initial state: Search "shoes" → only shoes in history
      * Macy's appears on page 2 of results
      * Visit evil.com (innocent-looking muffin website)
      * Evil site makes cross-site requests to search engine
      * Searches for: Macy's shoes, other terms
      * Pollutes search history without user knowledge
      * Search "shoes" again → Macy's now on front page
        * Search engine optimizing based on fake history
    * **Why It Works**
      * Browser sends cookies automatically with requests
      * Third party CAN cause browser to make requests (allowed by SOP)
      * Server can't distinguish legitimate from forged requests
      * No authentication that request came from user's actual click
    * **Defenses**
      * **CSRF Tokens**
        * Server generates unique token for each session/action
        * Token embedded in legitimate forms
        * Server validates token with each request
        * Attacker doesn't know token, can't forge valid request
      * **Authenticate Each Action**
        * Don't rely solely on session cookies
        * Require token that proves request came from legitimate user flow
        * Example: Banking requires multiple clicks + SMS verification
          * Each step has associated token
          * Multi-step process with verification
    * **Key Insight**: Request didn't come from legitimate click stream through website
* **Lecture Coverage: Web Privacy and Tracking**
  * **Third-Party Tracking Overview**
    * **Definition**: Any site other than the one you're visiting (first party)
    * **Characteristics**
      * Typically invisible to users
      * Examples: BlueKai, LiveRamp, Google Analytics, Facebook Pixel
      * Most users never heard of these companies
    * **How It Works**
      * Third-party scripts/images loaded on multiple first-party sites
      * Same third party on many different sites
      * Example: BlueKai on both Amazon and Walmart
      * Third party can correlate visits across all sites where embedded
    * **Live Demos**
      * Browser inspection showing multiple domains loaded
      * Disconnect plugin visualization
        * Graph showing trackers as hubs
        * Each spoke = website visited
        * Hub sees all connected sites
      * Amazon example: BlueKai, IMDB, multiple trackers loaded
      * News sites: Particularly heavy with trackers (4+ advertising domains)
    * **Common Third-Party Trackers**
      * **Advertising**: media.net, geoedge, LiveRamp
      * **Analytics**: Google Analytics (on ~50% of websites)
      * **Social**: Facebook Connect/Meta Pixel, Twitter/X button
      * **Tag Managers**: Google Tag Manager
      * **Other**: DoubleClick, AdSense
    * **Prevalence Statistics** (study from ~2017, likely higher now)
      * Google Analytics: ~50% of page loads
      * 75% of first-party websites include some Google tracker
      * Facebook trackers: Also on majority of sites
      * Consolidation: Small number of companies (Google, Meta) see most web activity
    * **Social Sharing Buttons as Trackers**
      * Twitter/X share button on page → Twitter sees you visited
      * Facebook like button → Facebook sees you visited
      * Don't have to click button - just loading it tracks you
  * **First-Party Tracking with Third-Party Code**
    * **Different Model**: Third-party code runs in first-party origin
    * **How It Works**
      * First party (e.g., Reverb) embeds advertiser's code on their site
      * Code runs under first-party origin (no SOP restriction)
      * Code can see everything: shopping cart, clicks, form inputs
      * Data sent to advertising company
    * **Real-World Example**
      * Put item in cart on Reverb
      * Later see ad for same item on Instagram
      * Advertising company saw cart contents, shared with Instagram
    * **Legal Implications**
      * First party liable for what embedded code collects
      * Privacy regulations (GDPR, CCPA, etc.) apply
      * Risk: Embedded code collecting PII without first party knowing
      * Class action lawsuits when code collects sensitive data (e.g., SSN)
      * First parties must audit third-party code carefully
    * **Business Model**
      * Advertising company likely gets commission on conversions
      * Re-marketing based on shopping cart/browsing behavior
  * **Cookie-Based Tracking**
    * **How Cookies Enable Cross-Site Tracking**
      * Visit Amazon → BlueKai sets cookie in browser
      * Visit Walmart → Browser sends same BlueKai cookie back
      * BlueKai: "Same browser, can correlate visits"
      * Builds profile of browsing history
    * **Cookie Mechanics**
      * Server sends `Set-Cookie` header
      * Browser stores cookie
      * Browser automatically sends cookie back to same domain
      * Third-party cookies sent to third party across multiple first-party sites
    * **Live Demo Attempts**
      * Tried to show cookies in browser inspector
      * Modern browsers (Firefox) blocking cross-site cookies by default
      * Safari also blocking
      * Protection now standard in browsers
    * **Browser Protections**
      * Cross-site cookie blocking (now default in Firefox, Safari)
      * Settings: "Block cross-site cookies"
      * Prevents third party from setting/reading cookies across sites
    * **Cookie Deletion**
      * Common advice: "Delete your cookies"
      * Good practice periodically
      * But NOT sufficient (see fingerprinting below)
  * **Browser Fingerprinting**
    * **Problem**: Even with cookies deleted, still trackable
    * **Concept**: Browser configuration uniquely identifies device
    * **Fingerprinting Attributes**
      * Browser type and version
      * Operating system
      * Screen size and resolution
      * Installed fonts
      * Installed plugins/extensions
      * Graphics card (affects rendering)
      * Language preferences
      * Canvas fingerprinting (how browser renders graphics)
      * Timezone
      * Many other attributes
    * **How JavaScript Accesses This**
      * JavaScript can query browser properties
      * BlueKai script can read fonts, screen size, browser version, etc.
      * Combine attributes → unique fingerprint
    * **Cover Your Tracks Exercise**
      * Website: coveryourtracks.eff.org (Electronic Frontier Foundation)
      * Students run test on their browsers
      * Shows uniqueness of browser fingerprint
      * Identifies which attributes are rare/unique
      * Example results:
        * Canvas hash: 1 in 250 (fairly unique)
        * Screen resolution: 1 in 250
        * Combined: Even more unique
    * **Live Demo Results**
      * Professor's Firefox: Some attributes common, some unique
      * Combination makes browser identifiable
      * Even with privacy protections enabled, still somewhat fingerprintable
    * **Key Insight for Midterm**
      * **Q**: Is deleting cookies sufficient to prevent tracking?
      * **A**: No, because of browser fingerprinting
      * Devices can be uniquely identified without cookies
    * **Defenses**
      * Use common browser configurations (don't customize)
      * Disable JavaScript (breaks most sites)
      * Use Tor Browser (designed to be non-unique)
      * Privacy-focused browsers with anti-fingerprinting
      * Trade-off: Privacy vs functionality
* **Topics Mentioned But Not Covered in Detail**
  * TLS details beyond what was covered in PKI lecture (slides in deck but not tested)
  * Device fingerprinting beyond browser (deferred, overlaps with browser fingerprinting)
* **Possible Midterm Topics**
  * SQL injection: Given code, write attack or identify vulnerable variable
  * SQL injection defenses: Explain how to prevent
  * Same origin policy: What's allowed vs blocked in various scenarios
  * XSS: Explain attack flow, identify vulnerable code
  * CSRF: Explain attack, describe token-based defense
  * Third-party tracking: Explain how tracker sees visits across multiple sites
  * Cookie-based tracking: How it works across sites
  * Browser fingerprinting: Why deleting cookies is insufficient
  * Given diagram/scenario: Explain how tracking works and defenses
* **Debate Topic**: Privacy Omnibus (mentioned but details not in transcript)
* **Break**: Taken around 6:20 PM
* **Topics After Break** (not in this transcript portion)
  * Device privacy (mentioned as next topic, details not provided)

# Meeting 6 

* In-Class Midterm

# Meeting 7

* **Administrative Updates**
  * **Midterm 1 Results**: Grades returned quickly, scores were high
  * **Regrade Policy**: Actual mistakes fixed immediately; discretionary requests will trigger re-reading entire exam
  * **Assignment Policy**: Using LLMs allowed but must acknowledge use and understand submissions
  * **Midterm 2 Preview (Week 9)**
    * Topics: Privacy law (emphasis), compliance enforcement, copyright, AI and privacy, content moderation (light), assignments
    * More assignment questions than Midterm 1
    * Not cumulative (except possibly Assignment 1)
  * **Course Schedule**: Topic 12 (Broadband Infrastructure) removed
* **Lecture Coverage: Privacy Law and Regulation**
  * **Historical Context**
    * Warren & Brandeis (1890): "The Right to Privacy" - response to photography and gossip journalism
    * Pattern: Privacy law reactive to new technology
  * **Computerized Records (1970s)**: Five new privacy threats from mainframe computers
  * **Fair Information Practice Principles (FIPPs) - 1973**
    * Source: HEW report "Records, Computers, and the Rights of Citizens"
    * Foundation for most privacy law worldwide
    * Five principles: (1) No secret record-keeping, (2) Right to know what's collected and how used, (3) Prevent secondary use without consent, (4) Right to correct records, (5) Reasonable security precautions
  * **Re-examining FIPPs**: Old model assumes static data in databases; modern reality involves queries, ML, probabilistic inference
  * **Personally Identifiable Information (PII)**
    * "Surprisingly difficult to define"
    * Clear examples: SSN, name, address
    * Gray area: Zip code, IP address
    * Key insight: "Any information that distinguishes one person from another can be used for re-identifying data"
    * Re-identification attacks: AOL search data, Netflix Prize (Arvind Narayanan), Massachusetts health records (Latanya Sweeney)
  * **US Privacy Law: Sectoral/Patchwork Approach**
    * No comprehensive federal law
    * Laws driven by: who has data, specific harms, data-sharing initiatives
    * Examples: Privacy Act (1974), FCRA (1970), FERPA (1974), Video Privacy Protection Act (1988), Driver's Privacy Protection Act (1994), HIPAA (1996), GLBA (1999), COPPA (1998), GINA (2008)
    * **HIPAA Gap**: Doesn't cover fitness apps, period trackers, mental health apps, 23andMe
    * **Breach Notification**: California 2003 first; now all 50 states have laws
    * **Compliance**: Companies typically apply strictest state law to everyone
  * **FTC - De Facto Privacy Regulator**
    * Primary tool: Section 5 FTC Act ("unfair or deceptive practices")
    * Recent cases: Amazon Prime (settlement), BetterHelp ($7.8M, 2023), GoodRx ($1.5M, 2023), Uber (2017), Facebook ($5B, 2019)
    * Pattern: Cases settle, rarely go to trial
  * **Privacy Principles**
    * Notice, Appropriate Uses, Individual Choice (opt-in vs opt-out), Access and Correction, Security, Minimization
    * Notice and consent model challenges: policies unreadable, implementation diverges from policy
  * **GDPR (European Union)**
    * Omnibus law with extraterritorial reach
    * Applies to any company offering services to EU residents
    * Requirements: consent (opt-in), right to be forgotten, cross-border transfer restrictions, DPIA
    * Enforcement: Major fines (Meta €1.2B 2023, Amazon €746M 2021, Google €90M+ 2021)
    * Debate: Protects privacy or strengthens incumbents? Compliance expensive for small companies
* **Key Concepts for Midterm 2**
  * FIPPs (five principles), PII challenges, sectoral vs omnibus laws, FTC Section 5, opt-in vs opt-out, GDPR scope, breach notification, minimization
* **Debate: Content Moderation** (may appear on Midterm 2)

# Meeting 8

* **Lecture Coverage: Automated Compliance Enforcement with Privacy Laws**
  * **Research Context**
    * Two studies: (1) CCPA compliance measurement, (2) Dark patterns in privacy opt-out
  * **California Consumer Privacy Act (CCPA)**
    * Signed into law June 2018, went into effect January 1, 2020
    * Privacy rights for consumers including right to opt out of sale of personal information
    * **Who is subject**: For-profit entities doing business in California with:
      * Gross revenues > $25 million, OR
      * Buying/selling PI of 50,000+ California consumers, OR
      * At least half of revenue from sale of personal data
  * **California Privacy Rights Act (CPRA)**
    * Passed November 2020 (Proposition 24), went into effect January 1, 2023
    * Amendment to CCPA, added provisions including prohibition of dark patterns in consent
  * **CCPA Requirements (Before CPRA, 2020-2023)**
    * Must have link with specific wording: "Do Not Sell My Personal Information"
    * Must appear in header or footer of webpage
    * Specific words required
  * **CPRA Requirements (January 2023 onward)**
    * Three alternatives for compliance:
      * Link with text "Do Not Sell or Share"
      * Link with text "Limit the Use of My Sensitive Personal Information"
      * Link with text "My Privacy Choices" + specific icon
    * Alternative: "Frictionless opt-out" via Global Privacy Control (GPC)
  * **Global Privacy Control (GPC)**
    * Browser setting that sends opt-out signal to websites
    * Implemented in Firefox, Chrome, and other browsers
    * Most users don't realize they're using it
    * Websites can comply by implementing GPC support
    * Increasingly common over past couple years
* **Study 1: Measuring Website Compliance with CCPA/CPRA**
  * **Research Questions**
    * How did websites respond to opt-out requirements over time?
    * What fraction remain in compliance vs non-compliance?
    * Spillover effect: Do non-California residents benefit? (Brussels/California effect)
    * Who's complying and who's not, and why?
  * **Spillover/California/Brussels Effect**
    * Phenomenon where laws in one jurisdiction benefit users in others
    * California/EU laws may cause companies to implement protections for everyone
    * Companies may find it too difficult to determine user location
    * Simpler to implement one policy for all users
    * Ongoing question in law and policy
  * **Study Methodology**
    * Examined websites from multiple states: California, Virginia, Colorado, Utah, Illinois
    * Virginia, Colorado, Utah enacted privacy laws in 2023
    * Study started mid-2022 - allowed before/after comparison
    * Illinois has no privacy law - control group for spillover analysis
    * Over 1,000 websites measured over time
  * **Automated Compliance Challenges**
    * **Problem 1**: Link may appear in page source but not visible on page
      * JavaScript logic determines whether to display
      * Can't rely on scraping page source alone
      * Must render page to verify visibility
    * **Problem 2**: Link visible on rendered page but not in source
      * Dynamic loading makes it difficult to detect
      * Reasons unclear from source alone
    * **Solution**: Both scrape source AND render page
    * **Detection challenges**: False positives and false negatives in automated detection
  * **Key Findings**
    * **Compliance over time**: Number of sites with opt-out link increased over time
      * Pronounced increase around January 2023 (CPRA enforcement)
    * **Compliance rates**: ~45% of sites had opt-out link
    * **Non-compliance issues**:
      * Text present but not in correct location (header/footer)
      * "Privacy choices" text without required icon
      * Wording doesn't match statute requirements exactly
    * **Spillover evidence**: Illinois websites showed similar opt-out link presence as states with privacy laws
      * Suggests California effect is real
      * Companies implementing for everyone, not just California
    * **GPC adoption**: Smaller fraction used GPC signals
      * Some sites used both opt-out link and GPC
      * Difficult to verify GPC actually works - based on privacy policy claims
      * Statute requires mentioning GPC in privacy policy if implemented
    * **Non-compliance among covered entities**: ~30% of websites subject to CCPA still don't implement opt-out link
    * **Reasons for non-compliance**:
      * 43 sites don't actually sell personal information (technically compliant)
      * Some don't mention CCPA or opt-out rights at all
      * Some mention opt-out methods in privacy policy (may be compliant)
      * Various errors and implementation issues
  * **Limitations**
    * Presence of opt-out link ≠ link is functional
    * Presence ≠ easy to use
    * No verification that opt-out actually prevents data sale
* **Study 2: Dark Patterns in Privacy Opt-Out Processes**
  * **Motivation**: Beyond link presence, examine actual opt-out process difficulty
  * **Dark Patterns Definition**: Deceptive user interfaces designed to trick users
    * Examples throughout various contexts (not just privacy)
    * FTC case: Amazon Prime subscription dark patterns (settled ~1 month ago)
      * Alleged millions of users tricked into subscribing
      * Example: "Do you want item in 2 days or 3 weeks?" → Clicking "2 days" subscribes to Prime
  * **Study Overview**
    * Large-scale measurement of opt-out processes
    * Tested whether opt-out requests actually succeed
    * Analyzed difficulty and user experience
  * **Key Findings - Success Rates**
    * Nearly 1/3 of attempted opt-out requests failed to complete
    * Process varies widely: some sites require just clicks, others require phone calls, mail, extensive paperwork
    * Some sites request additional personal information to opt out (e.g., driver's license)
  * **Opt-Out Control Methods**
    * **Browser-based opt-out**: Pop-up interface (often via OneTrust)
    * **Form-based opt-out**: Fill out form with personal information
    * **Hybrid**: Both methods available
    * **Third-party implementation**: Many sites use OneTrust or similar services
      * Sites pay these companies to maintain compliance
      * Paradoxically, many sites using these services still out of compliance
  * **Metrics Measured**
    * **Number of clicks required**: Ranged from 1 to 14 clicks
    * **Personal information requested**: Address, phone number, etc. required to opt out
    * **Dark patterns present**: Categorized by type
  * **Dark Pattern Categories** (IMPORTANT FOR MIDTERM)
    * **1. Obstruction**
      * Definition: Barriers or hurdles making it difficult to complete task
      * Examples:
        * **CAPTCHA required** to access privacy portal
        * **Mutually exclusive choices**: Can opt out of sale OR sharing, but not both
        * **Asymmetry**: 1 click to opt in, 2 clicks to opt out
          * Provisions in statutes now require symmetry
        * **Identity verification failure**: Request denied if verification not completed within 48 hours
    * **2. Interface Interference**
      * Definition: Manipulation of interface to make discovery difficult
      * Example: Hidden hyperlink on "this form" (hard to see it's clickable)
    * **3. Misdirection**
      * Definition: Instructions confusing or not mentioned
      * Example - **Confusing choices**:
        * Toggle switch unclear whether enabling means opting out or opting in for sale
        * Conflicting text: "opt out of sale" with button labeled "allow sale"
  * **Dark Pattern Prevalence**
    * Most sites have at least one dark pattern
    * Some sites have multiple dark patterns
    * Most common: Obstruction, information overload, unclear request receipt
    * More dark patterns in form-based opt-out than browser-based
  * **Third-Party Compliance Services (OneTrust)**
    * Many sites outsource compliance to companies like OneTrust
    * Sites using OneTrust still frequently out of compliance
    * Reasons unclear - possible explanations:
      * Deployment without configuration
      * Lack of testing
      * Corner cases not handled
      * Misunderstanding of statute requirements
      * Willful disregard vs simple oversight - difficult to determine
    * No litigation yet specifically on dark patterns in privacy opt-out
  * **Enforcement Challenges - Automated Compliance**
    * Some dark patterns clearly violate statute provisions:
      * "Require minimal steps" - violated by 14-click process
      * "Single option" - violated by mutually exclusive choices
      * "Easy to understand" - violated by confusing toggle switches
      * "Symmetry in choice" - violated by asymmetric opt-in/opt-out
      * "Avoid manipulative design" - violated by various dark patterns
    * Other issues ambiguous:
      * CAPTCHAs not mentioned in statute (may have legitimate security purpose)
      * Unclear request receipt not explicitly prohibited
      * Toggle switches not specifically addressed
    * Difficult to automate enforcement decisions
* **Connection to Earlier Concepts**
  * **Informed Consent** (from Lecture 1)
    * Is consent meaningful if obtained through deception?
    * Dark patterns undermine informed consent
    * Respect for persons and autonomy require genuine choice
    * Law and ethics overlap on this issue
* **Break and Debate**
  * 10-minute break taken around 1 hour into class
  * **Debate Topic: AI Accountability**
* **Topics After Debate** (to be covered)
  * Copyright and privacy as it pertains to AI
  * AI-related topics
