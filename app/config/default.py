# -*- coding: utf-8 -*-
import os
basedir = os.path.abspath(os.path.dirname(os.path.dirname(__file__)))
class Config:
    "配置基类"
    #密钥配置
    SECRET_KEY = os.environ.get('SECRET_KEY') or 'you cannot guess me'

    #数据库配置
    SQLALCHEMY_COMMIT_ON_TEARDOWN = True #当连接断开时是否提交事务

    #邮件配置
    MAIL_SERVER = 'smtp.163.com'
    MAIL_PORT=465
    MAIL_USE_SSL=True
    MAIL_USERNAME = os.environ.get('MAIL_USERNAME')#为了安全,不要把隐私信息直接写到
    MAIL_PASSWORD = os.environ.get('MAIL_PASSWORD')
    FLASKY_MAIL_SUBJECT_PREFIX = '[Flasky]'
    FLASKY_MAIL_SENDER = os.environ.get('MAIL_USERNAME')
    FLASKY_ADMIN = os.environ.get('FLASKY_ADMIN')

    @staticmethod
    def init_app(app):
        pass