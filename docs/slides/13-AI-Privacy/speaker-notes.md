# Speaker Notes: AI and Privacy

## Opening Hook (before title slide)

**Choose one of these hooks to open the lecture:**

**Hook 1 - The Samsung Leak:**
"In March 2023, Samsung engineers accidentally leaked proprietary source code and confidential meeting notes. How? They pasted it into ChatGPT asking for help debugging and summarizing. Within weeks, Samsung banned ChatGPT company-wide. Today we'll talk about why this happened—and why it could happen to you."

**Hook 2 - The Personal Question:**
"Quick show of hands: How many of you have used ChatGPT in the last week?" [wait for hands] "Keep your hand up if you've shared personal information with it—maybe about homework, your job search, health questions, relationship advice?" [most hands stay up] "Here's the thing: that data doesn't just disappear. Today we're going to talk about where it goes and who can access it."

**Hook 3 - The Therapy Bot:**
"Imagine you're going through a tough breakup. You can't sleep. It's 2 AM and you don't want to wake your friends. So you open ChatGPT and pour your heart out. It's empathetic, helpful, doesn't judge. You tell it things you haven't told anyone. Here's what you might not know: that conversation could be used to train the next version of the model. Your heartbreak could literally become part of the AI. Should that be allowed?"

**Hook 4 - The Paradox:**
"We're more careful about our data than ever before. We use VPNs, encrypted messaging, private browsing. And then we turn around and tell ChatGPT our medical symptoms, paste in our confidential emails, and ask it to help with sensitive work projects. Why? That's what we're exploring today."

## Slide 1: Title Slide
- Welcome students
- This lecture focuses on privacy risks specific to LLM-based systems
- Draws primarily from Zhang et al. (2024) "'It's a Fair Game', or Is It? Examining How Users Navigate Disclosure Risks and Benefits When Using LLM-Based Conversational Agents" published at CHI 2024
- Use one of the hooks above to grab attention before diving into content

**Primary Research Source:**
Zhang, Z., Jia, M., Lee, H. P., Yao, B., Das, S., Lerner, A., Wang, D., & Li, T. (2024). "It's a Fair Game", or Is It? Examining How Users Navigate Disclosure Risks and Benefits When Using LLM-Based Conversational Agents. In *Proceedings of the 2024 CHI Conference on Human Factors in Computing Systems*. DOI: 10.1145/3613904.3642385

## Slide 2: Today's Agenda
- Overview of what we'll cover
- Emphasize both technical and social aspects

## Slide 3: The Rise of LLM-Based Conversational Agents
- **Demo opportunity**: Show ChatGPT interface live
- Ask for show of hands on usage
- Discuss use cases students have tried

**Links:**
- [ChatGPT](https://chat.openai.com)
- [Claude](https://claude.ai)
- [Google Bard](https://bard.google.com)

## Slide 4: Why Privacy Matters in AI Systems
- Contrast with traditional software where data flows are clearer
- LLMs blur the line between "using" and "sharing" data

## Slide 5: Two Main Types of Privacy Risks
- Traditional risks: similar to any cloud service
- AI-specific: unique to how LLMs work
- Both types compound each other

## Slide 6: What Data Do Users Share with LLMs?
- Based on ShareGPT dataset analysis (real ChatGPT conversations)
- Users often don't realize how much they're sharing

**Case Study Links:**
- [ShareGPT data leak](https://twitter.com/goodside/status/1598253337400717313)
- [Privacy concerns in ChatGPT](https://www.theverge.com/2023/3/21/23649806/chatgpt-openai-user-data-leak-bug-outage)

## Slide 7: What Data Do Users Share? (cont'd)
- Less obvious PII can still identify individuals
- Combination of data points increases risk

## Slide 8: Example: Medical Information Sharing
- Walk through the fictional example
- Point out how conversational flow encourages disclosure
- Ask: "Would you share this with Google Search?"

**News Article:**
- [Mental health chatbot concerns](https://www.npr.org/sections/health-shots/2023/01/19/1147081115/chatgpt-ai-chatbot-mental-health-therapy)

## Slide 9: The Interdependent Privacy Problem
- Novel aspect: sharing others' data without their consent
- No clear legal framework for this
- Ethical questions about data ownership

**Discussion prompt**: "If your colleague shared your email with ChatGPT to draft a response, how would you feel?"

## Slide 10: Use Case Examples from Real Data
- All examples from actual ShareGPT dataset
- Show diversity of sensitive uses

## Slide 11: AI-Specific Risk #1: Memorization
- Technical explanation: LLMs memorize training data
- Can be extracted through prompt injection

**Demo opportunity**: Show examples of memorization extraction (use sanitized/public examples)

**Research Links:**
- [Carlini et al. (2021) "Extracting Training Data from Large Language Models"](https://arxiv.org/abs/2012.07805)
- [GPT-3 memorization examples](https://not-just-memorization.github.io/extracting-training-data-from-chatgpt.html)

## Slide 12: How Memorization Works
- Walk through the data flow diagram
- Emphasize: once it's memorized, hard to remove
- Note: OpenAI now offers opt-out, but it's not the default

## Slide 13: AI-Specific Risk #2: Human-Like Interactions
- Psychological research on anthropomorphization
- Users develop parasocial relationships with AI
- Leads to oversharing

**Research Link:**
- Zhang et al. (2024) "'It's a Fair Game', or Is It?" CHI paper (provided in readings)

## Slide 14: Progressive Disclosure in Action
- Similar to social engineering tactics
- AI doesn't intend to manipulate, but effect is the same
- Users gradually reveal more information

**Activity idea**: Role-play a conversation showing progressive disclosure

## Slide 15: Case Study: The Therapy Use Case
- Real quotes from research participants in Zhang et al. (2024) CHI study
- Participants P8, P10, P13, P15, P16, P19 used ChatGPT as "pen pal" or therapist
- Highly sensitive mental health information shared
- Question: Should LLMs be used for therapy?

**News Links:**
- [Koko chatbot controversy](https://www.vice.com/en/article/4ax9y4/AI-chatbot-for-mental-health-app-koko)
- [AI therapy apps](https://www.washingtonpost.com/technology/2023/01/19/chatgpt-ai-therapy/)

## Slide 16: User Mental Models: How Do People Think LLMs Work?
- Based on mental model analysis from Zhang et al. (2024) CHI study with 19 participants
- Model A: completely opaque ("magic") - 4 participants
- Model B: thinks it's search-based ("super searcher") - 8 participants
- Model C: understands ML basics ("stochastic parrot") - 6 participants

**Activity**: Ask students to draw their mental model (2 min)

## Slide 17: Mental Models: Training & Improvement
- Model D: quality rating only (misses memorization risk)
- Model E: training data (correct understanding)
- Many users had Model D - dangerous misconception

## Slide 18: User Awareness: The Opt-Out Problem
- Research finding from Zhang et al. (2024): 14 out of 19 participants were unaware of opt-out (all but P11, P14, P16, P17, P18)
- Even among technical users, awareness was low
- Lack of transparency from providers
- Dark patterns impeded adoption even after learning about controls

## Slide 19: Dark Patterns in Privacy Controls
- Show actual ChatGPT interface (screenshot or live demo)
- Navigate to settings → data controls
- Point out the bundling of chat history + training opt-out

**Demo**: Walk through ChatGPT settings live

**Reference:**
- [Dark patterns in privacy](https://www.deceptive.design/)

## Slide 20: How Users Navigate Privacy Trade-offs - Strategy 1
- Quote from participant: acceptance of risks
- "It's a fair game" is a recurring phrase
- Many feel they have no choice

## Slide 21: Strategy 2 & 3
- Some avoid entirely (opportunity cost)
- Most use manual sanitization (tedious, error-prone)

**Discussion**: "What strategies do you use?"

## Slide 22: The Problem: Is It Really a "Fair Game"?
- Key argument: informed consent requires understanding
- Users can't make informed decisions with flawed mental models
- Dark patterns prevent meaningful choice

## Slide 23: Perceived vs. Actual Sensitivity
- Individual differences in privacy preferences
- Resignation attitude is problematic
- "Everyone has my data anyway" - is that true?

## Slide 24: Company Policies and NDAs
- Real concern for professionals
- Creates tension between utility and compliance
- Some violate policies due to perceived necessity

**Discussion question**: Read aloud and discuss student responses

## Slide 25: Concerns About Being "Found Out"
- Social norms around AI use still forming
- Fear of judgment for using AI
- Meta-privacy concern

## Slide 26: Design Implications: What Should Change?
- Shift from user responsibility to system design
- Privacy by design, not privacy by configuration

## Slide 27: Design Implications (cont'd)
- Specific technical solutions
- Some already exist, need adoption

**Research Links:**
- [Privacy-preserving ML](https://www.microsoft.com/en-us/research/project/privacy-preserving-machine-learning/)
- [Differential privacy](https://privacytools.seas.harvard.edu/differential-privacy)

## Slide 28: Regulatory Considerations
- Current patchwork approach
- GDPR applies to ChatGPT (EU users)
- US lacks comprehensive framework

**Policy Links:**
- [GDPR enforcement on OpenAI](https://www.europarl.europa.eu/news/en/press-room/20230505IPR84904/)
- [FTC AI guidance](https://www.ftc.gov/business-guidance/blog/2023/02/keep-your-ai-claims-check)

## Slide 29: What About Fair Use and Copyright?
- Transition to next lecture
- Google v. Oracle relevant for training data questions
- Fair use defense for AI training?

## Slide 30: Activity: Privacy Trade-offs
**Facilitation notes:**
- Set timer for each portion
- Walk around during pair discussion
- Have 3-4 volunteers share
- Synthesize common themes

**Possible themes to highlight:**
- Financial data concerns
- Work/school policies
- Medical information
- Personal communications

## Slide 31-32: Practical Recommendations
- Actionable advice for students
- Emphasize: you can use these tools, but be aware
- Screenshot or bookmark the opt-out location

## Slide 33: Looking Ahead
- Acknowledge uncertainty
- Balance optimism with realism
- Ongoing research needed

## Slide 34: Key Takeaways
- Summarize main points
- Reinforce the "not a fair game" argument
- Emphasize need for systemic change

## Slide 35: Questions for Discussion
**Facilitation:**
- Pick 2-3 questions based on time
- Can use as small group discussions
- Or save for online forum

## Slide 36: Next Lecture Preview
- Bridge to copyright lecture
- Assign reading (Google v. Oracle case)

## Slide 37: Closing
- Thank students
- Remind about assignment
- Office hours availability

---

## Additional Resources for Instructor

### Case Studies to Reference
1. **[Samsung bans ChatGPT after code leak](https://www.bloomberg.com/news/articles/2023-05-02/samsung-bans-chatgpt-and-other-generative-ai-use-by-staff-after-leak)**
2. **[Italy temporarily bans ChatGPT](https://www.bbc.com/news/technology-65139406)**
3. **[ChatGPT data breach (March 2023)](https://openai.com/blog/march-20-chatgpt-outage)**

### Demonstrations/Activities

**Demo 1: Live ChatGPT Privacy Settings**
- Navigate Settings → Data Controls
- Show chat history toggle
- Show training opt-out (note: bundled with history)
- Show buried opt-out form in FAQ

**Demo 2: PII Detection Exercise**
- Give students sample prompts
- Have them identify what PII is being shared
- Discuss less obvious information (job title + company + city)

**Demo 3: Mental Model Drawing**
- Students draw how they think ChatGPT works
- Share a few examples
- Compare to actual architecture

**Activity: Privacy Policy Analysis**
- [OpenAI privacy policy](https://openai.com/policies/privacy-policy)
- Students find answers to:
    - How long is data retained?
    - Who can access your conversations?
    - Can you delete your data?
    - Is data used for training by default?

### Debate Topics
- "Resolved: LLM providers should be required to obtain explicit opt-in consent before using user data for training"
- "Resolved: The privacy risks of LLMs outweigh their benefits"

### Relevant Academic Papers
1. **Zhang, Z., Jia, M., Lee, H. P., Yao, B., Das, S., Lerner, A., Wang, D., & Li, T. (2024).** "'It's a Fair Game', or Is It? Examining How Users Navigate Disclosure Risks and Benefits When Using LLM-Based Conversational Agents." In *Proceedings of the 2024 CHI Conference on Human Factors in Computing Systems*. DOI: 10.1145/3613904.3642385 - **PRIMARY READING FOR SLIDES 15-19**
   - Available on arXiv: https://arxiv.org/abs/2309.11653
   - Study methodology: Analyzed real ChatGPT conversations + interviewed 19 users
   - Key findings: 14/19 unaware of opt-out, flawed mental models, dark patterns
2. Carlini et al. (2021) "Extracting Training Data from Large Language Models"
3. Carlini et al. (2023) "Quantifying Memorization Across Neural Language Models"
4. Brown et al. (2022) "What Does it Mean for a Language Model to Preserve Privacy?"

### News Articles (Regularly Updated)
- [The Verge AI coverage](https://www.theverge.com/ai-artificial-intelligence)
- [Ars Technica AI section](https://arstechnica.com/tag/artificial-intelligence/)
- [MIT Technology Review AI](https://www.technologyreview.com/topic/artificial-intelligence/)

### Technical Resources
- [OpenAI API documentation](https://platform.openai.com/docs/)
- [ChatGPT privacy controls](https://help.openai.com/en/articles/7730893-data-controls-faq)
- [Cover Your Tracks (browser fingerprinting)](https://coveryourtracks.eff.org/)

### Policy Documents
- [NIST AI Risk Management Framework](https://www.nist.gov/itl/ai-risk-management-framework)
- [White House AI Bill of Rights](https://www.whitehouse.gov/ostp/ai-bill-of-rights/)
- [EU AI Act](https://artificialintelligenceact.eu/)

### Videos
- [Computerphile on GPT](https://www.youtube.com/watch?v=_8yVOC4ciXc)
- [3Blue1Brown on neural networks](https://www.youtube.com/watch?v=aircAruvnKk)

---

## Timing Guide (75-minute class)

- Title/Intro: 2 min
- Slides 2-5 (Context): 8 min
- Slides 6-10 (Disclosure behaviors): 10 min
- Slides 11-15 (AI-specific risks): 12 min
- Slides 16-19 (Mental models): 10 min
- Slides 20-25 (Trade-offs): 10 min
- Slides 26-29 (Design/policy): 8 min
- Activity (slide 30): 10 min
- Slides 31-34 (Recommendations/takeaways): 5 min
- Discussion questions: 8 min
- Closing: 2 min

**Buffer: 10 minutes for questions, extended discussion, or demos**

---

## Talking Points for All Linked Resources

### ChatGPT, Claude, and Google Bard Links

**[ChatGPT](https://chat.openai.com)**
- **What it is:** OpenAI's conversational AI interface, launched Nov 2022
- **Why mention it:** Fastest-growing consumer application ever (100M users in 2 months)
- **Key points for discussion:**
    - Free tier uses GPT-3.5; Plus tier ($20/month) uses GPT-4
    - Has become default LLM for most people
    - Controversial for data privacy and training practices
    - Can demo live in class if available

**[Claude](https://claude.ai)**
- **What it is:** Anthropic's AI assistant, marketed as "safer" and more aligned
- **Why mention it:** Alternative to ChatGPT, emphasizes safety and honesty
- **Key points:**
    - Created by former OpenAI researchers
    - Uses "Constitutional AI" approach
    - Longer context window (100K+ tokens)
    - Also raises same privacy concerns as ChatGPT

**[Google Bard](https://bard.google.com)**
- **What it is:** Google's conversational AI, now called "Gemini"
- **Why mention it:** Shows how major tech companies are all racing for LLM dominance
- **Key points:**
    - Integrated with Google search and services
    - Had rocky launch (incorrect answer in demo)
    - Privacy implications since Google already has lots of user data

### ShareGPT Data Leak

**[ShareGPT data leak](https://twitter.com/goodside/status/1598253337400717313)**
- **What happened:** Website allowed users to share ChatGPT conversations via link
- **The problem:** ~90K conversations leaked containing PII, passwords, medical info
- **Key points:**
    - Users shared sensitive conversations thinking they were private
    - No warning that "share" made conversations public
    - Demonstrates how easily privacy violations occur
    - Many conversations contained work emails, confidential business info

**[Privacy concerns in ChatGPT](https://www.theverge.com/2023/3/21/23649806/chatgpt-openai-user-data-leak-bug-outage)**
- **What happened:** March 2023 bug exposed chat history titles and payment info
- **The bug:** Redis caching issue allowed users to see others' conversation titles
- **Key points:**
    - ChatGPT was taken offline for hours
    - Affected 1.2% of ChatGPT Plus subscribers
    - Payment info of 1.2% of active users potentially exposed
    - Shows even "secure" systems have vulnerabilities

### Mental Health and AI

**[Mental health chatbot concerns](https://www.npr.org/sections/health-shots/2023/01/19/1147081115/chatgpt-ai-chatbot-mental-health-therapy)**
- **What it covers:** Article explores people using ChatGPT for mental health support
- **Key concerns raised:**
    - Not trained as therapist, may give harmful advice
    - Users develop dependency on AI "therapist"
    - Highly sensitive mental health data being shared
    - No HIPAA protections since it's not healthcare
- **Discussion points:**
    - Should there be regulations on AI for mental health?
    - What's the difference between "life coaching" and "therapy"?
    - How do we balance accessibility vs. safety?

**[Koko chatbot controversy](https://www.vice.com/en/article/4ax9y4/AI-chatbot-for-mental-health-app-koko)**
- **What happened:** Mental health app Koko tested GPT-3 responses without informed consent
- **The backlash:** Users felt deceived, wanted human support not AI
- **Key points:**
    - 4,000 people received AI-generated mental health support
    - Founder posted about it on Twitter, users revolted
    - Raises ethical questions about AI in healthcare
    - Shows importance of transparency and consent

**[AI therapy apps](https://www.washingtonpost.com/technology/2023/01/19/chatgpt-ai-therapy/)**
- **What it covers:** Examines the trend of using AI for therapy/mental health
- **Apps mentioned:** Woebot, Replika, others
- **Key concerns:**
    - Data privacy (mental health records are sensitive)
    - Effectiveness (limited evidence base)
    - Risk of harm (bad advice in crisis situations)
    - Regulatory gaps (not considered medical devices)

### Carlini Research on Memorization

**[Carlini et al. (2021) "Extracting Training Data from Large Language Models"](https://arxiv.org/abs/2012.07805)**
- **What it found:** Could extract verbatim training data from GPT-2
- **Method:** Prompt the model repeatedly, look for repeated exact outputs
- **Results:** Extracted hundreds of memorized examples including:
    - Personal information (names, addresses, phone numbers)
    - Copyrighted text
    - Code with sensitive API keys
- **Implications:** Training data isn't as "anonymous" as assumed
- **Key quote to mention:** "By querying GPT-2, we extract hundreds of verbatim text sequences from the training data"

**[GPT-3 memorization examples](https://not-just-memorization.github.io/extracting-training-data-from-chatgpt.html)**
- **What it shows:** Interactive demos of extracted training data
- **Examples include:**
    - MIT Tech Review editor's contact information
    - IRC chat logs
    - Bitcoin addresses
    - News article excerpts
- **Teaching point:** Show one or two examples to make memorization concrete

### Dark Patterns

**[Dark patterns in privacy](https://www.deceptive.design/)**
- **What it is:** Catalog of deceptive UI/UX patterns that trick users
- **Relevant dark patterns for LLMs:**
    - Bundling: Combining chat history with training opt-out
    - Obstruction: Making privacy controls hard to find
    - Nagging: Repeatedly asking to enable features
- **Examples to show students:**
    - Cookie consent walls
    - Hard-to-find unsubscribe buttons
    - Pre-selected opt-ins
- **Discussion:** Ask students to identify dark patterns they've encountered

### Privacy-Preserving Technologies

**[Privacy-preserving ML](https://www.microsoft.com/en-us/research/project/privacy-preserving-machine-learning/)**
- **What it is:** Microsoft Research project on ML techniques that protect privacy
- **Key techniques:**
    - Federated learning (train on device, not cloud)
    - Differential privacy (add noise to prevent identification)
    - Homomorphic encryption (compute on encrypted data)
    - Secure multi-party computation
- **Talking point:** These exist but aren't widely adopted due to performance/cost tradeoffs

**[Differential privacy](https://privacytools.seas.harvard.edu/differential-privacy)**
- **What it is:** Mathematical framework for privacy (add statistical noise)
- **How it works:** Add carefully calibrated noise so individual data points can't be identified
- **Used by:** Apple (keyboard predictions), Google (mobility reports), US Census Bureau
- **Tradeoff:** Privacy vs. accuracy
- **Key point:** Could reduce memorization in LLMs but may reduce quality

### Regulatory Resources

**[GDPR enforcement on OpenAI](https://www.europarl.europa.eu/news/en/press-room/20230505IPR84904/)**
- **What it covers:** European Parliament's concerns about ChatGPT and GDPR
- **Key issues:**
    - Right to be forgotten (can't easily delete training data)
    - Data minimization (uses all available data)
    - Purpose limitation (training vs. serving different purposes)
    - Transparency (users don't know what data is used)
- **Status:** Ongoing investigations by EU data protection authorities

**[FTC AI guidance](https://www.ftc.gov/business-guidance/blog/2023/02/keep-your-ai-claims-check)**
- **What it says:** FTC warning to AI companies about deceptive practices
- **Key points:**
    - Don't exaggerate what your AI can do
    - Be transparent about limitations
    - Privacy laws apply to AI
    - Be careful with data from children
- **Significance:** Shows regulators are paying attention to AI

### Case Studies

**[Samsung bans ChatGPT after code leak](https://www.bloomberg.com/news/articles/2023-05-02/samsung-bans-chatgpt-and-other-generative-ai-use-by-staff-after-leak)**
- **What happened:** Three separate incidents where Samsung engineers leaked:
    - Proprietary source code
    - Internal meeting notes
    - Equipment data
- **Response:** Company-wide ban on ChatGPT and similar tools
- **Why it matters:** Shows real-world consequences of LLM data sharing
- **Discussion point:** How should companies balance productivity vs. security?

**[Italy temporarily bans ChatGPT](https://www.bbc.com/news/technology-65139406)**
- **What happened:** Italian data protection authority banned ChatGPT (March 2023)
- **Reasons:**
    - GDPR violations
    - Age verification concerns
    - Lack of legal basis for data processing
- **Resolution:** OpenAI made changes, ban lifted after 1 month
- **Significance:** First country to ban ChatGPT; showed regulators' power

**[ChatGPT data breach (March 2023)](https://openai.com/blog/march-20-chatgpt-outage)**
- **What OpenAI disclosed:** Bug exposed:
    - Chat history titles
    - First/last name, email, payment address
    - Last 4 digits of credit card
- **Root cause:** Bug in Redis caching library
- **Affected:** 1.2% of ChatGPT Plus subscribers during 9-hour window
- **Lesson:** Even well-resourced companies have security incidents

### Additional News Sources

**[The Verge AI coverage](https://www.theverge.com/ai-artificial-intelligence)**
- **Why useful:** Best source for ongoing AI news
- **Coverage includes:** Product launches, policy changes, lawsuits, controversies
- **Recommendation:** Subscribe to their AI newsletter for weekly updates

**[Ars Technica AI section](https://arstechnica.com/tag/artificial-intelligence/)**
- **Why useful:** More technical depth than general tech news
- **Strength:** Good analysis of how AI technology actually works
- **Audience:** More technical readers

**[MIT Technology Review AI](https://www.technologyreview.com/topic/artificial-intelligence/)**
- **Why useful:** Long-form investigative pieces
- **Strength:** Covers AI ethics, policy, and societal implications
- **Example stories:** AI bias, workforce impacts, regulatory approaches

### Technical Resources

**[OpenAI API documentation](https://platform.openai.com/docs/)**
- **What it contains:** Technical docs for developers using OpenAI's API
- **Relevant sections:**
    - Data usage policies
    - How to opt out of training
    - Rate limits and pricing
    - Safety best practices
- **Teaching use:** Show what data OpenAI collects from API users

**[ChatGPT privacy controls](https://help.openai.com/en/articles/7730893-data-controls-faq)**
- **What it explains:** How to control data usage in ChatGPT
- **Key info:**
    - How to turn off chat history
    - How to opt out of training
    - How to delete your data
    - What data is retained even after deletion
- **Demo opportunity:** Walk through these settings in class

**[Cover Your Tracks](https://coveryourtracks.eff.org/)**
- **What it does:** EFF tool that shows how trackable your browser is
- **Why include:** Illustrates broader privacy issues beyond LLMs
- **Class activity idea:** Have students run the tool and compare results
- **Teaching point:** Even without LLMs, we're already heavily tracked

### Policy Documents

**[NIST AI Risk Management Framework](https://www.nist.gov/itl/ai-risk-management-framework)**
- **What it is:** US government framework for managing AI risks
- **Key components:**
    - Govern: Policies and oversight
    - Map: Identify and categorize risks
    - Measure: Analyze and assess risks
    - Manage: Prioritize and respond to risks
- **Relevance:** Voluntary framework being adopted by companies and agencies

**[White House AI Bill of Rights](https://www.whitehouse.gov/ostp/ai-bill-of-rights/)**
- **What it is:** Non-binding blueprint for AI systems (Oct 2022)
- **Five principles:**
    1. Safe and effective systems
    2. Algorithmic discrimination protections
    3. Data privacy
    4. Notice and explanation
    5. Human alternatives and fallback
- **Status:** Not law, but influences policy discussion

**[EU AI Act](https://artificialintelligenceact.eu/)**
- **What it is:** Comprehensive AI regulation (adopted 2024)
- **Risk-based approach:**
    - Unacceptable risk: Banned (e.g., social scoring)
    - High risk: Strict requirements (e.g., hiring AI)
    - Limited risk: Transparency obligations
    - Minimal risk: No requirements
- **Where LLMs fit:** Likely "general purpose AI" category
- **Key requirements:** Transparency, documentation, oversight

### Videos

**[Computerphile on GPT](https://www.youtube.com/watch?v=_8yVOC4ciXc)**
- **What it covers:** How GPT models work (transformers, attention)
- **Length:** ~15 minutes
- **Audience:** Accessible to non-technical viewers
- **Use in class:** Could assign as pre-reading or show 5-minute segment
- **Key concepts explained:** Tokens, embeddings, attention mechanism

**[3Blue1Brown on neural networks](https://www.youtube.com/watch?v=aircAruvnKk)**
- **What it covers:** Visual explanation of how neural networks learn
- **Length:** ~19 minutes (first in series)
- **Strength:** Beautiful visualizations make abstract concepts concrete
- **Use in class:** Show 5-10 minute segment on backpropagation
- **Series:** Part of 4-video series on deep learning fundamentals

