from app.models.base import *
from app.extensions import db
from hashlib import md5

class User(db.Model):
    __tablename__='users'
    id = db.Column(db.Integer,primary_key=True)
    name = db.Column(db.String(20),index=True)
    email = db.Column(db.String(120),index=True,unique=True)
    password_hash = db.Column(db.String(128))
    avatar = db.Column(db.String(128))


    # relationship
    schedules = db.relationship('Schedule',backref='users',cascade='all, delete-orphan')
    cookbooks = db.relationship('Cookbook',backref='users',lazy='dynamic',cascade='all, delete-orphan')


    # Print
    def __repr__(self):
        return '<User {},{}>'.format(self.id,self.name)

    # Methods
    def get_avatar(self, size):
        '''用户头像'''
        digest = md5(self.email.lower().encode('utf-8')).hexdigest()
        return 'https://www.gravatar.com/avatar/{}?d=identicon&s={}'.format(digest, size)

