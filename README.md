# NBA DFS Spreadsheet

![IMG_0091](https://user-images.githubusercontent.com/58003892/135906041-df59f554-874d-4414-bbed-fd13f4c077f8.jpg)

This spreadsheet is used for NBA DFS purposes for the FanDuel website, all salaries & projections are tailored for FanDuel. The data used in the sheet comes from the following sources, scraped and updated daily; 

- FanDuel: player list CSV which includes; salary, fantasy points per game, players team, and players opponent
- NumberFire: player projections
- FantasyPros: player projections, DvP (defense vs. position)
- Rotogrinders: DvA (defense vs. archtype)
- NBA.com: Usage Rate

The spreadsheet uses both numberfire and fantasypros projections to get an average of both sites projections so we can pull projections from mulitple sources. It also calculates value for a player on a given slate. We find value by taking a players salary, dividing it by 1000, and the multiplying it by 5, for example; James Harden is priced at $11,400 so first we divide his salary by 1000 to get 11.4 and then we multiply it by 5 (11,400/1000)*5 = 57. Since DFS is all about finding value, in order for James Harden on this night that he costs $11,400 to hit 5x value he would need to score at least 57 fantasy points.

The columns for the main sheet are as follows;

- Players Position
- Players Name
- Salary
- Team
- Opponent
- Projection
- Value
- Usage
- DvP (Defense vs players position)
- DvA (Defense vs Archtype)
- USG% (players usage which is in float value but is read as a percentage)
- PTS for 5x value (amount of points a player needs to score in order to hit 5x value)


The main sheet labeled 'Data Table', uses VLOOKUP function to grab the data from the other sheets like 'numfire', 'fpros', and 'projections' for example;

=VLOOKUP(B2,numfire!A:C,3,false) -- the B column on Sheet 1 is the players name, so in the B2 cell that players name is found in the numfire sheet and the projection is pulled into the Data Table sheet, it searches for that players name between columns A:C and the projection value is located at index 3, false refers to [is_sorted] so by passing in false the function knows the players names on each sheet are not sorted.

** Players that have projections or cells that are N/A most likely means they're not playing that night, sheet is updated 2-3 times a day as news comes out closer to tipoff **

The .TSV sheet can be viewed right on github but you cannot filter columns or anything, the sheet is available for download in XLM form so you can import it into excel or google sheets(which I use to create the sheets)

# Breakdown of files included in this repository:

- numberfire_scrape.py file has comments to help you scrape numberfire projections on your own in python with selenium, the comments are very detailed
- usagescrape.py file is used to scrape usage rates from NBA.com; selenium connects to the website, filters to all players, scrapes just the players name and his usage rate
- dvp_scrape.py file is used to scrape Defense vs Position data from fantasypros based on Fantasy Points Per Game given up by defenses based on Fanduel scoring, the program connects to fantasypros DvP page and selects one of the following; points per game given up in the last 7 or 15 games just uncomment whichever range you want selenium to scrape (I personally have created lineups with both of them but have gravitated towards last 7 games), the program puts all of the data into a pandas DataFrames and then into a master_dataframe which joins all the dataframes for each position and saves the master dataframe to a csv file called 'dvp.csv'
- NBA_scrape.py is basically the numberfire and DvP scrape in one file
- fanduel_clean.py is a basic file, in order to use it you first need to download the slates player list from Fanduel, save it in your code editor as 'fanduel.csv' and scrape numberfire projections saved in a csv 'projections.csv'. Once you have done both this file opens the fanduel csv and drops columns we do not need (12 columns to be exact) as well as replacing apostrophes and periods in players names, the same replacing is done with the projections.csv file so players names all match when we import into excel, the changes to both files are saved back to the csv files.


Basic work flow : (1) numberfire_scrape.py > (2) dvp_scrape.py > (3) usagerate.py > (4) fanduel_clean.py > (5) export all CSV files to excel/google sheets

Or

(1) NBA_scrape.py > (2) usagerate.py > (3) fanduel_clean.py > (4) export all CSV files to excel/google sheets

This sheet and the data pulled will be building blocks to a machine learning program which will help create optimized lineups for each slate on the FanDuel website.  

Special thanks to contributor : Shan Mohamed - a long time friend, fantasy sport enthusiast, and excel expert.
