import pandas as pd


df = pd.read_csv('poker_points.csv')

df = df.fillna(0)
df = df.set_index('Player')
players_to_drop = ['Big G','Xiaoqian','Kurtis']
df.drop(players_to_drop, inplace=True)

dates = df.columns.tolist()[::-1]
players = df.index.tolist()
players.sort()

start_point = 5_000
start_date = '2021-08-16'

rnk_df = pd.DataFrame({
    'id': [],
    'date': [],
    'value': []
})

for p in players:
    points = start_point
    dt = start_date
    rnk_df.loc[len(rnk_df)] = [p, dt, points]
    for dt in dates:
        new_point = df.loc[p, dt]
        points += new_point
        rnk_df.loc[len(rnk_df)] = [p, dt, points]

rnk_df.to_csv('rank.csv', index=False)
