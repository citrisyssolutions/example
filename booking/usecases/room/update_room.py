

from dto.request.room.update_room import UpdateRoomRequest
from exception.errors import ValidationError
from entities.room import Room
from repositories.room import RoomRepository


class UpdateRoomUseCase:
    def __init__(self, repo: RoomRepository):
        self.repo = repo
    
    def handle(self, request: UpdateRoomRequest) -> Room:
        try:
            room_exist=self.repo.get_room(request.room_name)
            print(f"Is Room Exists=>{room_exist}")
            if room_exist !={}:
               room = self.repo.update(request)
            else:
                raise ValidationError("Data Not Exist")
        except Exception as _e:
            if isinstance(_e,ValidationError):
                raise _e

            raise Exception("Can't insert")
        return Room(
            room_id=room["room_id"],
            room_type=room["room_type"],
            room_name=room["room_name"]
        )