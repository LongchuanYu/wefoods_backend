from flask import Flask
from config import Config
from flask_cors import CORS
from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate
from app.api.app import bp
db = SQLAlchemy()
migrate = Migrate()

def create_app(config_class=Config):
    app = Flask(__name__)
    app.config.from_object(config_class)
    app.url_map.strict_slashes = False
    app.register_blueprint(bp, url_prefix='/api')


    CORS(app)
    db.init_app(app)
    migrate.init_app(app,db)

    return app

from app import models