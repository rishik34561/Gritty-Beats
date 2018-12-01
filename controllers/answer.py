from app import app
from flask import request
from flask import render_template
from flask import session
from helpers import GENRES_LIST
from helpers import get_score
from helpers import get_four_songs
from utility import get_preview_url
from question import *

@app.route('/answer', methods=['GET'])
def answer():
    #get user input from choice
    player_answer = request.args["choice"]
    correct_choice = request.args["correct_choice"]
    genre_correct = request.args["correct_genre"]

    #compare correct answer with player answer
    #if player answer is correct, add to num_correct
    if player_answer == correct_choice:
        player_is_correct = True
        session['num_correct'] += 1
    else:
        player_is_correct = False
    #regardless of correct or not, add one to total
    session['num_total'] += 1

    data = {
        "our_song" : correct_choice,
        "song" : player_answer,
        "choice" : correct_choice,
        "is_correct" : player_is_correct,
        "num_total" : session['num_total'],
        "num_correct" : session['num_correct'],
        "genre_correct" : genre_correct
    }
    score = get_score()
    return render_template("answer.html",score=score,**data)