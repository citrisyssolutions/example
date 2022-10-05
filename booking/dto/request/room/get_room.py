import dataclasses

from entities.room_type import RoomType
from .ibase import IBaseRequest

@dataclasses.dataclass
class GetRoomRequest(IBaseRequest):
    room_name: str

    def __post_init__(self):
        
        if not self.room_name:
            print("post_init")
            
            raise ValueError("Room Name required")
            