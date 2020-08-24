from flask import jsonify

from app.libs.error_code import Success, DeleteSuccess
from app.libs.redprint import Redprint
from app.libs.token_auth import login_required
from app.models.answer import Answer
from app.models.base import db
from app.models.history import History
from app.validators.forms import AnswerForm

api = Redprint('answer')


@api.route('/<int:aid>', methods=['PUT'])
@login_required
def update_answer(aid):
    answer = Answer.query.get_or_404(aid)
    form = AnswerForm().validate_for_api()
    with db.auto_commit():
        if form.content.data != answer.content:
            if form.is_teacher.data:
                history = History.create_from_teacher_answer(answer)
            else:
                history = History.create_from_student_answer(answer)
            form.populate_obj(answer)
            db.session.add(history)
    return Success()


@login_required
@api.route('/<int:aid>', methods=['GET'])
def get_answer(aid):
    answer = Answer.query.get_or_404(aid)
    return jsonify(answer)


@api.route('/<int:aid>', methods=['DELETE'])
@login_required
def delete_answer(aid):
    answer = Answer.query.get_or_404(aid)
    with db.auto_commit():
        db.session.delete(answer)
    return DeleteSuccess()


@api.route('/<int:qid>/like', methods=['GET'])
@login_required
def get_vote_num(qid):
    answer = Answer.query.get_or_404(qid)
    return jsonify({'likes': sum(map(lambda vote: vote.status == 1, answer.up_votes))})
