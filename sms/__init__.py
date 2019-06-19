# coding:utf-8

from flask import Flask
from config import config_map
from flask_sqlalchemy import SQLAlchemy
from flask_session import Session
from flask_wtf import CSRFProtect
from sms.utils.commons import ReConverter
from flask_celery import Celery


# 数据库
db = SQLAlchemy()
# 创建celery实例
celery = Celery()

# 工厂模式
def create_app(config_name):
    app = Flask(__name__)

    # 根据配置模式的名字获取配置参数的类
    config_class = config_map.get(config_name)
    app.config.from_object(config_class)

    # 使用app初始化db
    db.init_app(app)
    # config_class.init_app(app)
    # celery.init_app(app)

    # 为flask补充csrf防护
    CSRFProtect(app)


    # 注册蓝图
    from sms import api_1_0
    app.register_blueprint(api_1_0.api, url_prefix="/api/v1.0")

    # 注册celery管理蓝本
    from sms.api_1_0 import celery_manage as celery_manage_blueprint
    app.register_blueprint(celery_manage_blueprint)


    return app