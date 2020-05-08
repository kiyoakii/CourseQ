
SQLALCHEMY_TRACK_MODIFICATIONS = False
TOKEN_EXPIRATION = 30 * 24 * 3600
VALIDATE_URL = "https://passport.ustc.edu.cn/serviceValidate"
DEBUG = 1

# email authentication
MAIL_SERVER="mail.ustc.edu.cn"
MAIL_PORT = 465
# Change the following 2 lines to a common email account
# to send authentication emails
MAIL_USERNAME = 'email-address'
MAIL_PASSWORD = 'password'
MAIL_USE_TLS = False
MAIL_USE_SSL = True
MAIL_PREFIX="[USTC-SE]"