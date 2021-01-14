# -*- coding: utf-8 -*-
import smtplib
from core.utils import api_yaml
from email import encoders
from email.mime.base import MIMEBase
from email.mime.multipart import MIMEMultipart
from utils import getDir
import time
import os


# 使用email模块
def sentMail(newFile, to_addr, from_addr, passwd, smtp_server, smtp_port):
    resultPath = os.path.join(getDir.proDir, "report/API_report/report_html/")
    msg = MIMEMultipart()
    # msg.attach(body)
    msg['From'] = from_addr

    # 多个邮件接收者需要修改to_addr
    msg['To'] = ','.join(to_addr)
    msg['Subject'] = 'API Auto Testing Report'
    msg['date'] = time.strftime('%a,%d %b %Y %H:%M:%S %z')

    part = MIMEBase('application', 'octet-stream')
    part.set_payload(open(newFile, 'rb').read())
    encoders.encode_base64(part)
    part.add_header('Content-Disposition', 'attachment; filename="test_report.html"')
    msg.attach(part)
    server = smtplib.SMTP(smtp_server, smtp_port)
    server.set_debuglevel(1)
    server.login(from_addr, passwd)
    # for发给多个接收者
    # for to_addr in addrs:
    server.sendmail(from_addr, to_addr, msg.as_string())
    server.quit()
    print(u'Mail sent successfully')


def sendReport_newfile(flag):
    if flag == 'Y':
        resultPath = os.path.join(getDir.proDir, "report/API_report/report_html/")
        lists = os.listdir(resultPath)
        # 找到最新的测试报告
        lists.sort(key=lambda fn: os.path.getmtime(resultPath + fn) if not os.path.isdir(resultPath + fn) else 0)
        # 找到最新的文件
        newFile = os.path.join(resultPath, lists[-1])
        # print(newFile)
        # 调用发邮件模块
        sentMail(newFile)
    else:
        print('send email functional is off')
