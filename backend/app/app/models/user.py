from sqlalchemy import Column, String, SmallInteger

from app.models.base import Base, db
from app.libs.enums import UserTypeEnum


class User(Base):
    GID = Column(String(10), primary_key=True)
    email = Column(String(24), unique=True, nullable=False)
    nickname = Column(String(24), unique=True)
    _auth = Column("auth", SmallInteger, default=1)

    @property
    def auth(self):
        return UserTypeEnum(self._auth)

    @auth.setter
    def auth(self, status):
        self._auth = status.value

    @staticmethod
    def register(nickname, email, GID, id):
        """
        This function is used when user login with ustc-CAS for the first time.
        :param GID: general ID for students and staffs of USTC
        :param id: student ID(length = 10) or teacher ID(length = 5)
        :return:
        """
        with db.auto_commit():
            user = User()
            user.GID = GID
            user.nickname = nickname
            # email authentication
            user.email = email
            if(len(id) != 10):
                user.auth = UserTypeEnum.TEACHER
            else:
                user.auth = UserTypeEnum.STUDENT
            # TA authentication has not been solved

