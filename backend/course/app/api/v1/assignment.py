from flask import jsonify

from app.libs.error_code import Success
from app.libs.redprint import Redprint
from app.models.assignment import Assignment
from app.models.base import db
from app.validators.forms import AssignmentUpdateForm

api = Redprint('assignment')


@api.route('/<int:aid>', methods=['GET'])
def get_assignment(aid):
    assignment = Assignment.query.get_or_404(aid)
    return jsonify(assignment)


@api.route('/<int:aid>', methods=['PUT'])
def update_assignment(aid):
    assignment = Assignment.query.get_or_404(aid)
    form = AssignmentUpdateForm().validate_for_api()
    with db.auto_commit():
        form.populate_obj(assignment)
    return Success()
