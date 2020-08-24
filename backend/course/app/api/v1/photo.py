import binascii
import os

from flask import request, jsonify, g
from werkzeug.utils import secure_filename

from app.config.secure import UPLOAD_FOLDER
from app.libs.error_code import ParameterException, DeleteSuccess
from app.libs.redprint import Redprint
from app.libs.token_auth import login_required
from app.models import User
from app.models.base import db
from app.models.resource import Photo

api = Redprint('photo')


@api.route('', methods=['POST'])
@login_required
def upload_photo():
    if 'file' not in request.files:
        return ParameterException()
    file = request.files['file']
    if file.filename == '':
        return ParameterException()
    if file:
        with db.auto_commit():
            filename = secure_filename(file.filename)
            random_filename = str(binascii.b2a_hex(os.urandom(15)), encoding='UTF-8')
            print(os.path.join(UPLOAD_FOLDER, random_filename))
            file.save(os.path.join(UPLOAD_FOLDER, random_filename))
            photo = Photo()
            photo.filename = filename
            photo.file = random_filename
            photo.author_gid = g.user['gid']
            db.session.add(photo)
        return jsonify(photo)
    else:
        return ParameterException()


@api.route('', methods=['GET'])
@login_required
def get_photo():
    user = User.query.get_or_404(g.user['gid'])
    return jsonify(user.photos)


@api.route('/<int:fid>', methods=['DELETE'])
@login_required
def delete_photo(fid):
    photo = Photo.query.get_or_404(fid)
    with db.auto_commit():
        os.remove(os.path.join(UPLOAD_FOLDER, photo.file))
        db.session.delete(photo)
    return DeleteSuccess()
