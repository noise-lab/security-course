# Final Exam Generation Instructions

## Original Prompt

generate a final exam for this course. 1. roughly follow the format and question balance from previous finals here (https://github.com/noise-lab/security-course/tree/master/docs/final) 2. focus on topcs in meetins 7 amd 8 here (https://github.com/noise-lab/security-course/blob/master/docs/agenda.md) 3. there are some instructions in the midterm directory, generate-mideterm.md, which you should definitely follow as far as formatting, question design, point totals, etc. as a starting point. 4. in particular, focus on question design: plenty of multiple choice questions, yes/no questions with text boxes that allow students to explain why or why not, etc. 5. when you are done, please also include in the final directory not only a draft of the final in final/2025/ but also a copy of this prompt verbatim, to help students generate practice exams. also generate a generate-final.md file that encodes all of the instructions that we eventually use and put that into final/generate-final.md.

Additional requirements:
(1) be sure to include solutions using the solutions macro so we can turn those on/off
(2) DO NOT CHECK INTO GITHUB

---

## Exam Specifications

- **Total Points**: 85 points (MUST match midterm exactly)
- **Format**: Multiple choice, short answer, yes/no with explanation, and case study questions
- **Margins**: 0.4 inches (all sides) - reduced to fit on 6 pages
- **Target Pages**: 6 pages (compress if needed by reducing margins, not shrinking answer boxes excessively)
- **Solutions**: Use solution macros to enable/disable answers

## Coverage

The final exam covers material from **Meetings 7-8** according to the course agenda. Refer to `agenda.md` for the specific topics covered in these meetings.

## Question Types and Distribution

### Multiple Choice (Select All That Apply)
- **Count**: 8-9 questions
- **Points**: 4 points each
- **Total**: 32-36 points
- Use `\prob{4}` to start question
- Use `\correctanswercircle{text}` for correct answers
- Use `\answercircle{text}` for incorrect answers
- Clearly indicate "Select all that apply" in question text

### Yes/No Questions with Explanation
- **Count**: 3 questions
- **Points**: 4 points (yes/no) + 3 points (explanation) = 7 points total
- Use `\yesnoyes` or `\yesnono` for the yes/no answer
- Follow with explanation using `\answerbox{height}{solution}`
- Note: Some yes/no questions may be 4 points standalone

### Short Answer Questions
- **Count**: 4-5 questions
- **Points**: 3 points each
- **Total**: 12-15 points
- Use `\answerbox{height}{solution}` for answer boxes
- Typical heights: 1.25-2.0 inches
- Solutions should be 2-4 sentences

### Case Study Questions
- **Count**: 2-3 case studies with associated questions
- Use `\framebox` and `\parbox` for case study formatting
- Include scenarios for dark patterns, fair use arguments, ethics

### Feedback Questions
- **Count**: 2 questions
- **Points**: 1-3 points total
- Interest/difficulty ratings + open feedback

## Formatting Guidelines

### Page Breaks
- Use `\newpage` strategically to control pagination
- Break between major sections when appropriate

### Vertical Spacing
- Add `\vspace*{-0.1in}` before section headings to save space
- Use negative vspace (`\vspace*{-0.15in}` to `-0.25in`) before large elements

### Section Headings
- Use `\section*{Topic Name}` for major sections
- Topics: Privacy Law and Regulation, GDPR and International Privacy, CCPA/CPRA and Automated Compliance, Dark Patterns, AI and Privacy, Copyright and Fair Use

### Case Studies
```latex
\begin{center}
\framebox[0.9\linewidth]{
\parbox{0.8\linewidth}{
    {\bf Case Study:}
    Case study text...
}
}
\end{center}
```

## File Structure

- `exam.tex` - Main file with document class and geometry settings
- `instructions.tex` - Exam instructions and name acknowledgment
- `questions.tex` - All exam questions
- `feamster.sty` - Style file for exam formatting (copied from midterm)
- `Makefile` - Build system for both student and solution versions (copied from midterm)

## Building the Exam

```bash
make exam      # Builds student version (exam.pdf)
make solution  # Builds solution version (exam-solution.pdf)
make clean     # Removes auxiliary files
```

## Key Requirements

1. **Follow formatting from generate-midterm.md** - Use same macros, spacing, and structure
2. **Focus on Meetings 7 and 8 topics** - Privacy law, GDPR, CCPA/CPRA, dark patterns, AI privacy, copyright
3. **Include solutions using macros** - All answers in `\answerbox{}`, `\correctanswercircle{}`, etc.
4. **Balance question types** - Mix of multiple choice, short answer, yes/no, and case studies
5. **Use case studies for application** - Especially for dark patterns and fair use arguments
6. **Total 85 points** - MUST match midterm exactly
7. **Do not check into GitHub** - Local development only
8. **Point total verification** - Always verify final point count matches midterm using grep

## Question Design Best Practices

### What to AVOID
1. **No minutiae questions** - Avoid specific dates, obscure provisions, or implementation details
   - BAD: Asking for specific dates when legislation was signed
   - BAD: Asking about obscure provisions not covered in class lectures
   - GOOD: Asking about key features and requirements of legislation

2. **No ambiguous questions** - Questions should have clear, unambiguous answers
   - BAD: Using jargon or acronyms as standalone questions without context
   - BAD: Yes/No questions where the answer is obvious and doesn't test understanding
   - GOOD: Asking students to explain concepts in their own words

3. **No obvious Yes/No questions** - Replace with substantive short answer questions
   - BAD: Simple definitional yes/no questions
   - GOOD: "Explain why [concept/regulation] [has specific feature/requirement]"

4. **Don't test material not covered** - Only ask about concepts discussed in class
   - Verify each question relates to lecture content or assigned readings

5. **Avoid all-correct-first ordering** - Shuffle answer choices in multiple choice questions
   - BAD: All correct answers listed first, then all wrong answers
   - GOOD: Mix correct and incorrect answers throughout the choices

### What to INCLUDE

1. **Focus on understanding and application** - Test conceptual understanding, not memorization
   - Ask "why" and "explain" questions
   - Use case studies that require analysis
   - Ask students to construct arguments (e.g., fair use FOR and AGAINST)

2. **Bold key phrases** - Emphasize important parts of questions
   - Example: "Which represent [topic]-specific risks that **differ from traditional** risks?"
   - Helps students identify what's being asked

3. **Clear categorical questions** - When asking about categories or types, make distinctions clear
   - Provide concrete examples in case studies
   - Include obviously wrong options to avoid ambiguity

4. **Application-focused questions** - Test ability to apply concepts to new scenarios
   - Identification exercises from interface/scenario descriptions
   - Constructing arguments for and against positions
   - Analyzing implications in novel contexts

5. **Use specific terminology correctly and precisely**
   - Include full names of acts/regulations when relevant
   - Acknowledge nuances (e.g., "by default" for statements that have exceptions)
   - Use legally accurate phrasing (e.g., "factors courts consider" vs informal shorthand)

6. **Reframe confusing questions for clarity**
   - BAD: Using terms like "non-compliant" when the situation is nuanced
   - GOOD: Describing specific behaviors or failures ("failed to implement X")

7. **Connect to class discussions** - Reference themes and debates from lectures
   - Ask about implications and trade-offs discussed in class
   - Test understanding of why regulations have certain features
   - Explore connections between concepts

## Point Distribution Guidelines

- Multiple choice (select all that apply): 4 points
- Multiple choice (select one): 3 points
- Short answer: 2-3 points
- Yes/No with explanation: 4 points (yes/no) + 3 points (explanation)
- Feedback: 1-2 points

## Iterative Refinement Process

When generating the exam, expect multiple rounds of revision:

1. **Initial generation** - Create questions covering all topics
2. **Review for clarity** - Check each question for ambiguity
3. **Remove minutiae** - Replace detail-oriented questions with conceptual ones
4. **Shuffle answers** - Ensure MC answers aren't all correct-first
5. **Bold key terms** - Emphasize important distinctions in questions
6. **Verify coverage** - Only include material actually covered in class
7. **Check point total** - Must equal midterm (85 points)
8. **Compress to 6 pages** - Adjust margins first (0.4in), then answer box heights if needed
9. **Build and verify** - Compile both versions and confirm page count

## Final Checklist

Before considering the exam complete:

- [ ] Total points = 85 (matches midterm)
- [ ] Fits on exactly 6 pages
- [ ] No specific dates or obscure provisions
- [ ] MC answers are shuffled (not all correct first)
- [ ] No obvious yes/no questions
- [ ] Key phrases are bolded where needed
- [ ] All questions relate to class material
- [ ] Case studies test application, not memorization
- [ ] Both exam.pdf and exam-solution.pdf compile successfully
- [ ] Solutions are properly hidden/shown using macros
- [ ] Legal terminology is precise and accurate
