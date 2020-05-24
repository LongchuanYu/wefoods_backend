from flask import Blueprint
from flask_restful import Api

bp = Blueprint('api',__name__)
api = Api(bp)




from app.api.resources.ping import Ping

#（？）解读add_resource +
    # add_resource(resource, *urls, **kwargs)
    # urls:一个resource可匹配多个路由（urls）
    # api.add_resource(Ping,'/','/ping')
api.add_resource(Ping,'/ping')
