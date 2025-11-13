## LLM-Assisted Content Moderation

The goal of this assignment is to understand how large language models can be used for automated content moderation and to critically analyze the strengths, weaknesses, and policy implications of such systems.

### Background

Content moderation at scale is one of the most challenging problems facing online platforms. Platforms must balance free expression with safety, navigate cultural differences, and make millions of decisions per day about what content violates their policies. Increasingly, platforms are exploring the use of LLMs to augment or replace traditional keyword-based and machine learning approaches to content moderation.

In this assignment, you will use **Anthropic's Claude content moderation framework** as your baseline implementation, then extend and evaluate it for real-world platform policies.

### Required Reading

Before starting the assignment, review these resources:

1. **Anthropic's Content Moderation Guide:** https://docs.claude.com/en/docs/about-claude/use-case-guides/content-moderation
2. **Building a Moderation Filter (Cookbook):** https://github.com/anthropics/anthropic-cookbook/blob/main/misc/building_moderation_filter.ipynb

These resources demonstrate Claude's approach to content moderation, including prompt engineering techniques, risk-level classification, and best practices.

### Task

You will implement Anthropic's content moderation framework and evaluate its performance on a test dataset.

#### Part 1: Implementation

Following Anthropic's content moderation guide:

1. **Set up the Claude API** (free tier or educational credits available)
2. **Implement the basic moderation function** from the guide
3. **Choose a platform and policy focus:**
   - Select 1 platform (e.g., Reddit, Twitter/X, YouTube, Facebook)
   - Pick 2-3 content categories to focus on (e.g., hate speech, harassment, spam)
   - Document the platform's policy for these categories from their Terms of Service

4. **Create a test dataset** of 10-15 examples including:
   - Clear violations
   - Clear non-violations
   - Borderline/context-dependent cases

   Source from public datasets, create synthetic examples, or use anonymized real content.

#### Part 2: Testing and Analysis

1. **Test two prompting approaches:**
   - Basic classification (simple prompt)
   - Chain-of-thought reasoning (using `<thinking>` tags)

2. **Evaluate performance:**
   - Record your own judgment for each test case (human baseline)
   - Run both prompting strategies on your test dataset
   - Compare Claude's decisions to your judgments
   - Calculate basic accuracy for both approaches

3. **Analyze limitations:**
   - Identify cases where Claude struggled (sarcasm, context, etc.)
   - Test if Claude's safety training overrides your instructions on any examples
   - Note any policy conflicts between Claude's values and platform policies

#### Part 3: Policy Analysis

Write a 2-page analysis addressing:

1. **Performance:** How accurate was Claude? Where did it succeed/fail?
2. **Comparison of approaches:** Did chain-of-thought reasoning help? Why or why not?
3. **Context understanding:** How well did Claude handle nuance and context?
4. **Cost feasibility:** Using Anthropic's pricing, estimate costs for moderating at scale
5. **Policy recommendations:**
   - When is LLM-based moderation appropriate vs. problematic?
   - What safeguards are needed (human review, appeals)?
   - How should platforms balance automation with transparency?

### Submission

Your submission should include:

1. **Code and prompts**:
   - Your implementation based on Anthropic's framework
   - Both prompt variations (basic and chain-of-thought)
   - Test dataset with your human judgments

2. **Results documentation** (1 page):
   - Platform policy summary
   - Claude outputs for all test cases
   - Accuracy comparison between prompting strategies
   - Examples of successes and failures

3. **Policy analysis** (2 pages):
   - Performance evaluation
   - Limitations and edge cases
   - Cost analysis
   - Policy recommendations

4. **Your name and CNET ID**

You're encouraged to use AI tools to help with coding and analysis, but you must understand and be able to explain all aspects of your implementation.

To submit, add everything you'd like to include to your repo, commit the changes, and push to GitHub. Please do not push a compressed version (i.e., a zip file) of your submission.

### Tips

- **Start early!** Set up your Claude API access immediately
- **Follow Anthropic's guide closely**—it includes working code examples
- **Use Claude Haiku** for cost-effectiveness (recommended in guide)
- **Keep your test set small but diverse**—10-15 examples is sufficient to learn the patterns
- **Focus on interesting edge cases** rather than obvious violations
- **Document what you learn** about the technology's limitations

### Resources

- **Anthropic Content Moderation Guide:** https://docs.claude.com/en/docs/about-claude/use-case-guides/content-moderation
- **Anthropic Cookbook (Moderation Filter):** https://github.com/anthropics/anthropic-cookbook/blob/main/misc/building_moderation_filter.ipynb
- **Claude API Documentation:** https://docs.anthropic.com/
- **Claude Pricing:** https://www.anthropic.com/pricing (Note: Haiku is ~$2,590 per billion posts vs Sonnet at ~$31,080)
- **Academic hate speech datasets:** Search for datasets on HuggingFace, Kaggle, or academic repositories
