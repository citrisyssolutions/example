from abc import ABCMeta, abstractmethod
from application.dto.request.room.ibase import IBaseRequest
from application.entities.ibase import IBaseEntity

from application.entities.room import Room
from application.repositories.ibase import IBaseRepository
from application.providers.log import LogProvider

class IBaseUseCase(metaclass=ABCMeta):
    def __init__(self, repo: IBaseRepository = None) -> None:
        self.logger = LogProvider().get_logger()

    @abstractmethod
    def handle(self, req: IBaseRequest) -> IBaseEntity:
        raise NotImplementedError()