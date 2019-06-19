# coding:utf-8
import os
from datetime import timedelta
import sys

basedir = os.path.abspath(os.path.dirname(__file__))
# '/home/python/PycharmProjects/Send_Email'

class Config(object):
    """配置信息"""
    SECRET_KEY = "XHSOI*Y9dfs9cshd9"

    # 数据库
    SQLALCHEMY_DATABASE_URI = "mysql://root:mysql@127.0.0.1:3306/sms"
    SQLALCHEMY_TRACK_MODIFICATIONS = True
    # 定时任务配置
    # BROKER_URL = 'redis://:redis@127.0.0.1:6379/0'
    # CELERY_RESULT_BACKEND = 'redis://:redis@127.0.0.1:6379/0'
    #
    # CELERY_TIMEZONE = 'Asia/Shanghai'
    #
    # CELERY_IMPORTS = (
    #     'sms.api_1_0.read_excel',
    # )
    # # 定义任务名称：send_email
    # #  执行规则：每20秒运行一次
    # CELERYBEAT_SCHEDULE = {
    #     'add-every-20-seconds': {
    #         'task': 'send_email',
    #         'schedule': timedelta(seconds=20),
    #         # 'schedule':crontab(hour=10, minute=55),
    #     }
    # }

    @staticmethod
    def init_app(app):
        pass


class DevelopmentConfig(Config):
    """开发模式的配置信息"""
    DEBUG = True


class ProductionConfig(Config):
    """生产环境配置信息"""
    pass


config_map = {
    "develop": DevelopmentConfig,
    "product": ProductionConfig
}
