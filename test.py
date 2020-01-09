from flask import Flask, request, render_template, jsonify
# import pandas as pd
from flask_sqlalchemy import SQLAlchemy
import sqlite3
import pickle

app = Flask(__name__)



@app.route('/')
def home():
    return render_template('home.html')


@app.route('/song/<song_id>', methods = ['GET', 'POST'])
def song(song_id):
    """Route for recommendations based on song selected."""

    #song_id = request.json['key']
    song_id=str(song_id)
    print(song_id)

    # connecting to local database to retreive values
    conn = sqlite3.connect('songs_df.sqlite3')
    curs = conn.cursor()
    song_row = curs.execute(f"SELECT * FROM songs WHERE track_id = '{song_id}'").fetchall()
    print(song_row[0][1])

    #model
    # with open('model.pkl','rb') as mod:
    #     model = pickle.load(mod)

    #output
    # reccomendations = model.predict(song_id)
    # print(reccomendations)

    # The implimentation of the model might be a jsonify_function
    # the model output would then be jsonified in a format
    # that front end would need.
    # jsonify_function(function(song_id))

    #The above is what you would return
    return  str(song_row) #jsonify(reccomendations)

@app.route('/favorites',methods = ['POST'])
def favorites():
    my_dict = request.get_json(force=True)
    track_list = []
    for i in favorites.values():
        query = f"SELECT * FROM songs WHERE track_id = '{i}'"
        song_row = curs.execute(query).fetchall()
        song_rows.append(song_row[0])






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
