from io import BytesIO

from flask import jsonify

from app.libs.error_code import Success, Forbidden, ParameterException, FileSuccess
from app.libs.redprint import Redprint
from app.models.schedule import Schedule
from app.models.assignment import Assignment
from app.validators.forms import ScheduleUpdateForm, AssignmentCreateForm
from app.models.base import db
import datetime
import app

api = Redprint('schedule')


@api.route('/<int:sid>', methods=['GET'])
def get_schedule(sid):
    schedule = Schedule.query.get_or_404(sid)
    return jsonify(schedule)


@api.route('/<int:sid>', methods=['POST'])
def update_schedule(sid):
    schedule = Schedule.query.get_or_404(sid)
    form = ScheduleUpdateForm().validate_for_api()
    with db.auto_commit():
        form.populate_obj(schedule)
    return Success()


