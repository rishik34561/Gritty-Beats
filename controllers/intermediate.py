from app import app
from flask import render_template
from helpers import GENRES_LIST
from flask import request
from helpers import get_score
from helpers import clear_score
from urlparse import urlparse

@app.route('/intermediate', methods=['GET'])
def intermediate():
    url = request.url
    o = urlparse(url)
    print str(o)
    print str(o.query)
    query = str(o.query)
    print "hello"
    if query == "choice=Yes&Submit=Submit":
        clear_score()
    score_clear = request.args['choice']
    if score_clear == 'Yes':
        clear_score()
    return render_template("intermediate.html")