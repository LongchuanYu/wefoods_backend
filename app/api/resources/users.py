from flask_restful import Resource
from app.models import User
from flask_restful import Resource,fields,marshal_with,reqparse,inputs,marshal
from app.extensions import db


class fieldsRaw_avatar(fields.Raw):
    def output(self,key,obj):
        #（？）理解自定义输出格式 +
        # 用user模型来说明，obj指向user，key是user里面定义的字段。
        if obj.avatar:
            return obj.avatar
        return obj.generate_avatar(128)


user_fields = {
    # 返回响应的时候用
    'id':fields.Integer,
    'username':fields.String,
    'email':fields.String,
    'avatar':fieldsRaw_avatar
}
email_regex = '^(([^<>()\[\]\\.,;:\s@"]+(\.[^<>()\[\]\\.,;:\s@"]+)*)|(".+"))@((\[[0-9]{1,3}\.[0-9]{1,3}\.[0-9]{1,3}\.[0-9]{1,3}\])|(([a-zA-Z\-0-9]+\.)+[a-zA-Z]{2,}))$'

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
        super(UserListAPI, self).__init__()
    def get(self):
        '''获取用户合集'''
        pass
    def post(self):
        '''新增用户'''
        self.parser.add_argument(name='username',type=str,location='json',required=True)
        self.parser.add_argument(name='email',type=inputs.regex(email_regex),location='json',required=True,help='please provide a valid email.')
        self.parser.add_argument(name='password',type=str,location='json',required=True,help='Please provide a valid password.')
        args = self.parser.parse_args()
        user = User()
        error = {}
        if User.query.filter_by(username=args.get('username')).first():
            error['username'] = 'Duplicate username.'
        if User.query.filter_by(email=args.get('email')).first():
            error['email'] = 'Duuplicate email'
        if error:
            return {'message':error},400
        user.username = args.get('username')
        user.email = args.get('email')
        user.set_password(args.get('password'))
        db.session.add(user)
        db.session.commit()
        return marshal(user,user_fields)
