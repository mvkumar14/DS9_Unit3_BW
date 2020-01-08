from flask import Flask, request, render_template, jsonify
from flask_sqlalchemy import SQLAlchemy
from sklearn.neighbors import NearestNeighbors
from random import sample
import pandas as pd
import numpy as np
import json
import pickle
import sqlite3

df = pd.read_csv("https://raw.githubusercontent.com/Build-Week-Spotify-Song-Suggester-1/Data-science/master/MusicWithGenresFiltered.csv")
def process_input(song_id,return_json = True):
    c = ["duration_ms", "index", "genre", "artist_name", "track_id", "track_name", "key", "mode"] # Columns to Omit
    song = df[df["track_id"] == song_id].iloc[0] # Get Song
    df_selected = df.copy()
    if not pd.isnull(song["genre"]): # If genre, set subset to only genre
        df_selected = df[df["genre"] == song["genre"]]
    nn = NearestNeighbors(n_neighbors=31, algorithm="kd_tree") # Nearest Neighbor Model
    nn.fit(df_selected.drop(columns=c))
    song = song.drop(index=c)
    song = np.array(song).reshape(1, -1)
    if return_json is False:
        return df_selected.iloc[nn.kneighbors(song)[1][0][1:]]
    return df_selected.iloc[nn.kneighbors(song)[1][0][1:]].to_json(orient="records") # Return results

app = Flask(__name__)

@app.route('/')
def home():
    return render_template('home.html')


@app.route('/song/<song_id>', methods = ['GET'])
def song(song_id):
    """Route for recommendations based on song selected."""
    return  process_input(song_id) #jsonify(reccomendations)

@app.route('/favorites',methods = ['GET'])
def favorites():
    my_dict = request.get_json(force=True)
    track_list = pd.DataFrame()
    for i in my_dict.values():
        track_list = track_list.append(process_input(i,False))
    track_list.drop_duplicates()
    return track_list.sample(30).to_json(orient="records")
