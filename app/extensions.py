
from flask_sqlalchemy import SQLAlchemy

db = SQLAlchemy()

from flask_jwt import JWT

jwt = JWT()

from flask_migrate import Migrate

migrate = Migrate()

from flask_cors import CORS
cors=CORS(resources={r"/api/*": {"origins": "http://petstore.swagger.io"}})

