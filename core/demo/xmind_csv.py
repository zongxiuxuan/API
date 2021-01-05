# -*- coding: utf-8 -*-
# @File    : xmind_csv.py

from xmindparser import xmind_to_dict
import csv
import re
import logging
import logging.handlers
from logging.handlers import TimedRotatingFileHandler
from datetime import datetime


class XmindToCsv():

	def my_log(self):
		'''创建对象的类方法'''
		# 创建日志搜集器
		mylog = logging.getLogger('mylog')
		mylog.setLevel('DEBUG')
		# 创建日志输出渠道
		sh = logging.StreamHandler()
		sh.setLevel('INFO')
		# 按时间进行轮转的收集器
		file_name = datetime.now().strftime("%Y-%m-%d") + '.log'
		fh = TimedRotatingFileHandler(file_name, encoding='utf8', when='h', interval=24, backupCount=3)
		fh.setLevel('DEBUG')
		# 将日志输出渠道和日志收集器进行绑定
		mylog.addHandler(fh)
		mylog.addHandler(sh)
		# 设置日志输出格式
		fot = '%(asctime)s-[%(filename)s-->line:%(lineno)d]-%(message)s'
		formatter = logging.Formatter(fot)
		# 将日志输出格式与输出渠道进行绑定
		sh.setFormatter(formatter)
		fh.setFormatter(formatter)
		return mylog

	def topics_num(self, value):
		"""获取xmind标题个数"""
		try:
			return len(value['topics'])
		except KeyError:
			return 0

	def xmind_title(self, value):
		"""获取xmind标题内容"""
		return value['title']

	def write_csv(self, filename, case):
		'''写入csv文件，case为列表'''
		headers = ["模块","功能","测试标题", "前置条件", "测试步骤", "预期结果"]

		with open(filename, 'w')as f:
			f_csv = csv.writer(f)
			f_csv.writerow(headers)
			f_csv.writerows(case)
		print("success!")

	def read_xmind(self, filename):
		'''读取xmind内容，返回case列表'''
		# xmind内容
		xmind_content = xmind_to_dict(filename)[0]['topic']
		# 主题名
		topic_name = self.xmind_title(xmind_content)
		# 模块标题
		if "[" or "【" in topic_name:
			module_name = re.compile(r"[\u4e00-\u9fa5]+").findall(topic_name)[0]
			function_name = re.compile(r"[\u4e00-\u9fa5]+").findall(topic_name)[1]
		else:
			module_name = function_name = topic_name
		# 功能标题
		print(module_name)
		# 二级模块的数量
		module_num = self.topics_num(xmind_content)
		print(module_num)
		# 用例列表
		case_list = []

		for i in range(module_num):
			case_num = self.topics_num(xmind_content['topics'][i])
			if case_num == 0:
				print(f'第{i + 1}个功能模块下，测试的功能点数量为0，请确认用例是否编写完成')
				self.my_log().debug(f'第{i + 1}个功能模块下，测试的功能点数量为0，请确认用例是否编写完成')
			else:
				tag = self.xmind_title(xmind_content['topics'][i])
				case_point_num = self.topics_num(xmind_content['topics'][i])
				for j in range(case_point_num):
					case = []
					if case_point_num == 0:
						self.my_log().debug('测试用例为空，请确认用例是否编写完成')
					else:
						case_point = self.xmind_title(xmind_content['topics'][i]['topics'][j])
						case_preconditions = self.xmind_title(xmind_content['topics'][i]['topics'][j]['topics'][0])
						case_step = self.xmind_title(xmind_content['topics'][i]['topics'][j]['topics'][0]['topics'][0])
						expected_result = self.xmind_title(
							xmind_content['topics'][i]['topics'][j]['topics'][0]['topics'][0]['topics'][0])
						case_title = "【" + tag + "】" + case_point
						case.append(module_name)
						case.append(function_name)
						case.append(case_title)
						case.append(case_preconditions)
						case.append(case_step)
						case.append(expected_result)
						case_list.append(case)
		return case_list

	def main(self,xmind_file,csv_file=None,):
		case_list = self.read_xmind(xmind_file)
		if not csv_file:
			csv_file = xmind_file.replace('.xmind','.csv')
			print(csv_file)
			self.write_csv(csv_file, case_list)
		else:
			self.write_csv(csv_file, case_list)


if __name__ == '__main__':
	xmind_file = "/Users/mac/Desktop/123.xmind"
	XmindToCsv().main(xmind_file=xmind_file)
