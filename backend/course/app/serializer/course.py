from flask_restful import fields

course_fields = {
    'cid': fields.Integer,
    'name_zh': fields.String,
    'name_en': fields.String,
    'intro': fields.String,
    'pre_Course': fields.String,
    'textbooks': fields.String,
    'semester': fields.String,
    # 'resource': fields.String
}
