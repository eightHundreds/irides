# 上线时配置
import os
from .default import Config, basedir


class ProductionConfig(Config):
    SQLALCHEMY_DATABASE_URI = os.environ.get('DATABASE_URL') or \
                              'sqlite:///' + os.path.join(basedir, 'data-table-dev.sqlite')
