from flask import Flask
from flasgger import Swagger

from app.db import db

from app.routes.main_route import main_route_blueprint

def initialize_route(app: Flask):
    """This function initialize routes for the application.

    Args:
        app (Flask): The application instance.
    """
    
    with app.app_context():
        app.register_blueprint(main_route_blueprint)


def initialize_database(app: Flask):
    """This function initialize database for the application.

    Args:
        app (Flask): The application instance.
    """
    
    with app.app_context():
        db.init_app(app)
        db.create_all()
        db.session.commit()


def initialize_cors(app: Flask):
    """This function initialize CORS for the application.

    Args:
        app (Flask): The application instance.
    """
    
    pass


def initialize_logger(app: Flask):
    """This function initialize logger for the application.

    Args:
        app (Flask): The application instance.
    """
    
    pass

def initialize_swagger(app: Flask):
    """This function initialize Swagger for the application.

    Args:
        app (Flask): The application instance.
    """
    
    swagger = Swagger(app)
    
    return swagger