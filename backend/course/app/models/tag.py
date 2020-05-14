from sqlalchemy import Column, String, Integer
from sqlalchemy.orm import relationship

from app.models.base import Base


class Tag(Base):
    id = Column(Integer, primary_key=True)
    name = Column(String(20))
    questions = relationship('Question', backref='tag', secondary='QuestionTag')
