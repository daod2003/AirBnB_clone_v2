#!/usr/bin/python3
"""This is the state class"""
import models
from models.base_model import BaseModel, Base
from models.city import City
from os import getenv
import sqlalchemy
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy import Column, String, DateTime
from sqlalchemy import ForeignKey
from sqlalchemy.orm import relationship


class State(BaseModel, Base):
    """This is the class for State
    Attributes:
        name: input name
    """
    __tablename__ = 'states'
    name = Column(String(128), nullable=False)
    if getenv('HBNB_TYPE_STORAGE') == 'db':
        cities = relationship('City', backref='state')

    if getenv('HBNB_TYPE_STORAGE') != "db":
        @property
        def cities(self):
            """list of city instances related to the state"""
            cityList = []
            allCities = models.storage.all(City)
            for city in allCities.values():
                if city.state_id == self.id:
                    cityList.append(city)
            return cityList
