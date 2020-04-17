from . import auth
from ..models import User
from flask import jsonify, request
from flask_login import login_user, logout_user, login_required
from werkzeug.security import generate_password_hash, gen_salt, check_password_hash
from .. import db


@auth.route('/login', methods=['POST'])
def login():
    username = request.form.get('username')
    password = request.form.get('password')
    user = User.query.filter_by(username=username).first()
    if not user or not check_password_hash(user.password, password):
        return jsonify({'msg': 'Wrong username or password!', 'code': 401})
    login_user(user)
    return jsonify({'msg': 'Successfully login!', 'code': 200})


@auth.route('/register', methods=['POST'])
def register():
    email = request.form.get('email')
    username = request.form.get('username')
    password = request.form.get('password')
    test_email_user = User.query.filter_by(email=email).first()
    test_username_user = User.query.filter_by(username=username).first()
    if test_email_user:
        return jsonify({'msg': 'Email exists!', 'code': 409})
    if test_username_user:
        return jsonify({'msg': 'Username exists!', 'code': 409})
    new_user = User(email=email, username=username, password=generate_password_hash(password, method='sha256'))
    db.session.add(new_user)
    db.session.commit()
    return jsonify({'msg': 'Successfully register', 'code': 200})


@auth.route('/logout', methods=['POST'])
@login_required
def logout():
    logout_user()
    return jsonify({'msg': 'Successfully logout', 'code': 200})
