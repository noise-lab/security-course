## The Web of Trust: A GPG Key Signing Party

### 1. Overview

Before centralized Certificate Authorities, cryptographers built trust through personal verification and key signing parties. At these gatherings, people would meet in person, verify each other's identities, exchange public keys, and sign them to vouch for their authenticity. This created a "web of trust" — a decentralized network where trust was earned through personal connections, not corporate hierarchies.

In this activity, you'll experience this firsthand by creating your own GPG keypair, exchanging keys with classmates, verifying identities, and signing each other's keys. You'll also encrypt and decrypt messages to see the web of trust in action.

---

### 2. Learning Objectives

By the end of this session, you should be able to:

- Create and manage a GPG keypair using command-line tools
- Understand the structure of public/private key cryptography
- Export and import public keys to share with others
- Verify someone's identity before signing their key
- Sign another person's public key to vouch for their identity
- Encrypt messages using someone else's public key
- Decrypt messages using your private key
- Explore your local keyring and understand trust levels
- Reflect on the differences between centralized PKI and decentralized web of trust

---

### 3. Activity

#### Step 1: Install GPG and Generate Your Keypair

First, make sure you have GPG installed on your system.

**macOS:**
```bash
brew install gnupg
```

**Ubuntu/Debian:**
```bash
sudo apt-get install gnupg
```

**Windows:**
Download Gpg4win from [gpg4win.org](https://www.gpg4win.org/)

Verify installation:
```bash
gpg --version
```

Now create your own GPG keypair:

```bash
gpg --full-generate-key
```

When prompted:
1. Choose **RSA and RSA** (option 1)
2. Select **4096** bits for maximum security
3. Set expiration to **1 year** (this is good practice — keys shouldn't live forever)
4. Enter your **real name** and **university email address**
5. Add a comment if you wish (e.g., "Security Course 2025")
6. Create a **strong passphrase** (and remember it!)

Export your public key to share with others:

```bash
gpg --armor --export your.email@example.com > yourname.asc
```

The `--armor` flag creates ASCII-armored output (readable text instead of binary).

You can also print your key to the terminal:
```bash
gpg --armor --export your.email@example.com
```

Copy this output — you'll need to share it with your classmates.

Answer:
- What is your key ID? (You can find it with `gpg --list-keys`)
- What is your key fingerprint? (You can find it with `gpg --fingerprint`)

#### Step 2: Exchange and Verify Keys In Person

This is the crucial step: **verify identity before trusting a key**.

1. Find a partner (or small group of 2–3 people)
2. **Show your government-issued ID** or student ID to prove who you are
3. **Verbally confirm your key fingerprint** by reading it aloud while your partner checks
4. Exchange public keys by:
   - Sharing the `.asc` file via USB, AirDrop, or secure messaging, OR
   - Copying the ASCII-armored key directly

Save your partner's public key to a file (e.g., `partner.asc`), then import it:

```bash
gpg --import partner.asc
```

Verify it was imported:
```bash
gpg --list-keys
```

You should see their name and email in your keyring.

Before signing, **always verify the fingerprint** matches what your partner told you:

```bash
gpg --fingerprint partner@example.com
```

Compare this fingerprint with:
- What they told you verbally
- What's printed on their screen or ID card

If it matches, you can proceed. If not, **do not sign** — something is wrong.

#### Step 3: Sign Keys and Build the Web of Trust

If the fingerprint checks out, sign their key to vouch for their identity:

```bash
gpg --sign-key partner@example.com
```

You'll be asked to confirm. Type `y` and enter your passphrase.

This signature says: **"I have verified that this key belongs to this person."**

Now export their key (including your signature) and send it back to them:

```bash
gpg --armor --export partner@example.com > partner-signed.asc
```

Give this file back to your partner so they can import it into their keyring.

When you receive your own key back (now with signatures from others), import it:

```bash
gpg --import yourname-signed.asc
```

Check your key's signatures:
```bash
gpg --list-sigs your.email@example.com
```

You should see signatures from people who verified your identity.

Explore your keyring and see the trust relationships:

```bash
gpg --list-keys
gpg --list-sigs
```

Check the trust level of a key:
```bash
gpg --edit-key partner@example.com
```
Then type `trust` at the prompt to set or view trust level. Type `quit` to exit.

Answer:
- How many keys have you signed?
- How many people have signed your key?
- What trust level did GPG assign to keys you imported but didn't sign?

#### Step 4: Encrypt and Send Messages

Now use your partner's public key to encrypt a secret message to them:

```bash
echo "Your secret message here" | gpg --encrypt --armor --recipient partner@example.com > message.asc
```

Or encrypt a text file:
```bash
gpg --encrypt --armor --recipient partner@example.com message.txt
```

This creates an encrypted file that **only your partner** can decrypt with their private key.

View the encrypted message:
```bash
cat message.asc
```

Notice it's unreadable gibberish starting with `-----BEGIN PGP MESSAGE-----`.

Share the encrypted message with your partner using one of these methods:

**Option A: Direct file transfer**
- USB drive
- AirDrop (macOS)
- Email attachment
- Shared folder

**Option B: Copy/paste the ASCII-armored text**
```bash
cat message.asc
```
Copy the entire output (including the `-----BEGIN` and `-----END` lines) and send via:
- Slack/Discord
- Email body
- Shared document
- Even SMS or public forum (it's encrypted, so it's safe!)

**Option C: QR Code (for short messages)**
```bash
cat message.asc | qrencode -t UTF8
```
Your partner can scan and decrypt it. (Requires `qrencode` package)

#### Step 5: Decrypt Messages and Explore Signing

When you receive an encrypted message from your partner, decrypt it:

**If it's a file:**
```bash
gpg --decrypt message.asc
```

**If they pasted ASCII-armored text:**
1. Save the text to a file (e.g., `received.asc`)
2. Make sure it includes the full PGP message block
3. Decrypt:
   ```bash
   gpg --decrypt received.asc
   ```

You'll be prompted for your passphrase. If successful, you'll see the decrypted message.

Answer:
- Were you able to successfully decrypt your partner's message?
- Could anyone else decrypt it? Why or why not?
- What would happen if you lost your private key or forgot your passphrase?

**Bonus: Message Signing**

Encryption proves confidentiality. Signing proves authenticity. Try signing a message:

```bash
echo "I wrote this message" | gpg --clearsign > signed.asc
```

This creates a human-readable message with a signature attached.

Your partner can verify it came from you:
```bash
gpg --verify signed.asc
```

**Encrypt AND sign a message:**
```bash
echo "Secret and authenticated!" | gpg --encrypt --sign --armor --recipient partner@example.com > secret-signed.asc
```

This ensures the message is both **private** (encrypted) and **authenticated** (signed).

**Optional: Publish to a Keyserver**

You can publish your public key to a global keyserver so others can find it:

```bash
gpg --keyserver keys.openpgp.org --send-keys YOUR_KEY_ID
```

Anyone can now download your key:
```bash
gpg --keyserver keys.openpgp.org --recv-keys YOUR_KEY_ID
```

Note: Be careful — once uploaded, keys are **very hard to remove** from keyservers.

---

### 4. Discussion

We'll come back together and discuss what you observed.

- How does verifying someone's identity in person compare to trusting a certificate authority?
- What are the advantages of a web of trust over centralized PKI?
- What are the disadvantages? (Consider scalability, usability, revocation)
- If someone's private key is compromised, how does that affect the web of trust?
- Why do you think PGP/GPG never became mainstream, despite being around since the 1990s?
- In a web of trust, whose keys would you trust? Friends? Professors? Strangers with many signatures?
- How would you revoke a key if your laptop was stolen?

We'll wrap up by discussing why decentralized trust models are hard to scale — and whether blockchain-based alternatives might solve (or recreate) these problems.

---

### 5. GUI Alternatives (Optional)

If you prefer a graphical interface, try these tools (but make sure you still understand the GPG commands):

**macOS:**
- [GPG Suite](https://gpgtools.org/) — integrates with Apple Mail and Keychain

**Windows:**
- [Gpg4win](https://www.gpg4win.org/) — includes Kleopatra GUI for key management

**Linux:**
- [Seahorse](https://wiki.gnome.org/Apps/Seahorse) (GNOME)
- [KGPG](https://apps.kde.org/kgpg/) (KDE)

**Cross-platform:**
- [Thunderbird](https://www.thunderbird.net/) with built-in OpenPGP support
- [Mailvelope](https://www.mailvelope.com/) browser extension for webmail

All of these tools use GPG under the hood, so the concepts remain the same.
