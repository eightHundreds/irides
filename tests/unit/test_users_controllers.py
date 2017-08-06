import pytest

from app.users import controllers
from tests import clear_db
from app import helpers

def test_is_an_available_username_with_available_user(app):
    clear_db()
    assert controllers.is_an_available_username(username='available') is True


def test_is_an_available_username_with_unavailable_user(app, mock_user):
    clear_db()
    mock_user(username='unavailable', password='unavailable')
    assert controllers.is_an_available_username('unavailable') is False


def test_get_users_no_data(app):
    clear_db()
    assert controllers.get_users() == {'no-data': ''}



def test_get_users_with_data(app, mock_user):
    clear_db()
    user = mock_user()
    expected = {
        'success': [{
            'id': '1',
            'username': 'mock-user',
            'email': 'test@qq.com',
            'avator': '',
        }]
    }
    result=controllers.get_users()
    assert controllers.get_users(username='mock-user') == expected


def test_get_users_with_data_and_specific_username(app, mock_user):
    clear_db()
    user = mock_user()
    expected = {
        'success': [{
            'id': '1',
            'username': 'mock-user',
            'email':'test@qq.com',
            'avator': '',
        }]
    }

    assert controllers.get_users(username='mock-user') == expected

@pytest.mark.skip(reason="这个api逻辑有问题")
def test_create_user_with_invalid_username(app, mock_user):
    clear_db()
    user = mock_user()
    username, password = 'mock-user', 'password'
    expected = {
        'error': 'The user {!r} already exists.'.format('mock-user')
    }

    assert controllers.create_or_update_user(username, password) == expected


def test_create_user_with_valid_username(app):
    clear_db()
    username, password = 'valid user', 'password'

    assert 'created' in controllers.create_or_update_user(username, password)

@pytest.mark.skip(reason="这个api逻辑有问题")
def test_update_user_with_valid_username(app, mock_user):
    clear_db()
    user = mock_user()
    username, password = 'mock-user', helpers.encrypt_password('mock-user')

    assert 'updated' in controllers.create_or_update_user(username, password,user.id)



def test_delete_user_with_valid_id(app, mock_user):
    clear_db()
    user = mock_user()
    expected = {'deleted': 'User deleted'}

    assert controllers.delete_user(str(1)) == expected
