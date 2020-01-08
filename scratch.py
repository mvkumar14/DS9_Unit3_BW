import pandas as pd

track_list = pd.DataFrame()
df = pd.read_csv('SpotifyAudioFeaturesApril2019.csv')
track_list = track_list.append(df)

print(track_list.head())
print(df.head())
