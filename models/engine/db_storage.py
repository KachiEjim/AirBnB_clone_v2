#!/usr/bin/python3
"""database storage engine"""
import os
from sqlalchemy import create_engine
from sqlalchemy.orm import scoped_session, sessionmaker
from models.base_model import BaseModel, Base
from models.user import User
from models.state import State
from models.city import City
from models.amenity import Amenity
from models.place import Place
from models.review import Review



class DBStorage:
    """Defines DB storage class"""
    __engine = None
    __session = None

    def __init__(self):
        """initilazes DBstorage Class"""
        hbnb_dev = os.getenv('HBNB_ENV')
        hbnb_dev_db = os.getenv('HBNB_MYSQL_DB')
        hbnb_dev_user = os.getenv('HBNB_MYSQL_USER')
        hbnb_dev_pwd = os.getenv('HBNB_MYSQL_PWD')
        hbnb_dev_host = os.getenv('HBNB_MYSQL_HOST')        

        self.__engine = create_engine('mysql+mysqldb://{}:{}@{}/{}'
                                      .format(hbnb_dev_user, hbnb_dev_pwd,
                                              hbnb_dev_host, hbnb_dev_db),
                                      pool_pre_ping=True)

        Session = sessionmaker(bind=self.__engine, expire_on_commit=False)
        self.__session = scoped_session(Session())
        if os.getenv('HBNB_ENV') == 'test':
            Base.metadata.drop_all(bind=self.__engine)

    def all(self, cls=None):
        """query on the current database session (self.__session) all objects
        depending of the class name (argument cls)"""
        classes = {
                    'BaseModel': BaseModel, 'User': User, 'Place': Place,
                    'State': State, 'City': City, 'Amenity': Amenity,
                    'Review': Review
                  }
        if cls is not None:
            results = self.__session.query(classes[cls]).all()
        else:
            results = []
            for cls in classes.values():
                results.extend(self.__session.query(cls).all())
        return results
    
    def new(self, obj):
        """add the object to the current
        database session (self.__session)"""
        if obj is not None:
            try:
                self.__session.add(obj)
                self.__session.flush()
                self.__session.refresh(obj)
            except Exception as a:
                self.__session.rollback()
                raise a
    
    def save(self):
        '''commit all changes of the current db session'''
        self.__session.commit()

    def delete(self, obj=None):
        """Deletes an object from the database"""
        if obj is not None:
            self.__session.delete(obj)

    def reload(self):
        """"""
        Base.metadata.create_all(self.__engine)
        Session_maker = sessionmaker(bind=self.__engine,
                                     expire_on_commit=False)
        self.__session = scoped_session(Session_maker)()



    def close(self):
        """closes the working SQLAlchemy session"""
        self.__session.close()
