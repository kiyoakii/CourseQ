from sqlalchemy import Column, String, Integer, Sequence
from sqlalchemy.orm import reconstructor, relationship
import functools
from app.models.base import Base
from app.libs.error_code import Forbidden
from flask import g
from sqlalchemy.orm.exc import NoResultFound


class Course(Base):
    # todo return users json
    cid = Column(Integer, Sequence('course_id_seq'), primary_key=True)
    name_zh = Column(String(40), nullable=False)
    name_en = Column(String(40), nullable=False)
    intro = Column(String(200))
    pre_Course = Column(String(50))
    textbooks = Column(String(50))
    semester = Column(String(50))
    resource = relationship("CourseResource")

    @reconstructor
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields = ['cid', 'name_zh', 'name_en', 'intro',
                       'pre_Course', 'textbooks', 'semester']

    @staticmethod
    def access_scope(scope):
        def decorator(func):
            @functools.wraps(func)
            def wrapper(*args, **kwargs):
                from app.models.relation import Enroll
                try:
                    enroll = Enroll.query.filter_by(course_cid=args[0]).filter_by(user_id=g.user.gid)
                except NoResultFound:
                    return Forbidden()
                if enroll.enroll_type < scope:
                    return Forbidden()

                return func(*args, **kwargs)

            return wrapper

        return decorator
