import pytest
import json
from ..models.course import Course
from ..models.resource import CourseResource
from app.tests.base import client
from app.tests.base import get_test_token
from app.tests.test_course import create_courses
import io


def test_upload(client):
    response = create_courses(client)
    assert response.status[:3] == '200', response.data

    data = {}
    data["description"] = "test_file"
    data['file'] = (io.BytesIO(b"abcdef"), 'test.jpg')

    headers = {'Content-Type': 'multipart/form-data', 'Authorization': 'Bearer {0}'.format(get_test_token(client))}
    response = client.post('/v1/courses/1/resources', data=data, headers=headers, content_type='multipart/form-data')
    assert response.status[:3] == '200'


def test_get_resource(client):
    headers = {'Content-Type': 'application/json', 'Authorization': 'Bearer {0}'.format(get_test_token(client))}
    response = client.get('/v1/recources/1', headers=headers)
    assert response.status[:3] == '200'


def test_delete_recource(client):
    headers = {'Content-Type': 'application/json', 'Authorization': 'Bearer {0}'.format(get_test_token(client))}
    response = client.delete('/v1/recources/1', headers=headers)
    assert response.status[:3] == '204'
    assert not CourseResource.query.filter_by(id=1).first()