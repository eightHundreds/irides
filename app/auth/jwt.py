import datetime
from flask import current_app
from app import helpers, models
from flask_restful_swagger_2 import swagger, Schema


class UserLoginSchema(Schema):
    type = 'object'
    properties = {
        'username': {
            'type': 'string',
            "example": 'something'
        },
        'password': {
            'type': 'object'
        }
    }


def set_jwt_handlers(jwt):
    """Define handlers to jwt.
    :jwt: flask_jwt.JWT object
    :returns: None
    """

    # 注意这里是个函数不是类,不要觉得找不到jwt在哪定义

    @jwt.authentication_handler
    def authenticate(username, password):
        user = models.User.query.filter_by(username=username).first()

        if user and helpers.verify_password(password, user.password):
            return user
        return None

    @jwt.error_handler
    def error_handler(error):
        return 'Auth Failed: {}'.format(error.description), 400

    @jwt.payload_handler
    def make_payload(user):
        return {
            'user_id': str(user.id),
            'exp': (datetime.datetime.utcnow() +
                    current_app.config['JWT_EXPIRATION_DELTA']).isoformat()
        }

    @jwt.user_handler
    def load_user(payload):
        return models.User.query.filter_by(id=payload['user_id']).first()
