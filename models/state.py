#!/usr/bin/python3
""" State Module for HBNB project """
import models
from models.base_model import BaseModel, Base
from models.user import User
from models.city import City
from models.amenity import Amenity
from models.place import Place
from models.review import Review
from sqlalchemy import Column, Integer, String, ForeignKey
from sqlalchemy.orm import relationship
class State(BaseModel, Base):
    """ State class """
    __tablename__ = "states"
    name = Column(String(128), nullable=False)
    cities = relationship('City', cascade='all, delete', backref='state')
    @property
    def cities(self):
        list_cities = []
        dict_cities = models.storage.all(City)
        for key, city in dict_cities.items():
            if city.state_id == self.id:
                list_cities.append(city)
        return list_cities
