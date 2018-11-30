from app import app
from flask import render_template
from helpers import GENRES_LIST
from helpers import get_score
from helpers import clear_score
@app.route('/clear')
def question():
    return render_template("clear.html")