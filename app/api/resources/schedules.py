from flask import g,request
from app.models import User,Cookbook
from flask_restful import Resource,fields,marshal_with,reqparse,inputs,marshal
from app.extensions import db
from app.api.common.auth import token_auth
import json


class ScheduleAPI(Resource):
    def get(self):
        pass

class ScheduleListAPI(Resource):
    def get(self):
        '''获取一个用户的全部schedule'''
        pass
    def post(self):
        '''为一个用户创建schedule'''
        pass
    