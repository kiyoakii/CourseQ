import datetime

from sqlalchemy import Column, String, Integer, ForeignKey, Text
from sqlalchemy.orm import relationship, reconstructor

from app.models.base import Base
from app.models.relation import question_tag_table


class Question(Base):
    id = Column(Integer, primary_key=True)
    title = Column(String(127), nullable=False)
    content = Column(Text, nullable=False)
    author_gid = Column(String(10), ForeignKey('user.gid'))
    # stars = Column(Integer, default=0)
    root_qid = Column(Integer)
    answer = relationship('Answer')
    discussions = relationship('DiscussionTopic')
    course_id = Column(Integer, ForeignKey('course.cid'))
    tags = relationship('Tag', secondary=question_tag_table)
    update_time = Column(Integer)
    answers = relationship('Answer')
    up_votes = relationship('QuestionUpVote')

    @reconstructor
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields = ['id', 'title', 'tags', 'content']
        self.update_time = self.create_time

    @property
    def update_datetime(self):
        if self.create_time:
            return datetime.fromtimestamp(self.update_time)
        else:
            return None
