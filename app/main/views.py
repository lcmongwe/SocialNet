from ..models import User, Comment
from flask import redirect, render_template,url_for
from app.main.forms import CommentForm 
from app.main.urls import main
from .. import db

@main.route('/')
def index():
    comments= Comment.query.all()
    return render_template('index.html',comments=comments)

@main.route('/comment', methods= ["GET","POST"])
def comment():
    form = CommentForm()
    if form.validate_on_submit():
        comment = Comment(comment = form.comment.data)
        db.session.add(comment)
        db.session.commit()
        return redirect(url_for('main.index'))
    return render_template('comment.html', form = form)
        
        
        
        
        
        
    