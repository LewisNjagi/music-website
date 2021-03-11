
from flask import render_template
from . import main
from ..request import get_track
from .forms import SubscriberForm
from ..models import Subscriber
from ..import db
from ..emails import mail_message

# Views
@main.route('/')
def index():

    '''
    View root page function that returns the index page and its data
    '''
    track = get_track()
    # title = 'Hello'
    # ,track = track,title = title
    return render_template('index.html',track = track)

@main.route('/artists')
def artists():

    '''
    View root page function that returns the index page and its data
    '''
    artists = get_track()
    # ,artists = artists,title = title
    return render_template('artists.html',artists = artists)

@main.route('/songs')
def songs():

    '''
    View root page function that returns the index page and its data
    '''
    songs = get_playlist()
    print("rrrrrrrrrrrrrr")
    print(songs)
    print("hhhhhhhhhhh")
    return render_template('songs.html',songs = songs)

@main.route('/Subscribe',methods=['GET','POST'])
def subVis():
    
    form = SubscriberForm()
    if form.validate_on_submit():
        subs = Subscriber(email = form.email.data, username = form.username.data)    
        db.session.add(subs)
        db.session.commit()


        mail_message("You have successfully subscribed to Visplay website,Thank for joining us", "email/welcome_subs", subs.email,subs=subs)
    
    return render_template('subscribe.html',subscribe_form=form)
