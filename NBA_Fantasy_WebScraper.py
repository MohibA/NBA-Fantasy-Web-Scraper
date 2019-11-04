import requests
from bs4 import BeautifulSoup
import pandas as pd
import re


url = 'https://www.fantasypros.com/nba/stats/overall.php'
data = requests.get(url)

#convert to beautiful soup object
soup = BeautifulSoup(data.text, 'html.parser')


stat_table = soup.find('table',{'id': 'data'})
thead = stat_table.find('thead')
tbody = stat_table.find('tbody')


# this is a loop that allows us to check headings 
for tr in thead.find_all('tr'):
    title = tr.find_all('th')[1].text.strip()


players = []
total_points = []
rebounds = []
assists = []
blocks = []
steals = []
fg_pct = []
ft_pct = []
threes_pm = []
turnovers = []
gamesplayed = []
minutes_played = []
ftm = []
twos_pm = []


# inspect page and retrive all stats and append to our lists to store all stats of player
for tr in tbody.find_all('tr'):
    
    player = tr.find_all('td')[0].text.strip()
    player_total_points = tr.find_all('td')[1].text.strip()
    player_rebounds = tr.find_all('td')[2].text.strip()
    player_assists = tr.find_all('td')[3].text.strip()
    player_blocks = tr.find_all('td')[4].text.strip()
    player_steals = tr.find_all('td')[5].text.strip()
    player_fgPct = tr.find_all('td')[6].text.strip()
    player_ftPct = tr.find_all('td')[7].text.strip()
    player_threes_pm = tr.find_all('td')[8].text.strip()
    player_TO = tr.find_all('td')[9].text.strip()
    player_gp = tr.find_all('td')[10].text.strip()
    player_minPlayed = tr.find_all('td')[11].text.strip()
    player_ftm = tr.find_all('td')[12].text.strip()
    player_twos_pm = tr.find_all('td')[13].text.strip()
    
    players.append(player)
    total_points.append(player_total_points)
    rebounds.append(player_rebounds)
    assists.append(player_assists)
    blocks.append(player_blocks)
    steals.append(player_steals)
    fg_pct.append(player_fgPct)
    ft_pct.append(player_ftPct)
    threes_pm.append(player_threes_pm)
    turnovers.append(player_TO)
    gamesplayed.append(player_gp)
    minutes_played.append(player_minPlayed)
    ftm.append(player_ftm)
    twos_pm.append(player_twos_pm)
    

data_table = {'Name':players,
              'Points':total_points,
              'REB': rebounds,
              'AST': assists,
              'BLK':blocks,
              'STL':steals,
              'FG%':fg_pct,
              'FT%':ft_pct,
              '3PM':threes_pm,
              'TO':turnovers,
              'GP':gamesplayed,
              'MIN': minutes_played,
              'FTM': ftm,
              '2PM': twos_pm}

#Convert data into a pandas dataFrame
df = pd.DataFrame(data_table)


#function to get a players stats using their name, team and position
def get_stats_ByName(data_set, name):
    if name in players:
        player_stats = df.loc[df.Name == name]
    return player_stats

print(get_stats_ByName(df,'James Harden (HOU - PG,SG)'))
    
                
    
        




    
    
