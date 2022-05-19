import os



class Config:
    """
    Class that sets the app cofiguration variables
    """
    SECRET_KEY = os.environ.get(
        'SECRET_KEY') or '<try-guessing-one-might-work>'
    SQLALCHEMY_DATABASE_URI = os.environ.get('SQLALCHEMY_DATABASE_URI')
    SQLALCHEMY_TRACK_MODIFICATIONS = False
    UPLOADED_PHOTOS_DEST ='app/static/photos'

class ProdConfig(Config):
    pass


class DevConfig(Config):
    """
    Development configuration settings
    """
    DEBUG = True


# config envs
config_options = {
    'development': DevConfig,
    'production': ProdConfig
}
