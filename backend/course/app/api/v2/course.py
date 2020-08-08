from flask_restful import Resource, marshal_with

from app.libs.error_code import Success, Forbidden
from app.models import Course
from app.models.base import db
from app.models.relation import Enroll
from app.serializer.course import course_fields
from app.serializer.error import error_fields
from app.validators.forms import CourseCreateForm, CourseUpdateForm


class CourseViews(Resource):
    @marshal_with(course_fields)
    def get(self, pk=None):
        if pk:
            course = Course.query.get_or_404(pk)
        else:
            course = Course.query.all()
        return course

    @marshal_with(error_fields)
    def post(self):
        form = CourseCreateForm().validate_for_api()
        with db.auto_commit():
            course = Course()
            form.populate_obj(course)
            db.session.add(course)
            Enroll.add_user(course, form.teachers_gid.data, form.students_gid.data, form.TAs_gid.data, db)
        return Success()

    @marshal_with(error_fields)
    def put(self, pk):
        form = CourseUpdateForm().validate_for_api()
        course = Course.query.filter_by(cid=pk).first_or_404()
        enroll_set = Enroll.query.filter_by(course_cid=pk)
        if enroll_set.count() == 0:
            return Forbidden()
        with db.auto_commit():
            form.populate_obj(course)
            Enroll.add_user(course, form.new_teachers_gid.data, form.new_students_gid.data, form.new_TAs_gid.data, db)
            Enroll.del_user(course, form.del_teachers_gid.data, form.del_students_gid.data, form.del_TAs_gid.data, db)
        return Success()
