#!/usr/bin/python3
""" State Module for HBNB project """
from models.base_model import BaseModel, Base
from models.city import City
from sqlalchemy import Column, String, ForeignKey
from sqlalchemy.orm import relationship


class State(BaseModel, Base):
    """ State class """
    __tablename__ = 'states'
    name = Column(String(128), nullable=False)
    cities = relationship('City', backref='state',
                              cascade='all, delete, delete-orphan')

    from models import storage_t
    if storage_t != 'db':   
        @property
        def cities(self):
            """getter attribute cities that returns
            the list of City instances with
            state_id equals to the current State.id"""
            result = []
            from models import storage
            temp = storage.all(City)
            for city in temp.values():
                if city.state_id == self.id:
                    result.extend(city)
            return result
