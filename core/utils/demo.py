#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time     :2018/12/4
# File      :page_login.py

# import API.common.login
# import account
# import API.api.ci.getClubFeed as getClubFeed
# import API.request_data.getClubFeed_data as feedData
# import chardet
# API.common.login.login(account.account.super)
# token = API.common.login.token_id
#
# #
# # def get_clubcharts(request_data):
# # 	token_id = token
# # 	url = utils.url.Api.getClubCharts
# # 	data = request_data
# # 	r = utils.config.post(url, data, token_id)
# # 	return r
# #
# # data = {'startDate': 123, 'clubId': {'id': '12345641512456453'}, 'stopDate': 234, 'filter': {'pace': {'start': 0, 'stop': 999}, 'gender': 'MALE', 'age': {'start': 0, 'stop': 999}, 'connectivity': {'start': 0, 'stop': 999}, 'score': {'start': 0, 'stop': 999}, 'yearlyRound': {'start': 0, 'stop': 999}}, 'clubChartTypes': ['AGE_AND_GENDER', 'COURSE_DISTRIBUTION', 'NUMBER_OF_PLAYER', 'NUMBER_OF_ROUND', 'PACE_OF_PLAY', 'ROUND_FREQUENCY', 'SKILL_LEVEL', 'TIME_OF_PLAY'], 'clubGatherPatterns': [{'_TYPE': 'ClubSinglePattern', 'clubId': {'id': 'd140a890-86ac-11e4-8c28-020000005b00'}}]}
# # r = get_clubcharts(data)
# # print ,r.status_code,r.text
# p_data = feedData.getClubFeed_data()
# r = getClubFeed.getClubFeed(p_data)
# print  r.status_code
# print chardet.detect(200)

# send email demo
# import smtplib
# from email import encoders
# from email.mime.base import MIMEBase
# from email.mime.multipart import MIMEMultipart
# import os
# import time
# import utils.getDir
# # 使用mail模块
# # addrs = ['8535104@qq.com','30829351@qq.com']
#
# proDir = utils.getDir.proDir
# resultPath = os.path.join(proDir, "Output\\API_report\\")
# addrs = ['87859738@qq.com','1005369340@qq.com']
#
#
# def sentMail(newFile, from_addr='rain_zxx@163.com', passwd='zongxiuxuan000', smtp_server='smtp.163.com', to_addr=addrs):
#
#     msg = MIMEMultipart()
#     # msg.attach(body)
#     msg['From'] = from_addr
#
#     # 多个邮件接收者需要修改join
#     msg['To'] = ','.join(to_addr)
#     msg['Subject'] = '18Birdies - Web Auto Testing Report'
#     msg['date'] = time.strftime('%a,%d %b %Y %H:%M:%S %z')
#
#     part = MIMEBase('application', 'octet-stream')
#     part.set_payload(open(newFile, 'rb').read())
#     encoders.encode_base64(part)
#     part.add_header('Content-Disposition', 'attachment; filename="test_report.html"')
#     msg.attach(part)
#     server = smtplib.SMTP(smtp_server, 25)
#     server.set_debuglevel(1)
#     server.login(from_addr, passwd)
#
#     # for发给多个接收者
#     server.sendmail(from_addr, to_addr, msg.as_string())
#
#     server.quit()
#     print(u'Mail sent successfully')
#
#
# def sendReport(flag):
#     if flag == 'Y':
#         lists = os.listdir(resultPath)
#         # 找到最新的测试报告
#         lists.sort(key=lambda fn: os.path.getmtime(resultPath + fn) if not os.path.isdir(resultPath + fn) else 0)
#         # 找到最新的文件
#         newFile = os.path.join(resultPath, lists[-1])
#         # print(newFile)
#         # 调用发邮件模块
#         sentMail(newFile)
#     else:
#         return
#
# sendReport('Y')

# # mongodb demo
# import pymongo
# from utils.env import db_host as db_host
# from sshtunnel import SSHTunnelForwarder
#
#
# class ExecuteSQL(object):
#
#     # 传入需要连接的数据库的名称dbname和待执行的sql语句sql
#     def __init__(self, dbname, set, type, sql, limit, do=None):
#         self.dbname = dbname
#         # filter 条件
#         self.sql = sql
#         self.set = set
#         self.type = type
#         self.limit = limit
#         # do 可以是 select中的projection 也可以是update操作
#         self.do = do
#
#     def execute_sql(self):
#         results = ''
#         with SSHTunnelForwarder(
#                 # 跳板机地址和端口号
#                 ssh_address_or_host=('52.83.126.92', 42222),
#                 # private key地址，Robo 3T中的地址复制出来即可
#                 ssh_pkey='C:/Users/Administrator/.ssh/id_rsa',
#                 # 跳板机的user name
#                 ssh_username='work',
#                 # db的地址和端口号
#                 remote_bind_address=(db_host.host, 30000)
#         ) as server:
#             # 打开数据库连接
#             client = pymongo.MongoClient('127.0.0.1', username=db_host.username,
#                                          password=db_host.password, port=server.local_bind_port)
#             # connect db
#             db = client[self.dbname]
#             # connect set
#             collection = db[self.set]
#             # operation
#             if self.type == 'select':
#                 try:
#                     # 执行sql
#                     result = collection.find(self.sql, projection=self.do).limit(self.limit)
#                     return list(result)
#                 except Exception as e:
#                     print('Error: select fail，%s' % e)
#                 finally:
#                     client.close()
#
#             elif self.type == 'delete':
#                 try:
#                     # 执行sql
#                     collection.delete_many(self.sql)
#                     result = collection.find()
#                     return list(result)
#                 except Exception as e:
#                     print('Error: delete fail，%s' % e)
#                 finally:
#                     client.close()
#             elif self.type == 'insert':
#                 try:
#                     for record in self.sql:
#                         # 执行sql
#                         collection.save(record)
#                         result = collection.find()
#                         return list(result)
#                 except Exception as e:
#                     print('Error: insert fail，%s' % e)
#                 finally:
#                     client.close()
#             elif self.type == 'update':
#                 try:
#                     # 执行sql
#                     collection.update_many(self.sql, self.do)
#                     result = collection.find()
#                     return list(result)
#                 except Exception as e:
#                     print('Error: update fail，%s' % e)
#                 finally:
#                     client.close()
#             else:
#                 print('invalid type')
#                 client.close()
#
#
# if __name__ == '__main__':
#     # data和collection为查询的字段
#     dbname = 'course'
#     set = 'ClubBrief2'
#     type = 'select'
#     # sql为查询语句 {'enterpriseAccountId': {'$exists': False}} 为筛余不存在key为'enterpriseAccountId'的文档；
#     # projection={'_id': False, 'id': True} 为只输出id，不输出_id ；limit 限制查询数量
#     sql = {'enterpriseAccountId': {'$exists': False}}
#     do = {'_id': False, 'id': 1}
#     limit = 3
#     connect = ExecuteSQL(dbname, set, type, sql, limit,do)
#     print(connect.execute_sql())

# if demo
# a = {"one":1,"two":2,"three":3,"four":4}
# if a['one'] ==1  and a['two'] == 2:
#     if a["three"] == 3:
#         pass
#     if a["four"] == 5:
#         print('04')
#     if a["four"] == 6:
#         print(1)
#     else:
#         print("fail")
# else:
#     print("0")

# log demo
# import utils.log
#
# s = utils.log.fail_log(1,2,3,4,5)
# print(s)


# 全局变量 demo
# import API.common.enterprise.login as login
#
# class demo:
# 	def one(self):
# 		login.login()
# 	def two(self):
# 		r = login.token_id
# 		print(r)
#
# if __name__ == '__main__':
# 	demo().one()
# 	demo().two()

# while循环
# import Config
# round_num = Config.config.round_num
# # i=0
# # while i < round_num:
# # 	print(i)
# # 	i = i+1
# for i in range(round_num):
# 	print('hello')
# import random
# import API.enterprise.CI.request_data.updateClubInfo_data as data
# a= [1,2,3,4,5]
# for i in range(3):
# 	print(data.creat_updateClubInfo_data(address=random.choice(a)))
# import math
# print(int(math.pow(2,3))) #2的3次方
# print(math.sqrt(4)) #4的平方根
# list = {1,2,3,4,5}
# print(math.fsum(list)) #集合number求和
# a= {"a":1,"b":2,"c":3}
# s = (a.keys())
# print(s)
# print(type(s))
# for items in a.keys():
# 	print(items)
# s = ["a","b","c"]
# if a.keys() == s:
# 	print("ok")
# else:
# 	print("no")
# ----------------------------------------------------------
# import json
# import os
# # fp = open('/Users/mac/Documents/test.txt','r+')
# # s = {"22":22,"33":33}
# # print(type(s))
# # print(json.dumps(s))
# # print(type(json.dumps(s)))
# # fp.write(json.dump(s))
# # json.dump({'a':1,"b":2},fp)
# # fp.write('{"a":1}')
# # print(type(fp.read()))
# # fp.close()
# with open('/Users/mac/Documents/test.txt','a+') as fp:
# 	json.dump({"a":11,"s":2},fp)
# with open('/Users/mac/Documents/test.txt','r+') as fr:
# 	print(fr.read())

# import sys,os
# # print(sys.argv)
# print(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))


d = {'1':1,"2":2}
print(d.get("3",0))