import json
import os
from flask import Blueprint, render_template, request
from flask import jsonify
from dto.request.room.add_room import AddRoomRequest
from exception.errors import ValidationError
from repositories.room import RoomRepository
from usecases.room.add_room import AddRoomUseCase


room_blueprint = Blueprint('room_blueprint', __name__)

DATA_FILE ="/tmp/data.json"
@room_blueprint.route('/', methods=["GET"])
def index():
     data = []
     if os.path.exists(DATA_FILE):
        data = json.load(open(DATA_FILE, "r"))
     print(data)
     return data

   

@room_blueprint.route("/", methods=["POST"])
def create_room():
    data = json.loads(request.get_data())
    try:
        req = AddRoomRequest(**data)
    except:
        raise ValidationError("Invalid input")
    repo = RoomRepository()
    create_room = AddRoomUseCase(repo)
    res = create_room.handle(req)
  
    return jsonify(res)

