"""Authentication views"""
from flask import render_template
from app.main.urls import auth

# login route
@auth.route('/login')
def login():
    return render_template('auth/login.html')

# register