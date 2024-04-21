from flask import Blueprint, request

from app.controllers.objectDetect_controller import detect

objectDetect_blueprint = Blueprint('detect', __name__, url_prefix='/detect')


@objectDetect_blueprint.route('/', methods=['POST'])
def index():
    return detect()


# @objectDetect_blueprint.route('/', methods=['GET'])
# def getDetect():
#     print("I am in DETECT GET route")
#     return "Hello world!"
