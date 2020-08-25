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
            cls.TEACHER: '老师',
            cls.MANAGER: '管理员',
            cls.TA: '助教',
        }
        return key_map[status]

    @classmethod
    def scope_to_role(cls, scope):
        key_map = {
            'StudentScope': cls.STUDENT,
            'AdminScope': cls.MANAGER,
            'TeacherScope': cls.TEACHER,
        }
        return key_map.get(scope, None)