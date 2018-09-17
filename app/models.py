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
    username = DB.Column(DB.String(255), unique=True, nullable=False)
    email = DB.Column(DB.String(255), unique=True, index=True, nullable=False)

    image_file = DB.Column(DB.String(70), nullable=False, default='default.jpg')
    comments = DB.relationship('Comments', backref='user', lazy='dynamic')

    def __repr__(self):
        return f'User {self.username}'

    pass_secure = DB.Column(DB.String(255))

    @property
    def password(self):
        raise AttributeError('You cannot read the password attribute')

    @password.setter
    def password(self, password):
        self.pass_secure = generate_password_hash(password)

    def verify_password(self, password):
        return check_password_hash(self.pass_secure, password)

    @login_manager.user_loader
    def load_user(user_id):
return User.query.get(int(user_id))
