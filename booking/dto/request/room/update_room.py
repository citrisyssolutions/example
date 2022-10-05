import dataclasses

from entities.room_type import RoomType
from .ibase import IBaseRequest

@dataclasses.dataclass
class UpdateRoomRequest(IBaseRequest):
    room_type: RoomType
    room_name: str

    def __post_init__(self):
        
        if not self.room_name:
            
            raise ValueError("Room Name required")
            