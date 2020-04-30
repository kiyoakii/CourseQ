from urllib.parse import urlencode
from urllib.request import urlopen
from xml.etree import ElementTree

from flask import current_app
from sqlalchemy import Column, String, SmallInteger
from sqlalchemy.orm import relationship

from app.libs.enums import UserTypeEnum
from app.libs.error_code import AuthFailed
from app.models.base import Base, db
from app.models.enroll import enroll_table


class User(Base):
    gid = Column(String(10), primary_key=True)
    email = Column(String(24), unique=True, nullable=False)
    nickname = Column(String(24), unique=True)
    _auth = Column("auth", SmallInteger)
    courses = relationship('Course', secondary=enroll_table, back_populates='users')

    @property
    def auth(self):
        return UserTypeEnum(self._auth)

    @auth.setter
    def auth(self, status):
        self._auth = status.value

    def keys(self):
        return 'gid', 'email', 'nickname', 'auth'

    @staticmethod
    def verify(ticket, service):
        gid, uid = User.check_ticket(ticket, service)
        # uid can be used to identify the grade of users
        if not gid:
            raise AuthFailed()

        user = User.query.filter_by(gid=gid).first()
        if not user:
            scope = 'Scope'
        elif user.auth == UserTypeEnum.MANAGER:
            scope = 'AdminScope'
        elif user.auth == UserTypeEnum.TEACHER:
            scope = 'TeacherScope'
        elif user.auth == UserTypeEnum.STUDENT:
            scope = 'StudentScope'
        return {'gid': gid, 'scope': scope, 'uid': uid}


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
            user.gid = gid
            user.nickname = nickname
            # email authentication
            user.email = email
            user.uid = uid
            if len(uid) != 10:
                user.auth = UserTypeEnum.TEACHER
            else:
                user.auth = UserTypeEnum.STUDENT
            db.session.add(user)

    @staticmethod
    def check_ticket(ticket, service):
        validate = (current_app.config['VALIDATE_URL'] + "?" +
                    urlencode({"service": service, "ticket": ticket}))
        with urlopen(validate) as req:
            tree = ElementTree.fromstring(req.read())[0]
        cas = "{http://www.yale.edu/tp/cas}"
        if tree.tag == cas + "authenticationFailure":
            raise AuthFailed()
        gid = tree.find("attributes").find(cas + "gid").text.strip()
        uid = tree.find(cas + "user").text.strip()
        return gid, uid
