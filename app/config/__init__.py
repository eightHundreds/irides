# -*- coding: utf-8 -*-
from .production import ProductionConfig
from .development import DevelopmentConfig
from .testing import TestingConfig

config = {
    'development': DevelopmentConfig,
    'testing': TestingConfig,
    'default': DevelopmentConfig,
    'production':ProductionConfig
}
