"""
utility.py contains functions that are already implemented for you. To use them,
make sure to add the appropriate import statement to the top of the other file.

For example, if "get_four_choices" is needed, we would add the following statement
to the top of our Python file:

from utility import get_four_choices
"""

from flask import session
import random, requests

"""
REQUIRES: a valid iterable object (such as a list)
MODIFIES: nothing
EFFECTS: returns four unique objects from the list. For example, if we give it
         the list:

        [
            "Brady",
            "Gaurav",
            "Dania",
            "Divya",
            "Hiromichi",
            "Jordan",
            "Kirtana",
            "Michelle",
            "Tan"
        ]

        ...this function might return:

        ["Brady", "Dania", "Kirtana", "Michelle"]
        ["Gaurav", "Hiromichi", "Jordan", "Kirtana"]

        ...so on and so forth.
"""
def get_four_choices(data):
    return random.sample(range(0,len(data)), 4)

"""
REQUIRES: a valid title and artist
MODIFIES: nothing
EFFECTS: concatenates the title and artist together, calls the iTunes search API,
         and returns a dictionary with the results.
         - if something is found, returns a dictionary containing the title,
           artist, and preview_url
         - otherwise, returns the key "error"
"""
def get_preview_url(title, artist):
    name = "+".join("{} {}".format(title, artist).split())
    r = requests.get("https://itunes.apple.com/search?term={}&entity=song&limit=1".format(name))
    json = r.json()
    if not json['resultCount']:
        return {"error": "Song not found"}
    else:
        return {
            "artist": artist,
            "title": title,
            "url": json['results'][0]['previewUrl']
        }
