from app.models.base import *
from app.extensions import db
from datetime import datetime
class Cookbook(db.Model):
    __tablename__='cookbooks'
    id = db.Column(db.Integer,primary_key=True)
    name = db.Column(db.String(20),index=True)
    description = db.Column(db.String(200),default='')
    imageUrl = db.Column(db.String(128))
    myfoods = db.Column(db.Text)
    step = db.Column(db.Text)
    timestamp = db.Column(db.DateTime,index=True,default=datetime.utcnow)

    # ForeignKey
    user_id = db.Column(db.Integer,db.ForeignKey('users.id'))
    schedule_id = db.Column(db.Integer,db.ForeignKey('schedules.id'))

    # relationship
    foods = db.relationship('Food',backref='cookbooks',lazy='dynamic',cascade='all, delete-orphan')

    # Print
    def __repr__(self):
        return '<Cookbook {},{}>'.format(self.id,self.name)


    # Methods
    def from_dict(self,args):
        for field in ['name','description','step','myfoods']:
            if field in args:
                setattr(self,field,args.get(field))