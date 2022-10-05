from abc import ABCMeta, abstractmethod
import json
import os
from dto.request.room.update_room import UpdateRoomRequest
from dto.request.room.add_room import AddRoomRequest
from dto.request.room.ibase import IBaseRequest
from dto.response.room.add_room import AddRoomResponse

from entities.room import Room
from .ibase import IBaseRepository
DATA_FILE="/tmp/data.json"
class RoomRepository(IBaseRepository):
     
    def __init__(self):
        self.data=[]
        if os.path.exists(DATA_FILE):
            with open(DATA_FILE) as a:
                self.data=json.load(a)
        print(self.data)
    def get(self):
        return self.data

    def insert(self, add_room_req: AddRoomRequest) -> Room:
        print(f"inserting =>{add_room_req.room_name}")
        res = {

            "room_id": len(self.data)+1,
            "room_name": add_room_req.room_name,
            "room_type": add_room_req.room_type
        }
        self.data.append(res)
        with open(DATA_FILE, "w") as a:
            a.write(json.dumps(self.data))
        return res

    def update(self, update_room_req: UpdateRoomRequest) -> Room:
        updated_room = {}
        room_index = -1
        print("Updating")
        for index,room in enumerate(self.data):
            if room['room_name']==update_room_req.room_name:
                print(update_room_req.room_type)
                updated_room = room
                if update_room_req.room_type is not None:
                    updated_room["room_type"] = update_room_req.room_type
                room_index = index
                break
        print(updated_room)
        self.data[room_index] = updated_room

        with open(DATA_FILE,"w") as df:
            df.write(json.dumps(self.data))
        return updated_room 

    def get_room(self, room_name: str):
        data= {}
       
        for room in self.data:
            if room['room_name'] == room_name:
               return room

        return  data