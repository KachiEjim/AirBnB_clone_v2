#!/usr/bin/python3
from os import getenv

class DBStorage:
    """Defines DB storage class"""
    __engine = None
    __session = None

    def __init__(self):
        """Initializes the DBstorage class"""

        from sqlalchemy import create_engine
        from models.base_model import Base
        from models.user import User
        from models.state import State
        from models.city import City
        from models.place import Place
        from models.amenity import Amenity
        from models.review import Review

        mysql_user = getenv('HBNB_MYSQL_USER')
        mysql_pwd = getenv('HBNB_MYSQL_PWD')
        mysql_host = getenv('HBNB_MYSQL_HOST', default='localhost')
        mysql_db = getenv('HBNB_MYSQL_DB')

        loginStr = f"mysql+mysqldb://{mysql_user}:{mysql_pwd}@\
            {mysql_host}/{mysql_db}"
        self.__engine = create_engine(loginStr, pool_pre_ping=True)
        if getenv('HBNB_ENV') == 'test':
            Base.metadata.drop_all(bind=self.__engine)

    def all(self, cls=None):
        """query on the current database session (self.__session) all objects
        depending of the class name (argument cls)"""

        from models.base_model import BaseModel
        from models.user import User
        from models.state import State
        from models.city import City
        from models.place import Place
        from models.amenity import Amenity
        from models.review import Review

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
        """Reloads objects from the database"""

        from sqlalchemy.orm import sessionmaker, scoped_session
        from models.base_model import Base

        Base.metadata.create_all(self.__engine)
        Session_maker = sessionmaker(bind=self.__engine,
                                     expire_on_commit=False)
        self.__session = scoped_session(Session_maker)()

    def close(self):
        """closes the working SQLAlchemy session"""
        self.__session.close()
