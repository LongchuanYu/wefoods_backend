from app.models.base import Base
from flask import current_app
from app.extensions import db
from hashlib import md5
from time import time
from datetime import datetime,timedelta
from werkzeug.security import generate_password_hash,check_password_hash
from app.models.exts import Schedule
import jwt

class User(db.Model):
    __tablename__='users'
    id = db.Column(db.Integer,primary_key=True)
    username = db.Column(db.String(20),index=True,unique=True)
    nickname = db.Column(db.String(20),default='')
    email = db.Column(db.String(120),index=True,unique=True)
    password_hash = db.Column(db.String(128))
    avatar = db.Column(db.String(128),default='')


    # relationship
    schedules = db.relationship('Schedule',backref='users',cascade='all, delete-orphan',lazy='dynamic')
    cookbooks = db.relationship('Cookbook',backref='users',lazy='dynamic',cascade='all, delete-orphan')


    # Print
    def __repr__(self):
        return '<User {},{}>'.format(self.id,self.username)

    # Methods
    def generate_avatar(self, size):
        '''用户头像'''
        digest = md5(self.email.lower().encode('utf-8')).hexdigest()
        return 'https://www.gravatar.com/avatar/{}?d=identicon&s={}'.format(digest, size)
    
    def set_password(self,password):
        self.password_hash = generate_password_hash(password)

    def check_password_byhash(self,password):
        return check_password_hash(self.password_hash,password)
    
    def get_jwt(self,expires = None ):
        expires = expires if expires else current_app.config['LOGIN_EXPIRES_IN']
        now = datetime.utcnow()
        encoded_jwt = jwt.encode(
            {
                'userid':self.id,
                'username':self.username,
                'email':self.email,
                'avatar':self.avatar if self.avatar else self.generate_avatar(128),
                'exp': now + timedelta(seconds=expires),
                'iat':now
            },
            current_app.config['SECRET_KEY'],
            algorithm="HS256"
        ).decode('utf-8')
        return encoded_jwt
    @staticmethod
    def verify_jwt(token):
        try:
            decode_jwt = jwt.decode(
                token,
                current_app.config['SECRET_KEY'],
                algorithms=['HS256'],
            )
        except (jwt.ExpiredSignatureError,jwt.exceptions.InvalidSignatureError) as e:
            return False
        # 验证jwt没有过期，且有效则把解码后的jwt返回。
        return decode_jwt

    def initSchedule(self):
        schedules_list = [
            Schedule(day=x,users=self) for x in range(1,8)
        ]
        db.session.add_all(schedules_list)

        
