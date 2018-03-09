from app import app
from flask import render_template, session
from helpers import GENRES_LIST, get_score, clear_score

@app.route('/')
def index():

    data = {
        "genres": GENRES_LIST,
    }

    return render_template("index.html", **data)
