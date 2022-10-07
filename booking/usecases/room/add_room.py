

from booking.dto.request.room.add_room import AddRoomRequest
from booking.entities.room import Room
from booking.repositories.room import RoomRepository


class AddRoomUseCase:
    def __init__(self, repo: RoomRepository):
        self.repo = repo

    def handle(self, request: AddRoomRequest) -> Room:
        try:
            room = self.repo.insert(request)
        except Exception as _e:
            raise Exception(f"Can't insert, reason: {_e}")
        return room