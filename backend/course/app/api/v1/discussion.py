from flask import jsonify, g

from app.libs.enums import UserTypeEnum
from app.libs.error_code import Success, DeleteSuccess
from app.libs.redprint import Redprint
from app.libs.token_auth import login_required, role_required, enroll_required
from app.models.base import db
from app.models.discussion import DiscussionTopic, DiscussionAnswer
from app.validators.forms import TopicUpdateForm, TopicAnswerForm

api = Redprint('discussion')


@api.route('/<int:did>', methods=['PUT'])
@role_required(UserTypeEnum.TEACHER)
@enroll_required(DiscussionTopic)
def update_discussion(did):
    topic = DiscussionTopic.query.get_or_404(did)
    form = TopicUpdateForm().validate_for_api()
    with db.auto_commit():
        form.populate_obj(topic)
    return Success()


@api.route('/<int:did>', methods=['DELETE'])
@role_required(UserTypeEnum.TEACHER)
@enroll_required(DiscussionTopic)
def delete_discussion(did):
    topic = DiscussionTopic.query.get_or_404(did)
    with db.auto_commit():
        db.session.delete(topic)
    return DeleteSuccess()


@api.route('/<int:did>/answer', methods=['POST'])
@role_required(UserTypeEnum.STUDENT)
@enroll_required(DiscussionTopic)
def answer_discussion(did):
    topic = DiscussionTopic.query.get_or_404(did)
    form = TopicAnswerForm().validate_for_api()
    with db.auto_commit():
        answer = DiscussionAnswer(
            content=form.content.data,
            topic_id=topic.id,
            author_gid=g.user['gid']
        )
        db.session.add(answer)
    return Success()


@api.route('/<int:did>/answer', methods=['GET'])
@role_required(UserTypeEnum.STUDENT)
@enroll_required(DiscussionTopic)
def get_answers(did):
    topic = DiscussionTopic.query.get_or_404(did)
    return jsonify(DiscussionAnswer.query.filter_by(topic_id=topic.id).all())
