from flask import flash, jsonify, render_template, redirect, url_for, jsonify, request, current_app, abort
from flask_login import current_user
from app.main.urls import main
from app.models import *
from app.main.forms import *
from app import db
from flask_login import login_required

# from flask_login import current_user

from app.main.urls import main
from app.models import User, Comment
from app.main.forms import UpdateAccount, CommentForm
from app.auth.forms import RegistrationForm
from app import db, photos


@main.route('/', methods=['GET', 'POST'])
def index():
    posts = Post.query.all()
    # if request.method == 'POST':
    #     body = request.form['posttext']
    #     author = current_user.username
    #     output = {'body': body, 'author': author}
    #     return jsonify(output)
    return render_template('index.html', posts=posts)

# @main.route('/upload', methods=['GET', 'POST'])
# def upload():
#     new_post = Post(body=request.form['post-text'], author=current_user)
#     post = {
#         'body': new_post.body,
#         'author': new_post.author,
#     }
#     db.session.add(new_post)
#     db.session.commit()
#     return jsonify(post)


@main.route('/account/<uname>')
@login_required
def account(uname):
    form = UpdateAccount()
    user = User.query.filter_by(username=uname).first_or_404()
    if user is None:
        abort(404)
    return render_template('account.html', user=user, form=form)


@main.route('/account/<uname>/update/', methods=['GET', 'POST'])
@login_required
def update_account(uname):
    user = User.query.filter_by(username=uname).first()
    if user is None:
        abort(404)
    update = UpdateAccount()
    if update.validate_on_submit():
        user.bio = update.bio.data
        db.session.add(user)
        db.session.commit()

        return redirect(url_for('main.account', uname=user.username))
    return render_template('update.html', update=update)


@main.route('/account/<uname>/update/pic', methods=['POST'])
@login_required
def update_pic(uname):
    user = User.query.filter_by(username=uname).first()
    if 'photo' in request.files:
        filename = photos.save(request.files['photo'])
        path = f'photos/{filename}'
        user.profile_pic = path
        db.session.commit()
        return redirect(url_for('main.account', uname=user.username))

# comment view method


@main.route('/comment', methods=["GET", "POST"])
def comment():
    form = CommentForm()
    if form.validate_on_submit():
        comment = Comment(comment=form.comment.data)
        db.session.add(comment)
        db.session.commit()
        return redirect(url_for('main.index'))
    return render_template('comment.html', form=form)
