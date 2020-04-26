from app import create_app
from app.models.base import db
from app.models.user import User

app = create_app()
with app.app_context():
    with db.auto_commit():
        # 创建一个超级管理员
        user = User()
        user.nickname = 'Super'
        user.GID = '0000000000'
        user.email = '999@mail.ustc.edu.cn'
        user.auth = 4
        db.session.add(user)
