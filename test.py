from flask import Flask, request
import pandas as pd
from flask_sqlalchemy import SQLAlchemy
import sqlite3

app = Flask(__name__)

DB = SQLAlchemy()

df = pd.read_csv('SpotifyAudioFeaturesApril2019.csv')

conn = sqlite3.connect('songs_df.sqlite3')

df.to_sql('songs', conn, if_exists='replace')

# class Song(DB.Model):
#     """ Model for song entry in database """
#     id = DB.Column(DB.STring(30))

# app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///songs_df.sqlite3'
#
# @app.route('/song', methods = ['POST'])
# def song():
#     """Route for recommendations based on song selected."""
#
#     #input
#     song_id = request.get_json(force=True)
#
#     #get parameters:
#     # use song_id
#     # songs_df = SELECT * from songs WHERE df_id == song_id
#     danceability = songs_df['danceability']
#     energy = songs_df['energy']
#
#
#     #model
#     model = "some pickled model"
#
#     #output
#     #should be 30 reccomendations
#     recommendations = model.predict("parameters")
#
#     return recommendations
#
#
# @app.route('/mood')
# def mood():
#     """Route foor recommendations based on mood selected."""
#
#     mood = request.get_json(force=True)
#
#     recommendations =
#
#
# if __name__ == "__main__":
#     app.run()
