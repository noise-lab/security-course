# Internet Access Measurements

Over the past decade, various tools and techniques have been developed to
measure the performance of Internet access.  In class, we covered some of the
practices (and pitfalls) of client-based Internet measurement. In this
assignment, you will use data collected by the Federal Communications
Commission (FCC) on Internet speeds in the United States to explore what this
data does and does not tell you about the state of Internet access in the
United States.

You can read a bit about the sampling method and data collection technique
[here](https://www.fcc.gov/reports-research/reports/measuring-broadband-america/measuring-fixed-broadband-twelfth-report).


## Part 1: Understanding the Data

1. **Sampling.** The FCC documents describe the following approach: "The
   measurement clients (i.e., whiteboxes) were situated in the homes of 5,242
   panelists, each of whom received service from one of the 10 evaluated ISPs."
   The sample size is 5,242, but the report says nothing about how the sample was
   selected. As it turns out, the sample is stratified by ISP, but pays no
   attention to geography. The sample for an ISP like AT&T, for example, might be
   entirely contained in one region or city, and some regions or cities may
   not be represented at all. This is a common problem with Internet
   measurement datasets.

   a. What types of questions can be answered with this type of sample?
   b. What types of questions cannot be answered with this type of sample?
   
2. **Metrics.** The FCC report includes a number of metrics, including
   download speed, upload speed, and latency. There is also a web browsing
   test, which measures the time it takes to load a web page. 

   a. Why is latency important to measure?
   b. Why is web browsing important to measure?

3. **Method**. The FCC report includes this important caveat: "In-home
   networks, which typically include Wi-Fi, may not have sufficient capacities
   to support peak loads." 

   How does the FCC's measurement technique address
   this potential limitation and eliminate the potential effects of WiFi?

## Part 2: Downloading and Inspecting the Data

The FCC has collected data on Internet speeds in the United States since 2010. The
data is available in a variety of formats, including CSV, JSON, and XML.  

1.  Download the latest data from the FCC website.  The data is available in a
    variety of formats, including CSV, JSON, and XML.  For this assignment,
    we will use the CSV format.  The data is available at
    [here](https://www.fcc.gov/oet/mba/raw-data-releases).

2.  The data contains a variety of tests including the following:
   
      * Download speed - the speed at which a client can download data from a
        server. (curr_httpget.csv, curr_httpgetmt.csv, curr_httpgetmt6.csv)
      * Upload speed (curr_httppost.csv, curr_httppostmt.csv, curr_httppostmt6.csv)
      * Latency (curr_ping.csv)
      * Web browsing (curr_webget.csv)
   
   Each of these files respectively contains important information including:
      * The unit ID (the device that took the measurement)
      * The date and time of the measurement
      * The target (the server against which the measurement was taken)
   The web measurements also include important characteristics like time to
   first byte and total fetch time.

## Part 3: Analyzing the Data for Policy

State a single question that you would like to answer using the data and
**justify its relevance to policy**. Here are some examples:
   * You want to explore the effectiveness of the FCC's 80-80 metric versus
     other ways to aggregate throughput.
   * You want to explore the relationship between throughput and web browsing
     performance (e.g., page fetch time or time to first byte).
   * You want to understand how variable a user's experience is across time.

You are also welcome to pose your own question.  

Once you have a question, you will need to analyze the data to answer it.  As
some of the data is large, you are welcome to study a subset of the data
(e.g., a day or a week excerpt of the data).


## Part 4: Digital Equity

In class, we talked about digital equity and the inadequacy of existing
datasets for measuring it. This question is of utmost policy importance right
now, with federal BEAD funding due to states based on the ability to express
"unserved" and "underserved" regions of a state.

1. Briefly explain why the current FCC's Measuring
   Broadband America dataset is inadequate for this purposes.

2. What additional data would you need to measure digital equity?  What
   challenges would you face in collecting this data?

3. Take a look at the [Internet Equity
   Initiative](https://datascience.uchicago.edu/research/internet-innovation/) project at the University of
   Chicago and recall the discussion from class. How would a "hyper-local"
   approach, such as that being taken in this project, help to address the
   problem of under-sampled geographies?

The following
[paper](https://papers.ssrn.com/sol3/papers.cfm?abstract_id=4179787) might
provide some guidance on how to approach this question, with some initial food
for thought.

## Part 5: Reflection & Tinkering (required)

This is where you show the work is *yours*. In a short reflection (a few paragraphs):

   * What did you **try that didn't work** at first (a file too large to load, a
     column whose units you misread, a join on `unit_id` that dropped most rows, a
     plot that looked wrong until you filtered failed tests)? How did you fix it?
   * What **surprised you** in *your own* subset specifically — a target server
     that dominated the measurements, an ISP whose latency varied far more than
     its throughput, a time-of-day effect, a unit that reported impossible values?
   * If you used an LLM anywhere, name **one claim you checked against your data**
     (a column meaning, a unit conversion, a summary number it produced) and say
     whether it held up.

## Part 6: Stretch (extra credit, +10)

Anyone can summarize one file once; show you can reason about *how* the aggregation
changes the policy answer. Do **one** of these and paste the evidence:

   * **80/80 vs. the distribution.** On your own subset, compute the FCC's "80/80"
     statistic (the speed that 80% of panelists achieve at least 80% of the time)
     alongside medians and other percentiles (e.g., 10th, 50th, 90th) per ISP or
     per target. Paste the numbers side by side and explain which ISPs or users
     look different depending on the statistic, and why a regulator should care.
   * **Join a second dataset.** Join the MBA data with a second source (FCC
     Broadband Data Collection availability, Ookla open data, or Census ACS
     adoption or income data) on a key you can justify (ISP, technology,
     state, or time period). Paste the joined summary and explain what the
     second dataset lets you say that the MBA data alone cannot.

> **Using AI (encouraged, with verification).** You may use an LLM to help write
> analysis code or interpret a column you don't understand. If you do, **include the
> exchange in the appendix** and then **verify the model's claim against your own
> data** — point to the column, row count, or summary number that confirms (or
> contradicts) it. Submitting a number or interpretation you can't defend will lose
> points; catching the model in an error (a wrong unit, a misread column, a made-up
> field) will earn full marks for that item.

> **Be ready to defend it.** Per the syllabus, we may ask you to reproduce or explain any
> part of this lab live (office hours, a pop quiz, or the exam) — e.g., "open your
> notebook and recompute this table for a different ISP," or "why can't this sample
> answer a question about rural Illinois?" Do the work so you can.

### Submission Instructions

Submit a single markdown report named **`access-report.md`** plus the code or notebook
you used for the analysis. **Because your report is graded from its text, paste the
required evidence *as text* directly into the report** — the grader cannot run your
notebook or open your figures. In particular, paste the **summary numbers and tables**
your conclusions rest on, and describe each figure in words (what is on each axis, what
it shows). Screenshots and image files are welcome but are corroboration, not a
substitute for the pasted text.

Your report **must contain these headings, in this order** (they map one-to-one to the
rubric below):

```
# Internet Access Lab — <your name>

## 1. Sampling
   - Part 1 Q1a: what this ISP-stratified sample can answer
   - Part 1 Q1b: what it cannot answer

## 2. Metrics
   - Part 1 Q2a: why latency matters
   - Part 1 Q2b: why web browsing matters

## 3. Method
   - Part 1 Q3: how the whitebox design removes in-home Wi-Fi from the measurement

## 4. The Data
   - Which raw-data release (month/year) and which files you used
   - Row counts and date range of what you loaded; any subset you took and why

## 5. Your Policy Question
   - The single question, stated precisely
   - Why it matters for policy and who would act on the answer

## 6. Analysis & Results
   - Pasted summary numbers / tables; each figure described in words
   - How you computed them (grouping, aggregation, units, handling of failed tests)
   - Your answer to the question, with its limitations

## 7. Digital Equity
   - Part 4 Q1: why MBA cannot identify unserved/underserved areas
   - Part 4 Q2: what additional data you would need, and the collection challenges
   - Part 4 Q3: how a hyper-local approach addresses under-sampled geographies

## 8. Reflection & Tinkering
   - What you tried that didn't work; what surprised you in YOUR subset;
     one AI claim you verified against your data

## 9. (Extra credit) 80/80 vs. Distribution, or Second-Dataset Join
   - Which variant you did; pasted evidence; what differed and why

## Appendix: AI usage (if any)
   - Prompts, model output, and your verification against your data
```

Also include:

- Your analysis code or notebook, with **`access` or `equity` in the file name**
  (e.g., `access-analysis.ipynb` or `access-analysis.py`), so the grader can find it

Push the report and the code to your private GitHub repository. **Do not push the raw
FCC data files** (they are large); name the files you used in the report instead.

### Grading & Rubric (100 points)

Labs are graded primarily for thoughtful completion; points reward *understanding*,
not polish.

| Component | Points | What earns full marks |
|---|---|---|
| **Sampling** | 10 | You state what an ISP-stratified panel *can* answer (ISP-level and national comparisons, advertised vs. delivered, trends for the panel) and what it *cannot* (geographic questions, ISPs or tiers not in the panel, non-subscribers, in-home Wi-Fi experience). |
| **Metrics** | 8 | You explain why latency matters (it governs interactive applications and is not fixed by more bandwidth) and why web browsing matters (it is what users experience and does not keep improving with throughput). |
| **Method** | 7 | You explain how the whitebox, wired directly to the modem/router and testing only when the home network is idle, keeps Wi-Fi out of the measured path. |
| **The Data** | 10 | You name the release and files you used, give row counts and the date range you loaded, and state any subset you took and why. Your code or notebook is pushed. |
| **Your Policy Question** | 10 | One precise question the data you chose can actually answer, with a justification that names the policy decision and who would act on it. |
| **Analysis & Results (depth)** | 25 | You paste the summary numbers and tables, describe each figure, state how you computed them (grouping, aggregation, units, failed tests), answer your question directly, and tie limitations back to Part 1. |
| **Digital Equity (depth)** | 15 | You explain why a few thousand ISP-stratified volunteers cannot identify unserved or underserved places, what data digital equity actually needs and why it is hard to collect, and how a hyper-local approach exposes disparities a national panel averages away. |
| **Reflection & AI-verification** | 15 | You report what you *tried* (including dead ends), what surprised you in **your own** subset, and — if you used an LLM — at least one place you checked its claim against your data and what you found. |
| **Extra credit: 80/80 vs. distribution, or second-dataset join** | +10 | You compare aggregation statistics on your own subset, or join a second dataset, and paste the evidence. See the stretch task above. |

Cite evidence by **pasted numbers and tables** (with the file, columns, and subset they
came from) so a grader can check your reasoning without running your code. The
reflection must be grounded in *your* specific subset — generic prose that could
describe anyone's run earns little credit.
