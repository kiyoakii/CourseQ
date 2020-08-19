from flask import request
from sqlalchemy import Column, String, Integer, ForeignKey
from sqlalchemy.orm import reconstructor

from app.models.base import Base


class CourseResource(Base):
    id = Column(Integer, primary_key=True)
    description = Column(String(127))
    filename = Column(String(127))
    file = Column(String(127))
    course_id = Column(Integer, ForeignKey('course.cid'))

    @reconstructor
    def __init__(self):
        super().__init__()
        self.fields = ['id', 'filename', 'url']

    @property
    def url(self):
        return request.url_root + 'static/uploads/' + self.file


class Photo(Base):
    id = Column(Integer, primary_key=True)
    filename = Column(String(127))
    author_gid = Column(String(10), ForeignKey('user.gid'))
    file = Column(String(127))

    @reconstructor
    def __init__(self):
        super().__init__()
        self.fields = ['id', 'filename', 'url']

    @property
    def url(self):
        return request.url_root + 'static/uploads/' + self.file
