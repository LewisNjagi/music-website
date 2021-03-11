import json
import requests


def configure_request(app):
    pass

def get_playlist():

    get_playlist_url = "https://unsa-unofficial-spotify-api.p.rapidapi.com/playlist"

    querystring = {"id":"2IbZGv306zaldI0lap578G","start":"0","limit":"50"}

    headers = {
        'x-rapidapi-key': "66b57c6964msh8f34cedfde351fbp1c4ea2jsnae1dba8d4f0d",
        'x-rapidapi-host': "unsa-unofficial-spotify-api.p.rapidapi.com"
        }

    playlist_response = requests.get(get_playlist_url, headers=headers, params=querystring)


    return playlist_response.json()

def get_track():

    get_track_url = "https://genius.p.rapidapi.com/artists/16775/songs"
    

    headers = {
        'x-rapidapi-key': "66b57c6964msh8f34cedfde351fbp1c4ea2jsnae1dba8d4f0d",
        'x-rapidapi-host': "genius.p.rapidapi.com"
        }

    track_response = requests.get(get_track_url, headers=headers)
  

    return track_response.json()


def search():

    search_url = "https://genius.p.rapidapi.com/search"

    querystring = {"q":"Kendrick Lamar"}

    headers = {
        'x-rapidapi-key': "66b57c6964msh8f34cedfde351fbp1c4ea2jsnae1dba8d4f0d",
        'x-rapidapi-host': "genius.p.rapidapi.com"
        }

    search_response = requests.get(search_url, headers=headers, params=querystring)


    return search_response.json()

get_track()
get_playlist()
search()





