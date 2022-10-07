from dataclasses import dataclass

from booking.entities.room_type import RoomType

@dataclass
class Room:
    room_type: RoomType
    room_name: str
    room_id: int = None

