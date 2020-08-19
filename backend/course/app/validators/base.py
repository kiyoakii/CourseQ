from flask import request
from wtforms import Form

from app.libs.error_code import ParameterException


class BaseForm(Form):
    def __init__(self):
        if 'multipart/form-data' in request.content_type:
            data = request.form.to_dict()
        else:
            data = request.get_json(silent=True)
        args = request.args.to_dict()
        super().__init__(data=data, **args)

    def validate_for_api(self):
        valid = super(BaseForm, self).validate()
        if not valid:
            # form errors
            raise ParameterException(msg=self.errors)
        return self
