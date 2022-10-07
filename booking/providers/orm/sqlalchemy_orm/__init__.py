import sqlalchemy
from sqlalchemy import create_engine, MetaData
from sqlalchemy.orm import relationship, backref, sessionmaker, registry
from sqlalchemy.ext.declarative import declarative_base

from booking.entities import Room
from booking.providers.db import IDBProvider

from booking.providers.orm.sqlalchemy_orm.models import room, metadata

class SQLAlchemyORM:

    __instance = None

    @staticmethod
    def getInstance():
      """ Static access method. """
      if SQLAlchemyORM.__instance == None:
         SQLAlchemyORM()
      return SQLAlchemyORM.__instance


    def __init__(self, provider: IDBProvider):
        is_first = True
        if SQLAlchemyORM.__instance != None:
            is_first = False
        else:
            SQLAlchemyORM.__instance = self
        # super().__init__(provider)
        self.connection_string = provider.connection_string
        self.mapper_registry = registry()
        self.engine = create_engine(self.connection_string)
        metadata.create_all(self.engine)
        self.session = sessionmaker(bind=self.engine)()
        if is_first:
            self.mapping_registry()

    def mapping_registry(self):
        self.mapper_registry.map_imperatively(Room, room)


    def get_session(self):
        print("Initializing db...")
        return self.session


    