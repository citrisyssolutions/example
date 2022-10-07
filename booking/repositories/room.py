from abc import ABCMeta, abstractmethod
from booking.dto.request.room.add_room import AddRoomRequest
from booking.dto.request.room.ibase import IBaseRequest
from booking.dto.response.room.add_room import AddRoomResponse

from booking.entities.room import Room
from .ibase import IBaseRepository

class RoomRepository(IBaseRepository):
    def insert(self, add_room_req: AddRoomRequest) -> Room:
        new_room = Room(
            room_name=add_room_req.room_name,
            room_type=add_room_req.room_type
        )
        self.session.add(new_room)
        self.session.commit()
        self.session.flush()
        print(new_room)
        return new_room

    def update(self, req: AddRoomRequest) -> int:
        raise NotImplementedError()
