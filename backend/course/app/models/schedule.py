from sqlalchemy import Column, String, Integer, ForeignKey
from sqlalchemy.orm import reconstructor, relationship

from app.models.base import Base
from app.models.relation import assignment_schedule_table


class Schedule(Base):
    id = Column(Integer, primary_key=True)
    course_id = Column(Integer, ForeignKey('course.cid'))
    week = Column(Integer)
    topic = Column(String(255))
    reference = Column(String(255))
    assignments = relationship('Assignment', secondary=assignment_schedule_table)

    @reconstructor
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields = ['id', 'week', 'topic', 'reference', 'assignments']
