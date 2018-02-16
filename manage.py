#!/usr/bin/env python
import os
from flask_script import Manager, Shell, Server, Command, Option
from app.models import User, Picture, Tag
from app import create_app, helpers
from app.extensions import db
from flask_migrate import Migrate, MigrateCommand
from app.models import InitDataGenerator
app = create_app(os.getenv('FLASK_CONFIG') or 'default')

migrate = Migrate(app, db)
manager = Manager(app)

# access python shell with context
manager.add_command(
    "shell",
    Shell(make_context=lambda: {'app': app, 'db': db, 'user': User, 'pictures': Picture, 'tags': Tag}),
    use_ipython=True)

manager.add_command(
    "startserver",
    Server(port=(os.getenv('PORT') or 5000), host='0.0.0.0'))

manager.add_command('db', MigrateCommand)


class SeedCommand(Command):
    """
    初始化数据库
    """

    def run(self):
        db.drop_all()
        db.create_all()
        generator=InitDataGenerator()
        generator.init_all()

class GunicornServer(Command):

    description = 'Run the app within Gunicorn'

    def __init__(self, host='127.0.0.1', port=8000, workers=4):
        self.port = port
        self.host = host
        self.workers = workers

    def get_options(self):
        return (
            Option('-H', '--host',
                   dest='host',
                   default=self.host),

            Option('-p', '--port',
                   dest='port',
                   type=int,
                   default=self.port),

            Option('-w', '--workers',
                   dest='workers',
                   type=int,
                   default=self.workers),
        )

    def handle(self, app, host, port, workers):

        from gunicorn import version_info

        if version_info < (0, 9, 0):
            from gunicorn.arbiter import Arbiter
            from gunicorn.config import Config
            arbiter = Arbiter(Config({'bind': "%s:%d" % (host, int(port)),'workers': workers}), app)
            arbiter.run()
        else:
            from gunicorn.app.base import Application

            class FlaskApplication(Application):
                def init(self, parser, opts, args):
                    return {
                        'bind': '{0}:{1}'.format(host, port),
                        'workers': workers
                    }

                def load(self):
                    return app

            FlaskApplication().run()

manager.add_command('seed', SeedCommand)
manager.add_command("gunicorn", GunicornServer())

# run the app
if __name__ == '__main__':
    manager.run()
