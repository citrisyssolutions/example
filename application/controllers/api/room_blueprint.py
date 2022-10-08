import json
from flask import Blueprint, render_template, request
from flask import jsonify
from application.dto.request.room.add_room import AddRoomRequest
from application.dto.response.room.add_room import AddRoomResponse
from application.exception.errors import ValidationError
from application.repositories.room import RoomRepository
from application.usecases.room.add_room import AddRoomUseCase

room_blueprint = Blueprint('room_blueprint', __name__)

@room_blueprint.route('/')
def index():
    return [{"id": 1, "name": "Room #1"}]

@room_blueprint.route("/", methods=["POST"])
def create_room():
    data = json.loads(request.get_data())
    try:
        req = AddRoomRequest(**data)
    except Exception as _e:
        raise ValidationError(f"Invalid input {_e}")
    repo = RoomRepository()
    create_room = AddRoomUseCase(repo)
    room = create_room.handle(req)
    res = AddRoomResponse(
        id=room.id,
        room_name=room.room_name,
        room_type=room.room_type
    )
    return jsonify(res)
