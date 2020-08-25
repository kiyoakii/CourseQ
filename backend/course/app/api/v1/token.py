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
    # user = {
    #     'uid':'000',
    #     'gid':'0000000387',
    #     'scope': 'StudentScope'
    # }
    access_token = create_access_token(identity=user)
    return jsonify({'access_token': access_token, 'registered': user['scope'] != 'Scope', 'gid': user['gid']})
