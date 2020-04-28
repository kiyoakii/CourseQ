from sqlalchemy import Column, String, ForeignKey, Table
from .base import Base

enroll_table = Table('enroll',
                     Base.metadata,
                     Column('user_id', String(10), ForeignKey('user.gid')),
                     Column('course_id', String(15), ForeignKey('course.cid')))

# ta_table = Table('ta',
#                  Column('user_id', String(10), ForeignKey('user.GID')),
#                  Column('course_id', String(15), ForeignKey('course.cid')))
