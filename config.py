'''Configuration classes module'''

import os


class Config:

    '''
    General configuration parent class
    '''

    #SQLALCHEMY_DATABASE_URI = 'postgresql+psycopg2://reuben_ubuntu:password@localhost/blog'
    SECRET_KEY = os.environ.get('SECRET_KEY')
    SQLALCHEMY_TRACK_MODIFICATIONS = False

    # Images' save location when a user uploads one
    UPLOADED_PHOTOS_DEST = 'app/static/images'

    # Email configurations
    MAIL_SERVER = 'smtp.googlemail.com'
    MAIL_PORT = 587
    MAIL_USE_TLS = True
    MAIL_USERNAME = os.environ.get("MAIL_USERNAME")
    MAIL_PASSWORD = os.environ.get("MAIL_PASSWORD")
    SENDER_EMAIL = 'harryjbenj@gmail.com'


class ProdConfig(Config):

    '''
    Production  configuration child class

    Args:
        Config: The parent configuration class with General configuration settings
    '''

    SQLALCHEMY_DATABASE_URI = os.environ.get("DATABASE_URL")


class DevConfig(Config):

    '''
    Development  configuration child class

    Args:
        Config: The parent configuration class with General configuration settings
    '''

    SQLALCHEMY_DATABASE_URI = 'postgresql+psycopg2://reuben_ubuntu:password@localhost/blog'

    DEBUG = True


CONFIG_OPTIONS = {
    'development': DevConfig,
    'production': ProdConfig
}
