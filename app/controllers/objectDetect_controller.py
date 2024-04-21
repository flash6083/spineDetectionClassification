import json

from flask import Response, request
from PIL import Image

from app.utils.helper import detect_objects_on_image

# Get all users


def detect():
    buf = request.files["image_file"]
    boxes = detect_objects_on_image(Image.open(buf.stream))
    return Response(
        json.dumps(boxes),
        mimetype='application/json'
    )
