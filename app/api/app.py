from flask import Blueprint
from flask_restful import Api

bp = Blueprint('api',__name__)
api = Api(bp)




from app.api.resources.ping import Ping
from app.api.resources.users import UserAPI,UserListAPI
from app.api.resources.tokens import Token
from app.api.resources.cookbooks import CookbookAPI,CookbookListAPI
from app.api.resources.schedules import ScheduleAPI,ScheduleListAPI

#（？）解读add_resource +
    # add_resource(resource, *urls, **kwargs)
    # urls:一个resource可匹配多个路由（urls）
    # api.add_resource(Ping,'/','/ping')
# （？）这里的endpoint是什么？ +
# 沙雕了，这是指定endpoint名字，格式化响应资源的时候可以用fields.Url('端点名')来引用这条url
api.add_resource(Ping,'/ping')

# User
api.add_resource(UserListAPI, '/users', endpoint='users')
api.add_resource(UserAPI, '/users/<int:id>')

# 获取token
api.add_resource(Token,'/tokens',endpoint='tokens')

# cookbook
api.add_resource(CookbookListAPI,'/cookbooks',endpoint='cookbooks')
api.add_resource(CookbookAPI,'/cookbooks/<int:id>',endpoint='cookbook')

# Schedule
api.add_resource(ScheduleListAPI,'/schedules',endpoint='schedules')
api.add_resource(ScheduleAPI,'/schedules/<int:id>',endpoint='schedule')

