# Midterm Exam Preparation Guide

**Security, Privacy, and Consumer Protection**

This guide covers all material from the beginning of the course through **Privacy Law and Protections** (Meeting 11).

---

## Table of Contents

1. [Ethics & Research](#ethics--research)
2. [Cryptography Foundations](#cryptography-foundations)
3. [Public Key Infrastructure](#public-key-infrastructure)
4. [Authentication & Access Control](#authentication--access-control)
5. [OAuth](#oauth)
6. [Denial of Service Attacks](#denial-of-service-attacks)
7. [DNS Security and Privacy](#dns-security-and-privacy)
8. [Web Security](#web-security)
9. [Web Privacy & Tracking](#web-privacy--tracking)
10. [Privacy Law](#privacy-law)
11. [Practice Questions](#practice-questions)

---

## Ethics & Research

### Belmont Report Principles

The Belmont Report outlines three core ethical principles for research involving human subjects:

1. **Respect for Autonomy**
   - Individuals should be treated as autonomous agents
   - Informed consent is required
   - People have the right to make their own decisions about participation
   - **Example**: Snowden's belief that individuals have a right to know how their personal information is being used

2. **Beneficence**
   - Maximize benefits and minimize harm
   - Research should benefit participants or society
   - Must consider both potential benefits and risks
   - **For**: hiQ Labs' data analysis could improve workplace policies
   - **Against**: Privacy violations may outweigh benefits

3. **Justice**
   - Fair distribution of benefits and burdens of research
   - No group should bear disproportionate risks
   - Benefits should be distributed fairly

### Institutional Review Board (IRB)

- IRB approval does NOT guarantee that a study is ethical
- IRB reviews help ensure research meets ethical standards
- Researchers still have ethical responsibilities beyond IRB approval

### Key Case Studies

**hiQ Labs vs. LinkedIn**:
- hiQ scraped publicly available LinkedIn data
- LinkedIn objected citing terms of service and privacy
- Raises questions about:
  - Public vs. private data
  - Terms of service enforcement
  - CFAA applicability to public data
  - Competition and data access

**Edward Snowden**:
- Released classified NSA surveillance information
- Revealed indiscriminate surveillance without consent
- Ethical principle: Respect for Autonomy
- Tension between national security and privacy rights

---

## Cryptography Foundations

### Trusting Trust

**Key Concept**: You can't trust code that you didn't completely create yourself

- Compilers can be compromised to inject backdoors
- Even reviewing source code may not reveal vulnerabilities
- Backdoors can persist through multiple generations of compilation
- **Implication**: Trust must be established at multiple levels of the software stack

### Why Cryptosystems Fail

Common reasons for cryptographic system failures:

1. **Implementation errors** - bugs in code
2. **Protocol flaws** - design mistakes
3. **Key management problems** - poor key storage or distribution
4. **Human factors** - usability issues leading to misuse
5. **Side-channel attacks** - timing, power analysis
6. **Social engineering** - attacking the human element

### Kerckhoff's Principle

**"A cryptosystem should be secure even if everything about the system, except the key, is public knowledge"**

- Security should rely on key secrecy, not algorithm secrecy
- Public algorithms can be vetted by experts
- Proprietary "security through obscurity" is not reliable
- Modern standard: Use well-tested, public algorithms (AES, RSA)

---

## Public Key Infrastructure

### Symmetric vs. Asymmetric Cryptography

**Symmetric Cryptography**:
- Same key for encryption and decryption
- Fast and efficient
- **Problem**: Key distribution/exchange
- **Example**: AES
- **Use case**: Bulk data encryption

**Asymmetric Cryptography**:
- Public key (encrypt) + Private key (decrypt)
- Slower than symmetric
- Solves key distribution problem
- **Example**: RSA
- **Use cases**:
  - **Confidentiality**: Encrypt with public key, decrypt with private key
  - **Integrity/Authentication**: Sign with private key, verify with public key

### Diffie-Hellman Key Exchange

- Allows two parties to establish a shared secret over an insecure channel
- Based on discrete logarithm problem (hardness assumption)
- **Does NOT provide authentication** - vulnerable to man-in-the-middle
- Public exchange of values allows computation of shared secret

### Digital Signatures

- Provide **integrity** and **authenticity**
- Process:
  1. Hash the message
  2. Encrypt hash with private key → signature
  3. Recipient decrypts with public key and verifies hash
- **Use cases**: Software updates, document signing, certificate signing

### Certificates and Certificate Authorities

**Purpose**: Bind an entity's identity to their public key

**Certificate Components**:
- Subject (who the certificate is for)
- Public key
- Issuer (who signed it)
- Validity period
- Digital signature from CA

**Types of Certificates**:

1. **Self-Signed Certificate**:
   - Entity signs their own certificate
   - No third-party verification
   - Browsers show warnings
   - **Still encrypts traffic** but provides no authentication

2. **CA-Signed Certificate**:
   - Signed by a trusted Certificate Authority
   - CA verifies identity before issuing
   - Browser trusts it if CA is in root store

**Validation Levels**:

1. **Domain Validation (DV)**:
   - Proves control over a domain
   - Example: Let's Encrypt
   - Automated validation (place file on web server)

2. **Extended Validation (EV)**:
   - Proves legal entity identity
   - More rigorous verification process
   - Example: Bank websites

### Certificate Chains and Trust

**Chain of Trust**:
```
Website Certificate
    ↓ (signed by)
Intermediate CA
    ↓ (signed by)
Root CA (in OS trust store)
```

**Root Certificate Authorities**:
- Stored in operating system's trusted certificate store
- Pre-installed on devices
- Browsers and applications reference this store
- If compromised, attacker can impersonate any site

**Trust Dependencies**:
- Integrity of Root CAs
- Security of Root CAs' private keys
- Proper verification by CAs before issuing certificates
- Certificate revocation mechanisms

**Rogue Root CA Scenario**:
- If attacker installs rogue root CA on your machine:
  - Can decrypt past and future traffic (if MitM position)
  - Can impersonate any server to clients
  - Server cannot prevent this by revoking its certificate

### TLS/HTTPS in Practice

**TLS Handshake**:
1. Client connects, server sends certificate
2. Client verifies certificate chain
3. Key exchange (establish session key)
4. Switch to symmetric encryption for session

**Why Use Both Symmetric and Asymmetric?**:
- Asymmetric (RSA) for key exchange and authentication
- Symmetric (AES) for fast bulk data encryption

**TLS 1.2 vs. TLS 1.3**:
- TLS 1.3 encrypts more of the handshake
- Encrypted SNI (Server Name Indication) for better privacy

### Cryptographic Hash Functions

**Properties**:
1. **Collision Resistance**: Hard to find two inputs with same hash
2. **Preimage Resistance**: Given hash, hard to find original input
3. **Second Preimage Resistance**: Given input x, hard to find x' with same hash
4. **One-way**: Easy to compute, hard to reverse

**Common Uses**:
- Password storage (with salt)
- Data integrity verification
- Digital signatures
- Message authentication codes (HMAC)

**Rainbow Table Defense**:
- Add **salt** (random data) to passwords before hashing
- Each password gets unique salt
- Makes precomputed tables infeasible

---

## Authentication & Access Control

### Three Modes of Authentication

1. **Something You Know**
   - Passwords, PINs, security questions
   - Vulnerable to: guessing, phishing, keylogging
   - Example: 4-digit PIN for credit card

2. **Something You Have**
   - Physical keys, ID cards, security tokens, smartphones
   - 2FA tokens, UB keys
   - Vulnerable to: theft, loss
   - Example: RSA SecurID token

3. **Something You Are**
   - Biometrics: fingerprints, facial recognition, iris scans
   - Vulnerable to: spoofing, privacy concerns
   - Cannot be changed if compromised
   - Example: Touch ID, Face ID

**Multi-Factor Authentication (MFA)**: Combining multiple modes increases security

### Unix File Permissions

**Permission Structure**: `-rwxr-xr-x`
- First character: file type (`-` = file, `d` = directory)
- Next 3: owner permissions (read, write, execute)
- Next 3: group permissions
- Last 3: world (others) permissions

**Permission Bits**:
- `r` (4): Read
- `w` (2): Write
- `x` (1): Execute

**Examples**:
- `-rw-r--r--` (644): Owner can read/write, others can only read
- `-rwxr-xr-x` (755): Owner can read/write/execute, others can read/execute
- `drwxr-xr-x`: Directory with similar permissions

### Processes and Privileges

- Processes run as specific users
- OS mediates access based on process user
- Check with: `ps`, `whoami`, `groups`

**Special Users**:
- **root/superuser**: Ultimate privileges, can access everything
- Web servers should NOT run as root

**sudo**: "Super User Do"
- Temporarily elevate privileges
- Requires authentication
- Logged for auditing

### Principle of Least Privilege

**Definition**: Grant only the minimum privileges necessary to perform a task

**Examples**:
- Web servers run as limited user (not root)
- OAuth scopes limit what apps can access
- Database users with restricted permissions
- Containerization and sandboxing

**Privilege Escalation**:
- Vulnerability allowing process to gain higher privileges
- Major security concern
- Example: Buffer overflow leading to root access

### Access Control Models

**Discretionary Access Control (DAC)**:
- Users control access to their own resources
- Example: Unix permissions, Facebook privacy settings
- Owners can grant/revoke access

**Mandatory Access Control (MAC)**:
- System administrator sets policies regardless of ownership
- More rigid and secure
- Example: SELinux, military classifications
- Users cannot override policies

**Role-Based Access Control (RBAC)**:
- Access based on roles (e.g., student, staff, admin)
- Easier to manage in large organizations
- Example: Course repository access
- Users assigned to roles, roles have permissions

---

## OAuth

### Problems with Password Sharing

**Traditional approach**: Give third-party app your password

**Issues**:
- App has full access to your account
- Can't revoke access to one app without changing password
- Poor auditability (can't track which app did what)
- Security risk if app is compromised
- Violates principle of least privilege

### OAuth Solution

**Goal**: Delegate access without sharing credentials

**Key Features**:
- No password sharing
- Limited scope (specific permissions)
- Revocable access
- Better auditability

### OAuth Roles

1. **Resource Owner**: User who owns the protected data
2. **Client**: Third-party application requesting access
3. **Authorization Server**: Issues tokens (e.g., GitHub, Google)
4. **Resource Server**: Hosts the protected resources

### OAuth Flow

1. **Client requests authorization** from Resource Owner
2. **Resource Owner logs in** to Authorization Server and approves request
3. **Authorization Server** returns **authorization code** to Client
4. **Client exchanges authorization code** for **access token**
5. **Client uses access token** to access Resource Server

**Example**: Slack requesting access to your GitHub repositories

### Access Token Scoping

- Tokens encode specific permissions
- **Examples**:
  - `repo` - Full repository access
  - `read:user` - Read user profile
  - `public_repo` - Only public repositories
- Implements principle of least privilege
- Can set expiration times
- Can be revoked individually

### Key Concepts

- **Authorization Grant**: Temporary code proving user consent
- **Access Token**: Credential representing delegated permissions
- **Scope**: Set of permissions associated with token
- **Refresh Token**: Used to obtain new access tokens without re-authorization

---

## Denial of Service Attacks

### Definition

Attempt to exhaust limited resources in a system to deny service to legitimate users

### Types of Resources that Can Be Exhausted

1. **Network Bandwidth**
   - Saturate network link capacity
   - Example: 1 Gbps link flooded with traffic

2. **Connection Resources**
   - Maximum simultaneous connections
   - Example: TCP SYN flood

3. **Server Resources**
   - CPU, memory, disk I/O
   - Example: Expensive computations (TLS handshakes)

### Common Targets

- Web servers (most common)
- DNS servers
- Authentication services (e.g., Duo)
- Update servers
- File servers

### Three Characteristics of DoS Attacks

1. **Asymmetry**
   - Attacker's cost << Victim's cost
   - **Examples**:
     - Small packet triggers server to allocate memory
     - Small query generates large response (amplification)
     - Single attacker controls botnet of thousands

2. **Difficulty Distinguishing Legitimate from Attack Traffic**
   - Attack traffic looks like normal requests
   - Hard to filter without blocking legitimate users
   - Example: HTTP GET requests from botnet

3. **Difficulty of Attribution**
   - IP address spoofing common
   - Attacker doesn't need to receive responses
   - Hard to trace back to original source
   - Distributed attacks from many sources

### Case Study: Mirai Botnet (October 2016)

**Target**: Dyn (DNS infrastructure provider)

**Impact**: Major outages for Twitter, Netflix, Spotify, Reddit, etc.

**Attack Vector**:
- Targeted DNS servers, not end services
- Taking down DNS infrastructure affects all dependent services

**Botnet Composition**:
- Compromised IoT devices (cameras, home devices)
- ~100,000 endpoints (relatively small)
- "Army of vulnerable gadgets"

**Why Effective**:
- Application-level attack (not just bandwidth)
- Exhausted DNS query processing capacity
- Relatively low total traffic volume

**Death Spiral Effect**:
1. Attack traffic overloads DNS servers
2. Legitimate users can't resolve domains
3. Applications retry automatically (by design)
4. Legitimate retries amplify the attack
5. Impossible to distinguish attack from legitimate retries

**Lessons**:
- Critical infrastructure dependencies create cascading failures
- Easier to attack infrastructure than individual services
- Legitimate traffic patterns can amplify attacks

### DNS Reflection and Amplification Attack

**How It Works**:
1. Attacker sends small DNS query to open DNS resolver
2. Query has **spoofed source IP** (victim's address)
3. DNS server generates **large response**
4. Large response sent to victim (not attacker)

**Amplification Factor**: 60x to 3,000x possible

**Key Techniques**:
- **Reflection**: Bounce traffic off third party
- **Amplification**: Small query → large response
- **IP Spoofing**: Victim receives response they never requested

**Why Effective**:
- Asymmetry: Small queries, large responses
- IP spoofing: Hard to trace
- Can use many DNS servers simultaneously (distributed)

**Defense: Stateful Firewall**:
- Track outgoing DNS queries
- Drop incoming responses that don't match outgoing queries

**New Vulnerability**:
- Firewall must maintain state (memory)
- Attacker can exhaust firewall memory
- Send spoofed queries through firewall
- Firewall remembers, runs out of memory, crashes

**Defense Against Firewall Attack**:
- **Ingress filtering**: Check if packet source matches expected direction
- Drop packets claiming to be from inside but arriving from outside

**Open Resolvers**:
- DNS servers that answer queries from anyone
- Examples: Google (8.8.8.8), Cloudflare (1.1.1.1)
- Can be used for reflection attacks
- Misaligned incentives: Secure your server to protect others

### Security Principle

**Any defense requiring state introduces new attack surface**
- Stateful systems have limited memory
- Limited memory = potential DoS target
- Tradeoff: Security features vs. new vulnerabilities
- Always ask: "Have I introduced new vulnerabilities?"

---

## DNS Security and Privacy

### DNS Basics Review

- Translates domain names to IP addresses
- Hierarchical system
- Uses UDP port 53 (typically)
- Originally unencrypted and unauthenticated

### Security Risks

**DNS Cache Poisoning**:
- Attacker injects false DNS records into cache
- Victims redirected to malicious sites
- **Kaminsky Attack**: Discovered vulnerability allowing easy cache poisoning
- **Defense**: DNSSEC

**DNSSEC (DNS Security Extensions)**:
- Cryptographically signs DNS records
- Provides authentication and integrity
- Verifies DNS responses haven't been tampered with
- **Does NOT provide confidentiality** (queries still visible)

### Privacy Risks

**Unencrypted DNS reveals**:
- Which domains you're visiting
- Browsing patterns and habits
- Can be seen by:
  - ISP
  - Local network operator (WiFi owner)
  - Anyone monitoring network traffic

**Website Fingerprinting**:
- Even with HTTPS, DNS queries reveal sites visited
- Traffic analysis can identify specific pages
- Timing and size patterns leak information

### Privacy Protections

**DNS-over-TLS (DoT)**:
- Encrypts DNS queries using TLS
- Port 853
- Hides queries from network observers

**DNS-over-HTTPS (DoH)**:
- Encrypts DNS queries in HTTPS traffic
- Uses standard port 443
- Harder to block than DoT
- Implemented in modern browsers

### DNS-over-HTTPS Tradeoffs

**Privacy Improvements**:
- Local network operator can't see DNS queries
- ISP can't see DNS queries
- Protects against surveillance and tracking
- Prevents DNS-based filtering

**Privacy Concerns**:
- Centralizes DNS queries to specific providers (e.g., Cloudflare, Google)
- DoH provider can now see all your queries
- Creates new tracking opportunity
- If provider compromised, affects many users

**When Encrypted DNS is Enabled**:
- Local WiFi operator **CANNOT** see domain names you're visiting
- Still see IP addresses and traffic patterns
- DoH provider **CAN** see all queries

---

## Web Security

### Same-Origin Policy (SOP)

**Definition of Origin**: Combination of protocol + hostname + port

**Examples**:
- `http://example.com:80` ≠ `https://example.com:443` (different protocol AND port)
- `http://example.com` ≠ `http://api.example.com` (different hostname)
- `http://example.com:80` = `http://example.com` (default ports match)

**Purpose**:
- Prevents scripts from one origin accessing data from another
- Isolates web applications
- Foundation of web security

**What SOP Restricts**:
- JavaScript access to DOM of other origins
- Reading responses from other origins
- Access to cookies and storage of other origins

**What SOP Allows**:
- Loading resources (images, scripts) from other origins
- Submitting forms to other origins
- Navigation to other origins

### Cross-Origin Resource Sharing (CORS)

**Purpose**: Relax SOP in controlled way

**Mechanism**:
- Server sends `Access-Control-Allow-Origin` header
- Specifies which origins can access resources
- Browser enforces the policy

**Example**:
```
Access-Control-Allow-Origin: https://trusted-site.com
```

### Cross-Site Scripting (XSS)

**Definition**: Injecting malicious scripts into trusted websites

**Types**:

1. **Reflected XSS**:
   - Script in URL parameter
   - Server echoes it back to user
   - Example: `?search=<script>alert('XSS')</script>`

2. **Stored XSS**:
   - Script stored in database
   - Displayed to other users
   - Example: Forum post with malicious script

3. **DOM-based XSS**:
   - Vulnerability in client-side JavaScript
   - Never sent to server

**Example Attack**:
```
https://example.com/displayMessage?message=<script>document.body.style.color='red';</script>
```

**Impact**:
- Steal cookies and session tokens
- Deface website
- Redirect users
- Steal sensitive information

**Defenses**:

1. **Input Sanitization**:
   - Remove or encode dangerous characters
   - Escape `<`, `>`, `"`, `'`, `&`

2. **Input Validation**:
   - Whitelist allowed characters
   - Reject unexpected input

3. **Output Encoding**:
   - Escape output in HTML templates
   - Use framework's built-in encoding

4. **Content Security Policy (CSP)**:
   - HTTP header restricting script sources
   - Prevents inline scripts

### Cross-Site Request Forgery (CSRF)

**Definition**: Attacker tricks victim into making unwanted requests to a site where they're authenticated

**Example**:
User logged into `bank.com`, visits malicious site that submits:
```html
<form action="https://bank.com/transfer" method="POST">
  <input name="to" value="attacker">
  <input name="amount" value="1000">
</form>
<script>document.forms[0].submit();</script>
```

**Why It Works**:
- Browser automatically includes cookies
- Server sees legitimate session cookie
- Request appears to come from authenticated user

**GET Request CSRF**:
```html
<img src="https://bank.com/transfer?to=attacker&amount=1000">
```

**Defenses**:

1. **CSRF Tokens**:
   - Server generates random token
   - Include in form as hidden field
   - Verify token on submission
   - Attacker can't guess or access token

2. **SameSite Cookie Attribute**:
   - `SameSite=Strict`: Never sent cross-origin
   - `SameSite=Lax`: Sent for top-level navigation

3. **Check Referer Header**:
   - Verify request came from your site
   - Can be spoofed or stripped

4. **Use POST Instead of GET**:
   - Doesn't prevent CSRF, but makes it harder
   - Forms require POST

**Why XSS Bypasses CSRF Protection**:
- Malicious script runs in same origin
- Can access DOM and read CSRF token
- Can make requests that appear legitimate

### SQL Injection

**Definition**: Injecting SQL commands into database queries

**Example Vulnerable Code**:
```python
query = "SELECT * FROM users WHERE username='" + username + "' AND password='" + password + "'"
```

**Attack**:
```
username: admin' --
password: (anything)
```

**Resulting Query**:
```sql
SELECT * FROM users WHERE username='admin' -- ' AND password='...'
```

**Defenses**:

1. **Prepared Statements/Parameterized Queries**:
   ```python
   query = "SELECT * FROM users WHERE username=? AND password=?"
   cursor.execute(query, (username, password))
   ```

2. **Input Validation**:
   - Whitelist allowed characters
   - Type checking

3. **Escape Special Characters**:
   - Use database library's escaping functions
   - Still less safe than prepared statements

4. **Principle of Least Privilege**:
   - Database user should have minimal permissions
   - Read-only where possible

**Similar Defense**: Data Execution Prevention (DEP) for code injection

---

## Web Privacy & Tracking

### Third-Party Trackers

**How Tracking Works**:

1. **Third-Party Cookies**:
   - Site A embeds tracker from tracker.com
   - tracker.com sets cookie in browser
   - Site B also embeds tracker.com
   - Same cookie allows tracking across sites

**Example**:
```
Visit news.com → tracker.com sets cookie "user123"
Visit shopping.com → tracker.com reads cookie "user123"
→ tracker.com knows same user visited both sites
```

2. **Tracking Pixels**:
   - 1x1 invisible image
   - Loaded from tracking domain
   - Allows tracking without JavaScript

3. **JavaScript Trackers**:
   - More sophisticated tracking
   - Can collect detailed information
   - Examples: Google Analytics, Facebook Pixel

**Who Can Track**:
- Advertising networks
- Analytics providers
- Social media platforms (like buttons)
- CDN providers

### Browser Fingerprinting

**Definition**: Creating unique identifier from browser/device configuration

**Techniques**:

1. **Basic Information**:
   - User agent string
   - Screen resolution
   - Time zone
   - Language preferences
   - Installed fonts

2. **Hardware Information**:
   - CPU cores
   - Available memory
   - Graphics card details

3. **Browser Features**:
   - Installed plugins
   - Supported MIME types
   - WebGL capabilities

4. **Canvas Fingerprinting**:
   - Render text/graphics to hidden canvas
   - Extract image data
   - Tiny rendering differences create unique hash
   - Different hardware/drivers produce different results

**Why Effective**:
- Combination of attributes creates unique fingerprint
- Works even after deleting cookies
- No storage on user's device required
- Difficult to detect

**Does Deleting Cookies Prevent Tracking?**
- **NO** - Browser fingerprinting persists
- Fingerprint remains same across sessions
- Would need to change device/browser configuration

### Tracking Defenses

**User Defenses**:
1. **Cookie Blocking**:
   - Block third-party cookies
   - Clear cookies regularly

2. **Browser Extensions**:
   - Privacy Badger
   - uBlock Origin
   - Disconnect

3. **Private Browsing Mode**:
   - Isolates session
   - Clears cookies after closing
   - Doesn't prevent fingerprinting

4. **Tor Browser**:
   - Routes through anonymizing network
   - Standardizes fingerprint
   - Makes users look identical

**Browser Features**:
- Tracking Protection (Firefox)
- Intelligent Tracking Prevention (Safari)
- Enhanced Tracking Protection

**Legal Protections**:
- GDPR (Europe)
- CCPA/CPRA (California)
- Cookie consent requirements

---

## Privacy Law

### Privacy Principles

**Key Concepts**:
1. **Notice**: Users should know what data is collected
2. **Choice**: Users should control their data
3. **Access**: Users should access their data
4. **Security**: Data should be protected
5. **Accountability**: Organizations responsible for compliance

### California Privacy Rights Act (CPRA)

**Expansion of CCPA (California Consumer Privacy Act)**

**Key Rights**:

1. **Right to Know**:
   - What personal information is collected
   - How it's used
   - With whom it's shared

2. **Right to Delete**:
   - Request deletion of personal information
   - Some exceptions apply

3. **Right to Opt-Out**:
   - Sale of personal information
   - Sharing for cross-context behavioral advertising
   - "Do Not Sell or Share My Personal Information" link required

4. **Right to Correct**:
   - Inaccurate personal information

5. **Right to Limit**:
   - Use of sensitive personal information

**Requirements for Websites**:
- Clear privacy policy
- Opt-out mechanisms (links on homepage)
- Response to user requests within timeframe
- Cannot discriminate against users who exercise rights

**Spillover Effect**:
- Companies often apply CPRA to all users, not just Californians
- Easier than maintaining separate systems
- Similar to GDPR's global impact

### GDPR (General Data Protection Regulation)

**European Union regulation with global impact**

**Key Principles**:
- Data minimization
- Purpose limitation
- Storage limitation
- Accuracy
- Integrity and confidentiality

**Similar Rights to CPRA**:
- Right to access
- Right to rectification
- Right to erasure ("right to be forgotten")
- Right to data portability
- Right to object to processing

**Higher Penalties**:
- Up to 4% of global revenue
- Stronger enforcement than CPRA

### Automated Compliance Checking

**Challenge**: Verifying websites comply with privacy laws at scale

**Techniques**:
- Automated crawling for opt-out links
- Checking cookie consent mechanisms
- Analyzing privacy policies
- Monitoring data flows

**Example**: Checking for required "Do Not Sell My Personal Information" links

---

## Practice Questions

### Multiple Choice

**Question 1**: Which ethical principle is most closely related to informed consent?
- A. Justice
- B. Beneficence
- C. Respect for Autonomy ✓
- D. Accountability

**Question 2**: What aspects of security does a digital signature provide? (Select all that apply)
- A. Confidentiality
- B. Integrity ✓
- C. Availability
- D. Authenticity ✓

**Question 3**: Which of the following correctly describes the Same-Origin Policy?
- A. The combination of protocol, hostname, and port ✓
- B. The domain name only
- C. The IP address only
- D. The protocol only

**Question 4**: Which are characteristics of DoS attacks? (Select all that apply)
- A. Often launched from multiple sources ✓
- B. Traffic difficult to distinguish from legitimate ✓
- C. Often involve amplification ✓
- D. Always involve bandwidth exhaustion

**Question 5**: When encrypted DNS (DoH) is enabled in your browser, can the local WiFi operator see which domains you're visiting?
- A. Yes
- B. No ✓

**Question 6**: Does deleting cookies after every visit prevent a website from tracking you?
- A. Yes
- B. No ✓

### True/False

**Question 7**: Diffie-Hellman key exchange provides authentication between parties.
- **False** - It only establishes a shared secret, vulnerable to MitM

**Question 8**: A self-signed certificate can still encrypt traffic between client and server.
- **True** - Encryption works, but no authentication

**Question 9**: IRB approval of a research study guarantees that the study is ethical.
- **False** - IRB helps but doesn't guarantee ethics

**Question 10**: In OAuth, access tokens can be scoped to limit permissions.
- **True**

### Short Answer

**Question 11**: Name three modes of authentication and give an example of each.
- **Answer**:
  1. Something you know: password, PIN
  2. Something you have: security token, smartphone, ID card
  3. Something you are: fingerprint, facial recognition, iris scan

**Question 12**: Explain why DNS reflection attacks are effective from an attacker's perspective.
- **Answer**: DNS reflection attacks satisfy key DoS characteristics:
  - Asymmetry: Small query produces large response (amplification)
  - Attribution difficulty: Attacker spoofs victim's IP, DNS server sends response to victim
  - Can use many DNS servers simultaneously for distributed attack
  - Attacker's cost is minimal compared to impact on victim

**Question 13**: What is Kerckhoff's Principle?
- **Answer**: A cryptosystem should be secure even if everything about the system, except the key, is public knowledge. Security should rely on key secrecy, not algorithm secrecy.

**Question 14**: Describe how a CSRF attack works and name one defense.
- **Answer**: CSRF tricks an authenticated user into making unwanted requests. Attacker creates malicious page that submits requests to target site. Browser automatically includes cookies, so server sees legitimate session. Defense: CSRF tokens - server generates random token included in form, verified on submission. Attacker cannot access or guess token.

**Question 15**: Why does browser fingerprinting work even after deleting cookies?
- **Answer**: Browser fingerprinting creates a unique identifier from browser/device configuration (screen resolution, fonts, plugins, hardware details, etc.). These characteristics don't change when cookies are deleted, so the fingerprint persists across sessions.

### Scenario-Based Questions

**Question 16**: You visit a website using HTTPS, but your browser shows a warning about the certificate. What might cause this?

**Possible answers**:
- Self-signed certificate
- Certificate from untrusted CA
- Expired certificate
- Certificate for wrong domain (name mismatch)
- Certificate revoked

**Question 17**: An attacker installs a rogue root CA on your computer. What attacks are now possible?

**Answer**:
- Attacker can issue fake certificates for any website
- Can decrypt your HTTPS traffic (if in MitM position)
- Can impersonate any server to your browser
- Server cannot prevent this by revoking its real certificate

**Question 18**: A website displays user-submitted comments without sanitization. What vulnerability does this create and what attack is possible?

**Answer**:
- Vulnerability: Cross-Site Scripting (XSS)
- Attack: Stored XSS - attacker posts comment with malicious script
- When other users view the comment, script executes in their browser
- Can steal cookies, session tokens, or perform actions as the victim

**Question 19**: Explain the privacy tradeoff when using DNS-over-HTTPS.

**Answer**:
- **Improved privacy**: Local network operator and ISP can no longer see DNS queries
- **New privacy concern**: DNS queries now centralized to DoH provider (Cloudflare, Google, etc.)
- **Tradeoff**: Hide queries from local observers but trust new entity with all queries
- If DoH provider is compromised, affects many users at once

**Question 20**: You're designing a web application. How would you implement protection against both XSS and CSRF?

**Answer**:
- **XSS Protection**:
  - Sanitize all user input (remove/encode dangerous characters)
  - Escape output in HTML templates
  - Use Content Security Policy headers
  - Validate input against whitelist
- **CSRF Protection**:
  - Implement CSRF tokens (unique per session)
  - Verify token on form submission
  - Use SameSite cookie attribute
  - Check Referer header
  - Use POST for state-changing operations

**Note**: XSS can bypass CSRF protection because malicious script runs in same origin and can read CSRF token, so both protections are necessary.

---

## Key Formulas and Concepts to Remember

### Security Properties (CIA Triad)

- **Confidentiality**: Preventing unauthorized disclosure
- **Integrity**: Preventing unauthorized modification
- **Availability**: Ensuring authorized access when needed
- **Authenticity**: Verifying identity/origin
- **Accountability**: Ability to trace actions to entities

### Common Attack Patterns

| Attack Type | Target | Defense |
|------------|--------|---------|
| Buffer Overflow | Memory | DEP, ASLR, Stack Canaries |
| SQL Injection | Database | Prepared Statements |
| XSS | Web Client | Sanitization, Escaping |
| CSRF | Web Server | CSRF Tokens, SameSite |
| DoS | Resources | Rate Limiting, Filtering |
| MitM | Communications | TLS/HTTPS, Certificate Validation |

### Remember These Acronyms

- **PKI**: Public Key Infrastructure
- **CA**: Certificate Authority
- **TLS**: Transport Layer Security
- **DoS/DDoS**: Denial of Service / Distributed DoS
- **XSS**: Cross-Site Scripting
- **CSRF**: Cross-Site Request Forgery
- **SOP**: Same-Origin Policy
- **CORS**: Cross-Origin Resource Sharing
- **DoH**: DNS-over-HTTPS
- **DoT**: DNS-over-TLS
- **GDPR**: General Data Protection Regulation
- **CPRA**: California Privacy Rights Act

---

## Study Tips

1. **Understand concepts, not just memorize**
   - Focus on "why" things work, not just "what"
   - Be able to explain tradeoffs

2. **Practice with scenarios**
   - Given a situation, identify vulnerabilities
   - Propose defenses and explain limitations

3. **Know the relationships**
   - How do different topics connect?
   - Example: How XSS bypasses CSRF protection

4. **Review prior midterms**
   - See question formats and topics emphasized
   - Practice similar questions

5. **Do the assignments**
   - Hands-on experience reinforces concepts
   - Labs show practical applications

6. **Make connections to real world**
   - Remember case studies (Mirai, DigiNotar, Snowden)
   - Think about how concepts apply to systems you use

---

Good luck on your midterm!
