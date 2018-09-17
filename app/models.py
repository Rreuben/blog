'''Module containing classes'''

from datetime import datetime
from flask_login import UserMixin
from werkzeug.security import generate_password_hash, check_password_hash
from . import DB, LOGIN_MANAGER


@LOGIN_MANAGER.user_loader
def load_user(user_id):
    return User.query.get(int(user_id))

class User(UserMixin, DB.Model):

    __tablename__ = 'users'

    id = DB.Column(DB.Integer, primary_key=True)
    username = DB.Column(DB.String(255))
    email = DB.Column(DB.String(255), unique=True)
    password_hash = DB.Column(DB.String(255))
    bio = DB.Column(DB.String(255))
    profile_pic_path = DB.Column(DB.String())

    role_id = DB.Column(DB.Integer, DB.ForeignKey('roles.id'))
    blogs = DB.relationship('Blog', backref='user', lazy="dynamic")
    comments = DB.relationship('Comment', backref='user', lazy='dynamic')

    @property
    def password(self):
        raise AttributeError('You cannot read the password attribute')

    @password.setter
    def password(self, password):
        self.password_hash = generate_password_hash(password)

    def verify_password(self, password):
        return check_password_hash(self.password_hash, password)

    def __repr__(self):
        return f'{self.username}'


class Role(DB.Model):

    __tablename__ = 'roles'

    id = DB.Column(DB.Integer, primary_key=True)
    name = DB.Column(DB.String(255), index=True)

    users = DB.relationship('User', backref='role', lazy='dynamic')


class Blog(DB.Model):

    __tablename__ = 'blogs'

    id = DB.Column(DB.Integer, primary_key=True)
    title = DB.Column(DB.String(255), index=True)
    content = DB.Column(DB.String(), index=True)
    time = DB.Column(DB.DateTime, default=datetime.utcnow)

    user_id = DB.Column(DB.Integer, DB.ForeignKey('users.id'))
    comments = DB.relationship('Comment', backref='blog', lazy='dynamic')

    def save_blog(self):
        DB.session.add(self)
        DB.session.commit()


class Comment(DB.Model):

    __tablename__ = 'comments'

    id = DB.Column(DB.Integer, primary_key=True)
    body = DB.Column(DB.String(250))

    blog_id = DB.Column(DB.Integer, DB.ForeignKey("blogs.id"))
    user_id = DB.Column(DB.Integer, DB.ForeignKey("users.id"))

    def save_comments(self):
        DB.session.add(self)
        DB.session.commit()
