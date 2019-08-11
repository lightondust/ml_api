import os
import json
import pickle

KEY_PATH = '/home/sen/.ssh/test_machine_learning-c0d3e45f256b.json'

base_dir = '/media/data_disk2/sec/'
label_dir = '/media/data_disk2/sec/labels/'


def set_env(key_path):
    os.environ['GOOGLE_APPLICATION_CREDENTIALS'] = key_path


def get_vision_client(key_path):
    from google.cloud import vision
    set_env(key_path)
    client = vision.ImageAnnotatorClient()
    return client


client = get_vision_client(KEY_PATH)


def save_to_json(dict_obj, path):
    with open(path, 'w') as f:
        json.dump(dict_obj, f)


def load_json(path):
    with open(path, 'r') as f:
        return json.load(f)


def save(path, obj):
    with open(path, 'wb') as f:
        pickle.dump(obj, f)


def load(path):
    with open(path, 'rb') as f:
        obj = pickle.load(f)
    return obj


# remove these methods
def img_path_to_csv_path(img_path):
    csv_file_name = img_path.replace(base_dir, '').replace('/', '=').replace('.jpg', '.csv')
    return os.path.join(label_dir, csv_file_name)


def file_path_to_label_path(file_path, label_type):
    file_name = label_type + '#' + file_path.replace(base_dir, '').replace('/', '=').replace('.jpg', '.csv')
    return os.path.join(label_dir, file_name)


def file_path_to_rel_path(file_path, base_dir=base_dir):
    return file_path.replace(base_dir, '')


def rel_path_to_file_path(rel_path, base_dir=base_dir):
    return os.path.join(base_dir, rel_path)
