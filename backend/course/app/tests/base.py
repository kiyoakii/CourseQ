import pytest
from course import app
import json
from ..models.base import db


first_client = True

@pytest.fixture
def client():
    global first_client
    app.config['SQLALCHEMY_DATABASE_URI'] = app.config['TEST_DATABASE_URI']
    db.init_app(app)
    with app.test_client() as client:
        with app.app_context():
            # Only clear db at the first time
            if first_client:
                db.drop_all()
                db.create_all()
                first_client = False
        yield client


def get_test_token(client, gid='0000000195'):
    headers = {'Content-Type': 'application/json'}
    response = client.get('/v1/token/{0}'.format(gid), headers=headers)
    return json.loads(response.data)['access_token']
