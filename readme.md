# Log Analysis
## Intro 
This is a reporting tool used to gain insights into the data, it prints out the results in plain text. This tool is built using **Python**, queries are made using **PostgreSQL**.
## What it does?
The tool answers the following questions:
* What are the most popular three articles of all time?
* Who are the most popular article authors of all time?
* On which days did more than 1% of requests lead to errors?
## What you need beforehand
To use the tool you will need to:
* Have [Python](https://www.python.org/downloads/) installed.
* Install [VirtualBox](https://www.virtualbox.org/wiki/Downloads), to create a virtual machine.
* Install [Vagrant](https://www.vagrantup.com/), to manage the VM.
* Install [Git](https://git-scm.com/), you'll need Git Bash to run queries.
## Instructions
Follow these steps to use the reporting tool:
1. Update to the latest version of Python.
2. Install VirtualBox, Vagrant and Git.
3. Follow the instructions on this [link](https://github.com/udacity/fullstack-nanodegree-vm) to get Vagrant up and running. 
4. Download the [data](https://d17h27t6h515a5.cloudfront.net/topher/2016/August/57b5f748_newsdata/newsdata.zip), this is the news data that the reporting is performed on.
5. Unzip this file after downloading it. The file inside is called ```newsdata.sql```. Put this file into the ```vagrant``` directory.
6. To Load the data, ```cd``` into the ```vagrant``` directory and run the command ```psql -d news -f newsdata.sql```.
7. Connect to the database using ```sql -d news```.
**Note:** To answer the third question you must run the views first as shown later in the document.
8. To run the python file and get the required results, run the command ```python news.py```.
## About the data
The database includes three tables:
- The _authors_ table includes information about the authors of articles.
- The _articles_ table includes the articles themselves.
- The _log_ table includes one entry for each time a user has accessed the site.
## Navigate the data
To explore the database use the following commands:
* ```\dt``` — display tables — lists the tables that are available in the database.
* ```\d table``` — (replace table with the name of a table) — shows the database schema for that particular table.
## Views
Views are only used in the third question, run the following commands to generate them.
* The _up_ view, which counts the number of **bad** requests.
```create view up as select date(log.time)as date,count(status) as cnt from log where status like '404 NOT FOUND' group by date```
* The _down_ view, which counts the number of **all** requests.
```create view down as select date(log.time) as date,count(status) as cnt from log group by date```
* The _error_ view, which calculates the percentage of bad requests to total requests.
```create view error as select down.date ,CAST(up.cnt as FLOAT)*100/down.cnt as errorperc from up,down where up.date=down.date order by errorperc```


