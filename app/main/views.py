from flask import render_template
from app.auth.forms import RegistrationForm
from app.main.urls import main

@main.route('/',methods = ['GET','POST'])
def index():
    form =RegistrationForm()
    return render_template('index.html',registration_form=form)

