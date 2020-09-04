from sqlalchemy import Column, String, Integer, ForeignKey
from sqlalchemy.orm import reconstructor, relationship
from datetime import datetime
from app.models.base import Base
from flask import g


class Answer(Base):
    id = Column(Integer, primary_key=True)
    content = Column(String(500), nullable=False)
    author_gid = Column(String(10), ForeignKey('user.gid'))
    dump_fields = ['content']
    author = relationship('User')

    @reconstructor
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields = ['id', 'content', 'author', 'update_datetime']

    @property
    def update_datetime(self):
        return datetime.fromtimestamp(self.create_time)

    @property
    def belong_course(self):
        if g.user['scope'] == 'TeacherScope':
            return self.question_from_teacher.belong_course
        else:
            return self.question_From_student.belong_course

    @property
    def belong_author(self):
        return self.author_gid
