from app import app
from flask import request
from flask import render_template
from helpers import GENRES_LIST
from helpers import get_score
from helpers import get_four_songs
from utility import get_preview_url
import random
import billboard

correct_song = 0
song_list = [None]
@app.route('/question', methods=['GET'])
def question():
    chart_title = request.args['genres']
    chart_name = GENRES_LIST[chart_title]
    song_list = get_four_songs(chart_name)
    correct_song = random.choice(song_list)

    while not get_preview_url(correct_song.title, correct_song.artist):
        song_list = get_four_songs(chart_name)
        correct_song = random.choice(song_list)

    song = get_preview_url(correct_song.title, correct_song.artist)
    song_url = song["url"]

    data = {
        "questions": song_list,
        "preview": song_url,
        "genres": GENRES_LIST,
        "correct_song": correct_song,
        "chart_title": chart_title,
        "chart": chart_name
    }
    
    return render_template("question.html", **data)

def get_correct_song():
    return correct_song

def get_song_list():
    return song_list