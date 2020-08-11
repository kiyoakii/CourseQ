from app.libs.errors import APIException


class CreateSuccess(APIException):
    code = 201
    msg = 'created'
    error_code = 0


class Success(APIException):
    code = 200
    msg = 'ok'
    error_code = 0


class RegisterSuccess(Success):
    def __init__(self, token):
        super().__init__(msg=token)


class FileSuccess(Success):
    def __init__(self, url):
        super().__init__(msg=url)


class DeleteSuccess(Success):
    code = 204
    error_code = 1


class UpVoteSuccess(Success):
    msg = 'up vote successfully'


class CancelUpVoteSuccess(Success):
    msg = 'up vote cancelled'


class ServerError(APIException):
    code = 500
    msg = 'ServerError'
    error_code = 999


class ParameterException(APIException):
    code = 400
    msg = 'invalid parameter'
    error_code = 1000


class NotFound(APIException):
    code = 404
    msg = 'resource not found'
    error_code = 1001


class AuthFailed(APIException):
    code = 401
    error_code = 1005
    msg = 'authorization failed'


class TokenInvalid(APIException):
    code = 401
    error_code = 1002
    msg = 'Token invalid'


class TokenExpired(APIException):
    code = 401
    error_code = 1003
    msg = 'Token expired'


class TokenMissing(APIException):
    code = 401
    error_code = 1004
    msg = 'Token missing'


class Forbidden(APIException):
    code = 403
    error_code = 1004
    msg = 'forbidden, not in scope'


class Duplicate(APIException):
    code = 400
    error_code = 2001
    msg = 'duplicate error'


class Redirect(APIException):
    code = 303
    error_code = 2

    def __init__(self, url):
        super().__init__(msg=url)
