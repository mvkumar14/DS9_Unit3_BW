from flask import Flask, request

app = Flask(__name__)

@app.route('/song', methods = ['POST'])
def song():
    """Route for recommendations based on song selected."""

    #input
    song = request.get_json(force=True)

    #model
    model = "some pickled model"

    #parameters
    danceability = song['danceability']
    energy = song['energy']

    #output
    recommendations = model.predict("parameters")

    return


@app.route('/mood')
def mood():
    """Route foor recommendations based on mood selected."""

    mood = request.get_json(force=True)

    recommendations =


if __name__ == "__main__":
    app.run()
