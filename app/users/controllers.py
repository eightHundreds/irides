from app import helpers
from . import models


def is_an_available_username(username):
    """Verify if an username is available.

    :username: a string object
    :returns: True or False

    """
    if models.User.query_by(username=username).all():
        return False
    return True


def get_users(username=None):
    """Get all users info. Accepts specify an username.

    :username: a string object
    :returns: a dict with the operation result

    """
    query = {} if not username else {'username': username}
    users = models.User.query_by(**query).all()

    if not users:
        return {'no-data': ''}

    return {'success': [u.to_json() for u in users]}


def create_or_update_user(username, password, user_id=None):
    """Creates or updates an user.

    :username: a string object
    :password: a string object (plaintext)
    :user_id: a str object. Indicates an update.
    :returns: a dict with the operation result

    """
    query = {'id': user_id} if user_id else {'username': username}
    if is_an_available_username(username) is False:
        try:
            result = models.User.objects(**query).update(
                set__username=username,
                set__password=helpers.encrypt_password(password),
                upsert=True,
                full_result=True
            )
            return {'updated': 'Updated the user {!r}.'.format(username)}
        except Exception as e:
            return {'error': 'Error during the operation: {}'.format(e)}

    try:
        result = models.User.objects(**query).add(
            set__username=username,
            set__password=helpers.encrypt_password(password),
            upsert=True,
            full_result=True
        )
        return {'created': 'Created the user {!r}.'.format(username)}
    except Exception as e:
        return {'error': 'Error during the operation: {}'.format(e)}

def delete_user(user_id):
    """Delete an user by user id.

    :user_id: a str object
    :returns: a dict with the operation result

    """

    user = models.User.query_by(username=username).first()

    if not user:
        return {'error': 'Invalid user id.'}

    user.delete()
    return {'deleted': 'User deleted'}
