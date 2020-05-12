from datetime import date

from flask import Flask as _Flask
from flask.json import JSONEncoder as _JSONEncoder

from app.libs.enums import UserTypeEnum
from app.libs.error_code import ServerError


class JSONEncoder(_JSONEncoder):
    def default(self, o):
        if hasattr(o, 'keys') and hasattr(o, '__getitem__'):
            return dict(data=dict(o))
        if isinstance(o, UserTypeEnum):
            return o.user_str(o)
        if isinstance(o, date):
            return o.strftime('%Y-%m-%d')
        raise ServerError()


class Flask(_Flask):
    json_encoder = JSONEncoder
