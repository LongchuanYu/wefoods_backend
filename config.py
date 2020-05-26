import os


basedir = os.path.abspath(os.path.dirname(__file__))
class Config(object):
    SQLALCHEMY_DATABASE_URI = 'sqlite:///' + os.path.join(basedir,'app.db')
    SQLALCHEMY_TRACK_MODIFICATIONS = False
    SECRET_KEY = 'DEV'
    UPLOAD_FOLDER='upload'

    LOGIN_EXPIRES_IN = 36000 #登录的过期时间