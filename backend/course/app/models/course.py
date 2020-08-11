from sqlalchemy import Column, String, Integer, Sequence
from sqlalchemy.orm import reconstructor, relationship

from app.libs.enums import UserTypeEnum
from app.models.base import Base


class Course(Base):
    cid = Column(Integer, Sequence('course_id_seq'), primary_key=True)
    name_zh = Column(String(40), nullable=False)
    name_en = Column(String(40), nullable=False)
    intro = Column(String(200))
    pre_course = Column(String(50))
    textbooks = Column(String(50))
    semester = Column(String(50))
    resources = relationship("CourseResource")
    questions = relationship('Question')
    teachers = relationship('Enroll', primaryjoin='and_(Enroll.enroll_type=={0}, Enroll.course_cid==Course.cid)'.format(
        UserTypeEnum.TEACHER.value))
    students = relationship('Enroll', primaryjoin='and_(Enroll.enroll_type=={0}, Enroll.course_cid==Course.cid)'.format(
        UserTypeEnum.STUDENT.value))
    assistants = relationship('Enroll',
                              primaryjoin='and_(Enroll.enroll_type=={0}, Enroll.course_cid==Course.cid)'.format(
                                  UserTypeEnum.TA.value))
    schedules = relationship('Schedule')

    @reconstructor
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields = ['cid', 'name_zh', 'name_en', 'intro',
                       'pre_course', 'textbooks', 'semester', 'teachers', 'assistants', 'students', 'schedules',
                       'resources']
