from app.models import User
from flask_restful import Resource,fields,marshal_with,reqparse

resource_fields = {
    'name':fields.String,
    'email':fields.String,
    'password_hash':fields.String,
    'avatar':fields.String
}

class Ping(Resource):
    def __init__(self):
        self.parser = reqparse.RequestParser(bundle_errors=True)
        self.parser.add_argument('myname',type=str,help='oh No!!')
        self.parser.add_argument('myage',type=int,help='oh No!!')
    @marshal_with(resource_fields)
    def get(self):
        args = self.parser.parse_args(strict=True)
        user = User.query.get(1)
        return user