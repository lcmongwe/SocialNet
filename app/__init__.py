"""aplication factory"""
# from ensurepip import bootstrap
from flask import Flask
from flask_login import LoginManager
from flask_bootstrap import Bootstrap
from flask_sqlalchemy import SQLAlchemy
from app.config import config_options

# 

db = SQLAlchemy()
bootstrap = Bootstrap()

login_manager = LoginManager()
login_manager.session_protection = 'strong'
login_manager.login_view = 'auth.login'

def create_app(config_name):
    app = Flask(__name__)
    
    app.config.from_object(config_options[config_name])
    # flask imports
    db.init_app(app)
    bootstrap.init_app(app)
    login_manager.init_app(app)
    
    # blueprints
    from .main.urls import main, auth
    app.register_blueprint(main)
    app.register_blueprint(auth)
    
    # APP CONFIGS
    
    
    return app