# Election Audit Results and Analysis

## Overview of a Project

We have been asked to assist **Colorado Board of Elections** employees Tom and Seth in their election audit of the results for a U.S. congressional precinct in Colorado. Tom and Seth had asked us to create a Python code that would parse through election results data contained in a csv file and calculate and report the total number of votes cast, the total number of votes for each candidate, the percentage of votes for each candidate, and the winner of the election based on the popular vote. They have also asked us to calculate voter turnout for each county, percentage of votes from each county out of the total count and the county with the highest turnout.

We have broken down the project into the following 5 steps:

1. Calculate the total number of votes cast.
2. Get a complete list of candidates who received votes.
3. Calculate the total number of votes each candidate received.
4. Calculate the percentage of votes each candidate won.
5. Determine the winner of the election based on popular vote.


## Resources
 - Data Source: [election_results.csv](https://github.com/vkbt/Election_Analysis/blob/main/Resources/election_results.csv)
 - Software: Python **3.9.12**, Visual Studio Code, **1.72.2**


## Summary
The analysis of the election shows that:
 - There were 369,711 votes cast in the election.
 - The candidates were:
     - Charles Casper Stockham
     - Diana DeGette
     - Raymon Anthony Doane
 - The candidate results were:
     - Charles Casper Stockham received 23.0% of the vote and 85,213 number of votes.
     - Diana DeGette received 73.8% of the vote and 272,892 number of votes.
     - Raymon Anthony Doane received 3.1% of the vote and 11,606 number of votes.
 - The winner of the election was:
     - Diana DeGette, who received 73.8% of the vote and 272,892 number of votes.


[Election Results](https://github.com/vkbt/Election_Analysis/blob/main/analysis/election_results.txt)

<details>
 <summary>Click here to see Election Analysis text file</summary>
 
   ### [Election Results](https://github.com/vkbt/Election_Analysis/blob/main/analysis/election_results.txt)
  ```
  
Election Results
-------------------------
Total Votes: 369,711
-------------------------

County Votes:
Jefferson: 10.5% (38,855)
Denver: 82.8% (306,055)
Arapahoe: 6.7% (24,801)

-------------------------
Largest County Turnout: Denver
-------------------------
Charles Casper Stockham: 23.0% (85,213)
Diana DeGette: 73.8% (272,892)
Raymon Anthony Doane: 3.1% (11,606)
-------------------------
Winner: Diana DeGette
Winning Vote Count: 272,892
Winning Percentage: 73.8%
-------------------------
  ```
</details>

#### Terminal vs Text File
<p float="left">
 <img src="https://github.com/vkbt/Election_Analysis/blob/main/Resources/PyPoll%2Bcounties%20terminal%20output.png" width=40% height=40%>
 <img src="https://github.com/vkbt/Election_Analysis/blob/main/Resources/PyPoll%2Bcounties%20text%20file%20output.png" width=40% height=40%>
 </p>
 
## Challenge Overview

To get requested results we created a number of variables, loops and conditional statements in Visual Code Studio. For a better, user-friendly view, we have created a separate text file that showed election analysis result. The output in text file will change if data from csv file changes. This is useful if the script will be used for future election analyses.

## Challenge Summary


With additional ZIP code information  the script can go even further and show us which candidate is more popular within his or her ZIP code. 
We would also suggest additional demographic information to the data that would show us total population of the ZIP code or county allowing us to calculate percentage of voting population.
