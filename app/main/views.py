from flask import render_template
from app.main.urls import main

@main.route('/')
def index():
    return render_template('index.html')

