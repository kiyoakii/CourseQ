import pytest
import json
from ..models.schedule import Schedule
from app.tests.base import client
from app.tests.base import get_test_token
from app.tests.test_course import create_courses


def create_schedule(client):
    data = {
        "week": 11,
        "topic": "test_schedule_topic",
        "datetime": "2000-01-01",
        "reference": "test_schedule_reference"
    }
    headers = {'Content-Type': 'application/json', 'Authorization': 'Bearer {0}'.format(get_test_token(client))}
    response = client.post('/v1/courses/1/schedules', data=json.dumps(data), headers=headers)
    return response


def test_create_schedule(client):
    rsp = create_courses(client)
    assert rsp.status[:3] == '200', rsp.data
    rsp = create_schedule(client)
    assert rsp.status[:3] == '200', rsp.data

    assert Schedule.query.filter_by(id=1).first().week == 11
    assert Schedule.query.filter_by(id=1).first().topic == 'test_schedule_topic'
    assert Schedule.query.filter_by(id=1).first().datetime == '2000-01-01'
    assert Schedule.query.filter_by(id=1).first().reference == 'test_schedule_reference'


def test_get_schedule(client):
    headers = {'Content-Type': 'application/json', 'Authorization': 'Bearer {0}'.format(get_test_token(client))}
    rsp = client.get('/v1/schedules/1')
    assert rsp.status == '200 OK', rsp.data
    rsp_json = json.loads(rsp.data)
    assert rsp_json['week'] == 11
    assert rsp_json['topic'] == "test_schedule_topic"
    assert rsp_json['datetime'] == "2000-01-01"
    assert rsp_json['reference'] == "test_schedule_reference"


def test_update_schedule(client):
    data = {
        "week": 12,
        "topic": "test_update_schedule_topic",
        "datetime": "2000-01-02",
        "reference": "test_update_schedule_reference"
    }
    headers = {'Content-Type': 'application/json', 'Authorization': 'Bearer {0}'.format(get_test_token(client))}
    response = client.put('/v1/schedules/1', data=json.dumps(data), headers=headers)
    assert response.status == '200 OK'
    assert Schedule.query.filter_by(id=1).first().week == 12
    assert Schedule.query.filter_by(id=1).first().topic == 'test_update_schedule_topic'
    assert Schedule.query.filter_by(id=1).first().datetime == '2000-01-02'
    assert Schedule.query.filter_by(id=1).first().reference == 'test_update_schedule_reference'


def test_delete_schedule(client):
    headers = {'Content-Type': 'application/json', 'Authorization': 'Bearer {0}'.format(get_test_token(client))}
    response = client.delete('/v1/schedules/1', headers=headers)
    assert response.status[:3] == '204'
    assert not Schedule.query.filter_by(id=1).first()