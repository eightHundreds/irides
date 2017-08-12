from flask_restful import Resource, reqparse
from flask_jwt import jwt_required
from app import helpers, extensions
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

    return parse

class PicturesAPI(Resource):
    '''
    def _post_put_parser(self):
        """Request parser for HTTP POST or PUT.
        :returns: flask_restful.reqparse.RequestParser object

        """
        parse = reqparse.RequestParser()
        parse.add_argument(
            'username', type=str, location='json', required=True)
        parse.add_argument(
            'password', type=str, location='json', required=True)

        return parse
    '''

    @jwt_required()
    @helpers.standardize_api_response
    def get(self):
        """HTTP GET. Get all pictures"""

        return controllers.get_pictures()