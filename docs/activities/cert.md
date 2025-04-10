## Who Do You Trust? Digging Into Certificate Chains

### 1. Overview

Every time you visit a website over HTTPS, your browser uses digital certificates to verify that the server is who it claims to be. But where does that trust come from? Who says the certificate is valid? And what happens if something goes wrong?

In this activity, you’ll trace the certificate chain of a website back to a trusted root certificate on your own machine. You’ll see how Public Key Infrastructure (PKI) works in practice — and where the system might fall short.

---

### 2. Learning Objectives

By the end of this session, you should be able to:

- Inspect a website’s TLS certificate and identify its issuer, subject, and expiration  
- Understand how certificate chains link websites to root certificate authorities (CAs)  
- Locate trusted root certificates installed on your computer  
- Evaluate how revocation and trust decisions work (or fail) in practice  
- Use command-line tools to extract and examine certificate metadata  

---

### 3. Activity

#### Step 1: Pick a Website

Choose a well-known HTTPS site (e.g., https://github.com, https://uchicago.edu, https://mozilla.org). Avoid sites behind CDNs or pinned certs for now.

#### Step 2: Inspect the Certificate Chain

Use your browser’s tools to inspect the TLS certificate:

- In Chrome: Click the padlock → “Connection is secure” → “Certificate is valid”  
- In Firefox: Click the padlock → “Connection secure” → “More Information” → “View Certificate”

Answer these questions:

- What is the Common Name (CN) and organization for the **leaf** certificate (the site itself)?  
- Who issued the certificate (the **intermediate CA**)?  
- What is the name of the **root CA**?  
- What is the certificate’s expiration date?

#### Step 3: Find the Root CA on Your Machine

Now locate the **root certificate** on your system. This shows that your computer explicitly trusts it.

- **macOS:** Open Keychain Access → System Roots → search for the root CA  
- **Windows:** Run `certmgr.msc` → Trusted Root Certification Authorities  
- **Linux:** Look in `/etc/ssl/certs/` or use `openssl` (see Step 5)

Verify:

- Is the root certificate still valid (i.e., not expired or revoked)?  
- When was it issued and by whom?  
- Do you recognize the organization behind it?

#### Step 4 (Optional): Explore Certificate Revocation

Investigate how your browser or OS handles revocation:

- Does your browser use CRLs or OCSP?  
- Can you find any certs in your store marked as revoked or untrusted?  
- Try visiting a test site with a revoked or self-signed certificate (provided by the instructor if available)

Bonus: Compare how different browsers respond to revoked or expired certs.

#### Step 5: Use `openssl` or `certutil` to Dive Deeper

##### Option A: Using `openssl` (Linux/macOS/Windows with WSL)

1. Fetch the certificate from a server:
   ```
   openssl s_client -connect github.com:443 -showcerts
   ```

2. Copy one PEM-formatted certificate block (starts with `-----BEGIN CERTIFICATE-----`) and save it as `cert.pem`.

3. Inspect the certificate contents:
   ```
   openssl x509 -in cert.pem -text -noout
   ```

4. Answer the following based on the output:
   - What is the **Subject** (who the certificate is for)?
   - What is the **Issuer** (who issued it)?
   - What is the **Not Before / Not After** validity period?
   - What is the **Signature Algorithm**?
   - What is the **Public Key Algorithm** and **key size**?
   - Are there any **extensions** like Subject Alternative Names, Key Usage, etc.?

##### Option B: Using `certutil` (Windows)

1. List root certificates:
   ```
   certutil -store "Root"
   ```

2. Search for a specific issuer (e.g., DigiCert, ISRG Root X1):
   ```
   certutil -store "Root" | findstr /C:"DigiCert"
   ```

3. Export and inspect (optional):
   ```
   certutil -store "Root" > roots.txt
   ```

Write down any notable observations from the output.

---

### 4. Discussion

Let’s talk about what you found:

- How many root CAs are installed on your machine? Who selected them?  
- What surprised you about the certificate hierarchy?  
- How confident are you in the root CAs that your system trusts?  
- What happens if a root CA gets compromised — and how would you know?

We’ll wrap up by discussing what "trust" means in a system where you didn’t choose the root of the trust chain.
