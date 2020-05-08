from flask import request, json, jsonify, g

from app.libs.error_code import Success, DeleteSuccess
from app.libs.redprint import Redprint
from app.libs.token_auth import verify_email_auth_token
from app.models.base import db
from app.models.user import User
from app.validators.forms import UserForm
from app.libs.token_auth import auth

api = Redprint('user')


@api.route('/<string:gid>', methods=['GET'])
@auth.login_required
def super_get_user(gid):
    user = User.query.filter_by(gid=gid).first_or_404()
    return jsonify(user)


@api.route('', methods=['GET'])
@auth.login_required
def get_user():
    gid = g.user.gid
    user = User.query.filter_by(gid=gid).first_or_404()
    return jsonify(user)


@api.route('', methods=['DELETE'])
@auth.login_required
def delete_user():
    gid = g.user.gid
    with db.auto_commit():
        user = User.query.filter_by(gid=gid).first_or_404()
        user.delete()
    return DeleteSuccess()


@api.route('/register', methods=['POST'])
@auth.login_required
def register():
    form = UserForm().validate_for_api()
    user = User()
    user.register(form.nickname.data,
                  form.email.data,
                  g.user.gid,
                  g.user.uid)
    return Success()


@api.route('/email_auth/<token>', methods=['GET'])
def email_authenticate(token):
    gid = verify_email_auth_token(token)
    if gid:
        with db.auto_commit():
            user = User.query.filter_by(gid=gid).first_or_404()
            # Update user.auth or set another attribute to mark user's email is valid
        return Success()