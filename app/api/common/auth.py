from flask import g
from app.models import User
from flask_httpauth import HTTPBasicAuth,HTTPTokenAuth
from werkzeug.security import generate_password_hash, check_password_hash

basic_auth = HTTPBasicAuth()
token_auth = HTTPTokenAuth()

@basic_auth.verify_password
def verify_password(username,password):
    print('verify_password')
    user = User.query.filter_by(username=username).first()
    if not user:
        return False
    g.current_user = user
    return user.check_password_byhash(password)


@basic_auth.error_handler
def basic_auth_error():
    return 'Access Denied'


@token_auth.verify_token
def verify_token(token):
    decode_jwt = User.verify_jwt(token) if token else None
    if not decode_jwt:
        return False
    g.current_user = User.query.get(decode_jwt.get('userid'))
    return g.current_user is not None



@token_auth.error_handler
def token_auth_error():
    return 'Token verify failed'