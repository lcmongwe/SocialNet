'''all application forms'''
from xmlrpc.client import DateTime
from psycopg2 import Timestamp
from app.models import User, Comment
from wtforms import StringField, SubmitField
from flask_wtf import FlaskForm


class CommentForm(FlaskForm):
    post_id = StringField('the post id')
    Timestamp = DateTime('time posted')
    comment = StringField('enter comment')
    submit = SubmitField('post comments')