import json
from flask import Blueprint, render_template, request

from booking.dto.request.room.add_room import AddRoomRequest
from booking.exception.errors import ValidationError
from booking.repositories.room import RoomRepository
from booking.usecases.room.add_room import AddRoomUseCase

room_blueprint = Blueprint('room_blueprint', __name__)

@room_blueprint.route('/')
def index():
    return [{"id": 1, "name": "Room #1"}]

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
    

    print(res.room_id)
    return req.room_type
