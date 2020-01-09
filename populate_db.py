import pandas as pd
import sqlite3

df = pd.read_csv('SpotifyAudioFeaturesApril2019.csv')
conn = sqlite3.connect('songs_df.sqlite3')
df.to_sql('songs', conn, if_exists='replace')




# If we want to use SQL Alchemy instead here is some starter code:

# DB = SQLAlchemy()
# class Song(DB.Model):
#     """ Model for song entry in database """
#     id = DB.Column(DB.STring(30))
#
# app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///songs_df.sqlite3'
