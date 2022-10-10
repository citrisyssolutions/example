import os
import json
import os
from flask import Blueprint, render_template, request
from flask import jsonify
from dto.request.room.add_room import AddRoomRequest
from exception.errors import ValidationError
from repositories.room import RoomRepository
from usecases.room.add_room import AddRoomUseCase
from usecases.room.update_room import UpdateRoomUseCase
from dto.request.room.update_room import UpdateRoomRequest
from dto.request.room.get_room import GetRoomRequest
from usecases.room.get_room import GetRoomUseCase


room_blueprint = Blueprint('room_blueprint', __name__)

@room_blueprint.route("/all",methods=["GET"])
def get_all():
    repo = RoomRepository()
    get_room = GetRoomUseCase(repo)
    res = get_room.handle(None)
    return jsonify(res)

@room_blueprint.route("/",methods=["GET"])
def get_room():
    data = json.loads(request.get_data())
    print(data,type(data))
    try:
        req = GetRoomRequest(**data)
    except:
        raise ValidationError("Invalid input")
    repo = RoomRepository()
    get_room = GetRoomUseCase(repo)
    res = get_room.handle(req)
    return jsonify(res)

   

@room_blueprint.route("/", methods=["POST"])
def create_room():
    print("requestdata:",request.get_data(),type(request.get_data()))
    data = json.loads(request.get_data())
    print(data,type(data))
    try:
        req = AddRoomRequest(**data)
        print("helloi",req,type(req))

    except: 
        raise ValidationError("Invalid input")
    repo = RoomRepository()
    print("repo",repo)
    create_room = AddRoomUseCase(repo)
    res = create_room.handle(req)
  
    return jsonify(res)
@room_blueprint.route("/", methods=["PUT"])
def update_room():
    print("requestdata:",request.get_data(),type(request.get_data()))
    data = json.loads(request.get_data())
    print(data,type(data))
    try:
        req = UpdateRoomRequest(**data)
    except:
        raise ValidationError("Invalid input")
    repo = RoomRepository()
    print("repo",repo)
    update_room = UpdateRoomUseCase(repo)
    res = update_room.handle(req)
    return jsonify(res)

    

