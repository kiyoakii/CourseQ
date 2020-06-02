from sqlalchemy import Column, String, Integer, ForeignKey

from app.models.base import Base


class AnswerUpVote(Base):
    id = Column(Integer, primary_key=True)
    answer_id = Column(Integer, ForeignKey('answer.id'))
    user_gid = Column(String(10), ForeignKey('user.gid'))


class QuestionUpVote(Base):
    id = Column(Integer, primary_key=True)
    question_id = Column(Integer, ForeignKey('question.id'))
    user_gid = Column(String(10), ForeignKey('user.gid'))
