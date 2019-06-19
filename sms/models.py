# -*- coding:utf-8 -*-

from datetime import datetime
from . import db


class User(db.Model):
    __tablename__ = "user_info"

    object_id = db.Column(db.Integer, primary_key=True)  # 用户编号
    stu_id = db.Column(db.String(32))  # 学号
    name = db.Column(db.String(32))  # 姓名
    gender = db.Column(db.String(10))   # 性别
    grade = db.Column(db.String(32))  # 年级
    email = db.Column(db.String(32))  # 邮箱
    # create_time = db.Column(db.DateTime, default=datetime.now)  # 记录的创建时间

    def get_simple_info(self):
        info = {
            "stu_id":self.stu_id,
            "name" : self.name,
            "gender":self.gender,
            "grade":self.grade,
            "email":self.email
        }
        return info