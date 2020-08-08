import os
basedir = os.path.abspath(os.path.dirname(__file__))


class Config(object):
    SECRET_KEY = os.environ.get('SECRET_KEY') or 'THIS-IS-TOP-SECRET'
    SQLALCHEMY_DATABASE_URI = os.environ.get('DATABASE_URL') or  \
        'mysql://username:password@localhost/' + os.path.join(basedir, 'app.db')
    SQLALCHEMY_TRACK_MODIFICATIONS = False