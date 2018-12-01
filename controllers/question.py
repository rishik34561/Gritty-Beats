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

    #initialize url to error
    urlin = {"error": "Song not found"}
    
    #keep getting new url until no error
    while "error" in urlin:
        songs_chosen = get_four_songs(chart_name)
        index = random.randint(0,3)
        correct_song = songs_chosen[index]
        urlin = get_preview_url(correct_song.title, correct_song.artist)
    song_url = urlin["url"]



    data = {
        "song_answers": songs_chosen,
        "chartname": chart_name,
        "charttitle": chart_title,
        "songurl_correct": song_url,
        "correct_song": correct_song,
    }
    score = get_score()
    return render_template("question.html", score = score, **data)