# writing logic for fetching

import numpy as np
import pandas as pd
import json
matches=pd.read_csv("./Dataset/IPL_Matches_2008_2022.csv")


def teamsApi():
    teams=list(set(list(matches['Team1'])+list(matches['Team2'])))
    teams_dict={
        'teams':teams
    }
    return teams_dict

def teamVteamApi(team1,team2):
    temp_df=matches[(matches['Team1']==team1) & (matches['Team2']==team2)|(matches['Team1']==team2) & (matches['Team2']==team1)]
    total_matches=temp_df.shape[0]
    matches_won_team1=temp_df['WinningTeam'].value_counts()[team1]
    matches_won_team2=temp_df['WinningTeam'].value_counts()[team2]
    draws=total_matches-(matches_won_team1+matches_won_team2)

    response={
        team1:str(matches_won_team1),
        team2:str(matches_won_team2),
        'total_matches':str(total_matches),
        'draws':str(draws)
    }
    return response
