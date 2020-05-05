from flask import jsonify, g, request, send_file
from app.models.course import Course, CourseResource
from app.models.user import User
from app.models.enroll import Enroll
from app.libs.error_code import Success, DeleteSuccess, Forbidden, ParameterException
from app.libs.redprint import Redprint
from app.validators.forms import CourseCreateForm, CourseUpdateForm
from app.models.base import db
from sqlalchemy.orm.exc import NoResultFound
from werkzeug.utils import secure_filename
from io import BytesIO

api = Redprint('course')


# TODO gid check and scope

@api.route('/create', methods=['POST'])
def create_course():
    form = CourseCreateForm().validate_for_api()
    with db.auto_commit():
        course = Course()
        form.populate_obj(course)
        Enroll.add_user(course, form.teachers_gid.data, form.students_gid.data, form.TAs_gid.data, db)
        db.session.add(course)
    return Success()


@api.route('/<int:cid>', methods=['GET'])
def get_course(cid):
    course = Course.query.filter_by(cid=cid).first_or_404()
    return jsonify(course)


@api.route('/<int:cid>', methods=['PUT'])
def update_course(cid):
    form = CourseUpdateForm().validate_for_api()
    course = Course.query.filter_by(cid=cid).first_or_404()
    try:
        Enroll.query.filter_by(course_cid=cid)
    except NoResultFound:
        return Forbidden()
    with db.auto_commit():
        form.populate_obj(course)
        Enroll.add_user(course, form.new_teachers_gid.data, form.new_students_gid.data, form.new_TAs_gid.data, db)
        Enroll.del_user(course, form.del_teachers_gid.data, form.del_students_gid.data, form.del_TAs_gid.data, db)
    return Success()


@api.route('/<int:cid>', methods=['DELETE'])
def delete_course(cid):
    course = Course.query.filter_by(cid=cid).first_or_404()
    with db.auto_commit():
        course.delete()
    return DeleteSuccess()


@api.route('/<int:cid>/file', methods=['POST'])
def upload(cid):
    try:
        file = request.files['file']
    except ValueError:
        return ParameterException
    with db.auto_commit():
        filename = secure_filename(file.filename)
        data = file.read()
        resource = CourseResource()
        resource.name = filename
        resource.data = data
        db.session.add(resource)
    return Success()


@api.route('/<int:cid>/file', methods=['GET'])
def get_file_list(cid):
    pass


@api.route('<int:cid>/file/<int:fid>', methods=['GET'])
def download(cid, fid):
    pass
