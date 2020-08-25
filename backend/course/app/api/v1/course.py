from flask import jsonify, request, g

from app.config.secure import ALLOWED_EXTENSIONS
from app.libs.enums import UserTypeEnum
from app.libs.error_code import Success, DeleteSuccess, ParameterException
from app.libs.file import create_file
from app.libs.redprint import Redprint
from app.libs.token_auth import login_required, role_required, enroll_required
from app.models import Announce, CourseResource, Assignment
from app.models.base import db
from app.models.course import Course
from app.models.history import History
from app.models.question import Question
from app.models.relation import Enroll
from app.models.schedule import Schedule
from app.models.tag import Tag
from app.validators.forms import CourseCreateForm, CourseUpdateForm, QuestionCreateForm, AnnounceForm, ResourceForm, \
    AssignmentCreateForm
from app.validators.forms import ScheduleCreateForm

api = Redprint('course')


@api.route('', methods=['GET'])
# @login_required
def get_course_list():
    return jsonify(Course.query.filter_by().all())


@api.route('', methods=['POST'])
@role_required(UserTypeEnum.STUDENT)
def create_course():
    form = CourseCreateForm().validate_for_api()
    with db.auto_commit():
        course = Course()
        form.populate_obj(course)
        db.session.add(course)
        Enroll.add_user(course, form.teachers_gid.data, form.students_gid.data, form.TAs_gid.data, db)
    return Success()


@api.route('/<int:cid>', methods=['GET'])
@role_required(UserTypeEnum.MANAGER)
@enroll_required(Course)
def get_course(cid):
    course = Course.query.filter_by(cid=cid).first_or_404()
    course.fields.append('series_courses')
    return jsonify(course)


@api.route('/<int:cid>', methods=['PUT', 'PATCH'])
@role_required(UserTypeEnum.TEACHER)
@enroll_required(Course)
def update_course(cid):
    # todo: put
    form = CourseUpdateForm().validate_for_api()
    course = Course.query.filter_by(cid=cid).first_or_404()
    # enroll_set = Enroll.query.filter_by(course_cid=cid)
    # if enroll_set.count() == 0:
    #     return Forbidden()

    with db.auto_commit():
        if request.method == 'PATCH':
            for field, value in form.data.items():
                if value:
                    setattr(course, field, value)
        else:
            form.populate_obj(course)
        Enroll.add_user(course, form.new_teachers_gid.data, form.new_students_gid.data, form.new_TAs_gid.data, db)
        Enroll.del_user(course, form.del_teachers_gid.data, form.del_students_gid.data, form.del_TAs_gid.data, db)
    return Success()


@api.route('/<int:cid>', methods=['DELETE'])
@role_required(UserTypeEnum.TEACHER)
@enroll_required(Course)
def delete_course(cid):
    course = Course.query.filter_by(cid=cid).first_or_404()
    with db.auto_commit():
        db.session.delete(course)
    return DeleteSuccess()


@api.route('/<int:cid>/files', methods=['GET'])
@role_required(UserTypeEnum.STUDENT)
@enroll_required(Course)
def get_files_list(cid):
    course = Course.query.filter_by(cid=cid).first_or_404()
    return jsonify(files=course.resource)


@api.route('/<int:cid>/questions', methods=['POST'])
@role_required(UserTypeEnum.STUDENT)
@enroll_required(Course)
def create_question(cid):
    course = Course.query.filter_by(cid=cid).first_or_404()
    form = QuestionCreateForm().validate_for_api()
    with db.auto_commit():
        question = Question(
            title=form.title.data,
            content=form.content.data,
            course_id=course.cid,
            author_gid=g.user['gid']
        )
        history = History(root_question=question)
        for tag_name in form.tags.data:
            tag = Tag.get_or_create_tag(tag_name)
            question.tags.append(tag)
        db.session.add(question, history)
    return Success()


@api.route('/<int:cid>/questions', methods=['GET'])
@role_required(UserTypeEnum.STUDENT)
def get_question_list(cid):
    course = Course.query.filter_by(cid=cid).first_or_404()
    return jsonify(course.questions)


@api.route('/<int:cid>/schedules', methods=['POST'])
@role_required(UserTypeEnum.TEACHER)
@enroll_required(Course)
def create_schedule(cid):
    course = Course.query.filter_by(cid=cid).first_or_404()
    form = ScheduleCreateForm().validate_for_api()
    with db.auto_commit():
        schedule = Schedule(week=form.week.data,
                            topic=form.topic.data,
                            reference=form.reference.data,
                            course_id=course.cid,
                            additional_info=form.additional_info.data,
                            datetime=form.datetime.data
                            )
        resources = CourseResource.query.filter(CourseResource.id.in_(form.resource_ids.data)).all()
        schedule.resources = resources
        assignments = Assignment.query.filter(Assignment.id.in_(form.assignment_ids.data)).all()
        schedule.assignments = assignments
        db.session.add(schedule)
    return Success()


@api.route('/<int:cid>/schedules', methods=['GET'])
def list_schedules(cid):
    course = Course.query.filter_by(cid=cid).first_or_404()
    return jsonify(course.schedules)


@api.route('/<int:cid>/announces', methods=['POST'])
@role_required(UserTypeEnum.TA)
@enroll_required(Course)
def create_announce(cid):
    course = Course.query.filter_by(cid=cid).first_or_404()
    form = AnnounceForm().validate_for_api()
    with db.auto_commit():
        announce = Announce()
        form.populate_obj(announce)
        announce.course = course
        db.session.add(announce)
    return Success()


def allowed_file(filename):
    return '.' in filename and \
           filename.rsplit('.', 1)[1].lower() in ALLOWED_EXTENSIONS


@api.route('/<int:cid>/resources', methods=['POST'])
@role_required(UserTypeEnum.TA)
@enroll_required(Course)
def upload(cid):
    course = Course.query.get_or_404(cid)
    if 'file' not in request.files:
        return ParameterException
    file = request.files['file']
    form = ResourceForm().validate_for_api()
    if file.filename == '':
        return ParameterException()
    if file:
        with db.auto_commit():
            resource = CourseResource()
            create_file(file, resource)
            resource.course_id = cid
            resource.description = form.description.data
            db.session.add(resource)
        return jsonify({'id': resource.id})
    return ParameterException()


@api.route('/<int:cid>/resources', methods=['GET'])
def get_resources(cid):
    course = Course.query.get_or_404(cid)
    return jsonify(course.resources)


@api.route('/<int:cid>/assignments', methods=['POST'])
@role_required(UserTypeEnum.TA)
@enroll_required(Course)
def create_assignment(cid):
    course = Course.query.get_or_404(cid)
    form = AssignmentCreateForm().validate_for_api()
    with db.auto_commit():
        assignment = Assignment()
        form.populate_obj(assignment)
        assignment.course_cid = cid
        if 'file' in request.files:
            file = request.files['file']
            if file and file.filename != '':
                create_file(file, assignment)
        db.session.add(assignment)
    return jsonify({'id': assignment.id})


@api.route('/<int:cid>/assignments', methods=['GET'])
def get_assignment(cid):
    course = Course.query.get_or_404(cid)
    return jsonify(course.assignments)
