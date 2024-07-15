from flask_sqlalchemy import SQLAlchemy
from sqlalchemy.orm import DeclarativeBase

class Base(DeclarativeBase):
    """Base class for database models.

    This class serves as the base for all database models in the application.

    Args:
        DeclarativeBase (type): The base class for declarative models.
    """
    pass


db = SQLAlchemy(model_class=Base)