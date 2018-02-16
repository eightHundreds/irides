import flask
from flask_restful_swagger_2 import get_swagger_blueprint

from app.auth.jwt import UserLoginSchema
from app.models import InitDataGenerator
from . import extensions, config
from .auth import jwt



def create_app(config_name='default'):
    """Flask app factory

    :config_name: a string object.
    :returns: flask.Flask object

    """
    print('config name:%s' % config_name)
    app = flask.Flask(__name__)

    # set the config vars using the config name and current_app
    app.config.from_object(config.config[config_name])

    register_extensions(app)
    register_blueprints(app)
    append_swagger_doc(app)


    return app


def register_extensions(app):
    """Call the method 'init_app' to register the extensions in the flask.Flask
    object passed as parameter.

    :app: flask.Flask object
    :returns: None

    """
    # 注意大小写,JWT是类,jwt才是对象
    extensions.db.init_app(app)
    jwt.set_jwt_handlers(extensions.jwt)
    extensions.jwt.init_app(app)
    extensions.migrate.init_app(app=app, db=extensions.db)
    extensions.cors.init_app(app=app)


def register_blueprints(app):
    """Register all blueprints.

    :app: flask.Flask object
    :returns: None

    """
    from . import users, pictures,main
    app.register_blueprint(users.blueprint)
    app.register_blueprint(pictures.blueprint)
    app.register_blueprint(main.blueprint)

def append_swagger_doc(app):
    """
    添加swagger文档,从api中获得文档,并统一添加到一个blueprint中
    :param app:
    :return:
    """

    docs = []

    def append_custom_path(url, operator):
        nonlocal docs

    from . import users, pictures
    docs.append(users.api.get_swagger_doc())
    docs.append(pictures.api.get_swagger_doc())

    #特别的为JWT的登入接口 添加文档
    if len(docs) == 0:
        return
    doc = docs[0]
    doc['definitions'].update({
        UserLoginSchema.__name__:UserLoginSchema.definitions()
    })
    doc['paths'].update({
        '/auth': {
            'post': {
                'tags': ['auth'],
                'description': 'login',
                'summary': '登入',
                'parameters': [
                    {
                        'description': '',
                        'in': 'body',
                        'name': 'body',
                        'schema': {
                            "$ref": "#/definitions/UserLoginSchema"
                        }
                    },
                ],
                'responses': {
                    '200': {
                        'description': 'ok'
                    }
                }
            }
        }
    })

    # 下面所有的配置只会影响最后生成的文档
    app.register_blueprint(
        get_swagger_blueprint(docs,
                              '/api/swagger',  # 使用mydomain.com/api/swagger.json 访问文档
                              title='irides Api文档',
                              api_version='1',
                              tags=[{
                                  'name': 'pictures',
                                  'description': '图片'
                              }, {
                                  'name': 'auth',
                                  'description': '授权'
                              }, {
                                  'name': 'user',
                                  'description': '用户'
                              }],
                              base_path='/api',
                              # 请求前缀,最后所有的请求都是mydomain.com/base_path/....
                              schemes=['http','https'],
                              security_definitions={
                                  'jwt': {
                                      "type": "apiKey",
                                      "name": "Authorization",
                                      "in": "header",
                                      "description": "需要添加:'Bearer AccessToken'不包括引号"
                                  }
                              }
                          ))
