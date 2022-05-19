'''all application forms'''
from flask_wtf import FlaskForm
from wtforms import StringField, PasswordField, BooleanField, SubmitField, TextAreaField
from wtforms.validators import DataRequired, Length
from wtforms import ValidationError


class UploadPost(FlaskForm):
    body=TextAreaField('Text', validators=[DataRequired(), Length(min=1, max=140)])
    submit=SubmitField('Submit')