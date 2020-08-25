import pytest
import json
from ..models.course import Course
from ..models.discussion import DiscussionTopic, DiscussionAnswer
from app.tests.base import client
from app.tests.base import get_test_token
from app.tests.test_course import create_courses
from app.tests.test_question import create_questions


def test_create_topic(client):
    response = create_courses(client)
    assert response.status[:3] == '200', response.data
    response = create_questions(client)
    assert response.status[:3] == '200', response.data

    data = {
        "title": "test_topic_title",
        "content": "test_topic_content"
    }
    headers = {'Content-Type': 'application/json', 'Authorization': 'Bearer {0}'.format(get_test_token(client))}
    response = client.post('/v1/questions/1/discussions', data=json.dumps(data), headers=headers)
    assert response.status[:3] == '200'
    assert DiscussionTopic.query.filter_by(id=1).first().title == 'test_topic_title'
    assert DiscussionTopic.query.filter_by(id=1).first().content == 'test_topic_content'


def test_update_discussion(client):
    data = {
        "title": "test_update_topic_title",
        "content": "test_update_topic_content"
    }
    headers = {'Content-Type': 'application/json', 'Authorization': 'Bearer {0}'.format(get_test_token(client))}
    response = client.put('/v1/discussions/1', data=json.dumps(data), headers=headers)
    assert response.status[:3] == '200'
    assert DiscussionTopic.query.filter_by(id=1).first().content == 'test_update_topic_content'


def test_answer_discussion(client):
    data = {
        "reply_id": 123,
        "content": "test_topic_answer_content"
    }
    headers = {'Content-Type': 'application/json', 'Authorization': 'Bearer {0}'.format(get_test_token(client))}
    response = client.post('/v1/discussions/1/answer', data=json.dumps(data), headers=headers)
    assert response.status[:3] == '200'
    assert DiscussionAnswer.query.filter_by(id=1).first().content == 'test_topic_answer_content'


def test_get_answers(client):
    headers = {'Content-Type': 'application/json', 'Authorization': 'Bearer {0}'.format(get_test_token(client))}
    response = client.get('/v1/discussions/1/answer', headers=headers)
    assert response.status[:3] == '200', response.data
    res_json = json.loads(response.data)
    assert len(res_json) == 1
    assert res_json[0]['content'] == 'test_topic_answer_content'


def test_delete_answer(client):
    headers = {'Content-Type': 'application/json', 'Authorization': 'Bearer {0}'.format(get_test_token(client))}
    response = client.delete('/v1/discussions/1', headers=headers)
    assert response.status[:3] == '204'
    assert not DiscussionTopic.query.filter_by(id=1).first()