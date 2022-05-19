import os



class Config:
    """
    Class that sets the app cofiguration variables
    """
    SECRET_KEY = os.environ.get(
        'SECRET_KEY') or '<try-guessing-one-might-work>'
    
    SQLALCHEMY_TRACK_MODIFICATIONS = False
    UPLOADED_PHOTOS_DEST ='app/static/photos'

class ProdConfig(Config):
    pass


class DevConfig(Config):
    """
    Development configuration settings
    """
    SQLALCHEMY_DATABASE_URI='postgresql+psycopg2://lucy:4444@localhost/socialnet'

    # SQLALCHEMY_DATABASE_URI = os.environ.get('SQLALCHEMY_DATABASE_URI')
    DEBUG = True


# config envs
config_options = {
    'development': DevConfig,
    'production': ProdConfig
}
