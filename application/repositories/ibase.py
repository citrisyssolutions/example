from abc import ABCMeta, abstractmethod
from application.dto.request.room.ibase import IBaseRequest
from application.providers.orm.sqlalchemy_orm import SQLAlchemyORM
from application.config import Config


from application.entities.room import Room

class IBaseRepository(metaclass=ABCMeta):
    def __init__(self):
        orm = SQLAlchemyORM(Config.DB_SOURCE)
        self.session = orm.get_session()

    @abstractmethod
    def insert(self, req: IBaseRequest) -> Room:
        raise NotImplementedError()

    @abstractmethod
    def update(self, req: IBaseRequest) -> int:
        raise NotImplementedError()