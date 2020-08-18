from wtforms import StringField, FieldList, TextAreaField, IntegerField, DateTimeField, BooleanField
from wtforms import ValidationError
from wtforms.validators import DataRequired, length, Email

from app.models.user import User
from app.validators.base import BaseForm as Form


class UserForm(Form):
    email = StringField(validators=[
        Email(message='invalid email')
    ])
    nickname = StringField(validators=[DataRequired(),
                                       length(min=4, max=22)])

    name = StringField(validators=[length(max=24)])
    phone = StringField(validators=[length(max=24)])
    school = StringField(validators=[length(max=63)])

    def validate_email(self, value):
        """ Used for validation before changing email"""
        if User.query.filter_by(email=value.data).first():
            raise ValidationError("Email already exists.")


class UserUpdateForm(Form):
    email = StringField(validators=[
        Email(message='invalid email')
    ])
    name = StringField(validators=[length(max=24)])
    phone = StringField(validators=[length(max=24)])
    school = StringField(validators=[length(max=63)])


class TokenForm(Form):
    token = StringField(validators=[DataRequired()])


class CourseCreateForm(Form):
    name_zh = StringField(validators=[DataRequired(), length(max=40)])
    name_en = StringField(validators=[DataRequired(), length(max=40)])
    intro = StringField(validators=[DataRequired(), length(max=200)])
    pre_course = StringField(validators=[DataRequired(), length(max=50)])
    textbooks = StringField(validators=[DataRequired(), length(max=50)])
    series = StringField(validators=[DataRequired(), length(max=50)])
    semester = StringField(validators=[DataRequired(), length(max=50)])
    teachers_gid = FieldList(StringField('gid', validators=[DataRequired()]))
    students_gid = FieldList(StringField('gid', validators=[DataRequired()]))
    TAs_gid = FieldList(StringField('gid', validators=[DataRequired()]))


class CourseUpdateForm(Form):
    name_zh = StringField(validators=[length(max=40)])
    name_en = StringField(validators=[length(max=40)])
    intro = StringField(validators=[length(max=200)])
    pre_course = StringField(validators=[length(max=50)])
    series = StringField(validators=[length(max=50)])
    textbooks = StringField(validators=[length(max=50)])
    semester = StringField(validators=[length(max=50)])
    new_teachers_gid = FieldList(StringField('gid', validators=[DataRequired()]))
    new_students_gid = FieldList(StringField('gid', validators=[DataRequired()]))
    new_TAs_gid = FieldList(StringField('gid', validators=[DataRequired()]))
    del_teachers_gid = FieldList(StringField('gid', validators=[DataRequired()]))
    del_students_gid = FieldList(StringField('gid', validators=[DataRequired()]))
    del_TAs_gid = FieldList(StringField('gid', validators=[DataRequired()]))


class ResourceForm(Form):
    filename = StringField(validators=[DataRequired()])
    course_id = StringField(validators=[DataRequired()])


class QuestionCreateForm(Form):
    title = StringField(validators=[length(max=127), DataRequired()])
    content = TextAreaField(validators=[DataRequired()])
    tags = FieldList(StringField('tag', validators=[DataRequired()]))


class QuestionUpdateForm(Form):
    title = StringField(validators=[length(max=127)])
    content = TextAreaField(validators=[])
    new_tags = FieldList(StringField('tag', validators=[]))
    del_tags = FieldList(StringField('tag', validators=[]))


class AnswerForm(Form):
    is_teacher = BooleanField()
    content = TextAreaField(validators=[DataRequired()])


class TopicCreateForm(Form):
    title = StringField(validators=[length(max=127), DataRequired()])
    content = TextAreaField(validators=[DataRequired()])


class TopicUpdateForm(Form):
    title = StringField(validators=[length(max=127)])
    content = TextAreaField(validators=[])


class TopicAnswerForm(Form):
    reply_id = IntegerField(validators=[])
    content = TextAreaField(validators=[DataRequired()])


class ScheduleCreateForm(Form):
    week = IntegerField(validators=[DataRequired()])
    topic = StringField(validators=[length(max=255), DataRequired()])
    reference = StringField(validators=[length(max=255), DataRequired()])


class AnnounceForm(Form):
    title = StringField(validators=[length(max=63), DataRequired()])
    content = TextAreaField(validators=[DataRequired()])


class ScheduleUpdateForm(Form):
    week = IntegerField(validators=[])
    topic = StringField(validators=[length(max=255)])
    reference = StringField(validators=[length(max=255)])


class AssignmentCreateForm(Form):
    title = StringField(validators=[DataRequired(), length(max=255)])
    due = DateTimeField(validators=[DataRequired()])


class AssignmentUpdateForm(Form):
    title = StringField(validators=[length(max=255)])
    due = DateTimeField(validators=[])
