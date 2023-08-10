# EnglishPremierLeaguePredictor
A predictor of premier league games based on historic perfomances of teams taking into account their league table statistics. 

We gathered historic data from the league table using [Understat](https://understat.com/ "Understat's Homepage") and it's [API](https://understat.readthedocs.io/en/latest/ "Understat API") from 2017-2022 for each team one day before each individual match. We then mapped them to each historic result and odds gathered through [Football-Data.co.uk](https://www.football-data.co.uk/englandm.php "Football-Data.co.uk") and trained a linear regression algorithm to predict Home Goals and Away Goals. 

To include form into our method we repeated the above process but only kept the last 1 month of the league table thus computing a prediction of form. We then use a voting system to vote between the season long prediction and the form prediction. We then tested our model by cross validation, training from all seasons but one, and testing it on the hidden season. After the hyperparameter optimization it is concluded that betting on "Under" can provide profit. The cross validation of the method is provided in the 'PoissonPerSeason_CrossValidation.ipynb' file.

![Profit example of the run of the algorithm](https://github.com/nickpadd/EnglishPremierLeaguePredictor/blob/main/ExamplePlotProfit.png?raw=true)


To run the algorithm for the upcoming games we scrape the betting website Stoiximan, to gather the upcoming matches and the provided odds. This is done via the 'StoiximanScraping.ipynb' file. In that file there are also run all the scripts needed to run the predictor updated for the upcoming matches.

![Example of predicted match Odds](https://github.com/nickpadd/EnglishPremierLeaguePredictor/blob/main/ExamplePlot.png?raw=true)

The result of the above prediction was indeed correct as we can see below:

![Result](https://github.com/nickpadd/EnglishPremierLeaguePredictor/blob/main/Screenshot from 2023-08-10 15-20-42.png.png?raw=true)

