from sqlalchemy import Column, ForeignKey, Integer, SmallInteger, String, Table
from sqlalchemy.orm import reconstructor, relationship

from app.libs.enums import UserTypeEnum
from .base import Base
from .user import User


class Enroll(Base):
    id = Column('id', Integer, primary_key=True)
    user_gid = Column(String(10), ForeignKey('user.gid'))
    course_cid = Column(Integer, ForeignKey('course.cid'))
    enroll_type = Column('enroll_type', SmallInteger)
    user = relationship('User')
    course = relationship('Course')

    @staticmethod
    def add_user(course, teachers_gid, students_gid, TAs_gid, db):
        # TODO: repeat check
        with db.auto_commit():
            for teacher_gid in teachers_gid:
                teacher = User.query.filter_by(gid=teacher_gid).first_or_404()
                enroll = Enroll(
                    course_cid=course.cid,
                    user_gid=teacher.gid,
                    enroll_type=UserTypeEnum.TEACHER.value
                )
                db.session.add(enroll)
            for student_gid in students_gid:
                student = User.query.filter_by(gid=student_gid).first_or_404()
                enroll = Enroll(
                    course_cid=course.cid,
                    user_gid=student.gid,
                    enroll_type=UserTypeEnum.STUDENT.value
                )
                db.session.add(enroll)
            for TA_gid in TAs_gid:
                TA = User.query.filter_by(gid=TA_gid).first_or_404()
                enroll = Enroll(
                    course_cid=course.cid,
                    user_gid=TA.gid,
                    enroll_type=UserTypeEnum.TA.value
                )
                db.session.add(enroll)

    @staticmethod
    def del_user(course, teachers_gid, students_gid, TAs_gid, db):
        with db.auto_commit():
            for teacher_gid in teachers_gid:
                enroll = Enroll.query.filter_by(user_gid=teacher_gid, course_cid=course.cid)
                enroll.delete()
            for student_gid in students_gid:
                enroll = Enroll.query.filter_by(user_gid=student_gid, course_cid=course.cid)
                enroll.delete()
            for TA_gid in TAs_gid:
                enroll = Enroll.query.filter_by(user_gid=TA_gid, course_cid=course.cid)
                enroll.delete()

    @staticmethod
    def user_to_role(user_gid, course_cid):
        enroll = Enroll.query.filter_by(user_gid=user_gid, course_cid=course_cid).first()
        if not enroll:
            return None
        return UserTypeEnum(enroll.enroll_type)

    def serialize(self):
        return self.user

    @reconstructor
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields = ['user_gid', 'course_cid', 'enroll_type']


question_tag_table = Table(
    'question_tag_table',
    Base.metadata,
    Column('tag_id', Integer, ForeignKey('tag.id')),
    Column('question_id', Integer, ForeignKey('question.id'))
)


