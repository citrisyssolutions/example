from flask import Blueprint, render_template

room_blueprint = Blueprint('room_blueprint', __name__)

@room_blueprint.route('/')
def index():
    return [{"id": 1, "name": "Room #1"}]
