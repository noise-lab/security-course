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

* **Topics to Cover from Last Time**
  * Apple Private Relay
  * Session key that is exchanged in ODNS
  * RPKI bootstrapping question: How do you reach RPKI servers without validated BGP routes? (Answer: Use static routes, IGP routes, or deploy validators inside your network to avoid circular dependency)
* Debate: Privacy Omnibus
* Lecture Coverage
   * Web Tracking
     * Third-Party Web Trackers
     * How tracking works
     * Tracking defenses (plugins, etc.)
     * Legal issues?
   * Browser Fingerprinting
     * How it works
       * "Canvas Fingerprinting"
     * Defenses
* Possible Midterm Topic: Given a diagram/scenario, explain/draw how a tracking
  system works, and how it could be defended against.
* NOT Covered This Year: 09-Surveillance.ppt topics, in particular, third-party metadata
  inference, etc. (skipped entirely this year)

# Meeting 6 

* In-Class Midterm

# Meeting 7

* Debate: Copyright
* Software Copyright and Fair Use
   * Fair Use Principles
     * Purpose and Character of the Use (Is the use "transformative"?)
     * Nature of the Copyrighted Work (Factual vs. Creative)
     * Amount and Substantiality of the Portion Used (How much was used?)
     * Effect of the Use on the Market (Does it compete with the original?)
   * Reverse Engineering for Interoperability (Sega v. Accolade, Google v. Oracle)  
   * Possible Midterm Topic: Given a scenario, analyze whether a particular use
     of copyrighted material is likely to be considered fair use. Consider
     recent software copyright cases (Google v. Oracle, Splunk v. Cribl,
     etc.). Or, a hypothetical scenario (involving AI?)
* CPRA Compliance and Automated Compliance Checking
   * Requirements for Opt-Out Links
   * Spillover Effect
   * CPRA
     * Overview
     * Key Provisions
     * Automated Compliance Checking
* Debate: Content Moderation

# Meeting 8

* Internet Censorship
   * Censorship in China
   * The Great Firewall
* Why filtering may not be as effective at censorship as other techniques
* Backlash effects of censorship (installation of VPNs)
* Virtual Private Networks: How they work, the kinds of protections that they
  do or do not provide
* Possible Midterm Topic: Give examples of censorship by fear, friction, and
  flooding. Analyze the effectiveness of each.
* Debate: Censorship
