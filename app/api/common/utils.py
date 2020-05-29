from flask_restful import Resource,fields,marshal_with,reqparse
from werkzeug.utils import secure_filename
from flask import current_app,request
from werkzeug.datastructures import FileStorage
from datetime import datetime
import uuid
import os

ALLOWED_EXTENSIONS = {'png', 'jpg', 'jpeg'}



def upload_cookbooks_imgfile(imgfile):
    subdir = os.path.join(current_app.config['UPLOAD_FOLDER'],'cookbooks')
    uuidname = str(uuid.uuid3(uuid.NAMESPACE_DNS,imgfile.name+str(datetime.now())))
    imgfile.save(
        os.path.join(subdir,uuidname)
    )

# def allowed_file(filename):
#     return '.' in filename and \
#            filename.rsplit('.', 1)[1].lower() in ALLOWED_EXTENSIONS


# # 上传头像
# class Avatar(Resource):
#     def post(self):
#         parser = reqparse.RequestParser()
#         parser.add_argument('pic',type=FileStorage,location='files')
#         args = parser.parse_args()
#         file = args.get('pic')
#         file.save(
#             os.path.join(current_app.config['UPLOAD_FOLDER'],file.name)
#         )
#         z = file.name
#         return 'z',200

