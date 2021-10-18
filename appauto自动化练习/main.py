from HTMLTestRunner import HTMLTestRunner
import unittest
import smtplib
from smtplib import SMTP_SSL
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart
from email.header import Header
from email.mime.application import MIMEApplication


def run_case(path, name):
    tests = unittest.defaultTestLoader.discover(path, pattern="Test*.py")

    runner = HTMLTestRunner.HTMLTestRunner(
        title="这是一个新浪微博app的测试报告",
        description="这是一个登陆模块的测试报告",
        verbosity=1,
        stream=open(name + ".html", mode="wb")
    )

    runner.run(tests)


def send_email(name):
    mail_host = 'smtp.qq.com'
    sender = '1075361524@qq.com'
    mail_pass = 'qkskjdxduoorbadb'
    receiver = '2431320433@qq.com'
    mail_title = '微博app测试用例执行结果'

    # 构造邮件对象
    msg = MIMEMultipart()
    msg["Subject"] = Header(mail_title, 'utf-8')
    msg["From"] = Header(sender, "utf-8")
    msg["To"] = Header(receiver, "utf-8")
    msg_content = "这是一份测试用例执行报告"
    msg.attach(MIMEText(msg_content, 'plain', 'utf-8'))

    # 添加附件
    attachment = MIMEApplication(open(r'C:\Users\Administrator\Desktop\day05【app自动化框架】\代码\appauto自动化练习\login.html').read())
    attachment["Content-Type"] = 'application/octet-stream'
    attachment["Content-Disposition"] = 'attachment;filename="%s"' % name
    msg.attach(attachment)

    # 发送邮件
    try:
        smtp = SMTP_SSL(mail_host)  # ssl登录连接到邮件服务器
        smtp.login(sender, mail_pass)
        smtp.sendmail(sender, receiver, msg.as_string())
        smtp.quit()
        print("邮件发送成功")
    except smtplib.SMTPException as e:
        print("无法发送邮件", e)


run_case(r'C:\Users\Administrator\Desktop\day05【app自动化框架】\代码\appauto自动化练习', "login")
send_email("login.html")
