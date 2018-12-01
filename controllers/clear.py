from app import app
from flask import render_template
from helpers import GENRES_LIST
from helpers import get_score
from helpers import clear_score
@app.route('/clear', methods=['GET'])
def clear():
    score = get_score()
    return render_template("clear.html", score=score)
