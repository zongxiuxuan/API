# -*- coding: utf-8 -*-
import smtplib
from email.mime.text import MIMEText
from email import encoders
from email.mime.base import MIMEBase
from email.mime.multipart import MIMEMultipart
from utils import getDir
import time
import os


# 使用email模块
def sentMail(to_addr, from_addr, passwd, smtp_server, smtp_port, file=None, text=None):
    msg = MIMEMultipart()
    # msg.attach(body)
    msg['From'] = from_addr

    # 多个邮件接收者需要修改to_addr
    msg['To'] = ','.join(to_addr)
    msg['Subject'] = 'API Auto Testing Report'
    msg['date'] = time.strftime('%a,%d %b %Y %H:%M:%S %z')
    if not file:
        part = MIMEBase('application', 'octet-stream')
        part.set_payload(open(file, 'rb').read())
        encoders.encode_base64(part)
        part.add_header('Content-Disposition', 'attachment; filename="test_report.html"')
        msg.attach(part)
    if not text:
        msg.attach(MIMEText(text, 'plain', 'utf-8'))
        # body = MIMEText(text, _charset='utf-8')
        # msg.attach(body)
        # msg['Body'] = text
    server = smtplib.SMTP(smtp_server, smtp_port)
    server.set_debuglevel(1)
    server.login(from_addr, passwd)
    # for发给多个接收者
    # for to_addr in addrs:
    server.sendmail(from_addr, to_addr, msg.as_string())
    server.quit()
    print(u'Mail sent successfully')


def sendReport(flag, to_addr, from_addr, passwd, smtp_server, smtp_port, file=None, text=None):
    if flag == 'true':
        if not file:
            file = os.path.join(getDir.proDir, "report/report.html")
            # lists = os.listdir(resultPath)
            # # 找到最新的测试报告
            # lists.sort(key=lambda fn: os.path.getmtime(resultPath + fn) if not os.path.isdir(resultPath + fn) else 0)
            # # 找到最新的文件
            # newFile = os.path.join(resultPath, lists[-1])
            # # print(newFile)
            # # 调用发邮件模块
            sentMail(to_addr, from_addr, passwd, smtp_server, smtp_port, file)
        elif not text:
            text = text
            sentMail(to_addr, from_addr, passwd, smtp_server, smtp_port, text)
        else:
            pass
    else:
        print('send email functional is off')
