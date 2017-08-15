from flask_restful import Resource, reqparse
from flask_jwt import jwt_required
from flask_restful_swagger_2 import swagger, Schema
from flask import current_app, request
from app import helpers, extensions, UserLoginSchema
from app.helpers import SwgHelper
from . import controllers


def post_put_parser():
    """Request parser for HTTP POST or PUT.
    :returns: flask_restful.reqparse.RequestParser object
    """
    parse = reqparse.RequestParser()
    parse.add_argument(
        'username', type=str, location='json', required=True)
    parse.add_argument(
        'password', type=str, location='json', required=True)
    parse.add_argument(
        'avator', type=str, location='json', required=False)
    parse.add_argument(
        'email', type=str, location='json', required=False)
    return parse


class UsersAPI(Resource):
    """An API to get or create users."""

    _get_parse= reqparse.RequestParser()
    _get_parse.add_argument('username', type=str, location='args', required=False)
    @swagger.doc(SwgHelper.Operation(
        tags=['user'],
        description='获得用户',
        reqparser={'name':'GetUserSchema','parser':_get_parse},
        responses={
            '200': SwgHelper.Response(description="成功")
        }))
    @jwt_required()
    @helpers.standardize_api_response
    def get(self, username=None):
        """HTTP GET. Get one or all users.

        :username: a string valid as object id.
        :returns: One or all available users.

        """

        input = self._get_parse.parse_args()
        return controllers.get_users(input.get('username', None))

    @swagger.doc(SwgHelper.Operation(
        tags=['user'],
        description='创建用户',
        reqparser={'name':'PostUserSchema','parser':post_put_parser()},
        security=[SwgHelper.SecurityRequire('jwt')],
        responses={
            '200': SwgHelper.Response(description="成功")
        }))
    @jwt_required()
    @helpers.standardize_api_response
    def post(self):
        """HTTP POST. Create an user.

        :username: The user username
        :password: The user password (plaintext)
        :returns: The user id

        """

        parse = post_put_parser()
        args = parse.parse_args()
        username, password, avator, email = args['username'], args['password'], args['avator'], args['email']

        return controllers.create_or_update_user(username, password, avator, email)


class UserAPI(Resource):
    """An API to update or delete an user. """

    @jwt_required()
    @helpers.standardize_api_response
    def put(self):
        """HTTP PUT. Update an user.
        :returns:

        """

        parse = post_put_parser()
        parse.add_argument('user_id', type=str, location='json', required=True)
        args = parse.parse_args()

        username, password, avator, email = args['username'], args['password'], args['avator'], args['email']
        user_id = args['user_id']

        return controllers.create_or_update_user(username, password, avator, email, user_id)

    @jwt_required()
    @helpers.standardize_api_response
    def delete(self, user_id):
        """HTTP DELETE. Delete an user.
        :returns:

        """
        if controllers.is_an_available_id(user_id):
            return {'error': 'Invalid user id.'}
        return controllers.delete_user(user_id)
