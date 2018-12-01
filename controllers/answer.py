from app import app
from flask import request
from flask import render_template
from flask import session
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

@app.route('/answer', methods=['GET'])
def answer():
    user_answer = request.args["choice"]
    correct_song = request.args['correct_song']

    if user_answer == correct_song:
        correct = "Correct!"
        session['num_correct'] += 1
    else:
        correct = "Incorrect!"
    session['num_total'] += 1

    data = {'correct': correct,
            'correct_song': correct_song
            session['num_correct']: num_correct
            session['num_total']: num_total
    }
    return render_template("answer.html",**data)
