"""aplication factory"""
from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_login import LoginManager
from flask_migrate import Migrate
from app.config import config_options
from flask_uploads import UploadSet,IMAGES,configure_uploads
from flask_login import LoginManager

db = SQLAlchemy()
login_manager = LoginManager()
login_manager.login_view = 'auth.login'
photos = UploadSet('photos',IMAGES)

def create_app(config_name):
    app = Flask(__name__)
    
    app.config.from_object(config_options[config_name])
    
    
    # flask importspip
    
    db.init_app(app)
    login_manager.init_app(app)
    configure_uploads(app,photos)
    # blueprints
    from .main.urls import main, auth
    app.register_blueprint(main)
    app.register_blueprint(auth)
    
    # APP CONFIGS
    
    return app