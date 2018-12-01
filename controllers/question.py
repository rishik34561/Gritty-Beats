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
@app.route('/question', methods=['GET','POST'])
def question():
    chart_title = request.args["chart_name"]
    chart_name = GENRES_LIST[chart_title]

    url_info = {"error": "Song not found"}
    
    while "error" in url_info:
        songs_chosen = get_four_songs(chart_name)
        index = random.randint(0,3)
        correct_song = songs_chosen[index]
        url_info =get_preview_url(correct_song.title, correct_song.artist)

    
    song_url = url_info["url"]

    score = get_score()

    data = {
        "song_answers": songs_chosen,
        "song_url_right": song_url,
        "correct_song": correct_song,
        "chart_title": chart_title,
        "chart": chart_name
    }
    
    return render_template("question.html", score = score, **data)
