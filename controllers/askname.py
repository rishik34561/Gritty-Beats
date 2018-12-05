from app import app
from flask import render_template
from flask import request
from helpers import GENRES_LIST
from helpers import get_score
from helpers import clear_score
from flask import session

@app.route('/askname', methods=['GET'])
def askname():
    score = get_score()
    return render_template("askname.html",score=score)