from sqlalchemy import Column, String, Boolean, Integer, ForeignKey
from sqlalchemy.orm import relationship

from app.models.base import Base

class Question(Base):
    qid = Column(Integer, primary_key=True)
    author_id = Column(String(10), ForeignKey('user.gid'))
    stars = Column(Integer, default=0)
    answer = Column(Integer, ForeignKey('answer.id'), default=None)
    discussions = relationship('Discussion', backref='question')