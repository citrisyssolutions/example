import dataclasses
from booking.exception.errors import ValidationError

from booking.entities.room_type import RoomType
from booking.dto.request.room.ibase import IBaseRequest

DEFAULT_ROOM_TYPES = ["Delux", "Ordinary"]

@dataclasses.dataclass
class AddRoomRequest(IBaseRequest):
    room_type: RoomType
    room_name: str

    def __post_init__(self):
        if not self.room_type:
            raise ValueError("Room type required")
        elif not self.room_name:
            raise ValueError("Room name required")
        self.__validate_roomtype()
        self.__validate_room_name()


    def __validate_roomtype(self):
        if self.room_type not in DEFAULT_ROOM_TYPES:
            raise ValidationError("Invalid room type")
    
    def __validate_room_name(self):
        if type(self.room_name) != str:
            raise ValidationError("Room name must be string")


if __name__ == "__main__":
    rr = AddRoomRequest("Delux", "Delux")      
    print(rr)      