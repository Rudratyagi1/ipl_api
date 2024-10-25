import pandas as pd
import numpy as np
import json

class NpEncoder(json.JSONEncoder):
    def default(self, obj):
        if isinstance(obj, (np.integer, np.int64)):
            return int(obj)
        elif isinstance(obj, (np.floating, np.float64)):
            return float(obj)
        elif isinstance(obj, np.ndarray):
            return obj.tolist()
        return super().default(obj)

ipl_matches = "https://docs.google.com/spreadsheets/d/e/2PACX-1vRy2DUdUbaKx_Co9F0FSnIlyS-8kp4aKv_I0-qzNeghiZHAI_hw94gKG22XTxNJHMFnFVKsO4xWOdIs/pub?gid=1655759976&single=true&output=csv"
ipl_ball = "https://docs.google.com/spreadsheets/d/e/2PACX-1vRu6cb6Pj8C9elJc5ubswjVTObommsITlNsFy5X0EiBY7S-lsHEUqx3g_M16r50Ytjc0XQCdGDyzE_Y/pub?output=csv"

matches = pd.read_csv(ipl_matches)
balls = pd.read_csv(ipl_ball)

# Merging match and ball data for complex calculations
ball_withmatch = balls.merge(matches, on='ID', how='inner')
ball_withmatch['BowlingTeam'] = ball_withmatch['Team1'] + ball_withmatch['Team2']
ball_withmatch['BowlingTeam'] = ball_withmatch[['BowlingTeam', 'BattingTeam']].apply(lambda x: x[0].replace(x[1], ''), axis=1)

def team1vsteam2(team1, team2):
    df = matches[((matches['Team1'] == team1) & (matches['Team2'] == team2)) |
                 ((matches['Team1'] == team2) & (matches['Team2'] == team1))]
    return {'matchesplayed': df.shape[0], 'won': df[df.WinningTeam == team1].shape[0],
            'loss': df[df.WinningTeam == team2].shape[0], 'noResult': df['WinningTeam'].isnull().sum()}

def allRecord(team):
    df = matches[(matches['Team1'] == team) | (matches['Team2'] == team)]
    return {'matchesplayed': df.shape[0], 'won': df[df.WinningTeam == team].shape[0],
            'loss': df[df.WinningTeam != team].shape[0], 'noResult': df['WinningTeam'].isnull().sum()}

def teamAPI(team):
    TEAMS = matches.Team1.unique()
    against_records = {opponent: team1vsteam2(team, opponent) for opponent in TEAMS}
    return json.dumps({team: {'overall': allRecord(team), 'against': against_records}}, cls=NpEncoder)

# Define batsman/bowler functions as in your original but with optimizat
