import pytest
import json
from ..models.course import Course
from ..models.question import Question
from app.tests.base import client
from app.tests.base import get_test_token
from app.tests.test_course import create_courses


def create_questions(client):
    data = {
        "title": "test_question_title",
        "content": "test_question_content"
    }
    headers = {'Content-Type': 'application/json', 'Authorization': 'Bearer {0}'.format(get_test_token(client))}
    response = client.post('/v1/courses/1/questions', data=json.dumps(data), headers=headers)
    return response


def test_create_questions(client):
    response = create_courses(client)
    assert response.status[:3] == '200', response.data

    response = create_questions(client)
    assert response.status == "200 OK", response.data
    assert Question.query.filter_by(id=1).first().title == 'test_question_title'
    assert Question.query.filter_by(id=1).first().content == 'test_question_content'


def test_update_question(client):
    data = {
        "title": "test_update_question_title",
        "content": "test_update_question_content"
    }
    headers = {'Content-Type': 'application/json', 'Authorization': 'Bearer {0}'.format(get_test_token(client))}
    response = client.put('/v1/questions/1', data=json.dumps(data), headers=headers)
    assert response.status[:3] == '200', response.data
    assert Question.query.filter_by(id=1).first().title == 'test_update_question_title'
    assert Question.query.filter_by(id=1).first().content == 'test_update_question_content'


def test_get_question(client):
    headers = {'Content-Type': 'application/json', 'Authorization': 'Bearer {0}'.format(get_test_token(client))}
    response = client.get('/v1/questions/1', headers=headers)
    assert response.status[:3] == '200'
    assert json.loads(response.data)['title'] == 'test_update_question_title'
    assert json.loads(response.data)['content'] == 'test_update_question_content'


def test_delete_question(client):
    headers = {'Content-Type': 'application/json', 'Authorization': 'Bearer {0}'.format(get_test_token(client))}
    response = client.delete('/v1/questions/1', headers=headers)
    assert response.status[:3] == '204'
    assert not Question.query.filter_by(id=1).first()

