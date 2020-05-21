from sqlalchemy import Column, String, Integer, ForeignKey, Text
from sqlalchemy.orm import relationship, reconstructor
import datetime
from app.models.base import Base
from app.models.relation import question_tag_table


class Question(Base):
    id = Column(Integer, primary_key=True)
    title = Column(String(127), nullable=False)
    content = Column(Text, nullable=False)
    author_gid = Column(String(10), ForeignKey('user.gid'))
    # stars = Column(Integer, default=0)
    history_questions = relationship("HistoryQuestion", back_populates='question')
    answer = relationship('Answer')
    discussions = relationship('DiscussionTopic')
    course_id = Column(Integer, ForeignKey('course.cid'))
    tags = relationship('Tag', secondary=question_tag_table)
    update_time = Column(Integer)

    @reconstructor
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields = ['id', 'title', 'stars', 'tags', 'content']
        self.update_time = self.create_time

    @property
    def update_datetime(self):
        if self.create_time:
            return datetime.fromtimestamp(self.update_time)
        else:
            return None


class HistoryQuestion(Base):
    id = Column(Integer, primary_key=True)
    title = Column(String(127), nullable=False)
    content = Column(Text, nullable=False)
    question = relationship("Question", back_populates='history_questions')
    question_id = Column(Integer, ForeignKey('question.id'))

    @reconstructor
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields = ['id', 'title', 'content', 'create_time']
