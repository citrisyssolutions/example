from abc import ABCMeta, abstractmethod
from dto.request.room.add_room import AddRoomRequest
from dto.request.room.ibase import IBaseRequest
from dto.response.room.add_room import AddRoomResponse
import os
from flask import jsonify
import json
from dto.request.room.update_room import UpdateRoomRequest
from entities.room import Room
from .ibase import IBaseRepository
import sqlite3
import sqlalchemy
from sqlalchemy import Column, Integer, String, ForeignKey, Table, create_engine, MetaData
from sqlalchemy.orm import relationship, backref, sessionmaker, registry
from sqlalchemy.ext.declarative import declarative_base
from dataclasses import dataclass
from sqlalchemy import text

DATAFILE= "/tmp/data.json"

class RoomRepository(IBaseRepository):
    def __init__(self):
        # self.data =[]
        # if os.path.exists(DATAFILE):
        #    with open (DATAFILE) as cf:
        #          self.data = json.load(cf)
        self.metadata = MetaData()
        self.roomtable = Table(
                       "room",
                        self.metadata,
                        Column("room_id", Integer, primary_key=True, autoincrement=True),
                        Column("room_name", String(255)),
                        Column("room_type", String(255)))
        
        
        self.engine = create_engine("sqlite:////tmp/mydb.db")
        self.conn= self.engine.connect()
        self.metadata.create_all(self.engine)
        self.session = sessionmaker(bind=self.engine)()
        mapper_registry = registry()
        table_name = 'room'
        query = f'SELECT * FROM {table_name}'
      
        result= self.conn.execute(query)
        self.new1=[]
           
        for row in result:
            self.new1.append(dict(row))
            print(self.new1)
            print(type(self.new1))


        try:
            mapper_registry.map_imperatively(Room, self.roomtable)
        except:
            pass
        

    def insert(self, add_room_req: AddRoomRequest) -> Room:
        self.new_room = Room(
            room_name=add_room_req.room_name,
            room_type=add_room_req.room_type
        )
        result= self.session.add(self.new_room)
        print(result)
        self.session.commit()
        self.session.flush()
        return self.new_room

    def get(self):
        # table_name = 'room'
        # query = f'SELECT * FROM {table_name}'
        # result= self.conn.execute(query)
        # new1=[]
        # for row in result:
        #      new1.append(dict(row))
        #      print(new1)
        #      print(type(new1))
        return self.new1
  
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

        with open(DATAFILE,"w") as df:
            df.write(json.dumps(self.data))
        return updated_room 

    def get_by_name (self,room_name:str):
        self.data ={}
        
    
        for room in self.new1:
            if room['room_name']== room_name:
                
                return room
           
        return self.data