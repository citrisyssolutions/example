import dataclasses
from application.exception.errors import ValidationError

from application.entities.room_type import RoomType
from application.dto.request.ibase import IBaseRequest

DEFAULT_ROOM_TYPES = ["Delux", "Ordinary"]

@dataclasses.dataclass
class GetRoomRequest(IBaseRequest):
    pass