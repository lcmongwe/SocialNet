'''all application forms'''
from flask_wtf import FlaskForm
from wtforms import StringField, TextAreaField,SubmitField

#updates bio in user bio
class UpdateAccount(FlaskForm):
    bio = TextAreaField('bio')
    submit = SubmitField('update bio')
    