from sqlalchemy import Column, String, Integer, ForeignKey
from sqlalchemy.orm import relationship
from app.models.base import Base


class DiscussionTopic(Base):
    id = Column(Integer, primary_key=True)
    question_id = Column(Integer, ForeignKey('question.id'))
    title = Column(String(127), nullable=False)
    content = Column(String(500), nullable=False)
    author_gid = Column(String(10), ForeignKey('user.gid'))
    stars = Column(Integer, default=0)
    topic_answer = relationship('DiscussionAnswer')


class DiscussionAnswer(Base):
    id = Column(Integer, primary_key=True)
    topic_id = Column(Integer, ForeignKey(DiscussionTopic.id))
    content = Column(String(500), nullable=False)
    author_gid = Column(String(10), ForeignKey('user.gid'))
    reply_id = Column(Integer, default=0)
