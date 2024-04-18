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
    cities = relationship("City", cascade="all, delete", backref="state")


    @property
    def cities(self):
        """getter attribute cities that returns
        the list of City instances with
        state_id equals to the current State.id"""
        result = []
        from models import storage
        cities = storage.all(City)
        for city in cities.values():
            if city.state_id == self.id:
                result.append(city)
        return result
