from sqlalchemy import Column, String, Boolean, Integer, ForeignKey, Sequence, LargeBinary
from sqlalchemy.orm import reconstructor, relationship

from app.models.base import Base


class Course(Base):
    # todo return users json
    cid = Column(Integer, Sequence('course_id_seq'), primary_key=True)
    name_zh = Column(String(40), nullable=False)
    name_en = Column(String(40), nullable=False)
    intro = Column(String(200))
    pre_Course = Column(String(50))
    textbooks = Column(String(50))
    semester = Column(String(50))
    resource = relationship("CourseResource")

    @reconstructor
    def __init__(self):
        super().__init__()
        self.fields = ['cid', 'name_zh', 'name_en', 'intro',
                       'pre_Course', 'textbooks', 'semester']
