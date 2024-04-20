#!/usr/bin/python3
""" holds class User"""
from models.base_model import BaseModel
from os import getenv
import sqlalchemy
from sqlalchemy import Column, String


class User(BaseModel):
    """Representation of a user """
    pass