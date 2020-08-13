#!/usr/bin/python3
""" Place Module for HBNB project """
import models
from models.base_model import BaseModel, Base
from models.review import Review
from models.city import City
from sqlalchemy import Column, Integer, String, Float, ForeignKey


class Place(BaseModel, Base):
    """ A place to stay """
    __tablename__ = "places"
    city_id = Column(String(60), ForeignKey("cities.id"), nullable=False)
    user_id = Column(String(60), ForeignKey("users.id"), nullable=False)
    name = Column(String(128), nullable=False)
    description = Column(String(1024), nullable=True)
    number_rooms = Column(Integer, default=0, nullable=False)
    number_bathrooms = Column(Integer, default=0, nullable=False)
    max_guest = Column(Integer, default=0, nullable=False)
    price_by_night = Column(Integer, default=0, nullable=False)
    latitude = Column(Float, nullable=True)
    longitude = Column(Float, nullable=True)
    amenity_ids = []

    if models.storage.__class__.__name__ == "DBStorage":
        Place.reviews = relationship('Review',
                                     cascade='all, delete', backref='place')
    else:
        @property
        def reviews(self):
            """Getter for Review instances"""
            list_review = []
            dict_review = models.storage.all(Review)
            for key, review in dict_review.items():
                if review.place_id == self.id:
                    list_review.append(review)
            return list_review
