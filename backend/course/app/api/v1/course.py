from flask import jsonify, g
from sqlalchemy.orm.exc import NoResultFound

from app.libs.error_code import Success, DeleteSuccess, Forbidden
from app.libs.redprint import Redprint
from app.models.base import db
from app.models.course import Course
from app.models.enroll import Enroll
from app.validators.forms import CourseCreateForm, CourseUpdateForm
from app.libs.token_auth import auth
from app.libs.enums import UserTypeEnum

api = Redprint('course')


# TODO gid check and scope
@api.route('', methods=['GET'])
def get_course_list():
    return jsonify(courses=Course.query.all())


@api.route('/create', methods=['POST'])
@auth.login_required
@Course.access_scope(UserTypeEnum.MANAGER)
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
@auth.login_required
@Course.access_scope(UserTypeEnum.TEACHER)
def update_course(cid):
    form = CourseUpdateForm().validate_for_api()
    course = Course.query.filter_by(cid=cid).first_or_404()
    try:
        Enroll.query.filter_by(course_cid=cid).filter_by(user_gid=g.gid)
    except NoResultFound:
        return Forbidden()
    with db.auto_commit():
        form.populate_obj(course)
        Enroll.add_user(course, form.new_teachers_gid.data, form.new_students_gid.data, form.new_TAs_gid.data, db)
        Enroll.del_user(course, form.del_teachers_gid.data, form.del_students_gid.data, form.del_TAs_gid.data, db)
    return Success()


@api.route('/<int:cid>', methods=['DELETE'])
@auth.login_required
@Course.access_scope(UserTypeEnum.MANAGER)
def delete_course(cid):
    course = Course.query.filter_by(cid=cid).first_or_404()
    with db.auto_commit():
        course.delete()
    return DeleteSuccess()


@api.route('/<int:cid>/files', methods=['GET'])
def get_files_list(cid):
    pass
