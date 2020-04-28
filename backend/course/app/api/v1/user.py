from flask import request, json, jsonify, g

from app.libs.error_code import Success, DeleteSuccess
from app.libs.redprint import Redprint
from app.models.base import db
from app.models.user import User
from app.validators.forms import UserForm
from app.libs.token_auth import auth
api = Redprint('User')


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
def register():
    form = UserForm().validate_for_api()
    user = User()
    gid, uid = user.check_ticket(form.ticket.data, form.service.data)
    user.register(form.nickname.data, form.email.data,
                  gid, uid)
    return Success()
