from flask import jsonify
from flask_restful import Resource


class Ping(Resource):
    def get(self):
        return jsonify('hello')