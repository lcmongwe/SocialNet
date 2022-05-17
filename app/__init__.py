"""aplication factory"""
from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from app.config import config_options

# 
db = SQLAlchemy()

def create_app(config_name):
    app = Flask(__name__)
    
    # APP CONFIGS
    app.config.from_object(config_options[config_name])
    
    # flask imports
    db.init_app(app)
    
    # blueprints
    from .main.urls import main, auth
    app.register_blueprint(main)
    app.register_blueprint(auth)
    
    
    return app