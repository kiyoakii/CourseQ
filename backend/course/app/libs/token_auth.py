import wrapt
from flask import g
from flask_jwt_extended import JWTManager, get_jwt_identity, verify_jwt_in_request

from app.libs.enums import UserTypeEnum
from app.libs.error_code import Forbidden, TokenExpired, TokenInvalid, TokenMissing
from app.models.relation import Enroll

jwt = JWTManager()


# Endpoint-based
@wrapt.decorator
def login_required(wrapped, *args, **kwargs):
    verify_jwt_in_request()
    user = get_jwt_identity()
#     # if not is_in_scope(user['scope'], request.endpoint):
#     #     raise Forbidden
    return wrapped()


# Object-based
def role_required(required_role):
    @wrapt.decorator
    def wrapper1(wrapped, instance, args, kwargs):
        verify_jwt_in_request()
        user = get_jwt_identity()
        role = UserTypeEnum.scope_to_role(user['scope'])
        print(role)
        print(required_role)
        if not role or role.value < required_role.value:
            raise Forbidden
        return wrapped(*args, **kwargs)

    return wrapper1


def enroll_required(model):
    @wrapt.decorator
    def wrapper(wrapped, instance, args, kwargs):
        verify_jwt_in_request()
        user = get_jwt_identity()
        pk = next(iter(kwargs.values()))
        course_cid = model.query.get_or_404(pk).belong_course
        role = Enroll.user_to_role(user['gid'], course_cid)
        if not role and not user['role'] == UserTypeEnum.MANAGER:
            raise Forbidden
        return wrapped(*args, **kwargs)
    return wrapper


def private(model):
    @wrapt.decorator
    def wrapper(wrapped, instance, args, kwargs):
        verify_jwt_in_request()
        user = get_jwt_identity()
        resource_pk = next(iter(kwargs.values()))
        resource = model.query.get_or_404(resource_pk)
        if resource.belong_author != user['gid'] and not user['role'] == UserTypeEnum.MANAGER:
            raise Forbidden
        return wrapped(*args, **kwargs)
    return wrapper


@jwt.user_loader_callback_loader
def user_loader_callback(user):
    g.user = user
    user['role'] = UserTypeEnum.scope_to_role(user['scope'])
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
