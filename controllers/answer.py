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
    if correct_song == ##choice:
        correct = True
        num_correct += 1
    else:
        correct = False
    num_total += 1

