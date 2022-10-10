from dataclasses import dataclass

from entities.room_type import RoomType

@dataclass
class Room:
    room_type: RoomType
    room_name: str
    room_id: int = None

