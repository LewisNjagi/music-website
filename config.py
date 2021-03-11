import os
class Config:
    '''
    General configuration parent class
    '''
    SECRET_KEY = os.environ.get("SECRET_KEY")
    # SQLALCHEMY_DATABASE_URI = 'postgresql+psycopg2://moringa:kipkirui@localhost/music' 
    SQLALCHEMY_DATABASE_URI = 'postgresql+psycopg2://qyunky:Lewis860@localhost/music' 
    TRACK_BASE_URL = "https://genius.p.rapidapi.com/artists/16775/songs"

class prodConfig(Config):
    '''
    Production  configuration child class

    Args:
        Config: The parent configuration class with General configuration settings
    '''
    pass

class DevConfig(Config):
    '''
    Development configuration child class

    Args:
        Config: The parent configuration class with General configuration settings
    '''

    DEBUG = True
    SQLALCHEMY_TRACK_MODIFICATIONS = False

config_options = {
'development':DevConfig,
'production':prodConfig
}