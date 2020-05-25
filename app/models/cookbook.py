from app.models.base import *
from app.extensions import db
class Cookbook(db.Model):
    __tablename__='cookbooks'
    id = db.Column(db.Integer,primary_key=True)
    name = db.Column(db.String(20),index=True,unique=True)
    image_url = db.Column(db.String(128))


    # ForeignKey
    user_id = db.Column(db.Integer,db.ForeignKey('users.id'))
    schedule_id = db.Column(db.Integer,db.ForeignKey('schedules.id'))

    # relationship
    foods = db.relationship('Food',backref='cookbooks',lazy='dynamic',cascade='all, delete-orphan')

    # Print
    def __repr__(self):
        return '<Cookbook {},{}>'.format(self.id,self.name)
