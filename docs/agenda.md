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

* Lecture Coverage: Ethics
* Reading Discussion: Bit-by-Bit
   * How do the ethical considerations in this paper apply to the development and deployment of AI systems?
   * What are the implications of the ethical considerations in this paper for the design of privacy-preserving systems?
   * Not Covered: DMCA, SDMI Challenge Case Study, etc. (to be continued in later
     lectures)
   * Possible Midterm Question: Example of Ethical Issue, Apply Ethical Framework
* Debate: Data Breaches
* Authentication
  * Assignment: Public Key Infrastructure
  * PKI Overview
  * Modern Authentication: OAuth
  * Topics NOT covered: symmetric key crypto, legacy cryptosystems, the number
    theory of RSA/public key crypto, etc.


### Meeting 3

* Lecture Coverage: Denial of Service
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
* Debate: Encryption Backdoors
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
     * Purpose and Character of the Use
     * Nature of the Copyrighted Work
     * Amount and Substantiality of the Portion Used
     * Effect of the Use on the Market
   * Reverse Engineering for Interoperability  
   * Possible Midterm Topic: Given a scenario, analyze whether a particular use
     of copyrighted material is likely to be considered fair use. Consider
     recent software copyright cases (Google v. Oracle, Splunk v. Cribl, etc.)
* CPRA Compliance and Automated Compliance Checking
   * Requirements for Opt-Out Links
   * Spillover Effect
   * CPRA
     * Overview
     * Key Provisions
     * Automated Compliance Checking
* Debate: Content Moderation
