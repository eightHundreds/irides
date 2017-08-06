# -*- coding: utf-8 -*-
# 测试时配置
import os

from .default import Config, basedir


class TestingConfig(Config):
    """
    测试时配置
    """
    TESTING = True
    SQLALCHEMY_DATABASE_URI = 'sqlite:///:memory:'#内存数据库,每次测试自动销毁数据
    # SQLALCHEMY_BINDS = {
    #     'lessonTable': 'sqlite:///:memory:',
    # }
