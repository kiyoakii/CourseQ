from flask import jsonify, g

from app.libs.enums import UserTypeEnum
from app.libs.error_code import Success, DeleteSuccess
from app.libs.redprint import Redprint
from app.libs.token_auth import login_required, enroll_required, role_required
from app.models.answer import Answer
from app.models.base import db
from app.models.history import History
from app.validators.forms import AnswerForm

api = Redprint('answer')


@api.route('/<int:aid>', methods=['PUT'])
@role_required(UserTypeEnum.STUDENT)
@enroll_required(Answer)
def update_answer(aid):
    answer = Answer.query.get_or_404(aid)
    form = AnswerForm().validate_for_api()
    with db.auto_commit():
        if form.content.data != answer.content:
            if g.user['scope'] == 'TeacherScope':
                history = History.create_from_teacher_answer(answer)
            else:
                history = History.create_from_student_answer(answer)
            form.populate_obj(answer)
            db.session.add(history)
    return Success()


@api.route('/<int:aid>', methods=['GET'])
@role_required(UserTypeEnum.TEACHER)
@enroll_required(Answer)
def get_answer(aid):
    answer = Answer.query.get_or_404(aid)
    return jsonify(answer)


@api.route('/<int:aid>', methods=['DELETE'])
@role_required(UserTypeEnum.TEACHER)
@enroll_required(Answer)
def delete_answer(aid):
    answer = Answer.query.get_or_404(aid)
    with db.auto_commit():
        db.session.delete(answer)
    return DeleteSuccess()


@api.route('/<int:qid>/like', methods=['GET'])
@role_required(UserTypeEnum.STUDENT)
@enroll_required(Answer)
def get_vote_num(qid):
    answer = Answer.query.get_or_404(qid)
    return jsonify({'likes': sum(map(lambda vote: vote.status == 1, answer.up_votes))})
