#!/usr/bin/python
# -*- coding: utf-8 -*-
from flask_sqlalchemy import SQLAlchemy
from flask_script import Manager
from flask.ext.migrate import Migrate,MigrateCommand
from app import create_app #引入app有错

app = create_app()

mamager=Manager(app)

app.config['SECRET_KEY'] ='you cannot guess it'
app.config['SQLALCHEMY_DATABASE_URI']='mysql://irides:irides@localhost:3306/test'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = True
db = SQLAlchemy(app)

migrate=Migrate(app,db) #配置迁移
mamager.add_command("db",MigrateCommand) #配置迁移命令


from flask_jwt import JWT
jwt = JWT()
