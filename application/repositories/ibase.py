from abc import ABCMeta, abstractmethod
from application.dto.request.ibase import IBaseRequest
from application.config import Config


from application.entities.room import Room

class IBaseRepository(metaclass=ABCMeta):
    def __init__(self):
        # orm = SQLAlchemyORM(Config.DB_SOURCE)
        orm = Config.DB
        self.session = orm.get_session()

    @abstractmethod
    def select(self, req: IBaseRequest) -> Room:
        raise NotImplementedError()


    @abstractmethod
    def insert(self, req: IBaseRequest) -> Room:
        raise NotImplementedError()

    @abstractmethod
    def update(self, req: IBaseRequest) -> int:
        raise NotImplementedError()