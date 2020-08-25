import pytest
import json
from ..models.assignment import Assignment
from app.tests.base import client
from app.tests.base import get_test_token
from app.tests.test_course import create_courses
from app.tests.test_schedule import create_schedule


def test_create_assignment(client):
    rsp = create_courses(client)
    assert rsp.status[:3] == '200', rsp.data
    # rsp = create_schedule(client)
    # assert rsp.status[:3] == '200', rsp.data

    data = {
        "title": "test_assignment_title",
        "ddl": "test_ddl"
    }
    headers = {'Content-Type': 'application/json', 'Authorization': 'Bearer {0}'.format(get_test_token(client))}
    response = client.post('/v1/courses/1/assignments', data=json.dumps(data), headers=headers)
    assert response.status[:3] == '200'
    assert Assignment.query.filter_by(id=1).first().title == 'test_assignment_title'
    assert Assignment.query.filter_by(id=1).first().ddl == 'test_ddl'


def test_get_assignment(client):
    headers = {'Content-Type': 'application/json', 'Authorization': 'Bearer {0}'.format(get_test_token(client))}
    response = client.get('/v1/assignments/1', headers=headers)
    assert response.status[:3] == '200', response.data
    assert json.loads(response.data)['title'] == 'test_assignment_title'
    assert json.loads(response.data)['ddl'] == 'test_ddl'


def test_update_assignment(client):
    data = {
        "title": "test_update_assignment_title",
        "ddl": "test_update_ddl"
    }
    headers = {'Content-Type': 'application/json', 'Authorization': 'Bearer {0}'.format(get_test_token(client))}
    response = client.patch('/v1/assignments/1', data=json.dumps(data), headers=headers)
    assert response.status[:3] == '200', response.data
    assert Assignment.query.filter_by(id=1).first().title == "test_update_assignment_title"
    assert Assignment.query.filter_by(id=1).first().ddl == "test_update_ddl"


def test_delete_assignment(client):
    headers = {'Content-Type': 'application/json', 'Authorization': 'Bearer {0}'.format(get_test_token(client))}
    response = client.delete('/v1/assignments/1', headers=headers)
    assert response.status[:3] == '204'
    assert not Assignment.query.filter_by(id=1).first()
