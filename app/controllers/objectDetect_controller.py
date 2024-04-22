import json

from flask import Response, request
from PIL import Image

from app.utils.helper import detect_objects_on_image, extract_spine_images

# Get all users


def detect():
    buf = request.files["image_file"]
    boxes = detect_objects_on_image(Image.open(buf.stream))
    bounding_box_coords = [bbox[:4] for bbox in boxes]
    spine_images = extract_spine_images(
        Image.open(buf.stream), bounding_box_coords)
    print("The spine image is:", spine_images)
    return Response(
        json.dumps(boxes),
        mimetype='application/json'
    )
