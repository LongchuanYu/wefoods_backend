from app.models.base import *
from app.extensions import db
from hashlib import md5
from werkzeug.security import generate_password_hash,check_password_hash

class User(db.Model):
    __tablename__='users'
    id = db.Column(db.Integer,primary_key=True)
    username = db.Column(db.String(20),index=True,unique=True)
    nickname = db.Column(db.String(20),default='')
    email = db.Column(db.String(120),index=True,unique=True)
    password_hash = db.Column(db.String(128))
    avatar = db.Column(db.String(128),default='')


    # relationship
    schedules = db.relationship('Schedule',backref='users',cascade='all, delete-orphan')
    cookbooks = db.relationship('Cookbook',backref='users',lazy='dynamic',cascade='all, delete-orphan')


    # Print
    def __repr__(self):
        return '<User {},{}>'.format(self.id,self.name)

    # Methods
    def generate_avatar(self, size):
        '''用户头像'''
        digest = md5(self.email.lower().encode('utf-8')).hexdigest()
        return 'https://www.gravatar.com/avatar/{}?d=identicon&s={}'.format(digest, size)
    
    def set_password(self,password):
        self.password_hash = generate_password_hash(password)