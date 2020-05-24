from app.models.base import *
from app import db
class Food(db.Model):
    __tablename__='foods'
    id = db.Column(db.Integer,primary_key=True)
    name = db.Column(db.String(20),index=True,unique=True)
    amount = db.Column(db.String(10))

    # ForeignKey
    cookbook_id = db.Column(db.Integer,db.ForeignKey('cookbooks.id'))


    # Print
    def __repr__(self):
        return '<Food {},{}>'.format(self.id,self.name)
