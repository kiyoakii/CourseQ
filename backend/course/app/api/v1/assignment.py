from flask import jsonify, request

from app.libs.enums import UserTypeEnum
from app.libs.error_code import Success, DeleteSuccess
from app.libs.file import update_file, delete_file
from app.libs.redprint import Redprint
from app.libs.token_auth import login_required, enroll_required, role_required
from app.models.assignment import Assignment
from app.models.base import db
from app.validators.forms import AssignmentUpdateForm

api = Redprint('assignment')


@api.route('/<int:aid>', methods=['GET'])
@role_required(UserTypeEnum.STUDENT)
@enroll_required(Assignment)
def get_assignment(aid):
    assignment = Assignment.query.get_or_404(aid)
    return jsonify(assignment)


@api.route('/<int:aid>', methods=['PATCH'])
@enroll_required(Assignment, UserTypeEnum.TA)
def update_assignment(aid):
    assignment = Assignment.query.get_or_404(aid)
    form = AssignmentUpdateForm().validate_for_api()
    with db.auto_commit():
        if form.ddl.data:
            assignment.ddl = form.ddl.data
        if form.title.data:
            assignment.title = form.title.data
        if 'file' in request.files:
            file = request.files['file']
            if file and file.filename != '':
                update_file(file, assignment)
            else:
                delete_file(assignment)
                assignment.file = None
                assignment.filename = None
    return Success()


@api.route('/<int:aid>', methods=['DELETE'])
@enroll_required(Assignment, UserTypeEnum.TA)
def delete_assignment(aid):
    assignment = Assignment.query.get_or_404(aid)
    with db.auto_commit():
        delete_file(assignment)
        db.session.delete(assignment)
    return DeleteSuccess()
