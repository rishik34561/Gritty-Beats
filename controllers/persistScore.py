from app import app
from flask import render_template
from flask_cors import CORS, cross_origin
from flask import request
from helpers import GENRES_LIST
from helpers import get_score
from helpers import clear_score
from flask import session
from firebase import firebase

@app.route('/persistScore', methods=['POST'])
@cross_origin()
def persistScore():
    db_cursor = firebase.FirebaseApplication('https://dj-183-c7447.firebaseio.com/',None)
    userData = request.get_json()
    usernameValue = userData['value']
    num_correct = userData['num_correct']
    print(usernameValue)
    print("num_correct = ", num_correct)

    score_list = db_cursor.get('/',None)
    print score_list
    if usernameValue in score_list:
        user_score = db_cursor.get('/',usernameValue)
        prev_correct = int(user_score)
        if int(num_correct) > prev_correct:
            print "new score > old score"
            db_cursor.put('/',usernameValue,int(num_correct))
    else:
        print "added new user + score to database"
        db_cursor.put('/',usernameValue,int(num_correct))
    
    return 'persisted data'