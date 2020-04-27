from urllib.parse import urlencode
from urllib.request import urlopen
from xml.etree import ElementTree

from flask import current_app
from sqlalchemy import Column, String, SmallInteger
from sqlalchemy.orm import relationship

from app.libs.error_code import AuthFailed
from app.models.base import Base, db
from app.libs.enums import UserTypeEnum
from app.models.enroll import enroll_table


class User(Base):
    gid = Column(String(10), primary_key=True)
    email = Column(String(24), unique=True, nullable=False)
    nickname = Column(String(24), unique=True)
    _auth = Column("auth", SmallInteger)
    # courses = relationship('Course', secondary=enroll_table, back_populates='users')

    @property
    def auth(self):
        return UserTypeEnum(self._auth)

    @auth.setter
    def auth(self, status):
        self._auth = status.value

    @staticmethod
    def register(nickname, email, gid, uid):
        """
        This function is used when user login with ustc-CAS for the first time.
        :param gid: general ID for students and staffs of USTC
        :param uid: student ID(length = 10) or teacher ID(length = 5)
        :return:
        """
        with db.auto_commit():
            user = User()
            user.GID = gid
            user.nickname = nickname
            # email authentication
            user.email = email
            if(len(uid) != 10):
                user.auth = UserTypeEnum.TEACHER
            else:
                user.auth = UserTypeEnum.STUDENT
            # TA authentication has not been solved
            db.add(user)

