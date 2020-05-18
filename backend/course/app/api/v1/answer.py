from app.libs.redprint import Redprint
from app.validators.forms import AnswerForm
from app.models.answer import Answer
from app.models.base import db
from app.libs.error_code import Success, DeleteSuccess
from flask import jsonify

api = Redprint('answer')


@api.route('/<int:aid>/update', methods=['PUT'])
def update_answer(aid):
    answer = Answer.query.get_or_404(aid)
    form = AnswerForm().validate_for_api()
    with db.auto_commit():
        form.populate_obj(answer)
    return Success()


@api.route('/<int:aid>', methods=['GET'])
def get_answer(aid):
    answer = Answer.query.get_or_404(aid)
    return jsonify(answer)


@api.route('/<int:aid>', methods=['DELETE'])
def delete_answer(aid):
    answer = Answer.query.get_or_404(aid)
    with db.auto_commit():
        answer.delete()
    return DeleteSuccess()
