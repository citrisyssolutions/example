from abc import ABCMeta, abstractmethod
from booking.dto.request.room.ibase import IBaseRequest
from booking.entities.ibase import IBaseEntity

from booking.entities.room import Room
from booking.repositories.ibase import IBaseRepository
from booking.providers.log import LogProvider

class IBaseUseCase(metaclass=ABCMeta):
    def __init__(self, repo: IBaseRepository = None) -> None:
        self.logger = LogProvider().get_logger()

    @abstractmethod
    def handle(self, req: IBaseRequest) -> IBaseEntity:
        raise NotImplementedError()