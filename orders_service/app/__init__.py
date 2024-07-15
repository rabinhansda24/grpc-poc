from flask import Flask, request, jsonify
import grpc
from flasgger import Swagger
from sqlalchemy import create_engine, Column, Integer, String, Float
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker

from app.config.config import get_config_by_name
from app.extentions.initialize_function import initialize_route, initialize_database, initialize_cors, initialize_logger, initialize_swagger

def create_app(config):
    app = Flask(__name__)
    app.config.from_object(get_config_by_name(config))

    initialize_database(app)
    initialize_route(app)
    initialize_cors(app)
    initialize_logger(app)
    initialize_swagger(app)

    return app

__pdoc__ = {}
__pdoc__['orders_pb2_grpc.py'] = False
__pdoc__['orders_pb2.py'] = False
__pdoc__['orders_pb2.pyi'] = False
__pdoc__['payments_pb2_grpc.py'] = False
__pdoc__['payments_pb2.py'] = False
__pdoc__['payments_pb2.pyi'] = False
__pdoc__['users_pb2_grpc.py'] = False
__pdoc__['users_pb2.py'] = False
__pdoc__['users_pb2.pyi'] = False


