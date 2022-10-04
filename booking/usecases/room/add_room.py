

from exception.errors import ValidationError
from dto.request.room.add_room import AddRoomRequest
from entities.room import Room
from repositories.room import RoomRepository


class AddRoomUseCase:
    def __init__(self, repo: RoomRepository):
        self.repo = repo
    
    def handle(self, request: AddRoomRequest) -> Room:
        try:
            room_exist=self.repo.get_name(request.room_name)
            print(f"Is Room Exists=>{room_exist}")
            if room_exist =={}:
               room = self.repo.insert(request)

               print(room)
            else:
                raise ValidationError("Data Exist")
        except Exception as _e:
            if isinstance(_e,ValidationError):
                raise _e

            raise Exception("Can't insert")
        return Room(
            room_id=room["room_id"],
            room_type=room["room_type"],
            room_name=room["room_name"]
        )