from flask import current_app, jsonify, request
from itsdangerous import TimedJSONWebSignatureSerializer as Serializer

from app.libs.redprint import Redprint
from app.models.user import User

api = Redprint('token')


@api.route('', methods=['GET'])
def get_token():
    ticket = request.args.get("ticket")
    service = request.args.get("service")
    identity = User.verify(ticket, service)

    expiration = current_app.config['TOKEN_EXPIRATION']
    token = generate_auto_token(identity['scope'],
                                expiration,
                                gid=identity['gid'],
                                uid=identity['uid'])
    t = {
        'token': token.decode('ascii')
    }
    return jsonify(t), 201


def generate_auto_token(scope=None, expiration=7200, **kwargs):
    """generate token"""
    s = Serializer(current_app.config['SECRET_KEY'],
                   expires_in=expiration)
    return s.dumps(dict({'scope': scope}, **kwargs))

