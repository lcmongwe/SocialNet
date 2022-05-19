'''all application forms'''
from flask_wtf import FlaskForm
from wtforms import StringField, PasswordField, BooleanField, SubmitField, TextAreaField
from wtforms.validators import DataRequired, Length
from wtforms import ValidationError


class UploadPost(FlaskForm):
    body=TextAreaField('Text', validators=[DataRequired(), Length(min=1, max=140)])
    submit=SubmitField('Submit')
from app.models import Comment
from wtforms import StringField, TextAreaField,SubmitField

#updates bio in user bio
class UpdateAccount(FlaskForm):
    bio = TextAreaField('bio')
    submit = SubmitField('update bio')
   

class CommentForm(FlaskForm):
    comment = StringField('enter comment')
    submit = SubmitField('post comments')

