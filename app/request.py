import json
import requests
from .models import Track

def configure_request(app):
    pass

# def get_playlist():

#     get_playlist_url = "https://unsa-unofficial-spotify-api.p.rapidapi.com/playlist"

#     querystring = {"id":"2IbZGv306zaldI0lap578G","start":"0","limit":"50"}

#     headers = {
#         'x-rapidapi-key': "66b57c6964msh8f34cedfde351fbp1c4ea2jsnae1dba8d4f0d",
#         'x-rapidapi-host': "unsa-unofficial-spotify-api.p.rapidapi.com"
#         }

#     playlist_response = requests.get(get_playlist_url, headers=headers, params=querystring)

#     playlist = playlist_response.json()

#     return print(playlist)

# def get_track():

#     get_track_url = "https://genius.p.rapidapi.com/artists/16775/songs"
    

#     headers = {
#         'x-rapidapi-key': "66b57c6964msh8f34cedfde351fbp1c4ea2jsnae1dba8d4f0d",
#         'x-rapidapi-host': "genius.p.rapidapi.com"
#         }

#     track_response = requests.get(get_track_url, headers=headers).json()

#     track_results = None

#     if track_response['response']['songs']:

#         track_results_list = track_response['response']['songs']
#         track_results = process_tracks(track_results_list)

      
#         return track_results
    

# def process_tracks(track_list):

#     track_results = []
#     for track_item in track_list:
#         id = track_item.get('id')
#         song_art_image_thumbnail_url = track_item.get('song_art_image_thumbnail_url')
#         image_url = track_item.get('primary_artist').get('image_url')
#         name = track_item.get('primary_artist').get('name')
#         url = track_item.get('primary_artist').get('url')

#         if song_art_image_thumbnail_url:
#             track_object = Track(id,song_art_image_thumbnail_url,image_url,name,url)
#             track_results.append(track_object)

#     return track_results



# def search():

#     search_url = "https://genius.p.rapidapi.com/search"

#     querystring = {"q":"Kendrick Lamar"}

#     headers = {
#         'x-rapidapi-key': "66b57c6964msh8f34cedfde351fbp1c4ea2jsnae1dba8d4f0d",
#         'x-rapidapi-host': "genius.p.rapidapi.com"
#         }

#     search_response = requests.get(search_url, headers=headers, params=querystring)

    

#     return search_response.json()


# get_track()
# get_playlist()
# search()
