# Midterm Exam Generation Instructions

## Exam Specifications

- **Total Points**: 85 points
- **Page Count**: 6 pages
- **Format**: Multiple choice, short answer, and diagram-based questions
- **Margins**: 0.5 inches (all sides)

## Coverage

The midterm should cover material from **Meetings 1-5** according to the course agenda:

1. **Ethics** (Menlo Report principles)
2. **Foundations** (Trusting Trust, Anderson's "Why Cryptosystems Fail")
3. **Public Key Infrastructure** (CAs, certificate validation, PKI security)
4. **Authentication** (OAuth 2.0)
5. **Denial of Service and Botnets** (DNS amplification, DoS characteristics)
6. **Web Security** (Same-Origin Policy, XSS attacks)
7. **Web Tracking** (Third-party tracking, browser fingerprinting)
8. **DNS Security** (Kaminsky attack, DNSSEC, DNS privacy)

## Question Types and Distribution

### Multiple Choice Questions
- Use `\prob{points}` to start a question
- Use `\correctanswercircle{text}` for correct answers
- Use `\answercircle{text}` for incorrect answers
- For "Select all that apply" questions, clearly indicate in the question text

### Short Answer Questions
- Use `\answerbox{height}{solution}` for answer boxes
- Typical heights: 1.25-2.5 inches depending on expected answer length
- Solutions should be 2-4 sentences typically

### Yes/No Questions with Explanation
- Use `\yesnoyes` or `\yesnono` for the yes/no answer
- Follow with explanation question using `\answerbox{height}{solution}`
- Example format:
  ```latex
  \prob{4}
  Statement here. \yesnoyes
  \eprob
  \prob{3}
  Explain why or why not.\\
  \answerbox{1.25}{Explanation...}
  \eprob
  ```

### Diagram-Based Questions
- Use `\includegraphics[width=0.65\textwidth]{filename.png}` for diagrams
- Use conditional rendering for student vs. solution versions:
  ```latex
  \ifthenelse{\equal{\version}{solution}}{% raw %}{%{% endraw %}
  \includegraphics[width=0.65\textwidth]{diagram-solution.png}%
  }{% raw %}{%{% endraw %}
  \includegraphics[width=0.65\textwidth]{diagram.png}%
  }
  ```
- Add negative vspace before diagrams if needed for spacing: `\vspace*{-0.2in}`

## Formatting Guidelines

### Page Breaks
- Use `\newpage` strategically to control pagination
- Current strategic breaks: after Ethics case study, before PKI section

### Vertical Spacing
- Add `\vspace*{-0.1in}` before section headings to save space
- Use negative vspace (`\vspace*{-0.15in}` to `-0.25in`) before large elements

### Section Headings
- Use `\section*{Topic Name}` for major sections
- Add `\vspace*{-0.1in}` before each section heading for compression

### Case Studies
- Use `\framebox` and `\parbox` for case study formatting:
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
- `feamster.sty` - Style file for exam formatting
- `Makefile` - Build system for both student and solution versions

## Building the Exam

```bash
make exam      # Builds student version (exam.pdf)
make solution  # Builds solution version (exam-solution.pdf)
make clean     # Removes auxiliary files
```

## Key Requirements

1. **Include at least one question addressing Assignment 1** (typically PKI/certificates)
2. **Avoid duplicating questions from previous years** - check 2023 and 2024 exams
3. **Follow agenda's "possible midterm questions"** - these are specific topics called out in agenda.md
4. **Only include content covered in class** - don't ask about topics not discussed
5. **Use diagram-based questions** - include at least 2 visual/diagram questions
6. **Balance question types** - mix multiple choice, short answer, and diagrams

## Point Distribution Guidelines

- Multiple choice (select one): 3-4 points
- Multiple choice (select all that apply): 4 points
- Short answer: 3 points
- Short answer with explanation: 2-4 points
- Diagram-based: 4 points
- Yes/No with explanation: 4 points (yes/no) + 3 points (explanation) = 7 points total

## Recent Changes (2025)

- Added 0.5 inch margins using `\usepackage[margin=0.5in]{geometry}`
- Name acknowledgment box: 4.0 inches wide
- Feedback box: 0.7 inches tall
- Reduced spacing with negative vspace before all section headings
- Combined feedback interest/difficulty questions on one line
- Emphasis on diagram-based questions (reflected XSS, web tracking)
