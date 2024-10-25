import pandas as pd
import numpy as np

ipl_matches = "https://docs.google.com/spreadsheets/d/e/2PACX-1vRy2DUdUbaKx_Co9F0FSnIlyS-8kp4aKv_I0-qzNeghiZHAI_hw94gKG22XTxNJHMFnFVKsO4xWOdIs/pub?gid=1655759976&single=true&output=csv"
matches = pd.read_csv(ipl_matches)

def teamsAPI():
    teams = sorted(list(set(matches['Team1']).union(set(matches['Team2']))))
    return {'teams': teams}

def teamVteamAPI(team1, team2):
    valid_teams = teamsAPI()['teams']
    if team1 not in valid_teams or team2 not in valid_teams:
        return {'message': 'Invalid team name'}

    temp_df = matches[((matches['Team1'] == team1) & (matches['Team2'] == team2)) |
                      ((matches['Team1'] == team2) & (matches['Team2'] == team1))]
    total_matches = temp_df.shape[0]
    matches_won_team1 = temp_df['WinningTeam'].value_counts().get(team1, 0)
    matches_won_team2 = temp_df['WinningTeam'].value_counts().get(team2, 0)
    draws = total_matches - (matches_won_team1 + matches_won_team2)

    response = {
        'total_matches': total_matches,
        team1: matches_won_team1,
        team2: matches_won_team2,
        'draws': draws
    }
    return response
