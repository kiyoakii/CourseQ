from flask import jsonify

from app.libs.enums import UserTypeEnum
from app.libs.error_code import Success, DeleteSuccess
from app.libs.redprint import Redprint
from app.libs.token_auth import login_required, enroll_required, role_required
from app.models import CourseResource, Assignment
from app.models.base import db
from app.models.schedule import Schedule
from app.validators.forms import ScheduleUpdateForm

api = Redprint('schedule')


@api.route('/<int:sid>', methods=['GET'])
def get_schedule(sid):
    schedule = Schedule.query.get_or_404(sid)
    return jsonify(schedule)


@api.route('/<int:sid>', methods=['PUT'])
@role_required(UserTypeEnum.TEACHER)
@enroll_required(Schedule)
def update_schedule(sid):
    schedule = Schedule.query.get_or_404(sid)
    form = ScheduleUpdateForm().validate_for_api()
    with db.auto_commit():
        form.populate_obj(schedule)
        resources = CourseResource.query.filter(CourseResource.id.in_(form.resource_ids.data)).all()
        schedule.resources = resources
        assignments = Assignment.query.filter(Assignment.id.in_(form.assignment_ids.data)).all()
        schedule.assignments = assignments
    return Success()


@api.route('/<int:sid>', methods=['DELETE'])
@role_required(UserTypeEnum.TEACHER)
@enroll_required(Schedule)
def delete_schedule(sid):
    schedule = Schedule.query.get_or_404(sid)
    with db.auto_commit():
        db.session.delete(schedule)
    return DeleteSuccess()
