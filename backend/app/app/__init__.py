from .app import Flask


def register_blueprints(app):
    from app.api.v1 import create_blueprint_v1
    app.register_blueprint(create_blueprint_v1(), url_prefix='/v1')


def register_plugin(app):
    from app.models.base import db
    db.init_app(app)
    with app.app_context():
        db.create_all()


def create_app():
    app = Flask(__name__)
    app.config.from_object('app.config.settings')
    app.config.from_object('app.config.secure')

    register_blueprints(app)
    register_plugin(app)

    return app

# def create_app():
#     app = Flask(__name__)
#     db.init_app(app)
#     login_manager.init_app(app)
#     app.config['SECRET_KEY'] = 'your secret key'
#     app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///db.sqlite'
#
#     from .models import User
#
#     @login_manager.user_loader
#     def load_user(user_id):
#         return User.query.get(int(user_id))
#
#     from .auth import auth as auth_blueprint
#     app.register_blueprint(auth_blueprint, url_prefix='/auth')
#     return app
