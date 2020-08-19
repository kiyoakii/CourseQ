import binascii
import os

from werkzeug.utils import secure_filename

from app.config.secure import UPLOAD_FOLDER


def create_file(file, instance):
    filename = secure_filename(file.filename)
    random_filename = str(binascii.b2a_hex(os.urandom(15)), encoding='UTF-8')
    file.save(os.path.join(UPLOAD_FOLDER, random_filename))
    instance.filename = filename
    instance.file = random_filename


def update_file(file, instance):
    filename = secure_filename(file.filename)
    random_filename = str(binascii.b2a_hex(os.urandom(15)), encoding='UTF-8')
    print(os.path.join(UPLOAD_FOLDER, random_filename))
    file.save(os.path.join(UPLOAD_FOLDER, random_filename))
    if instance.file:
        os.remove(os.path.join(UPLOAD_FOLDER, instance.file))
    instance.filename = filename
    instance.file = random_filename


def delete_file(instance):
    os.remove(os.path.join(UPLOAD_FOLDER, instance.file))
