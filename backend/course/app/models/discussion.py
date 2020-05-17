from sqlalchemy import Column, String, Integer, ForeignKey

from app.models.base import Base


class Discussion(Base):
    id = Column(Integer, primary_key=True)
    question = Column(Integer, ForeignKey('question.id'))
    content = Column(String(500), nullable=False)
    author = Column(String(10), ForeignKey('user.gid'))
    stars = Column(Integer, default=0)
