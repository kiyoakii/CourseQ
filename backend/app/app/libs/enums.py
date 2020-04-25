
from enum import Enum

class UserTypeEnum(Enum):
    STUDENT = 1
    TA = 2
    TEACHER = 3
    MANAGER = 4

    @classmethod
    def user_str(cls, status):
        key_map = {
            cls.STUDENT: '学生',
            cls.TA: '助教',
            cls.TEACHER: '老师',
            cls.MANAGER: '管理员'
        }
        return key_map[status]