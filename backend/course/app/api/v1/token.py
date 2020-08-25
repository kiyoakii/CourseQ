from flask import jsonify, request
from flask_jwt_extended import create_access_token

from app.libs.redprint import Redprint
from app.models.user import User

api = Redprint('token')


@api.route('', methods=['GET'])
def get_token():
    ticket = request.args.get("ticket")
    service = request.args.get("service")
    user = User.verify(ticket, service)
    access_token = create_access_token(identity=user)
    return jsonify({'access_token': access_token, 'registered': user['scope'] != 'Scope', 'gid': user['gid']})


@api.route('/<string:gid>', methods=['GET'])
def super_get_token(gid):
    user = User.query.filter_by(gid=gid).first()
    scope = User.assign_scope(user)
    identity = {
        'uid': '0000000000',
        'gid': gid,
        'scope': scope
    }
    access_token = create_access_token(identity=identity)
    return jsonify({'access_token': access_token, 'registered': identity['scope'] != 'Scope', 'gid': identity['gid']})
