import pandas as pd


df = pd.read_csv('Epl2021.csv')
Odds = pd.read_csv('E0 (1).csv')

oddsA = []
oddsH = []
oddsD = []
oddsOv =[]
oddsUn =[]


Odds.rename(columns = {'HomeTeam':'Home Team'}, inplace = True)
Odds.rename(columns = {'AwayTeam':'Away Team'}, inplace = True)

DF = df.merge(Odds,how='inner',on=['Home Team','Away Team'])
df.reindex(['Home Team', 'Away Team'])

        

DF.to_csv('Full2021.csv')





