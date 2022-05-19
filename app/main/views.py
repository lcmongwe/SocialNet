from flask import render_template,redirect,url_for,request,abort
from flask_login import login_required

# from flask_login import current_user

from app.main.urls import main
from app.models import User, Comment
from app.main.forms import UpdateAccount, CommentForm  
from app.auth.forms import RegistrationForm
from app import db, photos


@main.route('/',methods = ['GET','POST'])
def index():

    comments= Comment.query.all()
    return render_template('index.html',comments=comments)



@main.route('/account/<uname>')
@login_required
def account(uname):
    form=UpdateAccount()
    user = User.query.filter_by(username=uname).first()
    if user is None:
        abort(404)
    return render_template('account.html',user=user,form=form)

    
@main.route('/account/<uname>/update/', methods=['GET', 'POST'])
@login_required
def update_account(uname):
    user = User.query.filter_by(username = uname).first()
    if user is None:
        abort(404)
    update = UpdateAccount()
    if update.validate_on_submit():
        user.bio = update.bio.data
        db.session.add(user)
        db.session.commit()
        
        return redirect(url_for('main.account',uname=user.username))
    return render_template('update.html',update=update)


@main.route('/account/<uname>/update/pic', methods=['POST'])
@login_required
def update_pic(uname):
    user = User.query.filter_by(username = uname).first()
    if 'photo' in request.files:
        filename = photos.save(request.files['photo'])
        path = f'photos/{filename}'
        user.profile_pic = path
        db.session.commit()
        return redirect(url_for('main.account',uname=user.username))
    
# comment view method
@main.route('/comment', methods= ["GET","POST"])
def comment():
    form = CommentForm()
    if form.validate_on_submit():
        comment = Comment(comment = form.comment.data)
        db.session.add(comment)
        db.session.commit()
        return redirect(url_for('main.index'))
    return render_template('comment.html', form = form)
    
    
    
    

    