import pytest
import json
from ..models.course import Course
from ..models.announce import Announce
from app.tests.base import client
from app.tests.base import get_test_token
from app.tests.test_course import create_courses

def test_create_announce(client):
    response = create_courses(client)
    assert response.status == '200 OK', response.data
    data = {
        "title": 'test_announce_title',
        "content": "test_announce_content"
    }
    headers = {'Content-Type': 'application/json', 'Authorization': 'Bearer {0}'.format(get_test_token(client))}
    response = client.post('/v1/courses/1/announces', data=json.dumps(data), headers=headers)
    assert response.status == "200 OK", response.data
    assert Announce.query.filter_by(id=1).first().title == 'test_announce_title'
    assert Announce.query.filter_by(id=1).first().content == 'test_announce_content'


def test_update_announce(client):
    data = {
        "title": 'test_update_announce_title',
        "content": "test_update_announce_content"
    }
    headers = {'Content-Type': 'application/json', 'Authorization': 'Bearer {0}'.format(get_test_token(client))}
    response = client.put('/v1/announces/1', data=json.dumps(data), headers=headers)
    assert response.status == '200 OK'
    assert Announce.query.filter_by(id=1).first().title == 'test_update_announce_title'
    assert Announce.query.filter_by(id=1).first().content == 'test_update_announce_content'


def test_delete_announce(client):
    headers = {'Content-Type': 'application/json', 'Authorization': 'Bearer {0}'.format(get_test_token(client))}
    response = client.delete('/v1/announces/1', headers=headers)
    assert response.status[:3] == '204'
    assert not Announce.query.filter_by(id=1).first()