from flask import g
from app.api.common.auth import basic_auth
from flask_restful import Resource,fields,marshal_with,reqparse


class Token(Resource):
    @basic_auth.login_required
    def post(self):
        return {'token':g.current_user.get_jwt()}
 