from sqlalchemy import Column, String, Integer, Sequence, ForeignKey
from sqlalchemy.orm import reconstructor, relationship
import functools
from app.models.base import Base
from app.libs.error_code import Forbidden
from flask import g
from sqlalchemy.orm.exc import NoResultFound


class Schedule(Base):
    id = Column(Integer, primary_key=True)
    course_id = Column(Integer, ForeignKey('course.cid'))
    week_id = Column(Integer)
    topic = Column(String(255))
    reference = Column(String(255))
    assignments = relationship('Assignment')

    @reconstructor
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields = ['id', 'week_id', 'topic', 'reference', 'assignments']
