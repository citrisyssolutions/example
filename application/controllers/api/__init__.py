from flask import Blueprint, render_template
from .room_blueprint import room_blueprint



api_blueprint = Blueprint('api_blueprint', __name__)
api_blueprint.register_blueprint(
    room_blueprint,
    url_prefix="/room"
)    

@api_blueprint.route('/')
def index():
    return "ok"

@api_blueprint.route('/ping')
def ping():
    return "pong"

