from flask import Blueprint, render_template

static_blueprint = Blueprint('static_blueprint', __name__)

@static_blueprint.route('/')
def index():
    return render_template("index.html")

@static_blueprint.route('/rooms')
def room():
    return render_template("room.html")

@static_blueprint.route('/contact')
def contact():
    return render_template("contact.html")
