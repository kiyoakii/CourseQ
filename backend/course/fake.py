from app import create_app
from app.libs.enums import UserTypeEnum
from app.models.base import db
from app.models.user import User

app = create_app()
with app.app_context():
    with db.auto_commit():
        for i in range(100, 200):
            # 创建亿个超级管理员
            user = User()
            user.nickname = 'Super' + str(i)
            user.gid = '%010d' % i
            user.email = '999{0}@ustc.edu.cn'.format(i)
            user.auth = UserTypeEnum.MANAGER
            db.session.add(user)
        for i in range(200, 300):
            # 创建亿个老师
            user = User()
            user.nickname = 'Super' + str(i)
            user.gid = '%010d' % i
            user.email = '999{0}@ustc.edu.cn'.format(i)
            user.auth = UserTypeEnum.TEACHER
            db.session.add(user)
        for i in range(300, 400):
            user = User()
            user.nickname = 'Super' + str(i)
            user.gid = '%010d' % i
            user.email = '999{0}@ustc.edu.cn'.format(i)
            user.auth = UserTypeEnum.STUDENT
            db.session.add(user)
