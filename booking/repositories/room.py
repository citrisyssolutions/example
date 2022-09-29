from abc import ABCMeta, abstractmethod
from booking.dto.request.room.add_room import AddRoomRequest
from booking.dto.request.room.ibase import IBaseRequest
from booking.dto.response.room.add_room import AddRoomResponse

from booking.entities.room import Room
from .ibase import IBaseRepository

class RoomRepository(IBaseRepository):
    def insert(self, add_room_req: AddRoomRequest) -> Room:
        res = {
            "room_id": 1,
            "room_name": add_room_req.room_name,
            "room_type": add_room_req.room_type
        }
        return res

    def update(self, req: AddRoomRequest) -> int:
        raise NotImplementedError()
