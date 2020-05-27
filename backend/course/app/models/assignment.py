from sqlalchemy import Column, String, Integer, Sequence, ForeignKey
from sqlalchemy.orm import reconstructor, relationship
import functools
from app.models.base import Base
from app.libs.error_code import Forbidden
from flask import g
from sqlalchemy.orm.exc import NoResultFound


class Assignment(Base):
    id = Column(Integer, primary_key=True)
    schedule_id = Column(Integer, ForeignKey('schedule.id'))
    title = Column(String(63))
    due = Column(Integer)

    @reconstructor
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)

        self.fields = ['id', 'schedule_id', 'title', 'due']
