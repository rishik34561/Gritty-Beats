# You might need to add more of these import statements as you implement your controllers.
from app import app
from flask import render_template
from helpers import GENRES_LIST

@app.route('/')
def index():

    data = {
        "genres": GENRES_LIST,
    }

    return render_template("index.html", **data)
