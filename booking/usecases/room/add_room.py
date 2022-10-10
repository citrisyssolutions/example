

from dto.request.room.add_room import AddRoomRequest
from entities.room import Room
from repositories.room import RoomRepository
from exception.errors import ValidationError


class AddRoomUseCase:
    def __init__(self, repo: RoomRepository):
        self.repo = repo

    def handle(self, request: AddRoomRequest) -> Room:
        print("with try")
        is_room_exist= self.repo.get_by_name(request.room_name)
        if is_room_exist =={}:
            room = self.repo.insert(request)
            print("handle")
        else:
            raise ValidationError("data exists")
        # except:
        #     raise ValidationError("Can't insert")
        return room