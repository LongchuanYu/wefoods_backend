from flask_restful import Resource
from app.models import User
from flask_restful import Resource,fields,marshal_with,reqparse,inputs,marshal
from werkzeug.datastructures import FileStorage
from app.extensions import db
from app.api.common.utils import upload_cookbooks_imgfile
class CookbookAPI(Resource):
    def get(self):
        '''获取单个菜谱'''
        pass
    def post(self):
        ''''''
        pass

class CookbookListAPI(Resource):
    def __init__(self):
        self.parser = reqparse.RequestParser()
        self.parser.add_argument('imgfile',type=FileStorage,location='files')
        self.parser.add_argument('name',type=str)
        self.parser.add_argument('descript',type=str)
    def get(self):
        '''获取菜谱合集'''
        pass
    def post(self):
        '''新增菜谱'''
        # （？）菜谱中包含图片，文字等等复合信息，如何处理？
        # （？）如果其中有一个处理失败且又写进了数据库，该如何回滚？
        args = self.parser.parse_args()
        imgfile = args.get('imgfile')
        name = args.get('name')
        upload_cookbooks_imgfile(imgfile)

        return 'yes'