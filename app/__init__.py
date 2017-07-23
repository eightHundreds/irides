import flask
from . import extensions, config
from .auth import jwt


def create_app(config_name='default'):
    """Flask app factory

    :config_name: a string object.
    :returns: flask.Flask object

    """

    app = flask.Flask(__name__)

    # set the config vars using the config name and current_app
    app.config.from_object(config.config[config_name])
    app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

    register_extensions(app)
    register_blueprints(app)
    jwt.set_jwt_handlers(extensions.jwt)

    return app


def register_extensions(app):
    """Call the method 'init_app' to register the extensions in the flask.Flask
    object passed as parameter.

    :app: flask.Flask object
    :returns: None

    """

    extensions.db.init_app(app)
    extensions.jwt.init_app(app)
    extensions.migrate.init_app(app=app,db=extensions.db)


def register_blueprints(app):
    """Register all blueprints.

    :app: flask.Flask object
    :returns: None

    """
    from . import users
    app.register_blueprint(users.blueprint)
