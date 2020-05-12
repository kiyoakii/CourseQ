from flask import jsonify, g, current_app

from app.api.v1.token import generate_auto_token
from app.libs.error_code import DeleteSuccess, RegisterSuccess
from app.libs.redprint import Redprint
from app.libs.token_auth import auth
from app.models.base import db
from app.models.user import User
from app.validators.forms import UserForm

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
    user = User().register(form.nickname.data,
                           form.email.data,
                           g.user.gid,
                           g.user.uid)
    scope = User.assign_scope(user)
    expiration = current_app.config['TOKEN_EXPIRATION']
    token = generate_auto_token(scope,
                                expiration,
                                gid=g.user.gid,
                                uid=g.user.uid)
    return RegisterSuccess(token.decode('ascii'))
