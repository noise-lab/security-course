## OAuth in Action

### 1. Overview

Every time you click "Sign in with Google" or connect a third-party app to Slack, you're using OAuth 2.0. Instead of sharing your password with every service, OAuth lets you delegate limited access through tokens. It's the modern standard for letting apps talk to each other on your behalf — without giving away the keys to your account.

In this activity, you'll see OAuth in action twice: first by watching a live demo of connecting a third-party app, and then by running through a hands-on OAuth implementation to see exactly how the authorization flow works under the hood.

---

### 2. Learning Objectives

By the end of this session, you should be able to:

- Identify the four roles in OAuth 2.0 and explain how they interact
- Understand why OAuth is better than sharing passwords with third parties
- Trace the steps of the authorization code grant flow
- Recognize what security properties OAuth provides (and what it doesn't)
- Run a working OAuth implementation and inspect tokens and redirects

---

### 3. Activity

#### Step 1: Watch OAuth in the Wild

Your instructor will demonstrate connecting a third-party app to a service (e.g., adding an app to Slack, connecting GitHub to a tool, or linking a calendar app).

As you watch, answer:

- What permissions is the user being asked to grant?
- Who are the four OAuth actors here? (resource owner, client, authorization server, resource server)
- Did the third-party app ever see the user's password?
- How would you revoke this access later?

Think about:

- What happens if the third-party app gets hacked? Is your password at risk?
- How is this different from just giving every app your username and password?

#### Step 2: Get the OAuth Demo Running

Clone the demo repository and follow the setup instructions:

```bash
git clone https://github.com/patrickbucher/oauth2-demo.git
cd oauth2-demo
```

Read the README to understand the architecture. The demo has three servers:

- **authserver** (port 9001): Issues tokens
- **resource** (port 9002): Holds the protected data (gossip)
- **client** (port 9000): Requests access on your behalf

Start all three servers according to the README instructions.

#### Step 3: Walk Through the Authorization Flow

Open http://localhost:9000 in your browser and request access to the gossip.

Watch what happens:

1. You get redirected to the authorization server. Look at the URL — what parameters are included? What is `client_id`? What is `state` for?

2. Log in and authorize the client (use the credentials from the README).

3. You get redirected back to the client. Look at the URL again — what changed? Do you see an authorization code?

4. The client now displays the gossip. Behind the scenes, it exchanged the authorization code for an access token and used that token to fetch the data.

Open your browser's Developer Tools (Network tab) and repeat the flow. Try to identify:

- Which steps happen in your browser (front-channel)?
- Which steps happen directly between servers (back-channel)?
- Where does the authorization code appear? Where does the access token appear?

#### Step 4: Explore the Code

Open the source code and find where these things happen:

- Where does the client build the authorization request?
- Where does the authorization server generate authorization codes?
- Where does the client exchange the code for a token?
- How does the resource server validate tokens?

Look at how tokens are created. Are they random strings, or do they contain information (like JWTs)?

#### Step 5 (Optional): Break Things

Try these experiments to see what security properties OAuth has:

- Reuse an authorization code after it's already been used. What happens?
- Tamper with the `state` parameter in the callback URL. Does the client accept it?
- Try to use an expired token (if the demo supports expiration).

---

### 4. Discussion

Let's talk about what you learned:

- What are the trust relationships in OAuth? Who trusts whom?
- What happens if the client app gets compromised? Can an attacker steal passwords?
- What happens if an access token gets stolen? How is the damage limited?
- Why does OAuth use two steps (code, then token) instead of issuing the token directly?
- What does the `state` parameter prevent?

Think about the design:

- Why is the authorization server so critical? What if it goes down or gets hacked?
- OAuth is a *delegation* protocol, not an *authentication* protocol. What does that mean?
- What does OAuth *not* provide that you might need for a real app?

We'll wrap up by discussing when you'd use OAuth vs. other approaches — and what additional protocols (like OpenID Connect) build on top of it.
