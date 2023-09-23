# EnglishPremierLeaguePredictor

EnglishPremierLeaguePredictor is a predictor of Premier League games based on historic performances of teams, taking into account advanced league table statistics. It uses traditional machine learning techniques and statistical modeling in order to deduct data driven predictions based on the team’s season performance and recent form. The model evaluation has shown promising results on predicting past seasons, proving its capability to be profitable using certain betting strategies something that could provide impactful data-driven insights for either the bookmaker as well as the bettor.


## Betting Disclaimer

The EnglishPremierLeaguePredictor project and its associated predictions are provided for informational purposes. The predictions generated by this project should not be considered as financial advice or recommendations to place bets on any Premier League matches or other events.

Betting involves risks, and there is no guarantee that the predictions provided by this project will result in accurate outcomes or profitable bets. The outcomes of sports events can be influenced by a wide range of variables that may not be fully captured by the prediction model.


## Visit the Github Page
The [EnglishPremierLeaguePredictor Github Page](https://nickpadd.github.io/EPLP.github.io/Home) provides a detailed description of the model creation and evaluation on past seasons, as well as the upcoming predictions of this week's premier league games!


## Running the project
### Installing the dependencies
1. Clone this repository to your local machine or download the project files.

   ```bash
   git clone https://github.com/nickpadd/EnglishPremierLeaguePredictor

2. Navigate to the project directory using the command line.
    ```bash
    cd EnglishPremierLeaguePredictor

3. Install project dependencies from the requirements file.

    ```bash
    pip install -r requirements.txt

### Running the scripts for the upcoming matches
To run the model for the upcoming games open the jupyter file 'BookmakerScraping.ipynb' and run it in the environment created from the requirements above to scrape the upcoming matches and odds provided by a popular greek betting site (be careful there might be location restrictions). This script also updates the file of the current season and runs some of the python scripts needed in order to produce the updated datasets needed for the upcoming games prediction. 

After completing the above steps open the 'PoissonVotingPredictor.ipynb' and run the jupyter file in the environment created from the requirements above to produce the upcoming games predictions and prediction figure. The last two are output with the names 'UpcomingMatchesPrediction.html' and 'UpcomingMatchesPredictionFigure.html'. 

Open the above files to see the predictions of the model or visit the [EnglishPremierLeaguePredictor Github Page Upcoming Matches section](https://nickpadd.github.io/EPLP.github.io/Upcoming) to just get updated on the predictions of the upcoming games.


## Future Plans
The project can be upgraded to include all of the most popular leagues included in Understat (Bundesliga, Ligue1, LaLiga, Serie A). Making an all around model that includes all of the mentioned leagues could be a future enchancement. This also opens the road for European competition predictions.
