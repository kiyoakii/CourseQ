from sqlalchemy import Column, String, ForeignKey, Table, Integer, SmallInteger
from sqlalchemy.orm import relationship
from .user import User
from .base import Base
from .course import Course
from app.libs.enums import UserTypeEnum


class Enroll(Base):
    id = Column('id', Integer, primary_key=True)
    user_gid = Column(Integer, ForeignKey('user.gid'))
    course_cid = Column(Integer, ForeignKey('course.cid'))
    user = relationship(User, backref='Enroll')
    course = relationship(Course, backref='Enroll')
    enroll_type = Column('enroll_type', SmallInteger)

    @staticmethod
    def add_user(course, teachers_gid, students_gid, TAs_gid, db):
        # TODO: repeat check
        with db.auto_commit():
            for teacher_gid in teachers_gid:
                teacher = User.query.filter_by(gid=teacher_gid).first_or_404()
                enroll = Enroll()
                enroll.course = course
                enroll.user = teacher
                enroll.enroll_type = UserTypeEnum.TEACHER.value
                db.session.add(enroll)
            for student_gid in students_gid:
                student = User.query.filter_by(gid=student_gid).first_or_404()
                enroll = Enroll()
                enroll.course = course
                enroll.user = student
                enroll.enroll_type = UserTypeEnum.STUDENT.value
                db.session.add(enroll)
            for TA_gid in TAs_gid:
                TA = User.query.get(gid=TA_gid).first_or_404()
                enroll = Enroll()
                enroll.course = course
                enroll.user = TA
                enroll.enroll_type = UserTypeEnum.TA.value
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
                enroll = Enroll.query.filter_by(user_gid=TA_gid, course_cid=course.gid)
                enroll.delete()
