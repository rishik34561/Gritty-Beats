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
    if request.args['questions'] == correct_song:
        correct = True
