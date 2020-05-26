from app.models import User
from app.api.common.auth import basic_auth
from flask_restful import Resource,fields,marshal_with,reqparse


class Ping(Resource):
    @basic_auth.login_required
    def get(self):
        return 'yes!!'