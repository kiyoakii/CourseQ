import pytest
from course import app
import json
from ..models.base import db
from app.models.course import Course


@pytest.fixture
def client():
    app.config['SQLALCHEMY_DATABASE_URI'] = app.config['TEST_DATABASE_URI']
    db.init_app(app)
    with app.test_client() as client:
        with app.app_context():
            db.drop_all()
            db.create_all()
        yield client


def test_courses_create(client):
    data = {
        "intro": "hi",
        "name_en": "jisuanke",
        "name_zh": "软件工程",
        "pre_course": "ads",
        "semester": "ad",
        "textbooks": "dcx",
    }
    headers = {'Content-Type': 'application/json'}
    response = client.post('/v1/courses', data=json.dumps(data), headers=headers)
    assert response.status == '201 CREATED'
    assert Course.query.filter_by(cid=2).first().name_en == 'jisuanke'
    assert Course.query.filter_by(cid=2).first().name_zh == '软件工程'
    assert Course.query.filter_by(cid=2).first().pre_course == 'ads'
    assert Course.query.filter_by(cid=2).first().semester == 'ad'
    assert Course.query.filter_by(cid=2).first().textbooks == 'dcx'
