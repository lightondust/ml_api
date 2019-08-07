import modules
import io
import os
from google.cloud import vision
from google.cloud.vision import types


client = vision.ImageAnnotatorClient()


def label_image(client, image_path, label_type='label'):
    # Loads the image into memory
    with io.open(image_path, 'rb') as image_file:
        content = image_file.read()

    image = types.Image(content=content)

    if label_type == 'label':
        # Performs label detection on the image file
        response = client.label_detection(image=image)
        labels = response.label_annotations
    elif label_type == 'object':
        response = client.object_localization(image=image)
        labels = response.localized_object_annotations
    elif label_type == 'face':
        response = client.face_detection(image=image)
        labels = response.face_annotations
    elif label_type == 'web':
        response = client.web_detection(image=image)
        labels = response.web_detection
    else:
        return None

    return labels


