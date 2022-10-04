

from dto.request.room.get_room import GetRoomRequest
from exception.errors import ValidationError
from entities.room import Room
from repositories.room import RoomRepository


class GetRoomUseCase:
    def __init__(self, repo: RoomRepository):
        self.repo = repo
    
    def handle(self, request: GetRoomRequest) -> Room:
        try:
            if request is None:
                room_data = self.repo.get()
            else:
                room_data = self.repo.get_name(request.room_name)
        except Exception as _e:
            if isinstance(_e,ValidationError):
                raise _e

            raise Exception("Can't insert")
        return room_data