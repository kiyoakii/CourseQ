from app.libs.redprint import Redprint
from app.validators.forms import TopicUpdateForm
from app.models.discussion import DiscussionTopic
from app.models.base import db
from app.libs.error_code import Success, DeleteSuccess
from flask import jsonify

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
