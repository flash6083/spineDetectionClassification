from flask import Flask

from app.routes import register_blueprints
from app.utils.logger import configure_logger

logger = configure_logger()


def create_app():
    app = Flask(__name__)
    register_blueprints(app)
    return app
