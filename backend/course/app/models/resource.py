from app.models.base import Base
from sqlalchemy import Column, String, Boolean, Integer, ForeignKey, Sequence, LargeBinary
from sqlalchemy.orm import reconstructor


class CourseResource(Base):
    id = Column(Integer, primary_key=True)
    name = Column(String(100))
    data = Column(LargeBinary)
    course_id = Column(Integer, ForeignKey('course.cid'))

    @reconstructor
    def __init__(self):
        super().__init__()
        self.fields = ['name']
