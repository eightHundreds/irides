from app import helpers
from . import models
from app.extensions import db

def is_an_available_username(username):
    """Verify if an username is available.

    :username: a string object
    :returns: True or False

    """
    if models.User.query.filter_by(username=username).all():
    	return False
    return True

def is_an_available_id(user_id):
    """Verify if an id is available.

    :returns: True or False

    """
    if models.User.query.filter_by(id=user_id).all():
        return False
    return True


def get_users(username=None):
    """Get all users info. Accepts specify an username.

    :username: a string object
    :returns: a dict with the operation result

    """
    query = {} if not username else {'username': username}
    users = models.User.query.filter_by(**query).all()

    if not users:
        return {'no-data': ''}

    return {'success': [u.to_json2() for u in users]}


def create_or_update_user(username, password, user_id=None):
    """Creates or updates an user.

    :username: a string object
    :password: a string object (plaintext)
    :user_id: a str object. Indicates an update.
    :returns: a dict with the operation result

    """
    user = models.User(username = username,
                       password = password)
    if is_an_available_username(username) is False:
        try:
            _user = models.User.query.filter_by(username=username).first()
            _password = _user.password
            if _password == password:
                db.session.add(user)
                db.session.commit()
                return {'updated': 'Updated the user {!r}.'.format(username)}
            return {'error': 'The user {!r} already exists.'.format(_user.username)}
        except Exception as e:
            return {'error': 'Error during the operation: {}'.format(e)}

    try:
        db.session.add(user)
        db.session.commit()
        return {'created': 'Created the user {!r}.'.format(username)}
    except Exception as e:
        return {'error': 'Error during the operation: {}'.format(e)}

def delete_user(user_id):
    """Delete an user by user id.

    :user_id: a str object
    :returns: a dict with the operation result

    """

    user = models.User.query.filter_by(id=user_id).first()

    if not user:
        return {'error': 'Invalid user id.'}

    db.session.delete(user)
    db.session.commit()
    return {'deleted': 'User deleted'}
