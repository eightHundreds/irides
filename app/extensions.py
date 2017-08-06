from flask_sqlalchemy import SQLAlchemy

db = SQLAlchemy()

from flask_jwt import JWT

jwt = JWT()

from flask_migrate import Migrate

migrate = Migrate()
