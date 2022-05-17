from flask import render_template
from app.auth.forms import RegistrationForm
from app.main.urls import main

@main.route('/')
def index():
    form =RegistrationForm()
    return render_template('auth/register.html',registration_form=form)

