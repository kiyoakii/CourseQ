from flask import jsonify, g

from app.libs.enums import UserTypeEnum
from app.libs.error_code import Success, DeleteSuccess, UpVoteSuccess, CancelUpVoteSuccess, Duplicate, LockForbidden
from app.libs.lock import question_lock
from app.libs.redprint import Redprint
from app.libs.token_auth import login_required, role_required, enroll_required
from app.models.answer import Answer
from app.models.base import db
from app.models.discussion import DiscussionTopic
from app.models.history import History
from app.models.question import Question
from app.models.tag import Tag
from app.models.upvote import QuestionUpVote
from app.validators.forms import QuestionUpdateForm, AnswerForm, TopicCreateForm

api = Redprint('question')


@api.route('/<int:qid>', methods=['PUT'])
@role_required(UserTypeEnum.TEACHER)
@enroll_required(Question)
def update_question(qid):
    question = Question.query.get_or_404(qid)
    form = QuestionUpdateForm().validate_for_api()
    with db.auto_commit():
        for new_tag_name in form.new_tags.data:
            tag = Tag.get_or_create_tag(new_tag_name)
            question.tags.append(tag)
        for del_tag_name in form.del_tags.data:
            tag_set = Tag.query.filter_by(name=del_tag_name)
            if tag_set.count():
                try:
                    question.tags.remove(tag_set.first())
                except ValueError:
                    continue
        if form.content.data or form.title.data:
            if form.content.data != question.content or form.title.data != question.title:
                history = History.create_from_question(question)
                form.populate_obj(question)
                db.session.add(history)
    return Success()


@api.route('/<int:qid>', methods=['DELETE'])
@role_required(UserTypeEnum.TEACHER)
@enroll_required(Question)
def delete_question(qid):
    question = Question.query.get_or_404(qid)
    with db.auto_commit():
        db.session.delete(question)
    return DeleteSuccess()


@api.route('/<int:qid>', methods=['GET'])
@role_required(UserTypeEnum.STUDENT)
@enroll_required(Question)
def get_question(qid):
    question = Question.query.get_or_404(qid)
    return jsonify(question)


@api.route('/<int:qid>/answers', methods=['POST'])
@role_required(UserTypeEnum.STUDENT)
@enroll_required(Question)
def create_answer(qid):
    question = Question.query.get_or_404(qid)
    form = AnswerForm().validate_for_api()
    with db.auto_commit():
        answer = Answer(
            content=form.content.data,
            author_gid=g.user['gid'],
            # author_gid=g.user['gid']
        )
        if form.is_teacher.data:
            if not question.teacher_aid:
                question.teacher_answer = answer
                # todo: history
                # history = History.create_from_teacher_answer(answer, create_answer=True)
            else:
                return Duplicate()
        else:
            if not question.student_aid:
                question.student_answer = answer
                # todo: history
                # history = History.create_from_student_answer(answer, create_answer=True)
            else:
                return Duplicate()
        db.session.add(answer)
    return Success()


# @api.route('/<int:qid>/answers', methods=['GET'])
# @role_required(UserTypeEnum.STUDENT)
# @enroll_required(Question)
# def list_answer(qid):
#     question = Question.query.get_or_404(qid)
#     return jsonify(question.answers)


@api.route('/<int:qid>/discussions', methods=['POST'])
@role_required(UserTypeEnum.STUDENT)
@enroll_required(Question)
def create_topic(qid):
    question = Question.query.get_or_404(qid)
    form = TopicCreateForm().validate_for_api()
    with db.auto_commit():
        topic = DiscussionTopic(
            question_id=question.id,
            # author_gid=g.user['gid'],
            author_gid=g.user['gid']
        )
        form.populate_obj(topic)
        db.session.add(topic)
    return Success()


@api.route('/<int:qid>/discussions', methods=['GET'])
@role_required(UserTypeEnum.STUDENT)
@enroll_required(Question)
def list_topic(qid):
    question = Question.query.get_or_404(qid)
    return jsonify(question.discussions)


@api.route('/<int:qid>/history', methods=['GET'])
@role_required(UserTypeEnum.STUDENT)
@enroll_required(Question)
def list_history(qid):
    question = Question.query.get_or_404(qid)
    return jsonify(question.history_questions)


@api.route('/<int:qid>/like', methods=['POST'])
@role_required(UserTypeEnum.STUDENT)
@enroll_required(Question)
def up_vote(qid):
    question = Question.query.get_or_404(qid)
    question_up_vote = QuestionUpVote.query \
        .filter_by(question_id=question.id) \
        .filter_by(user_gid=g.user['gid'])
    if question_up_vote.count():
        with db.auto_commit():
            db.session.delete(question_up_vote.first())
        return CancelUpVoteSuccess()
    else:
        with db.auto_commit():
            question_up_vote = QuestionUpVote(
                question_id=question.id,
                user_gid=g.user['gid']
            )
            db.session.add(question_up_vote)
        return UpVoteSuccess()


@api.route('/<int:qid>/like', methods=['GET'])
@role_required(UserTypeEnum.STUDENT)
@enroll_required(Question)
def get_vote_num(qid):
    question = Question.query.get_or_404(qid)
    return jsonify({'likes': sum(map(lambda vote: vote.status == 1, question.up_votes))})


@api.route('/<int:qid>/lock', methods=['POST'])
@role_required(UserTypeEnum.STUDENT)
@enroll_required(Question)
def lock_question(qid):
    if not question_lock.user(qid) or question_lock.user(qid) == g.user['gid']:
        question_lock.lock(qid, g.user['gid'])
        return Success()
    return LockForbidden()


@api.route('/<int:qid>/unlock', methods=['POST'])
@role_required(UserTypeEnum.STUDENT)
@enroll_required(Question)
def unlock_question(qid):
    if question_lock.user(qid) != g.user['gid']:
        return LockForbidden()
    question_lock.unlock(qid)
    return Success()


@api.route('/<int:qid>/isLocked', methods=['GET'])
@role_required(UserTypeEnum.STUDENT)
@enroll_required(Question)
def get_lock(qid):
    return jsonify({'isLocked': question_lock.is_locked(qid), 'user': question_lock.user(qid)})
