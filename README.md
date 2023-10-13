# README [![CI](https://github.com/nogibjj/Project7_Vivian/actions/workflows/ci.yml/badge.svg)](https://github.com/nogibjj/Project7_Vivian/actions/workflows/ci.yml)
This repository features the materials for Mini-Project 6. The important files are:
- setup.py
- Makefile
- cicd.yml
- lib.py
- main.py
- test_main.py
- .env(a hidden file)
- log.md (a log file)

## Purpose Of Project
- Connect to a cloud mySQL database
- Design a complex SQL query involving joins, aggregation, and sorting and perform the query with CICD.
- Create an ETL-Query pipeline utilizing MySQL cloud database and create an executable by packaging the project. 

## Preparation 
1. open the project in codespaces
2. container built and virtual environment to be activated through requirements.txt

## Steps
1. set up a cloud MySQL database called "BarBeerDrinker" which includes 2 tables: Bar and Sells. Bar includes all in-network bars and Sells includes all past time, type, and year of the beers sold at each bar. 
2. make a .env file and store my connection information including SERVER_HOSTNAME, SERVER_PORT, USER_NAME, ACCESS_TOKEN, and DATABASE_NAME.
3. build packaged project by running: "python setup.py develop --user"

<img width="936" alt="Screen Shot 2023-10-13 at 1 49 49 PM" src="https://github.com/nogibjj/Project7_Vivian/assets/143654445/8d5189ac-2b4e-4ab4-86eb-f99ebbbda072">

5. Run in command-line "etl_query" which will call main.py and do the following:
   - connect to the cloud database and run a complex query.
   - obtain the result after querying on the cloud database.
<img width="580" alt="Screen Shot 2023-10-13 at 1 48 39 PM" src="https://github.com/nogibjj/Project7_Vivian/assets/143654445/ea3b2761-4951-40e8-998f-32c3dcffe908">

## Check Format & Errors
1. make format
2. make lint
   
<img width="486" alt="Screen Shot 2023-10-13 at 1 50 39 PM" src="https://github.com/nogibjj/Project7_Vivian/assets/143654445/44ab2fd0-1a30-46f7-b1d3-a755895ce2b3">
   
3. make test
   
<img width="940" alt="Screen Shot 2023-10-13 at 1 50 23 PM" src="https://github.com/nogibjj/Project7_Vivian/assets/143654445/cbbd76f9-7c35-4f8b-ae52-e112b3676270">

## Query
Query and Results: 

<img width="527" alt="Screen Shot 2023-10-08 at 6 20 56 PM" src="https://github.com/vivianzzzzz/Template/assets/143654445/2d93b277-f24c-49ec-ad32-0f9dcd4f0485">

Explanation:
This query left-joins table "Bars" with a sub-table from "Sells" which I name it "a" 
- the sub-table "a" is created through the sub-query "SELECT s.bar FROM Sells s WHERE s.price > 5" which retrieves the names of bars from the Sells table where the selling price of some item is greater than 5.
- the LEFT JOIN attempts to join the result from the sub-table to the Bars table based on the condition where a.bar matches the name of the bar in the Bars table. The use of a LEFT JOIN ensures that all rows from the Bars table (even those that do not have a matching bar in the subquery) will be included in the result.
- "WHERE a.bar IS NULL": filters out all rows where there is a match between Bars and the subquery. In other words, it retains only those bars from Bars that don't sell any item for a price greater than 5. It effectively gives us bars that only sell items at a price of 5 or less.
- "GROUP BY city": After the join and filter conditions are applied, the resulting set of records is grouped by the city where the bars are located.
- "SELECT city, count(city)" Finally, the query selects the name of each city from these grouped records and counts how many bars in each city fit the criteria (only sell items for a price of 5 or less).

Final Output:
The result of the query will be a list of cities and the number of bars in each city that do not have any item priced above 5.
This result can also be retrieved in the log file. 


## Visualization

<img width="368" alt="Screen Shot 2023-09-30 at 11 31 51 AM" src="https://github.com/vivianzzzzz/Template/assets/143654445/8b808d80-0203-40e7-86d0-27380c4cfbae">




