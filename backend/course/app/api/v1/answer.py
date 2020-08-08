from flask import jsonify

from app.libs.error_code import CancelUpVoteSuccess, UpVoteSuccess
from app.libs.error_code import Success, DeleteSuccess
from app.libs.redprint import Redprint
from app.models.answer import Answer
from app.models.base import db
from app.models.upvote import AnswerUpVote
from app.validators.forms import AnswerForm

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


@api.route('/<int:qid>/like', methods=['POST'])
def up_vote(qid):
    answer = Answer.query.get_or_404(qid)
    answer_up_vote = AnswerUpVote.query \
        .filter_by(answer_id=answer.id) \
        .filter_by(user_gid='0000000000')
    if answer_up_vote.count():
        with db.auto_commit():
            answer_up_vote.first().delete()
        return CancelUpVoteSuccess()
    else:
        with db.auto_commit():
            answer_up_vote = AnswerUpVote(
                answer_id=answer.id,
                user_gid='0000000000'
            )
            db.session.add(answer_up_vote)
        return UpVoteSuccess()


@api.route('/<int:qid>/like', methods=['GET'])
def get_vote_num(qid):
    answer = Answer.query.get_or_404(qid)
    return jsonify({'likes': sum(map(lambda vote: vote.status == 1, answer.up_votes))})
