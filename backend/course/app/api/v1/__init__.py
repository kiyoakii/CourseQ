from flask import Blueprint
from app.api.v1 import user, token, course


def create_blueprint_v1():
    bp_v1 = Blueprint('v1', __name__)
    user.api.register(bp_v1, url_prefix='/user')
    token.api.register(bp_v1, url_prefix='/token')
    course.api.register(bp_v1, url_prefix='/courses')
    return bp_v1
