# Add more import statements as you need them!
from utility import get_four_choices
from flask import session
import billboard
import json

"""
Our dictionary to hold which genres we are giving to our users. Play around with
this dictionary to see how the starter code changes on index.html. The keys
represent the names as they appear on the website, and the values represent the
chart IDs for Billboard to use.

TODO: Add at least two more genres to this dictionary. Information on how to find
      more Billboard chart IDs is on the Billboard library documentation, as
      linked on the core page of the spec. Make sure you only choose charts that
      contain SONGS (not artists, albums, etc.).
"""
GENRES_LIST = {
    "Current Pop Hits": "hot-100",
    "Dance Club Hits": "dance-club-play-songs",
    "Country Classics": "greatest-country-songs",
    "Greatest of All Time Hot 100 Singles": "greatest-hot-100-singles",
    "Hot R and B/Hip Hop Songs": "r-b-hip-hop-songs"
}

GENRES_NAMES = ["Current Pop Hits", 
"Dance Club Hits", 
"Country Classics", 
"Greatest of All Time Hot 100 Singles", 
"Hot R and B/Hip Hop Songs"]


"""
REQUIRES: a valid chart name that corresponds to a chart name on Billboard
MODIFIES: nothing
EFFECTS: chooses four random songs from the valid Billboard chart and returns
         result in a list. Uses get_four_choices() and the Billboard library.
         Remember: if you want to use a library in Python, what must we put at
         the top of the file to access its member functions?
"""
def get_four_songs(chart_name):
    chart = billboard.ChartData(chart_name)
    choices = get_four_choices(chart)
    #get four songs from return value of four choices
    songs_list = [chart[choices[0]],chart[choices[1]],chart[choices[2]],chart[choices[3]]]
    #for song in songs_list:
       # print(song)
    return songs_list

"""
REQUIRES: nothing
MODIFIES: nothing
EFFECTS: returns a string with the score to print
"""



def get_score():
    #to avoid divide by zero error
    if session['num_total'] == 0:
        return "N/A"
    score = str(session['num_correct'])
    score += " / "
    score += str(session['num_total'])
    return score

"""
REQUIRES: nothing
MODIFIES: num_correct, num_total in session
EFFECTS: sets the num_correct and num_total to 0
"""
def clear_score():
    session['num_correct'] = 0
    session['num_total'] = 0
    

