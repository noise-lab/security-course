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
* Lecture Coverage: Denial of Service (To be continued)
* Typical Characteristics of DoS Attacks
  * Asymmetry
  * Difficulty of Attribution (IP Spoofing)
  * Difficulty of Distinguishing Legitimate from Attack Traffic
* Case Study: Mirai Botnet
  * DNS basics
  * Difficulty of mitigation, attribution
* Common defenses
  * Rate limiting
  * Captchas
* Possible Midterm Question: Example Recent DoS Attack, Analyze
  characteristics, propose mitigations
* Not covered: Technical details of TCP SYN Flood attacks, TCP handshake, TCP
  SYN cookies, etc. Details of defending against TCP-based attacks.
* More Denial of Service/Botnets
  * DNS Amplification
  * Traffic Injection (Great Cannon)
* Possible Midterm Topic: Present a reflection attack, analyze, ask about
  possible defenses.

### Meeting 4

* Lecture Coverage: DNS Security and Privacy
   * Background on DNS
   * Security Risks
     * DNS Cache Poisoning
   * Privacy Risks
     * Domain privacy
     * Website fingerprinting  
   * Defenses
     * DNS-over-TLS
     * DNSSEC
     * DNS-over-HTTPS
* Debate: CFAA
* Lecture Coverage: Web Security and Privacy
   * Web Architecture 
   * Same-Origin Policy
   * Cross-Origin Resource Sharing
   * Cross-Site Scripting, Cross-Site Request Forgery
   * Website Fingerprinting

# Meeting 5

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
