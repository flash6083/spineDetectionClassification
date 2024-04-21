from flask import Blueprint, request

from app.controllers.objectDetect_controller import detect

objectDetect_blueprint = Blueprint('detect', __name__, url_prefix='/detect')


@objectDetect_blueprint.route('/', methods=['GET'])
def index():
    return detect()
