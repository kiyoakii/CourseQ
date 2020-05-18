from sqlalchemy import Column, String, Integer, ForeignKey
from sqlalchemy.orm import reconstructor
from app.models.base import Base


class Answer(Base):
    id = Column(Integer, primary_key=True)
    question_id = Column(Integer, ForeignKey('question.id'))
    content = Column(String(500), nullable=False)
    author_gid = Column(String(10), ForeignKey('user.gid'))
    stars = Column(Integer, default=0)

    @reconstructor
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields = ['id', 'content', 'stars']
