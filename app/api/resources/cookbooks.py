from flask import g,request
from app.models import User,Cookbook
from flask_restful import Resource,fields,marshal_with,reqparse,inputs,marshal
from werkzeug.datastructures import FileStorage
from app.extensions import db
from app.api.common.utils import upload_file
from app.api.common.auth import token_auth
from app.api.resources.users import user_fields
import json



# （？）如何定义嵌套的有关系的输出字段呢？+
class AuthorRaw(fields.Raw):
    def output(self,key,obj):
        return marshal(obj.users,user_fields)



cookbook_fields = {
    'id':fields.Integer,
    'name':fields.String,
    'description':fields.String,
    'imageUrl':fields.String,
    'myfoods':fields.String,
    'step':fields.String,
    'timestamp':fields.String,
    'author':AuthorRaw
}

cookbooks_fields={
    'items':fields.List(fields.Nested(cookbook_fields)),
    '_meta':{
        'page':fields.Integer,
        'per_page':fields.Integer,
        'pages':fields.Integer,
        'total':fields.Integer
    }
}


class CookbookAPI(Resource):
    @marshal_with(cookbook_fields)
    def get(self,id):
        '''获取单个菜谱'''
        ck = Cookbook.query.get_or_404(id)
        return ck
    def post(self):
        ''''''
        pass

class CookbookListAPI(Resource):
    def __init__(self):
        self.parser = reqparse.RequestParser()
        self.parser.add_argument('imgfile',type=FileStorage,location='files')
        self.parser.add_argument('name',type=str)
        self.parser.add_argument('description',type=str)
        self.parser.add_argument('myfoods',type=str)
        self.parser.add_argument('step',type=str)
    def get(self):
        '''获取菜谱合集'''
        ck = Cookbook()
        page = request.args.get('page',type=int) or 1
        per_page = request.args.get('per_page',type=int) or 10
        resources = ck.query.order_by(Cookbook.timestamp.desc()).paginate(page,per_page,False)
        return marshal(resources,cookbooks_fields)


    @token_auth.login_required
    def post(self):
        '''新增菜谱'''
        # （？）菜谱中包含图片，文字等等复合信息，如何处理？
        # （？）如果其中有一个处理失败且又写进了数据库，该如何回滚？
        cookbook = Cookbook()
        args = self.parser.parse_args()
        imgfile = args.get('imgfile')
        z = args.get('step')
        imgfileUrl = upload_file(imgfile)
        cookbook.imageUrl = imgfileUrl
        cookbook.from_dict(args)
        cookbook.users = g.current_user
        db.session.add(cookbook)
        db.session.commit()
        return marshal(cookbook,cookbook_fields)