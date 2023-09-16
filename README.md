# EnglishPremierLeaguePredictor

EnglishPremierLeaguePredictor is a predictor of Premier League games based on historic performances of teams, taking into account their league table statistics. 

## Upcoming Matches

The predicted results of the following premier league matches in comparison with the bookmaker's odds can be seen in the following figure:

![Profit example of the algorithm](https://github.com/nickpadd/EnglishPremierLeaguePredictor/blob/main/UpcomingMatchesPredictionFigure.html?raw=true)

A more detailed view can be seen in the "UpcomingMatchesPredictionTable.html".

## Betting Disclaimer

The EnglishPremierLeaguePredictor project and its associated predictions are provided for informational purposes. The predictions generated by this project should not be considered as financial advice or recommendations to place bets on any Premier League matches or other events.

Betting involves risks, and there is no guarantee that the predictions provided by this project will result in accurate outcomes or profitable bets. The outcomes of sports events can be influenced by a wide range of variables that may not be fully captured by the prediction model.


## Data Collection and Training

We collected historic data from the league table using [Understat](https://understat.com/ "Understat's Homepage") and its [API](https://understat.readthedocs.io/en/latest/ "Understat API") from 2017 to 2022 for each team, one day before each individual match. This data was then correlated with historic results and odds gathered through [Football-Data.co.uk](https://www.football-data.co.uk/englandm.php "Football-Data.co.uk"). A linear regression algorithm was trained to predict Home Goals and Away Goals.

## Including Form into the Method

To incorporate recent form into our predictions, we repeated the process mentioned above, but only considered the last month of the league table. This allowed us to compute predictions based on the current form of teams. We then implemented a voting system to choose between the season-long prediction and the form-based prediction. Using the Poisson probability density function those predictions were converted to probabilities and the most popular odds of Home Win, Draw, Away Win, Over 2.5 Goals, Under 2.5 Goals and probable scorelines were calculated.

## Model Validation and Results

 The model's hyperparameters (the condfidence it needs to bet on something) were tuned via random shuffling technique including all seasons. After hyperparameter optimization, our findings indicated that betting on "Under" can be profitable.

![Profit example of the algorithm](https://github.com/nickpadd/EnglishPremierLeaguePredictor/blob/main/Examples/ExamplePlotProfit.png?raw=true)


We then tested our model using cross-validation, training on all seasons but one and testing it on the hidden season. More precisely with 'PoissonPerSeason.ipynb' we test the algorithm on seasons 2020-2022 with the following results:

![Betting on Under in 2020 Season](https://github.com/nickpadd/EnglishPremierLeaguePredictor/blob/main/Examples/Under2020.png?raw=true)
![Betting on Under in 2021 Season](https://github.com/nickpadd/EnglishPremierLeaguePredictor/blob/main/Examples/Under2021.png?raw=true)
![Betting on Under in 2022 Season](https://github.com/nickpadd/EnglishPremierLeaguePredictor/blob/main/Examples/Under2022.png?raw=true)

## Running the Algorithm for Upcoming Games

To predict upcoming game outcomes, we scrape the betting website Stoiximan to gather upcoming match details and provided odds. This scraping process is performed using the 'StoiximanScraping.ipynb' file. The file also contains all the necessary scripts to update and run the predictor for upcoming matches. For each match a plot containing the most popular odds as calculated by the algorithm and compared to the betting company is produced. This provides an easy evaluation of the provided odds of the betting company. Furthermore the script also produces a table with all the available matches and a suggested bet using the Kelly betting algorithm provided a bank of 50 euros (can be adjusted through the script bank variable).

![Example of predicted match Odds](https://github.com/nickpadd/EnglishPremierLeaguePredictor/blob/main/Examples/ExamplePlot.png?raw=true)

## Result Validation
In that exact case our prediction was succesfull and indeed better than that of the betting company.

![Result of predicted match Odds](https://github.com/nickpadd/EnglishPremierLeaguePredictor/blob/main/Examples/ExampleResult.png?raw=true)


