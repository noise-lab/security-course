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

   a. What types of questions can be answered with this type of sample?
   b. What types of questions cannot be answered with this type of sample?:w
   
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
   Initiative](https://internetequity.uchicago.edu/) project at the University of
   Chicago and recall the discussion from class. How would a "hyper-local"
   approach, such as that being taken in this project, help to address the
   problem of under-sampled geographies?

The following
[paper](https://papers.ssrn.com/sol3/papers.cfm?abstract_id=4179787) might
provide some guidance on how to approach this question, with some initial food
for thought.
