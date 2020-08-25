from sqlalchemy import Column, String, Integer, ForeignKey, Text
from sqlalchemy.orm import reconstructor, relationship

from app.models.base import Base


class Announce(Base):
    id = Column(Integer, primary_key=True)
    course_cid = Column(Integer, ForeignKey('course.cid'))
    author_gid = Column(String(10), ForeignKey('user.gid'))
    title = Column(String(63))
    content = Column(Text, nullable=False)
    course = relationship('Course')
    author = relationship('User')

    @reconstructor
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields = ['id', 'create_datetime', 'title', 'content', 'author']

    @property
    def belong_course(self):
        return self.course_cid

    @property
    def belong_author(self):
        return self.author_gid
