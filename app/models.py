from app import db
from datetime import datetime


class User(db.Model):
    __tablename__ = 'users'
    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(100), unique=True)
    email = db.Column(db.String(100), unique=True)
    profile_pic = db.Column(db.String(20))
    bio = db.Column(db.String(200))
    password = db.Column(db.String(120))
    timestamp = db.Column(db.DateTime, index=True, default=datetime.utcnow)
    post_id = db.relationship('Post', backref='author', lazy='dynamic')
    comment_id = db.relationship('Comment', backref='author', lazy='dynamic')
    # follow_id = db.relationship ('Follow', backref='author',lazy='dynamic')

    def __repr__(self):
        return f'<User: {self.username}>'


class Post(db.Model):
    __tablename__ = 'posts'
    id = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String(200))
    body = db.Column(db.String(255))
    post_pic = db.Column(db.String(50))
    timestamp = db.Column(db.DateTime, index=True, default=datetime.utcnow)
    user_id = db.Column(db.Integer, db.ForeignKey('users.id'))
    post_comment = db.relationship('Comment', backref='pitch', lazy='dynamic')

    def __repr__(self):
        return f'<Post: {self.title}>'


class Comment(db.Model):
    __tablename__ = 'comments'
    id = db.Column(db.Integer, primary_key=True)
    comment = db.Column(db.String(200))
    timestamp = db.Column(db.DateTime, index=True, default=datetime.utcnow)
    user_id = db.Column(db.Integer, db.ForeignKey('users.id'))
    post_id = db.Column(db.Integer, db.ForeignKey('posts.id'))

    def __repr__(self):
        return f'<Comment: {self.comment}>'
    
    
# class Follow(db.Model):
#     __tablename__ = 'followers'
#     id = db.Column(db.Integer, primary_key=True)
#     follower= db.column(db.Integer,ForeignKey('users.id'))
#     followed= db.column(db.Integer,ForeignKey('users.id'))
    

    


