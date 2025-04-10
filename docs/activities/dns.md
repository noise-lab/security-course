## DNS Privacy 

### 1. Overview

Every time you visit a website, your browser makes DNS queries to resolve domain names into IP addresses. Traditionally, these queries are sent in plaintext over UDP on port 53, which means they can be seen — and sometimes modified — by anyone on the network. More recently, browsers have started supporting **DNS over HTTPS (DoH)** to encrypt this traffic and prevent surveillance or tampering.

In this activity, you’ll use browser tools and Wireshark to explore what DNS information is visible under different settings — and what can be inferred about you just from your DNS traffic.

---

### 2. Learning Objectives

By the end of this session, you should be able to:

- Observe how DNS requests are made and where they appear in network traffic  
- Understand the difference between plaintext DNS and encrypted DNS (DoH)  
- Identify which browser settings control DNS privacy behavior  
- Reflect on what personal or behavioral data can be inferred from DNS logs  

---

### 3. Activity

#### Step 1: Inspect DNS Activity in the Browser

1. Open your browser and go to a few common sites (e.g., https://nytimes.com, https://reddit.com, https://wikipedia.org).  
2. Open the developer tools (`F12` or right-click → "Inspect") and look under the **Network** tab.  
3. Look for any **preconnect**, **dns-prefetch**, or other name resolution hints.  
4. Note which third-party domains are being queried — not just the main site.

Answer:

- How many different domains were resolved during a single page load?  
- Can you infer what services or trackers are embedded just from the domains?  
- Are there any domains that surprise you?

#### Step 2: Check and Change DNS Settings

1. Open your browser’s DNS privacy settings.

   - **Firefox:** Preferences → Network Settings → Enable DNS over HTTPS  
   - **Chrome:** Settings → Privacy & security → Security → Use secure DNS  
   - **Brave/Edge/etc.:** Similar locations under Security or Privacy settings

2. Toggle **DoH on and off** and note which provider is used (e.g., Cloudflare, Google).

Answer:

- What setting was enabled by default?  
- Does the browser use the system resolver or a trusted recursive resolver?

#### Step 3: Monitor DNS Traffic with Wireshark

1. Open **Wireshark** and start capturing traffic on your active network interface.  
2. Filter the traffic by entering:
   ```
   udp.port == 53
   ```
   This shows traditional plaintext DNS traffic.

3. Visit a new website (one you haven’t already loaded).  

4. Then change your browser settings to **enable DoH**, clear cache, and reload the site.  

5. Observe whether any new traffic appears on port 53.

Answer:

- Do you see DNS traffic when DoH is disabled? What domains are visible?  
- Do you see any DNS traffic when DoH is enabled?  
- What does this imply about how visible your browsing is to network observers?

Optional: Try searching for traffic on port 443 instead to see HTTPS-based DNS lookups:
```
tcp.port == 443
```

#### Step 4 (Optional Extension): Use `dig` or `nslookup`

If you're comfortable in the terminal, try:
```
dig nytimes.com
```
or
```
nslookup nytimes.com
```
Then compare what DNS server is used when DoH is on vs. off.

---

### 4. Discussion

Let’s talk about what you found:

- Who on the network can see your DNS queries when DoH is disabled?  
- What could a government, ISP, or employer infer from your DNS logs?  
- Do you fully trust the DNS provider your browser uses when DoH is enabled?  
- What are the tradeoffs between system-level vs. browser-level DNS privacy?

We’ll wrap up by discussing how DNS visibility can affect censorship, tracking, or security — and what you can do to protect yourself.
