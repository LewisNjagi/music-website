from werkzeug.security import generate_password_hash,check_password_hash
from flask_login import UserMixin
from . import db
from . import login_manager

class User(UserMixin,db.Model):

    __tablename__ = 'users'

    id = db.Column(db.Integer,primary_key = True)
    username = db.Column(db.String(255),index = True)
    email = db.Column(db.String(255),unique = True,index = True)
    # role_id = db.Column(db.Integer,db.ForeignKey('roles.id'))
    password_hash = db.Column(db.String(255))
    pass_secure = db.Column(db.String(255))

    @property
    def password(self):
        raise AttributeError('You cannot read the password attribute')
    @password.setter
    def password(self,password):
        self.pass_secure = generate_password_hash(password)

    def verify_password(self,password):
        return check_password_hash(self.pass_secure,password)

    @login_manager.user_loader
    def load_user(user_id):
        return User.query.get(int(user_id))

class Track:
    def __init__(self,id,song_art_image_thumbnail_url,image_url,name,url):

        self.id = id
        self.song_art_image_thumbnail_url = song_art_image_thumbnail_url
        self.image_url = image_url
        self.name = name
        self.url = url

class Playlist:
    def __init__(self,id,name):

        self.id = id
        self.name = name
class Subscriber(db.Model):
    __tablename__ = 'subscriber'

    id = db.Column(db.Integer,primary_key = True)
    username = db.Column(db.String(255))
    email = db.Column(db.String(255),unique = True,index = True)

    def __repr__(self):
        return f'Subscriber {self.username}'     