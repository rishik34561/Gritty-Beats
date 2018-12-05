from app import app
from flask import render_template
from flask import request
from helpers import GENRES_LIST
from helpers import get_score
from helpers import clear_score
from flask import session
from firebase import firebase

@app.route('/recordscore', methods=['GET'])
def recordscore():
    db_cursor = firebase.FirebaseApplication('https://dj-183-c7447.firebaseio.com/',None)
    username = request.args['username']
    score_list = db_cursor.get('/',None)
    print score_list
    score = get_score()
    score.replace(" ", "")
    index = score.find('/')
    num_correct = float(score[0:index])
    print "num_correct = ", num_correct
    num_total = float(score[index+1:])
    if username in score_list:
        user_score = db_cursor.get('/',username)
        prev_correct = float(user_score)
        if num_correct > prev_correct:
            print "new score > old score"
            db_cursor.put('/',username,num_correct)
    else:
        print "added new user + score to database"
        db_cursor.put('/',username,num_correct)
    clear_score()

    return render_template("recordscore.html")