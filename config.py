import os
class Config:
    '''
    General configuration parent class
    '''
    SECRET_KEY = os.environ.get("SECRET_KEY")
    # SQLALCHEMY_DATABASE_URI = 'postgresql+psycopg2://moringa:kipkirui@localhost/music' 
    SQLALCHEMY_DATABASE_URI = 'postgresql+psycopg2://moringa:kipkirui@localhost/music' 
    TRACK_BASE_URL = "https://genius.p.rapidapi.com/artists/16775/songs"
    
    #  email configurations
    MAIL_SERVER = 'smtp.googlemail.com'
    MAIL_PORT = 587
    MAIL_USE_TLS = True
    MAIL_USERNAME =os.environ.get("MAIL_USERNAME")
    MAIL_PASSWORD =os.environ.get("MAIL_PASSWORD")

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