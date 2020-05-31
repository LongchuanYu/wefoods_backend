from flask import Flask
from config import Config
from app.api.app import bp
from app.extensions import db,CORS,migrate

def create_app(config_class=Config):
    app = Flask(__name__,static_folder='../upload')
    app.config.from_object(config_class)
    app.url_map.strict_slashes = False
    app.register_blueprint(bp, url_prefix='/api')


    CORS(app)
    db.init_app(app)
    migrate.init_app(app,db)

    return app
