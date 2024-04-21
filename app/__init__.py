from flask import Flask
from flask_cors import CORS  # Import CORS

from app.routes import register_blueprints
from app.utils.logger import configure_logger

logger = configure_logger()


def create_app():
    app = Flask(__name__)
    CORS(app)
    register_blueprints(app)
    return app
