import numpy as np
import math
import asyncio
import aiohttp
import pandas as pd
from datetime import date, timedelta
from dateutil.relativedelta import relativedelta
import datetime
from understat import Understat


async def main():
        async with aiohttp.ClientSession(cookies={'beget':'begetok'}) as session:
            understat = Understat(session)
            df = pd.read_csv('GatheredData/ExFiles/E0-2023.csv')
            df = df.dropna(subset=['FTHG'])
            df['Result'] = np.nan
            for i, x in enumerate(df['Result']):
                df['Result'][i] = '[\'' + str(df['FTHG'][i]) + ' \', \' ' + str(df['FTAG'][i]) + '\']'
                
            df = df[['Date', 'HomeTeam', 'AwayTeam', 'Result', 'B365H', 'B365D', 'B365A', 'B365>2.5', 'B365<2.5']]
            df = df.rename(columns={'B365>2.5': 'BbAv>2.5', 'B365<2.5': 'BbAv<2.5'})
            df['Date'] = pd.to_datetime(df['Date'], format='%d/%m/%Y')
            df['Date'] = df['Date'].dt.strftime('%d/%m/%Y')


            UniqDates = df["Date"].unique()

            HOME = []
            AWAY = []
            HOME1 = []
            AWAY1 = []

            for i, x in enumerate(UniqDates):
                #TEAMSTATS
                #format dates for understat fixtures and go to the previous day of the match
                print(x)
                helpdf = df.loc[df['Date'] == str(UniqDates[i])]
                UniqDates[i] = datetime.datetime.strptime(UniqDates[i], '%d/%m/%Y').date()
                UniqDates[i] = UniqDates[i] - datetime.timedelta(days=1)
                start = str(UniqDates[i] - relativedelta(months=3))
                print(UniqDates[i])
                
                UniqDates[i] = str(UniqDates[i])
                print(UniqDates[i])
                
                table = await understat.get_league_table("EPL", "2023", end_date=UniqDates[i], start_date=start)
                Table = pd.DataFrame(table)
                Table.columns = Table.iloc[0]
                Table = Table.iloc[1: , :]
                Table = Table[['Team', 'M', 'G', 'GA', 'PTS', 'xG', 'xGA', 'PPDA', 'OPPDA', 'DC', 'ODC']]
        
                print(helpdf['HomeTeam'])
                print(helpdf['AwayTeam'])

                HomeStats = Table.loc[Table['Team'].isin(helpdf['HomeTeam'].to_list())]
                HomeStats['Team'] = pd.Categorical(
                    HomeStats['Team'], 
                    helpdf['HomeTeam'].to_list(), 
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
                


                AwayStats = Table.loc[Table['Team'].isin(helpdf['AwayTeam'].to_list())] 
                AwayStats['Team'] = pd.Categorical(
                    AwayStats['Team'], 
                    helpdf['AwayTeam'].to_list(), 
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
                
                print(HomeStats)
                print(AwayStats)
                
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


            TELIKO.to_csv('~/Documents/EnglishPremierLeaguePredictor/GatheredData/Epl20xx_3Months/Epl2023_3Months.csv')

                
                
                

        
loop = asyncio.get_event_loop()
loop.run_until_complete(main())