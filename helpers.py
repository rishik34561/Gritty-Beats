from flask import session
import billboard, random, requests
from utility import get_four_choices

"""
Modify this variable to change what chart you are pulling from. Be careful that
you know how many songs are going to be pulled depending on this chart you
choose.
"""
GENRES_LIST = {
    "Current Pop Hits": "hot-100",
    "Dance Club Hits": "dance-club-play-songs",
    "Country Classics": "greatest-country-songs"
}

"""
REQUIRES: nothing
MODIFIES: nothing
EFFECTS: returns a string with the score to prin
"""
def get_score():
    pass

"""
REQUIRES: nothing
MODIFIES: num_correct, num_total in session
EFFECTS: sets the num_correct and num_total to 0
"""
def clear_score():
    pass

"""
REQUIRES: a valid chart name that corresponds to a chart name on Billboard
MODIFIES: nothing
EFFECTS: chooses four random songs from the valid Billboard chart and returns
         result in a list.
         Uses: get_four_choices()
"""
def get_four_songs(chart_name):
    pass

