from ..models import User, Comment
from flask import redirect, render_template,url_for
from app.main.forms import CommentForm 
from app.main.urls import main
from .. import db

@main.route('/')
def index():
    return render_template('index.html')

@main.route('/comment', methods= ["GET","POST"])
def Comment():
    form = CommentForm()
    if form.validate_on_submit():
        comments= form.comments.data
        comments = Comment(comments = comments)
        db.session.add(comments)
        db.session.commit()
        return redirect(url_for('main.comment'))
    return render_template('main/index.html', form = form)
        
        
        
        
        
        
    