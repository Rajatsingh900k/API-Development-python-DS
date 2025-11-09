# writing logic for fetching

import numpy as np
import pandas as pd

matches=pd.read_csv("./Dataset/IPL_Matches_2008_2022.csv")


def teamsApi():
    teams=list(set(list(matches['Team1'])+list(matches['Team2'])))
    teams_dict={
        'teams':teams
    }
    return teams_dict