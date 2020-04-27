from sqlalchemy import Column, String, Boolean, Integer, ForeignKey
from sqlalchemy.orm import relationship

from app.models.base import Base
from app.models.enroll import enroll_table


class Course(Base):
    cid = Column(String(15), primary_key=True)
    name_zh = Column(String(20), nullable=False)
    name_en = Column(String(20), nullable=False)
    # teachers, students
    users = relationship('User', secondary=enroll_table,
                         back_populates='courses')
    # TAs = relationship('User', secondary=ta_table,
    #                    back_populates='courses')
    intro = Column(String(200))
    pre_Course = Column(String(50))
    textbooks = Column(String(50))
    semester = Column(String(50))
