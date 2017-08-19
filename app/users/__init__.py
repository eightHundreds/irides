from flask import Blueprint
from app import helpers
from . import resources


blueprint = Blueprint('users', __name__)
api = helpers.MyApi(blueprint, prefix='/api', add_api_spec_resource=False)

api.add_resource(resources.UsersAPI, '/users')
api.add_resource(resources.UserAPI, '/user', '/user/<user_id>')
