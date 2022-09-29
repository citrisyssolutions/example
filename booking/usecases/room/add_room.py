

from booking.dto.request.room.add_room import AddRoomRequest
from booking.entities.room import Room
from booking.repositories.room import RoomRepository


class AddRoomUseCase:
    def __init__(self, repo: RoomRepository):
        self.repo = repo

    def handle(self, request: AddRoomRequest) -> Room:
        try:
            room = self.repo.insert(request)
        except:
            raise Exception("Can't insert")
        return Room(
            room_id=room["room_id"],
            room_type=room["room_type"],
            room_name=room["room_name"]
        )