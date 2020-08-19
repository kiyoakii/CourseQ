import binascii
import os

from flask import request
from werkzeug.utils import secure_filename

from app.config.secure import UPLOAD_FOLDER
from app.libs.error_code import Success, ParameterException, DeleteSuccess
from app.libs.redprint import Redprint
from app.models import CourseResource
from app.models.base import db
from app.validators.forms import ResourceForm

api = Redprint('resource')





@api.route('/<int:fid>', methods=['PATCH'])
def update_file(fid):
    resource = CourseResource.query.get_or_404(fid)
    form = ResourceForm().validate_for_api()
    file = request.files['file']
    if file.filename == '':
        return ParameterException

    with db.auto_commit():
        if file:
            filename = secure_filename(file.filename)
            random_filename = str(binascii.b2a_hex(os.urandom(15)), encoding='UTF-8')
            print(os.path.join(UPLOAD_FOLDER, random_filename))
            file.save(os.path.join(UPLOAD_FOLDER, random_filename))
            os.remove(os.path.join(UPLOAD_FOLDER, resource.file))
            resource.filename = filename
            resource.file = random_filename
        if form.description.data:
            resource.description = form.description.data
    return Success()


@api.route('/<int:fid>', methods=['DELETE'])
def delete_file(fid):
    resource = CourseResource.query.get_or_404(fid)
    with db.auto_commit():
        os.remove(os.path.join(UPLOAD_FOLDER, resource.file))
        db.session.delete(resource)
    return DeleteSuccess()
