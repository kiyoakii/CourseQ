import pytest
import json
from ..models.course import Course
from app.tests.base import client
from app.tests.base import get_test_token


def create_courses(client):
    data = {
        "intro": "test_intro",
        "name_en": "test_name_en",
        "name_zh": "test_name_zh",
        "pre_course": "test_pre_course",
        "semester": "test_semester",
        "textbooks": "test_textbooks",
        "series": "test_series"
    }
    headers = {'Content-Type': 'application/json', 'Authorization': 'Bearer {0}'.format(get_test_token(client))}
    response = client.post('/v1/courses', data=json.dumps(data), headers=headers)
    return response


def test_create_courses(client):
    response = create_courses(client)
    assert response.status == '200 OK', response.data
    assert Course.query.filter_by(cid=1).first().name_en == 'test_name_en'
    assert Course.query.filter_by(cid=1).first().name_zh == 'test_name_zh'
    assert Course.query.filter_by(cid=1).first().pre_course == 'test_pre_course'
    assert Course.query.filter_by(cid=1).first().semester == 'test_semester'
    assert Course.query.filter_by(cid=1).first().textbooks == 'test_textbooks'
    assert Course.query.filter_by(cid=1).first().series == 'test_series'


def test_get_course(client):
    headers = {'Content-Type': 'application/json', 'Authorization': 'Bearer {0}'.format(get_test_token(client))}
    response = client.get('/v1/courses/1', headers=headers)
    res_json = json.loads(response.data)
    assert response.status == '200 OK', res_json
    assert res_json['intro'] == 'test_intro'
    assert res_json['name_en'] == 'test_name_en'
    assert res_json['name_zh'] == 'test_name_zh'
    assert res_json['pre_course'] == 'test_pre_course'
    assert res_json['semester'] == 'test_semester'


def test_update_course(client):
    data = {
        "intro": "test_update_intro",
        "name_en": "test_update_name_en",
        "name_zh": "test_update_name_zh",
        "pre_course": "test_update_pre_course",
        "semester": "test_update_semester",
        "textbooks": "test_update_textbooks",
        "series": "test_update_series"
    }
    headers = {'Content-Type': 'application/json', 'Authorization': 'Bearer {0}'.format(get_test_token(client))}
    response = client.put('/v1/courses/1', data=json.dumps(data), headers=headers)
    assert response.status == '200 OK', response.data
    assert Course.query.filter_by(cid=1).first().name_en == 'test_update_name_en'
    assert Course.query.filter_by(cid=1).first().name_zh == 'test_update_name_zh'


def test_delete_course(client):
    headers = {'Content-Type': 'application/json', 'Authorization': 'Bearer {0}'.format(get_test_token(client))}
    response = client.delete('/v1/courses/1', headers=headers)
    assert response.status == '204 NO CONTENT', response.data
    assert not Course.query.filter_by(cid=1).first()
