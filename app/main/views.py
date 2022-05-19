from flask import flash, jsonify, render_template, redirect, url_for, jsonify, request, current_app
from flask_login import current_user
from app.main.urls import main
from app.models import Post
from app.main.forms import UploadPost
from app import db

@main.route('/', methods=['GET', 'POST'])
def index():
    posts = Post.query.all()
    if request.method == 'POST':
        body = request.form['posttext']
        author = current_user.username
        output = {'body': body, 'author': author}
        return jsonify(output)
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