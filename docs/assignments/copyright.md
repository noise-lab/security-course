## Copyright Detection Systems

The goal of this assignment is to understand how automated copyright detection systems work by building a simple fingerprinting detector, then analyzing the tension between copyright protection and fair use.

### Background

Platforms like YouTube, TikTok, and SoundCloud use automated content identification systems (like YouTube's Content ID) to detect copyrighted material. These systems analyze audio and video fingerprints to match uploaded content against databases of copyrighted works. While these systems help rights holders protect their content, they also raise important questions about fair use, over-blocking, and the balance between automation and human judgment.

### Task

You will build a simple audio or video fingerprinting system to understand how copyright detection works, test it with various content, and analyze the policy implications.

#### Part 1: Build a Simple Detection System

Build your own basic audio or video fingerprinting system:

1. **Choose your approach:**
   - **Audio fingerprinting:** Use libraries like `dejavu`, `chromaprint`, or build a simple spectrogram-based matcher
   - **Video fingerprinting:** Use perceptual hashing (pHash) or frame-based similarity matching with OpenCV

2. **Create a test environment:**
   - Create a reference database with 5-10 media files:
     - Your own original content (music you made, videos you recorded)
     - Public domain content (from archive.org, public domain music/video databases)
     - Creative Commons licensed content
   - Create test variations of these files:
     - **Audio modifications:** Pitch shift, speed change, reverb, background noise, re-encoding
     - **Video modifications:** Cropping, color grading, flipping, adding overlays, re-encoding
     - **Length variations:** Full clip vs. 5s, 15s, 30s excerpts

3. **Implement matching algorithm:**
   - Implement a similarity detection algorithm that can identify matching content
   - Test against your variations to measure:
     - True positives (correctly identifies matches)
     - False positives (incorrectly flags non-matches)
     - False negatives (misses actual matches)

4. **Document performance:**
   - Which modifications successfully evade detection?
   - What are the technical challenges in building a robust system?
   - What tradeoffs exist between sensitivity (catching matches) and specificity (avoiding false positives)?

#### Part 2: Fair Use and Policy Analysis

Write a 2-3 page analysis addressing:

1. **Technical limitations:**
   - What did you learn about the challenges of automated copyright detection?
   - How do technical limitations affect fair use protection?
   - What modifications were most effective at evading detection, and why?

2. **Fair use evaluation:**
   - Research 3-5 real-world examples of copyright claims on platforms (YouTube's copyright disputes, fair use cases in the news)
   - For each, apply the four-factor fair use test:
     1. Purpose and character of use
     2. Nature of the copyrighted work
     3. Amount and substantiality used
     4. Effect on market value
   - Did the automated system or platform make the right call? Why or why not?

3. **Over-blocking and false positives:**
   - What happens when automated systems flag fair use content?
   - Research the appeal/dispute process on major platforms (YouTube, TikTok, etc.)
   - What is the burden on users to contest false claims?

4. **Policy recommendations:**
   - Strengths and weaknesses of automated copyright detection
   - When is automated takedown appropriate vs. problematic?
   - How should platforms balance copyright protection with fair use?
   - What role should human review play?
   - Recommendations for transparency and user rights

### Submission

Your submission should include:

1. **Code and implementation**:
   - Your fingerprinting/detection code
   - Reference database setup instructions
   - Test results showing true positives, false positives, and false negatives

2. **Technical documentation** (1-2 pages):
   - How your detection system works
   - Performance on various modifications
   - Technical challenges and limitations you discovered

3. **Fair use and policy analysis** (2-3 pages):
   - Analysis of real-world copyright cases
   - Fair use evaluation using the four-factor test
   - Over-blocking analysis and appeal process research
   - Policy recommendations

4. **Your name and CNET ID**

You're encouraged to use AI tools to help with coding and analysis, but you must understand and be able to explain all aspects of your implementation.

To submit, add everything you'd like to include to your repo, commit the changes, and push to GitHub. Please do not push a compressed version (i.e., a zip file) of your submission.

### Tips

- **Start simple**—even basic fingerprinting reveals key challenges
- **Use only content you have rights to**: your own creations, public domain, or Creative Commons
- **Focus on understanding the technology**, not defeating it
- Python libraries that may be helpful: `librosa`, `pydub`, `opencv-python`, `imagehash`, `dejavu`, `chromaprint`
- For real-world examples, search for "YouTube fair use dispute" or "copyright false positive" cases

### Optional Extension

If you're interested in platform testing (optional, not required):
- The in-class [Copyright activity](../activities/copyright.md) involves testing platform detection systems
- You may optionally explore how real platforms handle copyright detection
- If you choose to test platforms, only use your own original content or public domain material
- Document your findings as additional context for your policy analysis

### Resources

- **YouTube Content ID:** https://support.google.com/youtube/answer/2797370
- **Fair Use Guidelines:** https://www.copyright.gov/fair-use/
- **Audio fingerprinting:** https://en.wikipedia.org/wiki/Acoustic_fingerprint
- **Perceptual hashing:** https://en.wikipedia.org/wiki/Perceptual_hashing
- **Public domain music:** https://archive.org/details/audio
- **Public domain video:** https://archive.org/details/movies
- **Creative Commons search:** https://search.creativecommons.org/
