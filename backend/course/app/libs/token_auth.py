import wrapt
from flask import g, request
from flask_jwt_extended import JWTManager, get_jwt_identity, verify_jwt_in_request

from app.libs.error_code import Forbidden, TokenExpired, TokenInvalid, TokenMissing
from app.libs.scope import is_in_scope
from app.models.relation import Enroll

jwt = JWTManager()


# Endpoint-based
@wrapt.decorator
def login_required(wrapped, instance, args, kwargs):
    verify_jwt_in_request()
    user = get_jwt_identity()
    if not is_in_scope(user['scope'], request.endpoint):
        raise Forbidden
    g.user = user
    return wrapped(*args, **kwargs)


# Object-based
def role_required(required_role):
    @wrapt.decorator
    def wrapper(wrapped, instance, args, kwargs):
        verify_jwt_in_request()
        user = get_jwt_identity()
        course_cid = kwargs['cid']
        role = Enroll.user_to_role(user['gid'], course_cid)
        if not role or role.value < required_role.value:
            raise Forbidden
        g.user = user
        return wrapped(*args, **kwargs)

    return wrapper


@jwt.user_loader_callback_loader
def user_loader_callback(user):
    g.user = user
    return True


@jwt.expired_token_loader
def expired_token_callback(expired_token):
    return TokenExpired()


@jwt.invalid_token_loader
def invalid_token_callback(invalid_token):
    if invalid_token == '':
        return TokenMissing()
    else:
        return TokenInvalid()
