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

# DB = SQLAlchemy()
#
# df = pd.read_csv('SpotifyAudioFeaturesApril2019.csv')
#
# conn = sqlite3.connect('songs_df.sqlite3')
#
# df.to_sql('songs', conn, if_exists='replace')

# class Song(DB.Model):
#     """ Model for song entry in database """
#     id = DB.Column(DB.STring(30))

# app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///songs_df.sqlite3'
#


@app.route('/')
def home():
    return render_template('home.html')


@app.route('/song/<song_id>', methods = ['GET'])
def song(song_id):
    """Route for recommendations based on song selected."""

    # song_id = request.json['key']
    song_id=str(song_id)
    print(song_id)

    # connecting to local database to retreive values
    # conn = sqlite3.connect('songs_df.sqlite3')
    # curs = conn.cursor()
    # song_row = curs.execute(f"SELECT * FROM songs WHERE track_id = '{song_id}'").fetchall()
    # print(song_row[0][1])

    #model
    # with open('model.pkl','rb') as mod:
    #     model = pickle.load(mod)

    #output
    reccomendations = process_input(song_id)
    print(type(process_input(song_id)))
    # print(reccomendations)

    # The implimentation of the model might be a jsonify_function
    # the model output would then be jsonified in a format
    # that front end would need.
    # jsonify_function(function(song_id))

    #The above is what you would return

    # print(type(reccomendations))
    # print('\n')
    # print(reccomendations[0])
    # print('\n')
    # print(type(reccomendations[0]))
    # print('\n')
    # print(reccomendations)
    # print('\n')
    return  process_input(song_id) #jsonify(reccomendations)

@app.route('/favorites',methods = ['GET'])
def favorites():
    my_dict = request.get_json(force=True)
    track_list = pd.DataFrame()
    for i in my_dict.values():
        track_list = track_list.append(process_input(i,False))
    track_list.drop_duplicates()
    return track_list.sample(30).to_json(orient="records")










#
# @app.route('/song/<track_id>', methods = ['GET','POST'])
# def song(track_id):
#     """Route for recommendations based on song selected."""
#     print(type(track_id))
#
#     if request.method == 'POST':
#         test = request.get_json(force=True)
#         print(test)
#     return render_template('echo.html',echo=track_id)
#
#     #input
#     # curs.execute()
#
#     #get parameters:
#     # use song_id
#     # songs_df = SELECT * from songs WHERE df_id == song_id
#     # danceability = songs_df['danceability']
#     # energy = songs_df['energy']
#
#
#     #model
#     # model = "some pickled model"
#
#     #output
#     #should be 30 reccomendations
#     # recommendations = model.predict("parameters")


@app.route('/post_get_json_test',methods=['POST','GET'])
def post_with_get_json():
    """ Method to test the POST method/ retreiving data with the
    request.get_json method """
    a = request.get_json(force=True)
    print(a['track_id'])
    if request.method == 'GET':
        return a
    # render the template when testing locally, but just return
    # the actual values when you deploy the application.
    return a #render_template('echo.html',echo=a)

@app.route('/post_query',methods =['GET'])
def post_query():
    """ Method to test the GET method with the query in url instead of
    with the get_json from the message body"""
    a = request.args['track_id']
    print(a)

    return render_template('echo.html',echo=a)


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
