from flask import session
import billboard, random, requests


"""
REQUIRES: chart is a valid Chart instance from the Billboard API
MODIFIES: nothing
EFFECTS: returns four unique numbers between 0 and the size of the chart passed in
"""
def get_four_choices(chart):
    return random.sample(range(0,len(chart)), 4)

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

