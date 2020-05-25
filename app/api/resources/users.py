from flask_restful import Resource
from app.models import User
from flask_restful import Resource,fields,marshal_with,reqparse

user_fields = {
    'name':fields.String,
    'email':fields.String,
    'password_hash':fields.String,
    'avatar':fields.String
}

class UserAPI(Resource):

    @marshal_with(user_fields)
    def get(self,id):
        '''获取单个用户'''
        user = User.query.get_or_404(id)
        return user
    def put(self,id):
        '''修改单个用户'''
        pass
    def delete(self,id):
        '''删除单个用户'''
        pass

    
class UserListAPI(Resource):
    def __init__(self):
        self.parser = reqparse.RequestParser()
    def get(self):
        '''获取用户合集'''
        pass
    def post(self):
        '''新增用户'''
        self.parser.add_argument(name='name',type=str,location='json',required=True)
        self.parser.add_argument(name='email',type=str,location='json',required=True)
