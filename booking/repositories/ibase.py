from abc import ABCMeta, abstractmethod
from booking.dto.request.room.ibase import IBaseRequest
from booking.providers.orm.sqlalchemy_orm import SQLAlchemyORM
from booking.providers.db.sqlite_db_source import SQLiteDBSource


from booking.entities.room import Room

class IBaseRepository(metaclass=ABCMeta):
    def __init__(self):
        orm = SQLAlchemyORM(SQLiteDBSource)
        self.session = orm.get_session()

    @abstractmethod
    def insert(self, req: IBaseRequest) -> Room:
        raise NotImplementedError()

    @abstractmethod
    def update(self, req: IBaseRequest) -> int:
        raise NotImplementedError()