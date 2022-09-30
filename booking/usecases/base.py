from abc import ABCMeta, abstractmethod
from booking.dto.request.room.ibase import BaseRequest, IBaseRequest
from booking.dto.response.room.add_room import InsertRoomResponse
from booking.entities.ibase import IBaseEntity

from booking.entities.room import Room
from booking.repositories.ibase import IBaseRepository

class IBaseUseCase(metaclass=ABCMeta):
    def __init__(self, repo: IBaseRepository) -> None:
        pass

    @abstractmethod
    def handle(self, req: IBaseRequest) -> IBaseEntity:
        raise NotImplementedError()