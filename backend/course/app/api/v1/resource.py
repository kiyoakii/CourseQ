from flask import jsonify, g, request, send_file
from app.models.course import Course
from app.models.resource import CourseResource
from app.models.user import User
from app.models.enroll import Enroll
from app.libs.error_code import Success, DeleteSuccess, Forbidden, ParameterException, FileSuccess
from app.libs.redprint import Redprint
from app.validators.forms import ResourceForm
from app.models.base import db
from sqlalchemy.orm.exc import NoResultFound
from werkzeug.utils import secure_filename
from io import BytesIO

api = Redprint('resource')


# TODO scope & maybe there are better ways to handle files
@api.route('/', methods=['POST'])
def create():
    form = ResourceForm().validate_for_api()
    with db.auto_commit():
        course = Course.query.filter_by(cid=form.course_id.data).first_or_404()
        resource = CourseResource()
        resource.name = form.filename.data
        resource.status = 0
        course.resource.append(resource)
    return FileSuccess(url=resource.id.__str__())


@api.route('/<int:fid>', methods=['PUT'])
def upload(fid):
    try:
        file = request.files['file']
    except ValueError:
        return ParameterException
    with db.auto_commit():
        resource = CourseResource.query.get_or_404(fid)
        if resource.status == 1:
            return Forbidden()
        resource.data = file.read()
        resource.status = 1
    return Success()


@api.route('/<int:fid>', methods=['GET'])
def download(fid):
    file = CourseResource.query.get_or_404(fid)
    return send_file(BytesIO(file.data), attachment_filename=file.name, as_attachment=True)
