from app import app
from flask import render_template
from flask import request
from helpers import GENRES_LIST
from helpers import get_score
from helpers import clear_score
from flask import session
from firebase import firebase
import operator
from collections import OrderedDict
from itertools import islice

@app.route('/', methods=['GET'])
def index():
    #create new session for each
    if 'num_correct' not in session:
        session['num_correct'] = 0

    if 'num_total' not in session:
        session['num_total'] = 0

    db_cursor = firebase.FirebaseApplication('https://dj-183-c7447.firebaseio.com/',None)
    score_list = db_cursor.get('/',None)
    if len(score_list) >= 5:
        score_list = OrderedDict(sorted(score_list.items(), key=operator.itemgetter(1), reverse=True))
        n_items = take(5, score_list.iteritems())
        print n_items
        score_list = {}
        score_list = Convert(n_items,score_list)
    else:
        score_list = OrderedDict(sorted(score_list.items(), key=operator.itemgetter(1), reverse=True))
    score_list = OrderedDict(sorted(score_list.items(), key=operator.itemgetter(1), reverse=True))
    data = {
        "genres": GENRES_LIST,
        "score_list": score_list
    }

    score = get_score()

    return render_template("index.html", score=score, **data)

def take(n, iterable):
    "Return first n items of the iterable as a list"
    return list(islice(iterable, n))

def Convert(tup, di): 
    di = dict(tup) 
    return di