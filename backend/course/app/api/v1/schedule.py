from io import BytesIO

from flask import request, send_file

from app.libs.error_code import Success, Forbidden, ParameterException, FileSuccess
from app.libs.redprint import Redprint
from app.models.base import db
from app.models.course import Course
from app.models.resource import CourseResource
from app.validators.forms import ResourceForm

api = Redprint('schedule')
