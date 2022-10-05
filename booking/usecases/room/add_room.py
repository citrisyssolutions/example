

from traitlets import ValidateHandler
from dto.request.room.add_room import AddRoomRequest
from entities.room import Room
from repositories.room import RoomRepository
from exception.errors import ValidationError


class AddRoomUseCase:
    def __init__(self, repo: RoomRepository):
        self.repo = repo

    def handle(self, request: AddRoomRequest) -> Room:
        is_room_exist = self.repo.get_room(request.room_name)
        
        if is_room_exist == {}:
           room = self.repo.insert(request)
        else:
           raise ValidationError("data exists")
       
        return Room(
            room_id=room["room_id"],
            room_type=room["room_type"],
            room_name=room["room_name"]
        )