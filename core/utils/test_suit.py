#!/usr/bin/env python
# -*- coding: utf-8 -*-

import unittest
import Config
import os
import Common.getDir
import smtplib
from email import encoders
from email.mime.base import MIMEBase
from email.mime.multipart import MIMEMultipart
import time
"""
配置测试数据集
"""

proDir = Common.getDir.proDir


# 建立test suit
def WebTestSuite():
    # set program
    program = Config.config.program
    suite = unittest.TestSuite()
    # setting case dir
    CaseDir = os.path.join(proDir, 'UI', 'GuangBen')
    # search test case
    d = unittest.defaultTestLoader.discover(start_dir=CaseDir, pattern='*.py')
    for case in d:
        suite.addTest(case)
    return suite


# 使用email模块
def sentMail(newFile, from_addr='rain_zxx@163.com', passwd='zongxiuxuan000', smtp_server='smtp.163.com'):
    to_addr = Config.config.send_email_to
    msg = MIMEMultipart()
    # msg.attach(body)
    msg['From'] = from_addr

    # 多个邮件接收者需要修改to_addr
    msg['To'] = ','.join(to_addr)
    msg['Subject'] = '18Birdies - Enterprise Auto Testing Report'
    msg['date'] = time.strftime('%a,%d %b %Y %H:%M:%S %z')

    part = MIMEBase('application', 'octet-stream')
    part.set_payload(open(newFile, 'rb').read())
    encoders.encode_base64(part)
    part.add_header('Content-Disposition', 'attachment; filename="test_report.html"')
    msg.attach(part)
    server = smtplib.SMTP(smtp_server, 25)
    server.set_debuglevel(1)
    server.login(from_addr, passwd)

    # for发给多个接收者
    # for to_addr in addrs:
    server.sendmail(from_addr, to_addr, msg.as_string())

    server.quit()
    print(u'Mail sent successfully')


def sendReport():
    flag = Config.config.send_email
    if flag == 'Y':
        resultPath = os.path.join(proDir, "Output/API_report/report_html/")
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
