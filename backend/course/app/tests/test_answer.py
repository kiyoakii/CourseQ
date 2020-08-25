import pytest
import json
from ..models.course import Course
from ..models.answer import Answer
from app.tests.base import client
from app.tests.base import get_test_token
from app.tests.test_course import create_courses
from app.tests.test_question import create_questions


def test_create_answer(client):
    response = create_courses(client)
    assert response.status[:3] == '200', response.data
    response = create_questions(client)
    assert response.status[:3] == '200', response.data

    data = {
        "is_teacher": False,
        "content": "test_answer_content"
    }
    headers = {'Content-Type': 'application/json', 'Authorization': 'Bearer {0}'.format(get_test_token(client))}
    response = client.post('/v1/questions/1/answers', data=json.dumps(data), headers=headers)
    assert response.status[:3] == '200'
    assert Answer.query.filter_by(id=1).first().content == 'test_answer_content'


def test_get_answer(client):
    headers = {'Content-Type': 'application/json', 'Authorization': 'Bearer {0}'.format(get_test_token(client))}
    response = client.get('/v1/answers/1', headers=headers)
    assert response.status[:3] == '200'
    assert json.loads(response.data)['content'] == 'test_answer_content'


def test_update_answer(client):
    data = {
        "is_teacher": False,
        "content": "test_update_answer_content"
    }
    headers = {'Content-Type': 'application/json', 'Authorization': 'Bearer {0}'.format(get_test_token(client))}
    response = client.put('/v1/answers/1', data=json.dumps(data), headers=headers)
    assert response.status[:3] == '200'
    assert Answer.query.filter_by(id=1).first().content == 'test_update_answer_content'


def test_delete_answer(client):
    headers = {'Content-Type': 'application/json', 'Authorization': 'Bearer {0}'.format(get_test_token(client))}
    response = client.delete('/v1/answers/1', headers=headers)
    assert response.status[:3] == '204'
    assert not Answer.query.filter_by(id=1).first()