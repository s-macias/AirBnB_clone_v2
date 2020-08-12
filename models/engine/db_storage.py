#!/usr/bin/python3
""" State Module for HBNB project """
from sqlalchemy import Column, Integer, String, ForeignKey
from sqlalchemy.orm import relationship
from sqlalchemy import create_engine
from models.base_model import BaseModel, Base
from models.user import User
from models.state import State
from models.city import City
from models.amenity import Amenity
from models.place import Place
from models.review import Review
from os import getenv
class DBStorage:
    """Database"""
    __engine = None
    __session = None
    def __init__(self):
        """Initializes DBStorage class"""
        user = getenv('HBNB_MYSQL_USER')
        pwd = getenv('HBNB_MYSQL_PWD')
        host = getenv('HBNB_MYSQL_HOST')
        db = getenv('HBNB_MYSQL_DB')
        self.__engine = create_engine(
            'mysql+mysqldb://{}:{}@localhost/{}'.format(
                user, pwd, host, db, pool_pre_ping=True))
        if getenv('HBNB_ENV') == "test":
                Base.metadata.drop_all(self.__engine)
    def all(self, cls=None):
        """"""
        dict_obj = {}
        if cls is None:
            for obj in self.__session.query(
                    User, State, City, Amenity, Place, Review).all():
                key = "{}.{}".format(obj.__class__.__name__, obj.id)
                dict_obj[key] = obj
            else:
                for obj in self.__session.query(cls.__name__).all():
                    key = "{}.{}".format(obj.__class__.__name__, obj.id)
                    dict_obj[key] = obj
            return dict_obj
    def new(self, obj):
        """add the object to the current database session"""
        self.__session.add(obj)
    def save(self):
        """commit all changes of the current database session"""
        self.__session.commit()
    def delete(self, obj=None):
        """ delete from the current database session"""
        self.__session.delete(obj)
    def reload(self):
        """
        create all tables in the database feature
        of SQLAlchemy and create a new session
        """
        Base.metadata.create_all(self.__engine)
        session_factory = sessionmaker(
                bind=self.__engine, expire_on_commit=False)
        Session = scoped_session(session_factory)
        self.__session = Session()
    def close(self):
        """"""
        self.__session.remove()
