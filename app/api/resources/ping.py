from flask import g
from app.models import User
from app.api.common.auth import basic_auth,token_auth
from flask_restful import Resource,fields,marshal_with,reqparse


class Ping(Resource):
    def get(self):
        return 'yes!!'
    @basic_auth.login_required        
    def post(self):
        # 获取token
        token = g.current_user.get_jwt()
        return {'token':token}

