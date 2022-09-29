import dataclasses

from booking.entities.room_type import RoomType
from .ibase import IBaseRequest

@dataclasses.dataclass
class AddRoomRequest(IBaseRequest):
    room_type: RoomType
    room_name: str

    def __post_init__(self):
        if not self.room_type:
            raise ValueError("Room type required")
        elif not self.room_name:
            raise ValueError("Room name required")