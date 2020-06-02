from flask import jsonify

from app.libs.error_code import Success, DeleteSuccess
from app.libs.redprint import Redprint
from app.models.base import db
from app.models.discussion import DiscussionTopic, DiscussionAnswer
from app.validators.forms import TopicUpdateForm, TopicAnswerForm

api = Redprint('discussion')


@api.route('/<int:did>', methods=['PUT'])
def update_discussion(did):
    topic = DiscussionTopic.query.get_or_404(did)
    form = TopicUpdateForm().validate_for_api()
    with db.auto_commit():
        form.populate_obj(topic)
    return Success()


@api.route('/<int:did>', methods=['DELETE'])
def delete_discussion(did):
    topic = DiscussionTopic.query.get_or_404(did)
    with db.auto_commit():
        topic.delete()
    return DeleteSuccess()


@api.route('/<int:did>/answer', methods=['POST'])
def answer_discussion(did):
    topic = DiscussionTopic.query.get_or_404(did)
    form = TopicAnswerForm().validate_for_api()
    with db.auto_commit():
        answer = DiscussionAnswer(
            content=form.content.data,
            topic_id=topic.id,
            # author_id=g.user.gid
            author_gid='0000000000'
        )
        db.session.add(answer)
    return Success()


@api.route('/<int:did>/answer', methods=['GET'])
def get_answers(did):
    topic = DiscussionTopic.query.get_or_404(did)
    return jsonify(DiscussionAnswer.query.filter_by(topic_id=topic.id).all())
