

from booking.dto.request.room.add_room import AddRoomRequest
from booking.entities.room import Room
from booking.usecases.base import IBaseUseCase
from booking.repositories.room import RoomRepository


class AddRoomUseCase(IBaseUseCase):
    def __init__(self, repo: RoomRepository):
        super().__init__()
        self.repo = repo
        self.logger.info("Adding new room")

    def handle(self, request: AddRoomRequest) -> Room:
        try:
            room = self.repo.insert(request)
        except Exception as _e:
            raise Exception(f"Can't insert, reason: {_e}")
        return room