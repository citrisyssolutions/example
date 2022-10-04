from abc import ABCMeta, abstractmethod
from dto.request.room.add_room import AddRoomRequest
from dto.request.room.ibase import IBaseRequest
from dto.response.room.add_room import AddRoomResponse
import os
import json

from entities.room import Room
from .ibase import IBaseRepository

DATAFILE= "data.json"

class RoomRepository(IBaseRepository):
    def __init__(self):
        self.data =[]
        if os.path.exists(DATAFILE):
           with open (DATAFILE) as cf:
                 self.data = json.load(cf)

    def insert(self, add_room_req: AddRoomRequest) -> Room:
        res = {
            "room_id": len(self.data)+1,
            "room_name": add_room_req.room_name,
            "room_type": add_room_req.room_type
        }

        self.data.append(res)
        with open (DATAFILE,"w") as a:
            a.write(json.dumps(self.data))
        return res

    def get(self):
        return self.data
  
    def update(self, req: AddRoomRequest) -> int:
        raise NotImplementedError()

    def get_by_name (self,room_name:str):
        data ={}
       
        for room in self.data:
            if room['room_name']== room_name: 
                return room
        return data