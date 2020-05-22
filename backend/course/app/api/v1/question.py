from app.libs.redprint import Redprint
from app.models.question import Question, HistoryQuestion
from app.models.answer import Answer
from app.models.tag import Tag
from app.validators.forms import QuestionUpdateForm, AnswerForm, TopicCreateForm
from app.models.base import db
from app.models.discussion import DiscussionTopic
from app.libs.error_code import Success, DeleteSuccess, UpVoteSuccess, CancelUpVoteSuccess
from flask import jsonify, g
from app.models.upvote import QuestionUpVote

api = Redprint('question')


@api.route('/<int:qid>', methods=['PUT'])
def update_question(qid):
    question = Question.query.get_or_404(qid)
    form = QuestionUpdateForm().validate_for_api()
    with db.auto_commit():
        form.populate_obj(question)
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
            history_question = HistoryQuestion()
            form.populate_obj(history_question)
            history_question.create_time = question.update_time
            question.history_questions.append(history_question)
            db.session.add(history_question)
    return Success()


@api.route('/<int:qid>', methods=['DELETE'])
def delete_question(qid):
    question = Question.query.get_or_404(qid)
    with db.auto_commit():
        question.delete()
    return DeleteSuccess()


@api.route('/<int:qid>', methods=['GET'])
def get_question(qid):
    question = Question.query.get_or_404(qid)
    return jsonify(question)


@api.route('/<int:qid>/star', methods=['POST'])
def star_question(qid):
    pass


@api.route('/<int:qid>/answers', methods=['POST'])
def create_answer(qid):
    question = Question.query.get_or_404(qid)
    form = AnswerForm().validate_for_api()
    with db.auto_commit():
        answer = Answer(
            content=form.content.data,
            question_id=question.id,
            author_gid='0000000000',
            # author_gid=g.user.gid
        )
        db.session.add(answer)
    return Success()


@api.route('/<int:qid>/answers', methods=['GET'])
def list_answer(qid):
    question = Question.query.get_or_404(qid)
    return jsonify(question.answers)


@api.route('/<int:qid>/discussions', methods=['POST'])
def create_topic(qid):
    question = Question.query.get_or_404(qid)
    form = TopicCreateForm().validate_for_api()
    with db.auto_commit():
        topic = DiscussionTopic(
            question_id=question.id,
            # author_gid=g.user.gid,
            author_gid='0000000000'
        )
        form.populate_obj(topic)
        db.session.add(topic)
    return Success()


@api.route('/<int:qid>/discussions', methods=['GET'])
def list_topic(qid):
    question = Question.query.get_or_404(qid)
    return jsonify(question.discussions)


@api.route('/<int:qid>/history', methods=['GET'])
def list_history(qid):
    question = Question.query.get_or_404(qid)
    return jsonify(question.history_questions)


@api.route('/<int:qid>/like', methods=['POST'])
def up_vote(qid):
    question = Question.query.get_or_404(qid)
    question_up_vote = QuestionUpVote.query \
        .filter_by(question_id=question.id) \
        .filter_by(user_gid='0000000000')
    if question_up_vote.count():
        with db.auto_commit():
            question_up_vote.first().delete()
        return CancelUpVoteSuccess()
    else:
        with db.auto_commit():
            question_up_vote = QuestionUpVote(
                question_id=question.id,
                user_gid='0000000000'
            )
            db.session.add(question_up_vote)
        return UpVoteSuccess()


@api.route('/<int:qid>/like', methods=['GET'])
def get_vote_num(qid):
    question = Question.query.get_or_404(qid)
    return jsonify({'likes': sum(map(lambda vote: vote.status == 1, question.up_votes))})
