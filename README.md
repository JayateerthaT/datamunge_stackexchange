# datamunge_stackexchange

## Project related to SimpliLearn course
### Steps to followed
   * Dowload the file from specified url
   * Clean data file: Retain required columns. Processing of file becomes much easier. 
   * Run PigLatin scripts on the processed file to arrive at the solution. 
   
Refer socialmedia_project_report.pdf contains all the steps followed. This approach was taken as CloudLab was taking too much time in running scripts. Executed all scripts local system. Final working report generated based on the CloudLab results.  

### stack is scrapy example 
   * Crawls stackoverflow.com extracts title, url, description & question tag details
   * After processing first page navigates to next page t extract the details.
   * Execute the following command to extract site details
   * scrapy crawl stack -o output.json -t json
