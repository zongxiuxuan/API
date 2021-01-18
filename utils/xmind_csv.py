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
        headers = ["模块", "子模块", "功能", "功能点", "用例标题", "前置条件", "测试步骤", "预期结果"]

        with open(filename, 'w', encoding='utf-8-sig', newline='')as f:
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
        # 模块/子模块
        if "#" in topic_name:
            module_name = re.compile(r"[\u4e00-\u9fa5]+").findall(topic_name)[0]
            sub_module_name = re.compile(r"[\u4e00-\u9fa5]+").findall(topic_name)[1]
        else:
            module_name = sub_module_name = topic_name  # 模块名
        # 功能的数量
        fun_num = self.topics_num(xmind_content)
        # 用例列表
        case_list = []

        for i in range(1):
            fun_point_num = self.topics_num(xmind_content['topics'][i])
            if fun_point_num == 0:
                self.my_log().debug(f'第{i + 1}个功能模块下，测试的功能点数量为0，请确认用例是否编写完成')
            else:
                fun_name = self.xmind_title(xmind_content['topics'][i])
                for j in range(fun_point_num):
                    fun_point_name = self.xmind_title(xmind_content['topics'][i]['topics'][j])
                    case_point_num = self.topics_num(xmind_content['topics'][i]['topics'][j])
                    for k in range(case_point_num):
                        case = []
                        if case_point_num == 0:
                            self.my_log().debug('测试用例为空，请确认用例是否编写完成')
                        else:
                            case_title = self.xmind_title(xmind_content['topics'][i]['topics'][j]['topics'][k])
                            case_preconditions = self.xmind_title(
                                xmind_content['topics'][i]['topics'][j]['topics'][k]['topics'][0])
                            if not case_preconditions:
                                case_preconditions = "系统管理员登录"
                            case_step = self.xmind_title(
                                xmind_content['topics'][i]['topics'][j]['topics'][k]['topics'][0]['topics'][0])
                            expected_result = self.xmind_title(
                                xmind_content['topics'][i]['topics'][j]['topics'][k]['topics'][0]['topics'][0][
                                    'topics'][0])
                            case.append(module_name)
                            case.append(sub_module_name)
                            case.append(fun_name)
                            case.append(fun_point_name)
                            case.append(case_title)
                            case.append(case_preconditions)
                            case.append(case_step)
                            case.append(expected_result)
                            case_list.append(case)
                            print(case_list)
        return case_list

    def main(self, xmind_file, csv_file=None):
        """
        :param xmind_file: xmind测试用例的路径
        :param csv_file: 保存为csv格式测试用例的路径，可不填默认保存到对应的xmind测试用例同一路径下
        :return:
        """
        case_list = self.read_xmind(xmind_file)
        if not csv_file:
            csv_file = xmind_file.replace('.xmind', '.csv')
            self.write_csv(csv_file, case_list)
        else:
            self.write_csv(csv_file, case_list)


if __name__ == '__main__':
    xmind_file = r"C:\Users\87859\Desktop\123.xmind"
    XmindToCsv().main(xmind_file)
