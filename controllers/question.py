from app import app
from flask import render_template
from helpers import GENRES_LIST
from helpers import get_score

@app.route('/question')
def question():
    return render_template("question.html")