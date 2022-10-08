from dataclasses import dataclass

from application.entities.room_type import RoomType

@dataclass
class Room:
    room_type: RoomType
    room_name: str
    id: int = None

