

from application.dto.request.room.get_room_request import GetRoomRequest
from application.entities.room import Room
from application.usecases.base import IBaseUseCase
from application.repositories.room import RoomRepository


class GetAllRoomUseCase(IBaseUseCase):
    def __init__(self, repo: RoomRepository):
        super().__init__()
        self.repo = repo
        self.logger.info("Adding new room")

    def handle(self, request: GetRoomRequest) -> Room:
        try:
            room = self.repo.select(request)
        except Exception as _e:
            raise Exception(f"Can't insert, reason: {_e}")
        return room