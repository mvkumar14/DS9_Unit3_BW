from flask import Flask, request, render_template
import pandas as pd
from flask_sqlalchemy import SQLAlchemy
import sqlite3

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

@app.route('/song/<track_id>', methods = ['GET'])
def song(track_id):
    """Route for recommendations based on song selected."""
    print(type(track_id))
    #input
    # curs.execute()

    #get parameters:
    # use song_id
    # songs_df = SELECT * from songs WHERE df_id == song_id
    # danceability = songs_df['danceability']
    # energy = songs_df['energy']


    #model
    # model = "some pickled model"

    #output
    #should be 30 reccomendations
    # recommendations = model.predict("parameters")
    if request.method == 'POST':
        test = request.get_json(force=True)
        print(test)
    return render_template('echo.html',echo=track_id)

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
