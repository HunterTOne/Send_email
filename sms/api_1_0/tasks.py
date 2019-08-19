# -*-coding:utf-8-*-
from celery import Celery
from flask_mail import Mail, Message
from datetime import timedelta
import time
from flask import Flask, request
from sms.models import User
from sms import db
<<<<<<< .mine
# 邮件发送 hhahah
# 再次测试
=======
# 邮件发送

>>>>>>> .theirs
c = Celery('mails',
           broker='redis://:redis@127.0.0.1/0',
           backend='redis://:redis@127.0.0.1:6379/0',
           beat_schedule={
               'add-every-20-seconds': {
                   'task': 'send_email',
                   'schedule': timedelta(seconds=60),
                   # 'schedule':crontab(hour=10, minute=55),
               }
           })



@c.task(name="send_failed_email")
def send_failed_email(reci_email):
    app = Flask(__name__)
    app.config.update(
        DEBUG=True,
        MAIL_SERVER='smtp.qq.com',
        MAIL_PROT=465,
        MAIL_USE_TLS=True,
        MAIL_USERNAME='728363298@qq.com',
        MAIL_PASSWORD='pztwrvdpxtwsbfje',
    )
    print (reci_email + u"邮件发送失败")
    # from .read_excel import send_email
    mail = Mail(app)
    time.sleep(60)
    db.session.commit()
    stu_id = request.form.get("stu_id", default="20155956", type=str)
    stu_id = User.query.filter_by(stu_id=stu_id).first()
    if not stu_id:
        print(u"没有该学生")
    else:
        reci_email = stu_id.email
        print (reci_email)
    msg = Message("This is a test ", sender='728363298@qq.com', recipients=[reci_email])
    # 邮件内容
    msg.body = u"测试二二"
    try:
        # 发送邮件
        mail.send(msg)
    except Exception as e:
        print(str(e))
        print(reci_email + u"又发送失败了")

    else:
        print(u"第二次邮件发送成功")
        # return "Sent Succeed222"


