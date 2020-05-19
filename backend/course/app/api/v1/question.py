from app.libs.redprint import Redprint
from app.models.question import Question
from app.models.answer import Answer
from app.models.tag import Tag
from app.validators.forms import QuestionUpdateForm, AnswerForm, TopicCreateForm
from app.models.base import db
from app.models.discussion import DiscussionTopic
from app.libs.error_code import Success, DeleteSuccess
from flask import jsonify, g

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
        answer = Answer(content=form.content.data, question_id=question.id, author_gid=g.user.gid)
        db.session.add(answer)
    return Success()


@api.route('/<int:qid>/answers', methods=['GET'])
def list_answer(qid):
    question = Question.query.get_or_404(qid)
    return jsonify(Answer.query.filter_by(question_id=question.id).all())


@api.route('/<int:qid>/discussions', methods=['POST'])
def create_topic(qid):
    question = Question.query.get_or_404(qid)
    form = TopicCreateForm().validate_for_api()
    with db.auto_commit():
        topic = DiscussionTopic(
            question_id=question.id,
            author_gid=g.user.gid
        )
        form.populate_obj(topic)
        db.session.add(topic)
    return Success()


@api.route('/<int:qid>/discussions', methods=['GET'])
def list_topic(qid):
    question = Question.query.get_or_404(qid)
    return jsonify(DiscussionTopic.query.filter_by(question_id=question.id).all())
