from app import app
from flask import render_template
from helpers import GENRES_LIST
from helpers import get_score
from helpers import get_four_songs

@app.route('/answercorrect')
def answercorrect():
    num_correct += 1
    num_total += 1
    return render_template("answercorrect.html"_)
