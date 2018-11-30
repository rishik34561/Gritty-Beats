from app import app
from flask import request
from flask import render_template
from helpers import GENRES_LIST
from helpers import get_score
from helpers import get_four_songs
from utility import get_preview_url
from question import correct_song


@app.route('/answer', methods=['POST'])
def answer():
<<<<<<< HEAD
    if request.args['questions'] == correct_song:
=======
    if correct_song == ##choice:
>>>>>>> f81253c434feffc0eccd449682b4d611e4df59ba
        correct = True
        num_correct += 1
    else:
        correct = False
    num_total += 1

