'''all application forms'''
from flask_wtf import FlaskForm
from app.models import Comment
from wtforms import StringField, TextAreaField,SubmitField

#updates bio in user bio
class UpdateAccount(FlaskForm):
    bio = TextAreaField('bio')
    submit = SubmitField('update bio')
   

class CommentForm(FlaskForm):
    comment = StringField('enter comment')
    submit = SubmitField('post comments')

