import pytest
from course import app
import json
from ..models.base import db


@pytest.fixture
def client():
    app.config['SQLALCHEMY_DATABASE_URI'] = app.config['TEST_DATABASE_URI']
    db.init_app(app)
    with app.test_client() as client:
        with app.app_context():
            db.create_all()
        yield client


def test_courses_create(client):
    data = {
        "intro": "hi",
        "name_en": "jisuanke",
        "name_zh": "软件工程",
        "pre_Course": "ads",
        "semester": "ad",
        "textbooks": "dcx",
    }
    headers = {'Content-Type': 'application/json'}
    response = client.post('/v1/courses', data=json.dumps(data), headers=headers)
    assert response.status == '201 CREATED'
