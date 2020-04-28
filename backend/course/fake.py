from app import create_app
from app.libs.enums import UserTypeEnum
from app.models.base import db
from app.models.user import User

app = create_app()
with app.app_context():
    with db.auto_commit():
        # 创建一个超级管理员
        user = User()
        user.nickname = 'Super'
        user.GID = '0000000000'
        user.email = '999@ustc.edu.cn'
        user.auth = UserTypeEnum.MANAGER
        db.session.add(user)
