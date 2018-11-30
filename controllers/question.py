from app import app
from flask import request
from flask import render_template
from helpers import GENRES_LIST
from helpers import get_score
from helpers import get_four_songs
from utility import get_preview_url
import random

@app.route('/question', methods=['GET'])
def question():
    x = request.args['genres']
    x = GENRES_LIST[x]
    song_list = get_four_songs(x)
    song_choice = random.choice(song_list)

    while not get_preview_url(song_choice.title, song_choice.artist):
        song_list = get_four_songs(x)
        song_choice = random.choice(song_list)

    song = get_preview_url(song_choice.title, song_choice.artist)
    song_url = song["url"]

    data = {
        "questions": song_list,
        "preview": song_url,
        "genres": GENRES_LIST
    }

    return render_template("question.html", **data)
