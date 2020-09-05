from flask import request, jsonify

from app.libs.enums import UserTypeEnum
from app.libs.error_code import Success, DeleteSuccess
from app.libs.file import delete_file, update_file
from app.libs.redprint import Redprint
from app.libs.token_auth import login_required, enroll_required, role_required
from app.models import CourseResource
from app.models.base import db
from app.validators.forms import ResourceForm

api = Redprint('resource')


@api.route('/<int:fid>', methods=['GET'])
def get_resource(fid):
    resource = CourseResource.query.get_or_404(fid)
    return jsonify(resource)


@api.route('/<int:fid>', methods=['PATCH'])
@enroll_required(CourseResource, UserTypeEnum.TA)
def update_resource(fid):
    resource = CourseResource.query.get_or_404(fid)
    form = ResourceForm().validate_for_api()
    with db.auto_commit():
        if 'file' in request.files:
            file = request.files['file']
            if file and file.filename != '':
                update_file(file, resource)
        if form.description.data:
            resource.description = form.description.data
    return Success()


@api.route('/<int:fid>', methods=['DELETE'])
@enroll_required(CourseResource, UserTypeEnum.TA)
def delete_resource(fid):
    resource = CourseResource.query.get_or_404(fid)
    with db.auto_commit():
        delete_file(resource)
        db.session.delete(resource)
    return DeleteSuccess()
