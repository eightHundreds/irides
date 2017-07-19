# -*- coding: utf-8 -*-
#测试时配置
import os

from .default import Config,basedir
class TestingConfig(Config):
    TESTING = True
    # SQLALCHEMY_BINDS = {
    #     'lessonTable': 'sqlite:///:memory:',
    # }
