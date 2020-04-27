from collections import namedtuple

from flask import current_app, g, request
from flask_httpauth import HTTPBasicAuth
from itsdangerous import TimedJSONWebSignatureSerializer as Serializer, BadSignature, SignatureExpired

from app.libs.error_code import AuthFailed, Forbidden
from app.libs.scope import is_in_scope

auth = HTTPBasicAuth()
User = namedtuple('User', ['gid', 'scope'])


@auth.verify_password
def verify_password(token, password):
    user = verify_auth_token(token)
    if not user:
        return False
    else:
        g.user = user
        return True


def verify_auth_token(token):
    s = Serializer(current_app.config['SECRET_KEY'])
    try:
        data = s.loads(token)
    except BadSignature:
        raise AuthFailed(msg='token is invalid', error_code=1002)
    except SignatureExpired:
        raise AuthFailed(msg='token is expired', error_code=1003)
    gid = data['gid']
    scope = data['scope']
    allow = is_in_scope(scope, request.endpoint)
    if not allow:
        raise Forbidden()
    return User(gid, scope)
