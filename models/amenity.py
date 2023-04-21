#!/usr/bin/python3
<<<<<<< HEAD
""" State Module for the HBNB project """
from os import getenv
from models.base_model import BaseModel, Base
from sqlalchemy import Column, String
from sqlalchemy.orm import relationship


class Amenity(BaseModel, Base):
    """class for amenities"""
    __tablename__ = 'amenities'
    if getenv("HBNB_TYPE_STORAGE") == "db":
        name = Column(String(128), nullable=False)
        place_amenities = relationship("Place", secondary="place_amenity",
                                       back_populates="amenities")
    else:
        name = ""
=======
""" State Module for HBNB project """
from models.base_model import BaseModel


class Amenity(BaseModel):
    name = ""
>>>>>>> cbaedfdd56b6e339a0af634cae7c81972e647043
