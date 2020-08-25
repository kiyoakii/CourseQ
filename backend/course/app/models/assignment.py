from flask import request
from sqlalchemy import Column, String, Integer, ForeignKey
from sqlalchemy.orm import reconstructor

from app.models.base import Base


class Assignment(Base):
    id = Column(Integer, primary_key=True)
    title = Column(String(63))
    ddl = Column(String(63))
    course_cid = Column(Integer, ForeignKey('course.cid'))
    file = Column(String(40))
    filename = Column(String(63))

    @reconstructor
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)

        self.fields = ['id', 'title', 'ddl', 'url', 'filename']

    @property
    def url(self):
        if self.file:
            return request.url_root + 'static/uploads/' + self.file

    @property
    def belong_course(self):
        return self.course_cid
