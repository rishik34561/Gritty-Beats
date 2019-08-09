from app import app
from flask import render_template
from flask_cors import CORS, cross_origin
from flask import request, jsonify
from helpers import GENRES_LIST
from helpers import get_score
from helpers import clear_score
from flask import session
from firebase import firebase
import operator
from collections import OrderedDict
from itertools import islice

@app.route('/getLeaderboard', methods=['GET'])
@cross_origin()
def getLeaderboard():
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
    return jsonify(score_list)

def take(n, iterable):
    "Return first n items of the iterable as a list"
    return list(islice(iterable, n))

def Convert(tup, di): 
    di = dict(tup) 
    return di