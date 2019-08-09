from flask import jsonify, request
from flask_cors import CORS, cross_origin
from app import app
from helpers import GENRES_LIST, GENRES_NAMES, get_four_songs
from utility import get_preview_url
import json, random 

@app.route('/getGenres', methods=['GET','POST'])
@cross_origin()
def getGenres():
    if (request.method == 'POST'):
        json_data = request.get_json()
        print(json_data['value'])
        chart_title = json_data['value']
        chart_name = GENRES_LIST[chart_title]

        #initialize url to error
        urlin = {"error": "Song not found"}
    
        #keep getting new url until no error
        while "error" in urlin:
            songs_chosen = get_four_songs(chart_name)
            index = random.randint(0,3)
            correct_song = songs_chosen[index]
            urlin = get_preview_url(correct_song.title, correct_song.artist)
        song_url = urlin["url"]
        print('Song url: ', song_url)
        print('Correct song: ', correct_song)
        songList = []
        for song in songs_chosen:
            print('song: ', song)
            songList.append("'" + song.title + "' by " + song.artist)
        correct_song_new = "'" + correct_song.title + "' by " + correct_song.artist

        data = {
        "song_answers": songList,
        "chartname": chart_name,
        "charttitle": chart_title,
        "songurl_correct": song_url,
        "correct_song": correct_song_new,
        }

        return jsonify(data)
    else:
        return jsonify(GENRES_NAMES)