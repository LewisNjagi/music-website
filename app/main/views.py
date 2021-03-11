
from flask import render_template
from . import main
# from ..request import get_track

# Views
@main.route('/')
def index():

    '''
    View root page function that returns the index page and its data
    '''
    # track = get_track()
    # title = 'Hello'
    # ,track = track,title = title
    return render_template('index.html')

@main.route('/artists')
def artists():

    '''
    View root page function that returns the index page and its data
    '''
    # artists = get_track()
    # ,artists = artists,title = title
    return render_template('artists.html')

