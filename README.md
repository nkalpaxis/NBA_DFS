# NBA DFS Spreadsheet

This spreadsheet is used for NBA DFS purposes for the FanDuel website, all salaries & projections are tailored for FanDuel. The data used in the sheet comes from the following sources, updated daily; 

- FanDuel player list CSV which includes: salary, fantasy points per game, players team, and players opponent
- NumberFire: player projections
- LineUps: player projections, usage rate (in %), and DvP (defense vs position) -- this sheet is named DFF in the spreadsheet

The spreadsheet uses both numberfire and lineups projections to get an average of both sites projections so we can pull projections from mulitple sources. It also calculates value for a player on a given slate. We find value by taking a players salary, dividing it by 1000, and the multiplying it by 5, for example; James Harden is priced at $11,400 so first we divide his salary by 1000 to get 11.4 and then we multiply it by 5 (11,400/1000)*5 = 57. Since DFS is all about finding value, in order for James Harden on this night that he costs $11,400 to hit 5x value he would need to score at least 57 fantasy points.

The columns for the main sheet are as follows;

- Players Position
- Players Name
- Fantasy Points Per Game (FPPG)
- Salary
- Team
- Opponent
- NF Proj (numberfire projection)
- NF Value (numberfire value)
- DFF Proj (lineups projection)
- DFF Value (lineups value)
- DvP (Defense vs players position)
- USG% (players usage which is in float value but is read as a percentage)
- Final Proj (numberfire and lineups projections added and divided by 2 for the average)
- Final Value (numberfire and lineups value added and divided by 2 for the average)
- PTS for 5x value (amount of points a player needs to score in order to hit 5x value)
- Minutes (per game) 

The main sheet labeled 'Sheet 1', uses VLOOKUP function to grab the data from the other sheets like 'numfire' and 'dff', for example;

=VLOOKUP(B2,numfire!A:C,3,false) -- the B column on Sheet 1 is the players name, so in the B2 cell that players name is found in the numfire sheet and the projection is pulled into Sheet 1, it searches for that players name between columns A:C and the projection value is located at index 3, false refers to [is_sorted] so by passing in false the function knows the players names on each sheet are not sorted.

** Players that have projections or cells that are N/A most likely means they're not playing that night, sheet is updated 2-3 times a day as news comes out closer to tipoff **

The .TSV sheet can be viewed right on github but you cannot filter columns or anything, the sheet is available for download in XLM form so you can import it into excel or google sheets(which I use to create the sheets)

This sheet and the data pulled will be building blocks to a machine learning program which will help create optimized lineups for each slate on the FanDuel website.  

Special thanks to contributor : Shan Mohamed - a long time friend, fantasy sport enthusiast, and excel expert.
