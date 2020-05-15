from sqlalchemy import Column, String, Integer, ForeignKey

from app.models.base import Base


class Answer(Base):
    ansid = Column(Integer, primary_key=True)
    qid = Column(Integer, ForeignKey('question.id'))
    content = Column(String(500), nullable=False)
    author = Column(String(10), ForeignKey('user.gid'))
    stars = Column(Integer, default=0)
