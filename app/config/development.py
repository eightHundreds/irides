# -*- coding: utf-8 -*-
import os
#开发时配置
from .default import Config,basedir
class DevelopmentConfig(Config):
    #开启调试模式
    DEBUG = True
    #使用sqlite数据库
    SQLALCHEMY_DATABASE_URI = os.environ.get('DEV_DATABASE_URL') or \
        'sqlite:///' + os.path.join(basedir, 'data-table-dev.sqlite')
    # SQLALCHEMY_BINDS = {
    #     'lessonTable': 'sqlite:///' + os.path.join(basedir, 'data-table-dev.sqlite'),
    # }
