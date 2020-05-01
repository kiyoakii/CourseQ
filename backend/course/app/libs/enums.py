from enum import Enum


class UserTypeEnum(Enum):
    STUDENT = 1
    TEACHER = 2
    MANAGER = 3
    TA = 4

    @classmethod
    def user_str(cls, status):
        key_map = {
            cls.STUDENT: '学生',
            cls.TEACHER: '老师',
            cls.MANAGER: '管理员',
            cls.TA: '助教',
        }
        return key_map[status]
