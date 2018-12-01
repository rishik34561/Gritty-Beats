from app import app
from flask import render_template
from helpers import GENRES_LIST
from helpers import get_score
from flask import session

@app.route('/', methods=['GET'])
def index():
    #create new session for each
    if 'num_correct' not in session:
        session['num_correct'] = 0

    if 'num_total' not in session:
        session['num_total'] = 0

    data = {
        "genres": GENRES_LIST,
    }
    score= get_score()
    return render_template("index.html", score=score, **data)