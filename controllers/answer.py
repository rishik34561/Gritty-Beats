from app import app
from flask import request
from flask import render_template
from helpers import GENRES_LIST
from helpers import get_score
from helpers import get_four_songs
from utility import get_preview_url
from question import get_correct_song
from helpers import get_num_correct
from helpers import set_num_correct
from helpers import get_num_total
from helpers import set_num_total
from question import get_song_list
from question import *

@app.route('/answer', methods=['POST'])
def answer():
    num_correct = get_num_correct()
    correct_song = get_correct_song()
    song_list = get_song_list()
    y = request.form.get('questions')
    y = song_list[y]
    if y == correct_song:
        correct = "Correct!"
        set_num_correct(num_correct + 1)
    else:
        correct = "Incorrect!"
    num_total = get_num_total()
    set_num_total(num_total + 1)

    data = {'correct': correct,
            'correct_song': correct_song
    }
    return render_template("answer.html",**data)

