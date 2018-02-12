from flask import Blueprint
from app import helpers
from . import resources


blueprint = Blueprint('pictures', __name__)
api = helpers.MyApi(blueprint, prefix='/api')

api.add_resource(resources.PicturesAPI, '/pictures')
api.add_resource(resources.PictureAPI, '/pictures', '/pictures/Search', '/pictures/<user_id>')
