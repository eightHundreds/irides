import json

import pytest
from app import models
from app.extensions import db
from . import jrequest, get_jwt_auth_header
from tests import clear_db

unauthorized_scenarios = [
    ['GET', 'api/users', 'Authorization Required', 401],
]

@pytest.mark.parametrize(
    'method, url, error, status_code ', unauthorized_scenarios)
def test_unauthorized_request(method, url, error, status_code, client):

    response = jrequest(method, url, client)

    assert response.status_code == status_code
    assert json.loads(response.data.decode('utf-8'))['error'] == error

def test_get_pictures(client, mock_user, mock_picture):
    clear_db()
    user = mock_user('user', 'password')
    pic = mock_picture(user)
    # pic = models.Picture(
    #     userId=str(user.id),
    #     despriction='testdes',
    #     address='testaddress'
    # )
    #
    # db.session.add(pic)
    # db.session.commit()
    print(pic.tags)
    jwt_header = get_jwt_auth_header('user', 'password', client)

    response = json.loads(jrequest(
        'GET', '/api/pictures', client, jwt_header).data.decode('utf-8'))
    response = json.loads(response)

    templist = []
    for tag in pic.tags.all():
        templist.append(tag.to_json())

    expected = {
        'status_code': 200,
        'data': [{
            'id': str(pic.id),
            'userid': pic.userId,
            'dsepriction': pic.despriction,
            'adress': pic.address,
            'tags': templist
        }],
        'description': 'Successful Operation',
    }

    assert sorted(response.items()) == sorted(expected.items())