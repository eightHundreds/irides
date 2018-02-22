import json
import pytest

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
    print(pic.tags)
    jwt_header = get_jwt_auth_header('user', 'password', client)
    response = json.loads(jrequest(
        'GET', '/api/pictures', client, jwt_header).data.decode('utf-8'))
    response = json.loads(response)

    templist = []
    for tag in pic.tags:
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



def test_get_specific_picture(client, mock_user, mock_picture):
    clear_db()
    user = mock_user('username', 'password')
    pic1 = mock_picture(user)
    pic2 = mock_picture(user, 'testtags', 'descriptin1', 'address1')

    jwt_header = get_jwt_auth_header('username', 'password', client)

    response = jrequest('GET', '/api/picture/search?searchKey={}'.format('testtags'), client, jwt_header)
    response = json.loads(response.data.decode('utf-8'))
    response = json.loads(response)

    templist1 = []
    for tag in pic1.tags:
        templist1.append(tag.to_json())
    templist2 = []
    for tag in pic2.tags:
        templist2.append(tag.to_json())

    expected = {
        'status_code': 200,
        'data': [{
            'id': str(pic1.id),
            'userid': pic1.userId,
            'dsepriction': pic1.despriction,
            'adress': pic1.address,
            'tags': templist1
        },
            {
                'id': str(pic2.id),
                'userid': pic2.userId,
                'dsepriction': pic2.despriction,
                'adress': pic2.address,
                'tags': templist2
            }],
        'description': 'Successful Operation',
    }

    assert sorted(response.items()) == sorted(expected.items())