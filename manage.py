#!/usr/bin/env python
import os
from flask_script import Manager, Shell, Server, Command
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


manager.add_command('seed', SeedCommand)

# run the app
if __name__ == '__main__':
    manager.run()
