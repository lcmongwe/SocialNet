from flask import render_template,redirect,url_for,request,abort
from flask_login import login_required
from app.main.urls import main
from app.models import User
from app.main.forms import UpdateAccount
from app import db,photos


@main.route('/')
def index():
    return render_template('index.html')


@main.route('/account/<uname>')
#@login_required
def account(uname):
    form=UpdateAccount()
    user = User.query.filter_by(username=uname).first()
    if user is None:
        abort(404)
    return render_template('account.html',form=form, user=user)

    
@main.route('/account/<uname>/update/', methods=['GET', 'POST'])
#@login_required
def update_account(uname):
    user = User.querry.filter_by(username = uname).first()
    if user is None:
        abort(404)
    update = UpdateAccount()
    if update.validate_on_submit():
        user.bio = update.bio.data
        db.session.add(user)
        db.session.commit()
        
        return redirect(url_for('account',uname=user.username))
    return render_template('update.html',update=update)


@main.route('/account/<uname>/update/pic', methods=['POST'])
# @login_required
def update_pic(uname):
    user = User.querry.filter_by(username = uname).first()
    if 'photo' in request.files:
        filename = photos.save(request.files['photo'])
        path = f'photos/{filename}'
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    