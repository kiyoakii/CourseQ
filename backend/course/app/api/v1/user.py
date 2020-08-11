from flask import jsonify, g
from flask_jwt_extended import create_access_token

from app.libs.enums import UserTypeEnum
from app.libs.error_code import DeleteSuccess, RegisterSuccess
from app.libs.redprint import Redprint
from app.libs.token_auth import role_required, login_required
from app.models.base import db
from app.models.user import User
from app.validators.forms import UserForm

api = Redprint('user')


@api.route('/teachers', methods=['GET'])
def get_teachers():
    users = User.query.filter_by(_auth=UserTypeEnum.TEACHER.value).all()
    return jsonify(users)


@api.route('/students', methods=['GET'])
def get_students():
    users = User.query.filter_by(_auth=UserTypeEnum.STUDENT.value).all()
    return jsonify(users)


@api.route('/<string:gid>', methods=['GET'])
@role_required(UserTypeEnum.MANAGER)
def super_get_user(gid):
    user = User.query.filter_by(gid=gid).first_or_404()
    return jsonify(user)


@api.route('', methods=['GET'])
@login_required
def get_user():
    gid = g.user.gid
    user = User.query.filter_by(gid=gid).first_or_404()
    return jsonify(user)


@api.route('', methods=['DELETE'])
def delete_user():
    gid = g.user.gid
    with db.auto_commit():
        user = User.query.filter_by(gid=gid).first_or_404()
        user.delete()
    return DeleteSuccess()


@api.route('/register', methods=['POST'])
@login_required
def register():
    form = UserForm().validate_for_api()
    user = User().register(form.nickname.data,
                           form.email.data,
                           g.user.gid,
                           g.user.uid)
    scope = User.assign_scope(user)
    identity = {
        'scope': scope,
        'uid': g.user.uid,
        'gid': g.user.gid
    }
    access_token = create_access_token(identity)

    return RegisterSuccess(access_token)


@api.route('/<string:gid>/courses', methods=['GET'])
def get_courses(gid):
    user = User.query.filter_by(gid=gid).first_or_404()
    courses = user.courses
    return jsonify(courses)
