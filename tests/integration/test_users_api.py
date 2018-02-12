import json

import pytest
from app import models
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



def test_create_an_user_invalid_username(client, mock_user):

    clear_db()
    user = mock_user('user', 'password')
    jwt_header = get_jwt_auth_header('user', 'password', client)

    payload = json.dumps({'username': user.username, 'password': 'foo', 'avator': '', 'email': 'test@qq.com'})
    response = jrequest('POST', '/api/users', client, jwt_header, data=payload)
    response = json.loads(response.data.decode('utf-8'))
    response = json.loads(response)

    expected = {
        'status_code': 400,
        'data': "The user {!r} already exists.".format(user.username),
        'error': 'Bad Request'
    }

    assert sorted(response.items()) == sorted(expected.items())


def test_create_an_user_valid_username(client, mock_user):

    clear_db()
    mock_user('user', 'password')
    jwt_header = get_jwt_auth_header('user', 'password', client)

    payload = json.dumps({'username': 'valid', 'password': 'foo', 'avator': 'test', 'email': '_test@qq.com'})
    response = jrequest('POST', '/api/users', client, jwt_header, data=payload)
    response = json.loads(response.data.decode('utf-8'))
    response = json.loads(response)

    expected = {
        'status_code': 201,
        'data': "Created the user 'valid'.",
        'description': 'Successfully created'
    }

    assert sorted(response.items()) == sorted(expected.items())


def test_update_an_user_invalid_username(client, mock_user):

    clear_db()
    # user to auth
    user_to_auth = mock_user('auth', 'auth')

    # to test if an username is really unique
    user_to_test = mock_user('user', 'password', 'test', 'another_test@qq.com')

    jwt_header = get_jwt_auth_header('auth', 'auth', client)
    payload = json.dumps({
        'user_id': str(user_to_auth.id),
        'username': user_to_test.username,
        'password': 'password',
        'avator': '',
        'email': 'test@qq.com'
    })

    response = jrequest('PUT', '/api/user', client, jwt_header, data=payload)
    response = json.loads(response.data.decode('utf-8'))
    response = json.loads(response)

    expected = {
        'status_code': 400,
        'data': "The user {!r} already exists.".format(user_to_test.username),
        'error': 'Bad Request'
    }

    assert sorted(response.items()) == sorted(expected.items())


def test_update_an_user_valid_username(client, mock_user):

    clear_db()

    user = mock_user('user', 'password')
    jwt_header = get_jwt_auth_header('user', 'password', client)
    payload = json.dumps({
        'user_id': str(user.id),
        'username': 'it works',
        'password': 'password',
        'avator': '',
        'email': 'test123@qq.com'
    })

    response = jrequest('PUT', '/api/user', client, jwt_header, data=payload)
    response = json.loads(response.data.decode('utf-8'))
    response = json.loads(response)

    expected = {
        'status_code': 200,
        'data': "Updated the user 'it works'.",
        'description': 'Successfully updated'
    }

    assert sorted(response.items()) == sorted(expected.items())
    result=models.User.query.filter_by(username='it works').all()
    assert len(result)==1
    assert result[0].email=='test123@qq.com'



# def test_delete_an_user_invalid_user_id(client, mock_user):
#
#     clear_db()
#
#     mock_user('user', 'password')
#     jwt_header = get_jwt_auth_header('user', 'password', client)
#
#     response = jrequest(
#         'DELETE', '/api/user/{}'.format(ObjectId()), client, jwt_header)
#     response = json.loads(response.data.decode('utf-8'))
#     response = json.loads(response)
#
#     expected = {
#         'status_code': 400,
#         'data': 'Invalid user id.',
#         'error': 'Bad Request'
#     }
#
#     assert sorted(response.items()) == sorted(expected.items())


def test_delete_an_user_valid_user_id(client, mock_user):

    clear_db()
    user_to_delete = mock_user('delete', 'delete', 'delete', 'delete')
    # user_to_auth
    mock_user('user', 'password')

    jwt_header = get_jwt_auth_header('user', 'password', client)

    response = jrequest(
        'DELETE', '/api/user/{}'.format(user_to_delete.id), client, jwt_header)
    response = json.loads(response.data.decode('utf-8'))
    response = json.loads(response)

    expected = {
        'status_code': 200,
        'data': 'User deleted',
        'description': 'Successfully deleted'
    }

    assert sorted(response.items()) == sorted(expected.items())




def test_get_users_without_username(client, mock_user):
    clear_db()
    mock_user('user', 'password')
    jwt_header = get_jwt_auth_header('user', 'password', client)

    response = json.loads(jrequest(
        'GET', '/api/users', client, jwt_header).data.decode('utf-8'))
    response = json.loads(response)

    expected = {
        'status_code': 200,
        'data': [{
            'id': '1',
            'username': 'user',
            'avator': '',
            'email': 'test@qq.com'
        }],
        'description': 'Successful Operation',
    }

    assert sorted(response.items()) == sorted(expected.items())


def test_get_users_specifing_username(client, mock_user):
    clear_db()
    mock_user('user', 'password')
    mock_user('user2','password')
    jwt_header = get_jwt_auth_header('user', 'password', client)

    response = json.loads(jrequest(
        'GET', '/api/users?username=%s' % 'user2', client, jwt_header).data.decode('utf-8'))
    response = json.loads(response)

    expected = {
        'status_code': 200,
        'data': [{
            'id': '2',
            'username': 'user2',
            'avator': '',
            'email': 'test@qq.com'
        }],
        'description': 'Successful Operation',
    }

    assert sorted(response.items()) == sorted(expected.items())
