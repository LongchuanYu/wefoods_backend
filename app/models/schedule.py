from app.models.base import *
from app import db

class Schedule(db.Model):
    __tablename__='schedules'
    id = db.Column(db.Integer,primary_key=True)
    day = db.Column(db.Integer)



    # ForeignKey
    user_id = db.Column(db.Integer,db.ForeignKey('users.id'))
    

    # relationship
    cookbooks = db.relationship('Cookbook',uselist=False,backref='schedules')


    # Print
    def __repr__(self):
        return '<Schedule {}>'.format(self.id)
