import json
import requests
from .models import Track

def configure_request(app):
    pass

def get_track():

    get_track_url = "https://genius.p.rapidapi.com/artists/16775/songs"

    headers = {
        'x-rapidapi-key': "66b57c6964msh8f34cedfde351fbp1c4ea2jsnae1dba8d4f0d",
        'x-rapidapi-host': "genius.p.rapidapi.com"
        }

    track_response = requests.get(get_track_url, headers=headers).json()

    track_results = None

    if track_response['response']['songs']:

        track_results_list = track_response['response']['songs']
        track_results = process_tracks(track_results_list)

      
        return track_results
    

def process_tracks(track_list):

    track_results = []
    for track_item in track_list:
        id = track_item.get('id')
        song_art_image_thumbnail_url = track_item.get('song_art_image_thumbnail_url')
        image_url = track_item.get('primary_artist').get('image_url')
        name = track_item.get('primary_artist').get('name')
        url = track_item.get('primary_artist').get('url')
        cover = track_item.get('cover')

        if song_art_image_thumbnail_url:
            track_object = Track(id,song_art_image_thumbnail_url,image_url,name,url)
            track_results.append(track_object)

    return track_results


# def albums():
    
#     url = 'https://api.happi.dev/v1/music/artists/120/albums?apikey=d6a945O7Im1cINbOASSSN2z8UPQFdNQLUSw6PjqzGcYPHr2rh16326nJ'

#     album_response = requests.get(url).json()

#     album_results = None

#     if album_response['results']['albums']:

#         album_results_list = album_response['results']['albums']
#         album_results = process_album(album_results_list)
        
#         return album_results

# def process_album(album_list):

#     album_results = []
#     for album_item in album_list:
#         cover = track_item.get('cover')

#         if cover:
#             album_object = Album(cover)
#             album_results.append(album_object)

#     return album_results


# get_track()
# playlist()
# search()