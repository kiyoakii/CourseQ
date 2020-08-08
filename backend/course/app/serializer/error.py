from flask_restful import fields

error_fields = {
    'code': fields.Integer,
    'msg': fields.String,
    'error_code': fields.Integer
}
