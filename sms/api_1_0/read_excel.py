# coding:utf-8

from . import api, tasks
from sms import db, models,celery
from flask import current_app
from flask import Flask, request
from flask_mail import Mail, Message
import os, time
from xlrd import open_workbook
from sms.models import User



@api.route("/read_excel/file_info", methods=['POST', 'GET'])
def file_info():
    excelName = "/home/python/Desktop/sms.xlsx"
    bk = open_workbook(excelName, encoding_override="utf-8")
    try:
        sh = bk.sheets()[0]  # 因为Excel里只有sheet1有数据，如果都有可以使用注释掉的语句
    except:
        print("no sheet in %s named sheet1" % excelName)
    else:
        nrows = sh.nrows
        ncols = sh.ncols
        print(os.getcwd(), "行数 %d,列数 %d" % (nrows, ncols))
        row_list = []
        for i in range(1, nrows):
            row_data = sh.row_values(i)
            row_list.append(row_data)
            print(row_list)
            n = i - 1
            user = User()
            user.stu_id = row_list[n][0]
            user.name = row_list[n][1]
            user.gender = row_list[n][2]
            user.grade = row_list[n][3]
            user.email = row_list[n][4]
            db.session.add(user)

        db.session.commit()
        db.session.close()

    users = User.query.all()
    print(users)
    return "读取成功"




@api.route("/read_excel/send_email", methods=["POST", "GET"])
# @celery.task(name="send_email")
def send_email():
    app = Flask(__name__)
    # 配置邮件：服务器／端口／传输层安全协议／邮箱名／密码
    app.config.update(
        DEBUG=True,
        MAIL_SERVER='smtp.qq.com',
        MAIL_PROT=465,
        MAIL_USE_TLS=True,
        MAIL_USERNAME='728363298@qq.com',
        MAIL_PASSWORD='pztwrvdpxtwsbfje',
    )

    mail = Mail(app)
    stu_id = request.form.get("stu_id", default="20155956", type=str)
    user_name = db.session.query(User.name).filter().all()
    stu_id = User.query.filter_by(stu_id=stu_id).first()
    if not stu_id:
        print(u"没有该学生")
    else:
        reci_email = stu_id.email
 # sender 发送方，recipients 接收方列表
    msg = Message("This is a test ",sender='728363298@qq.com', recipients=[reci_email])
    #邮件内容
    msg.body = "测试erer一"
    try:
        #发送邮件
        mail.send(msg)
    except Exception as e:
        print(str(e))
        print(reci_email)
        tasks.send_failed_email(reci_email)
        return "Sent Succeed222"
    else:
        print u"第一次邮件发送成功"
        return "Sent　Succeed111"


