import os

from PIL import Image
from ultralytics import YOLO


def detect_objects_on_image(buf):
    """
    Function receives an image,
    passes it through YOLOv8 neural network
    and returns an array of detected objects
    and their bounding boxes
    :param buf: Input image file stream
    :return: Array of bounding boxes in format 
    [[x1,y1,x2,y2,object_type,probability],..]
    """
    model_path = os.path.join(os.path.dirname(__file__), 'best.pt')
    model = YOLO(model_path)
    results = model.predict(buf)
    result = results[0]
    output = []
    for box in result.boxes:
        x1, y1, x2, y2 = [
            round(x) for x in box.xyxy[0].tolist()
        ]
        class_id = box.cls[0].item()
        prob = round(box.conf[0].item(), 2)
        output.append([
            x1, y1, x2, y2, result.names[class_id], prob
        ])
    return output


def extract_spine_images(image, bounding_boxes):
    spine_images = []

    for bbox in bounding_boxes:
        x1, y1, x2, y2 = bbox

        # Crop the spine head image from the original image
        # Image.crop(image, (x1, y1, x2, y2))
        spine_image = image.crop((x1, y1, x2, y2))

        spine_images.append(spine_image)
    return spine_images
