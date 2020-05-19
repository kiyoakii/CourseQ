from app.libs.redprint import Redprint
from app.validators.forms import TopicUpdateForm, TopicAnswerForm
from app.models.discussion import DiscussionTopic, DiscussionAnswer
from app.models.base import db
from app.libs.error_code import Success, DeleteSuccess
from flask import jsonify, g

api = Redprint('topic_answer')


@api.route('/<int:topic_answer_id>', methods=['POST'])
def answer_discussion(topic_answer_id):
    topic_answer = DiscussionAnswer.query.get_or_404(topic_answer_id)
    form = TopicAnswerForm().validate_for_api()
    with db.auto_commit():
        answer = DiscussionAnswer(
            content=form.content.data,
            topic_id=topic_answer.topic_id,
            reply_id=topic_answer.id,
            author_id=g.user.gid
        )
        db.session.add(answer)
    return Success()


@api.route('/<int:topic_answer_id>', methods=['GET'])
def get_answer_discussion(topic_answer_id):
    topic_answer = DiscussionAnswer.query.get_or_404(topic_answer_id)
    return jsonify(topic_answer)


@api.route('/<int:topic_answer_id>', methods=['PUT'])
def update_answer_discussion(topic_answer_id):
    topic_answer = DiscussionAnswer.query.get_or_404(topic_answer_id)
    form = TopicAnswerForm().validate_for_api()
    with db.auto_commit():
        topic_answer.content = form.content.data
    return jsonify(topic_answer)


@api.route('/<int:topic_answer_id>', methods=['DELETE'])
def delete_answer_discussion(topic_answer_id):
    topic_answer = DiscussionAnswer.query.get_or_404(topic_answer_id)
    with db.auto_commit():
        topic_answer.delete()
    return DeleteSuccess()
