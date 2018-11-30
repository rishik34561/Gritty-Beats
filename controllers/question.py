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
    trial = request.args['genres']
    trial = GENRES_LIST[trial]
    song_list = get_four_songs(trial)
    song_choice = random.choice(song_list)
    i = 0
    while get_preview_url(song_choice.title, song_list[i].artist):
        song_list = get_four_songs(trial)
        song_choice = random.choice(song_list)

    song = get_preview_url(song_choice.title, song_choice.artist)
    song_url = song["url"]

    data = {
        "questions": song_list,
        "preview": song_url,
        "genres": GENRES_LIST
    }
    
    return render_template("question.html", **data)