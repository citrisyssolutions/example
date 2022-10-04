from abc import ABCMeta, abstractmethod
from dto.request.room.ibase import IBaseRequest

from entities.room import Room

class IBaseRepository(metaclass=ABCMeta):
    @abstractmethod
    def insert(self, req: IBaseRequest) -> Room:
        raise NotImplementedError()

    @abstractmethod
    def update(self, req: IBaseRequest) -> int:
        raise NotImplementedError()