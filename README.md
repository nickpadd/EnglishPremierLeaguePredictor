# EnglishPremierLeaguePredictor

EnglishPremierLeaguePredictor is a predictor of Premier League games based on historic performances of teams, taking into account their league table statistics.

## Data Collection and Training

We collected historic data from the league table using [Understat](https://understat.com/ "Understat's Homepage") and its [API](https://understat.readthedocs.io/en/latest/ "Understat API") from 2017 to 2022 for each team, one day before each individual match. This data was then correlated with historic results and odds gathered through [Football-Data.co.uk](https://www.football-data.co.uk/englandm.php "Football-Data.co.uk"). A linear regression algorithm was trained to predict Home Goals and Away Goals.

## Including Form into the Method

To incorporate recent form into our predictions, we repeated the process mentioned above, but only considered the last month of the league table. This allowed us to compute predictions based on the current form of teams. We then implemented a voting system to choose between the season-long prediction and the form-based prediction.

## Model Validation and Results

We tested our model using cross-validation, training on all seasons but one and testing it on the hidden season. After hyperparameter optimization, our findings indicated that betting on "Under" can be profitable. The cross-validation results are available in the 'PoissonPerSeason_CrossValidation.ipynb' file.

![Profit example of the algorithm](https://github.com/nickpadd/EnglishPremierLeaguePredictor/blob/main/ExamplePlotProfit.png?raw=true)

## Running the Algorithm for Upcoming Games

To predict upcoming game outcomes, we scrape the betting website Stoiximan to gather upcoming match details and provided odds. This scraping process is performed using the 'StoiximanScraping.ipynb' file. The file also contains all the necessary scripts to update and run the predictor for upcoming matches.

![Example of predicted match Odds](https://github.com/nickpadd/EnglishPremierLeaguePredictor/blob/main/ExamplePlot.png?raw=true)

## Result Validation

The accuracy of our predictions was evident in the following correct prediction:

![Result of predicted match Odds](https://github.com/nickpadd/EnglishPremierLeaguePredictor/blob/main/ExampleResult.png?raw=true)

This demonstrates the effectiveness of our approach in predicting Premier League match outcomes.

