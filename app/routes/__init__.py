# app/routes/__init__.py
from .objectDetect_route import objectDetect_blueprint

blueprints = [
    objectDetect_blueprint
]


def register_blueprints(app):
    for blueprint in blueprints:
        app.register_blueprint(blueprint)
