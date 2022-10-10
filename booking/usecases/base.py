from abc import ABCMeta, abstractmethod
from dto.request.room.ibase import BaseRequest, IBaseRequest
from dto.response.room.add_room import InsertRoomResponse
from entities.ibase import IBaseEntity

from entities.room import Room
from repositories.ibase import IBaseRepository

class IBaseUseCase(metaclass=ABCMeta):
    def __init__(self, repo: IBaseRepository) -> None:
        pass

    @abstractmethod
    def handle(self, req: IBaseRequest) -> IBaseEntity:
        raise NotImplementedError()