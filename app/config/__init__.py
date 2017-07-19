# -*- coding: utf-8 -*-
from .development import DevelopmentConfig
from .testing import TestingConfig

config = {
    'development': DevelopmentConfig,
    'testing': TestingConfig,
    'default': DevelopmentConfig
}