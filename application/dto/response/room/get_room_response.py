import dataclasses

from application.entities.room_type import RoomType

@dataclasses.dataclass
class GetRoomResponse:
    data: list