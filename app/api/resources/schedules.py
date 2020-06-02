from flask import g,request
from app.models import User,Cookbook,Schedule
from flask_restful import Resource,fields,marshal_with,reqparse,inputs,marshal
from app.extensions import db
from app.api.common.auth import token_auth
from app.api.resources.users import user_fields
import json


class ScheduleAPI(Resource):
    def get(self):
        pass



class AuthorRaw(fields.Raw):
    def output(self,key,obj):
        return marshal(obj.users,user_fields)


class ItemRaw(fields.Raw):
    def output(self,key,obj):
        z=obj
        return '1'

schedule_fields = {
    'id':fields.Integer,
    'day':fields.Integer,
    'author':AuthorRaw,
}



class ScheduleListAPI(Resource):
    def __init__(self):
        self.parser = reqparse.RequestParser()
        self.parser.add_argument(name='day_name',required=True,location='json',type=str,help='day_name verify failed')
        self.parser.add_argument(name='cookbook_id',required=True,location='json',type=str,help='cookbook_id verify failed')
    @token_auth.login_required
    def get(self):
        '''获取当前用户的所有schedule'''
        response = g.current_user.schedules.order_by(Schedule.day).all()
        return marshal(response,schedule_fields)
    @token_auth.login_required
    def post(self):
        '''为当前用户创建schedule'''

        args = self.parser.parse_args()
        ck = Cookbook.query.get_or_404(args.get('cookbook_id'))
        sc = Schedule()
        sc.users = g.current_user
        sc.day = args.get('day_name')
        sc.cookbooks = ck
        db.session.add(sc)
        db.session.commit()
        return {'message':'created ok'},201
    @token_auth.login_required
    def put(self):
        '''修改当前用户一个schedule'''
        args = self.parser.parse_args()
        error = {}
        ck = Cookbook.query.get_or_404(args.get('cookbook_id'))
        sc = g.current_user.schedules.filter_by(day=args.get('day_name'))
        if not sc:
            error['error'] = 'selected day not found'
        if error:
            return error,404
        sc.cookbooks = ck
        db.session.add(sc)
        db.session.commit()
        return {'message':'Changed Success.'},200
            



    