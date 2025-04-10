## What Do LLMs Remember About You?

### 1. Overview

Large Language Models (LLMs) like ChatGPT, Claude, and open-source systems such as Phoenix AI (UChicago's internal LLM) have raised important questions about privacy. Models trained on massive datasets can memorize rare sequences — sometimes regurgitating sensitive information. In this activity, you'll explore how inference and memorization risks play out in real-world systems, and investigate what settings are (or are not) available to users to protect their data.

We’ll look at real case studies and then test a few LLM interfaces to see what privacy tools are built in — and how transparent they really are.

---

### 2. Learning Objectives

By the end of this session, you should be able to:

- Explain the difference between memorization and inference in LLMs  
- Identify the types of data that LLMs are most likely to "leak"  
- Evaluate privacy risks when interacting with commercial or institutional LLMs  
- Locate and assess the privacy settings in real-world LLM tools  

---

### 3. Activity

#### Step 1: Case Study Discussion

Read the short summary of a real case study (provided by the instructor) where an LLM appeared to memorize or infer sensitive data. Examples may include:

- A user discovering leaked email addresses or API keys from training data  
- An LLM inferring that a user is part of a specific organization or demographic  
- Security researchers extracting phone numbers, passwords, or names via prompt engineering

In your group, discuss:

- What kind of training data might have led to this leak?  
- Was this true memorization or just inference?  
- Could this have been prevented? If so, how?

#### Step 2: Hands-On: Privacy Controls in LLMs (20–25 minutes)

Pick at least **two** LLM interfaces from the list below and try to answer the following questions by exploring the UI, settings, or documentation:

- What happens to your data after you use the model?  
- Can you opt out of having your chats used to improve the model?  
- Is there a clear way to delete past conversations or disable chat history?  
- Is your data encrypted or stored locally?  
- Does the system make any privacy guarantees?

**LLM Interfaces to Explore:**

- ChatGPT (https://chat.openai.com)  
- Claude (https://claude.ai)  
- Phoenix AI (UChicago internal system — access via UChicago credentials)  
- Perplexity AI (https://www.perplexity.ai)  
- GitHub Copilot (optional)

Each group should take notes on their findings and compare how different systems approach privacy and user control.

---

### 4. Discussion

As a class, we’ll talk about:

- Where are privacy protections strong? Where are they vague or absent?  
- Did any of the systems surprise you — positively or negatively?  
- What would it take to make these tools safe for sensitive tasks?  
- Do users know what risks they’re taking when they use these tools?

We’ll wrap up by considering: How can developers, institutions, or regulators create stronger norms and expectations around LLM privacy?
