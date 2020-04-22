#!/usr/bin/python3
"""This is the city class"""
import models
from models.base_model import BaseModel, Base
import sqlalchemy
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy import Column, String, DateTime
from sqlalchemy import ForeignKey
from sqlalchemy.orm import relationship
from models.place import Place


class City(BaseModel, Base):
    """This is the class for City
    Attributes:
        state_id: The state id
        name: input name
    """
    if models.storage_t == 'db':
        __tablename__ = 'cities'
        name = Column(String(128), nullable=False)
        state_id = Column(String(60), ForeignKey('states.id'), nullable=False)
        places = relationship("Place", backref="cities")
    else:
        state_id = ""
        name = ""
