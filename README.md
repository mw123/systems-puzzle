# Insight DevOps Engineering Systems Puzzle

## Table of Contents
1. [Understanding the puzzle](README.md#understanding-the-puzzle)
2. [Introduction](README.md#introduction)
3. [Puzzle summary](README.md#puzzle-summary)
4. [Instructions to submit your solution](README.md#instructions-to-submit-your-solution)
5. [FAQ](README.md#faq)

# Understanding the puzzle

We highly recommend that you take a few dedicated minutes to read this README in its entirety before starting to think about potential solutions. You'll probably find it useful to review the examples and understand the problem at a high-level before digging into the specific details, many of which are covered in the FAQ.

# Introduction



# Puzzle summary




## Instructions to submit your solution
* To submit your entry please use the link you received in your systems puzzle invite email
* You will only be able to submit through the link one time 
* Do NOT attach a file - for security, we will not open solutions submitted via files
* Use the submission box to enter the link to your GitHub repo or Bitbucket ONLY
* Link to the specific repo for this project, not your general profile
* Put any comments in the README inside your project repo, not in the submission box
* We are unable to accept systems puzzles that are emailed to us 

# FAQ

Here are some common questions we've received. If you have additional questions, please email us at `devops@insightdata.com` and we'll answer your questions as quickly as we can (during PST business hours), and update this FAQ. Again, only contact us after you have read through the Readme and FAQ one more time and cannot find the answer to your question.


### Which Github link should I submit?
You should submit the URL for the top-level root of your repository. For example, this repo would be submitted by copying the URL `https://github.com/InsightDataScience/edgar-analytics` into the appropriate field on the application. **Do NOT try to submit your coding puzzle using a pull request**, which would make your source code publicly available.

### Do I need a private Github repo?
No, you may use a public repo, there is no need to purchase a private repo. You may also submit a link to a Bitbucket repo if you prefer.

### Are the session durations inclusive or exclusive?  
As shown in the above example, the duration is inclusive. In other words, if the timestamps for the session start is 00:00:01 and session end is 00:00:03, the duration is 3 seconds.  

### What if there is a single request in a session?  
As shown in the above example, the minimum duration for a session is 1 second.  

### If a user requests the same document more than once during a session, how many webpage requests is that?
Every time a user accesses an EDGAR document, that request should be counted even if the user is requesting the same document multiple times. For instance, if within a session, there are two requests, once for cik: `1608552.0`, accession: `0001047469-17-004337` and extention: `-index.htm` and then a second time for the same exact combination, the count of webpage requests for that session would be 2.

### How do you know when a session is over?  
As shown in the above example, the session is over when the end of the file is reached or after a period of inactivity has elapsed with no requests from that user. For example, if the inactivity period is 2 seconds, and the session start is 00:00:01 and there are no further requests from that user by 00:00:04, then the session is considered over at 00:00:01.  

### Where can I get the input file, `log.csv`?
We've provided one example as shown above in this README for you to better understand the puzzle but you should create your own data to test your program. You can obtain other data [directly from the SEC](https://www.sec.gov/dera/data/edgar-log-file-data-set.html) but be aware that the weblog files are quite large and you also may have problems decompressing the archive file. `Unzip` may not work on the EDGAR zip file, and you may have to use open source software such as `7zip`. If you are unable to decompress the zip file, revert to creating your own data for the puzzle. Do not spend too long on trying to decompress the archive file.

### May I use R, Matlab, or other analytics programming languages to solve the puzzle?
It's important that your implementation scales to handle large amounts of data. While many of our Fellows have experience with R and Matlab, applicants have found that these languages are unable to process data in a scalable fashion, so you must consider another language.

### May I use distributed technologies like Hadoop or Spark?
Your code will be tested on a single machine, so using these technologies will negatively impact your solution. We're not testing your knowledge on distributed computing, but rather on computer science fundamentals and software engineering best practices. 

### What sort of system should I use to run my program on (Windows, Linux, Mac)?
You may write your solution on any system, but your source code should be portable and work on all systems. Additionally, your `run.sh` must be able to run on either Unix or Linux, as that's the system that will be used for testing. Linux machines are the industry standard for most data engineering teams, so it is helpful to be familiar with this. If you're currently using Windows, we recommend installing a virtual Unix environment, such as VirtualBox or VMWare, and using that to develop your code. Otherwise, you also could use tools, such as Cygwin or Docker, or a free online IDE such as Cloud9.

### How fast should my program run?
While there are no strict performance guidelines to this coding puzzle, we will consider the amount of time your program takes when grading the puzzle. Therefore, you should design and develop your program in the optimal way (i.e. think about time and space complexity instead of trying to hit a specific run time value). 

### Can I use pre-built packages, modules, or libraries?
This coding puzzle can be completed without any "exotic" packages. While you may use publicly available packages, modules, or libraries, you must document any dependencies in your accompanying README file. When we review your submission, we will download these libraries and attempt to run your program. If you do use a package, you should always ensure that the module you're using works efficiently for the specific use-case in the puzzle, since many libraries are not designed for large amounts of data.

### Should I use the Pandas library for Python?  
While the Pandas library is useful for many problems related to small batches of data, it is not scalable at dealing with streaming data problems like this puzzle. As a result, you should strongly consider alternative algorithms and data structus that scale with larger, streaming data.

### Will you email me if my code doesn't run?
Unfortunately, we receive hundreds of submissions in a very short time and are unable to email individuals if their code doesn't compile or run. This is why it's so important to document any dependencies you have, as described in the previous question. We will do everything we can to properly test your code, but this requires good documentation. More so, we have provided a test suite so you can confirm that your directory structure and format are correct.

### Can I use a database engine?
This coding puzzle can be completed without the use of a database. However, if you use one, it must be a publicly available one that can be easily installed with minimal configuration.

### Do I need to use multi-threading?
No, your solution doesn't necessarily need to include multi-threading - there are many solutions that don't require multiple threads/cores or any distributed systems, but instead use efficient data structures.

### What should the format of the output be?
In order to be tested correctly, you must use the format described above. You can ensure that you have the correct format by using the testing suite we've included.

### Should I check if the files in the input directory are text files or non-text files(binary)?
No, for simplicity you may assume that all of the files in the input directory are text files, with the format as described above.

### Can I use an IDE like Eclipse or IntelliJ to write my program?
Yes, you can use whatever tools you want - as long as your `run.sh` script correctly runs the relevant target files and creates the `sessionization.txt` file in the `output` directory.

### What should be in the input directory?
You can put any text file you want in the directory since our testing suite will replace it. Indeed, using your own input files would be quite useful for testing. The file size limit on Github is 100 MB so you won't be able to include the larger sample input files in your `input` directory.

### How will the coding puzzle be evaluated?
Generally, we will evaluate your coding puzzle with a testing suite that provides a variety of inputs and checks the corresponding output. This suite will attempt to use your `run.sh` and is fairly tolerant of different runtime environments. Of course, there are many aspects (e.g. clean code, documentation) that cannot be tested by our suite, so each submission will also be reviewed manually by a data engineer.

### How long will it take for me to hear back from you about my submission?
We receive hundreds of submissions and try to evaluate them all in a timely manner. We try to get back to all applicants **within two or three weeks** of submission, but if you have a specific deadline that requires expedited review, please email us at `cc@insightdataengineering.com`.

