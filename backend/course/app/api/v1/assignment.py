from io import BytesIO

from flask import request, send_file, jsonify

from app.libs.error_code import Success, Forbidden, ParameterException, FileSuccess
from app.libs.redprint import Redprint
from app.models.base import db
from app.models.assignment import Assignment
from app.validators.forms import AssignmentUpdateForm
from app.models.resource import CourseResource
from app.validators.forms import ResourceForm

api = Redprint('assignment')


@api.route('/<int:aid>', methods=['GET'])
def get_assignment(aid):
    assignment = Assignment.query.get_or_404(aid)
    return jsonify(assignment)


@api.route('/<int:aid>', methods=['POST'])
def update_assignment(aid):
    assignment = Assignment.query.get_or_404(aid)
    form = AssignmentUpdateForm().validate_for_api()
    with db.auto_commit():
        form.populate_obj(assignment)
    return Success()
