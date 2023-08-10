import numpy as np
import math
import pandas as pd
import asyncio
import aiohttp
import pandas as pd
from datetime import date, timedelta
import datetime
from understat import Understat
from dateutil.relativedelta import relativedelta


async def main():
        async with aiohttp.ClientSession() as session:
            understat = Understat(session)
            df = pd.read_csv('Newfixtures.csv')
            df.rename(columns = {'1':'B365H'}, inplace = True)
            df.rename(columns = {'x':'B365D'}, inplace = True)
            df.rename(columns = {'2':'B365A'}, inplace = True)
            df.rename(columns = {'Over':'BbAv>2.5'}, inplace = True)
            df.rename(columns = {'Under':'BbAv<2.5'}, inplace = True)
            df = df[['Date', 'Home Team', 'Away Team', 'Result', 'B365H', 'B365D', 'B365A', 'BbAv>2.5', 'BbAv<2.5']]
            df['Date'] = list(df['Date'].str.split(' '))
            df['Date'] = df['Date'].str[0]


            UniqDates = df["Date"].unique()

            HOME = []
            AWAY = []
            HOME1 = []
            AWAY1 = []

            for i, x in enumerate(UniqDates):
                #TEAMSTATS
                #format dates for understat fixtures and go to the previous day of the match
                helpdf = df.loc[df['Date'] == str(UniqDates[i])]
                UniqDates[i] = datetime.datetime.strptime(UniqDates[i], '%d/%m/%Y').date()
                UniqDates[i] = UniqDates[i] - datetime.timedelta(days=1)

                table = await understat.get_league_table("EPL", 2022, start_date=str(UniqDates[i]+relativedelta(months=-2)))
                Table = pd.DataFrame(table)
                Table.columns = Table.iloc[0]
                Table = Table.iloc[1: , :]
                Table = Table[['Team', 'M', 'G', 'GA', 'PTS', 'xG', 'xGA', 'PPDA', 'OPPDA', 'DC', 'ODC']]
        

                print(x)
                print(helpdf['Home Team'])
                print(helpdf['Away Team'])

                HomeStats = Table.loc[Table['Team'].isin(helpdf['Home Team'].to_list())]
                HomeStats['Team'] = pd.Categorical(
                    HomeStats['Team'], 
                    helpdf['Home Team'].to_list(), 
                    ordered=True
                    )
                HomeStats = HomeStats.sort_values('Team')
                try:
                    HomeStats['PTS/M'] = HomeStats['PTS'].div(HomeStats['M'])
                    HomeStats['DC'] = HomeStats['DC'].div(HomeStats['M'])
                    HomeStats['ODC'] = HomeStats['ODC'].div(HomeStats['M'])
                except ZeroDivisionError:
                    HomeStats['PTS/M'] = 0
                    HomeStats['DC'] = 0
                    HomeStats['ODC'] = 0
                


                AwayStats = Table.loc[Table['Team'].isin(helpdf['Away Team'].to_list())] 
                AwayStats['Team'] = pd.Categorical(
                    AwayStats['Team'], 
                    helpdf['Away Team'].to_list(), 
                    ordered=True
                    )
                AwayStats = AwayStats.sort_values('Team')
                try:
                    AwayStats['PTS/M'] = AwayStats['PTS'].div(AwayStats['M'])
                    AwayStats['DC']=AwayStats['DC'].div(AwayStats['M'])
                    AwayStats['ODC']=AwayStats['ODC'].div(AwayStats['M'])   
                except ZeroDivisionError:
                    AwayStats['PTS/M'] = 0
                    AwayStats['DC']=0
                    AwayStats['ODC']=0
                
                
                li = HomeStats.values.tolist()
                HOME.append(li)
    

                
                li = AwayStats.values.tolist()
                AWAY.append(li)
                
            for i in range(len(HOME)):
                for j in range(len(HOME[i])):
                    HOME1.append(HOME[i][j])
            
            for i in range(len(AWAY)):
                for j in range(len(AWAY[i])):
                    AWAY1.append(AWAY[i][j])
                    

        
            HOME = pd.DataFrame(HOME1, columns=['HTeam', 'HM', 'HG', 'HGA', 'HPTS', 'HxG', 'HxGA', 'HPPDA', 'HOPPDA','HDC', 'HODC', 'HPTS/M'])
            AWAY = pd.DataFrame(AWAY1, columns=['ATeam', 'AM', 'AG', 'AGA', 'APTS', 'AxG', 'AxGA', 'APPDA', 'AOPPDA','ADC', 'AODC', 'APTS/M'])
            print(HOME)
            print(AWAY)
                
            TELIKO = pd.concat([df, HOME, AWAY], axis=1)
            print(TELIKO)


            TELIKO.to_csv('PredictionMonth.csv')

                
                
                

        
loop = asyncio.get_event_loop()
loop.run_until_complete(main())


    