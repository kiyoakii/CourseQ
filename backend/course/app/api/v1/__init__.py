from flask import Blueprint

from app.api.v1 import user, token, course, resource, answer, question, discussion, topic_answer, schedule, assignment, \
    announce


def create_blueprint_v1():
    bp_v1 = Blueprint('v1', __name__)
    user.api.register(bp_v1, url_prefix='/users')
    token.api.register(bp_v1, url_prefix='/token')
    course.api.register(bp_v1, url_prefix='/courses')
    resource.api.register(bp_v1, url_prefix='/resources')
    answer.api.register(bp_v1, url_prefix='/answers')
    question.api.register(bp_v1, url_prefix='/questions')
    discussion.api.register(bp_v1, url_prefix='/discussions')
    topic_answer.api.register(bp_v1, url_prefix='/topic_answers')
    schedule.api.register(bp_v1, url_prefix='/schedules')
    assignment.api.register(bp_v1, url_prefix='/assignments')
    announce.api.register(bp_v1, url_prefix='/announces')
    return bp_v1
