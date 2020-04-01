#!/usr/bin/python3
"""This is the user class"""
from models.base_model import BaseModel, Base
from os import getenv
import sqlalchemy import Column, String


class User(BaseModel):
    """This is the class for user
    Attributes:
        email: email address
        password: password for you login
        first_name: first name
        last_name: last name
    """
    if models.storage_t =='db':
        __tablename__ = 'users'
        email = Column(String(128), nullable=False)
        password = Column(String(128), nullable=False)
        first_name = Column(String(128))
        last_name = Column(String(128))
    else:
        email = ""
        password = ""
        first_name = ""
        last_name = ""
