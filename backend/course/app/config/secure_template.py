"""
This is the template for secure.py, please created your own secure.py this way.
"""
import os
from os import getenv
from os.path import join

SQLALCHEMY_DATABASE_URI = \
    'mysql+pymysql://{0}:{1}@{2}:{3}/{4}'.format(
        getenv('MYSQL_USER'),
        getenv('MYSQL_PWD'),
        getenv('MYSQL_HOST'),
        getenv('MYSQL_PORT') or '3306',
        getenv('DATABASE_NAME')
    )

# SECRET_KEY = 'Lin Huancheng wudi'
UPLOAD_FOLDER = join(os.path.abspath(os.path.join(os.getcwd())), "static/uploads")
ALLOWED_EXTENSIONS = ['*']
MAX_CONTENT_LENGTH = 1000 * 1024 * 1024  # 1000mb
HOST = 'http://localhost/'
JWT_SECRET_KEY = 'Lin Huancheng zuishuai'

LOCK_TIMEOUT = 20

# Uncomment this line when testing with pytest
# DEBUG = False

# email authentication
MAIL_SERVER="smtp.163.com"
MAIL_PORT = 465
# Change the following 2 lines to a common email account
# to send authentication emails
MAIL_USERNAME = 'ustc_se_sender@163.com'
MAIL_PASSWORD = 'ASRBXEKXRUNWBKZF'
MAIL_USE_TLS = False
MAIL_USE_SSL = True
MAIL_PREFIX="[USTC-SE]"
EMAIL_AUTH_SECRET_KEY = 'Lin Huancheng zuishuai'
