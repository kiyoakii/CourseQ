from sqlalchemy import Column, String, Integer, ForeignKey, LargeBinary
from sqlalchemy.orm import reconstructor

from app.models.base import Base


class CourseResource(Base):
    id = Column(Integer, primary_key=True)
    name = Column(String(100))
    data = Column(LargeBinary)
    course_id = Column(Integer, ForeignKey('course.cid'))

    @reconstructor
    def __init__(self):
        super().__init__()
        self.fields = ['id', 'name']
