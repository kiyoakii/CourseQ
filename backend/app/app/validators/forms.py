from wtforms import StringField
from wtforms.validators import DataRequired, length, Email
from wtforms import ValidationError

from app.models.user import User
from app.validators.base import BaseForm as Form


class UserForm(Form):
    account = StringField(validators=[
        Email(message='invalid email')
    ])
    nickname = StringField(validators=[DataRequired(),
                                       length(min=4, max=22)])

    def validate_account(self, value):
        """ Used for validation before changing email"""
        if User.query.filter_by(email=value.data).first():
            raise ValidationError()


class TokenForm(Form):
    token = StringField(validators=[DataRequired()])