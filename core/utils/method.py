#!/usr/bin/env python
# -*- coding: utf-8 -*-
import random
import json
import arrow
from faker import Factory
import os
import time
"""
创建测试数据方法
"""
f = Factory().create('zh-CN')


# 获取根目录
def rootPath():
    # 获取当前文件路径
    currentDir = os.path.abspath(os.path.dirname(__file__))
    # 截取根目录路径
    proDir = os.path.split(currentDir)[0]
    # # 获取当前路径
    # get_currentDir = os.path.dirname(os.getcwd())
    return proDir


# 随机取任意长度数字字符
def strNum(len=1):
    text = '1234567890'
    text_new = (''.join(random.choice(text) for i in range(len)))
    return text_new


# 随机获取任意长度数字
def long_num(lenth=1):
    text = '1234567890'
    num = (''.join(random.choice(text) for i in range(lenth)))
    return int(num)

# 随机取任意数量字符
def Uppercase(number=1):
    text = 'ABCDEFGHIJKLMNOPQRSTUVWXYZ'
    text_new = (''.join(random.choice(text) for i in range(number)))
    return text_new

# 随机取任意数量字符
def lowercase(number=1):
    text = 'abcdefghijklmnopqrstuvwxyz'
    text_new = (''.join(random.choice(text) for i in range(number)))
    return text_new

# 随机取任意数量字符
def chinese(number=1):
    text = '离离原上草，一岁一枯荣。野火烧不尽，春风吹又生。远芳侵古道，晴翠接荒城。又送王孙去，萋萋满别情。人间四月芳菲尽，山寺桃花始盛开。长恨春归无觅处，不知转入此中来。天长地久有时尽，此恨绵绵无绝期。在天愿作比翼鸟，在地愿为连理枝。' \
	'别有幽愁暗恨生，此时无声胜有声。同是天涯沦落人，相逢何必曾相识。细草微风岸，危樯独夜舟。星垂平野阔，月涌大江流。名岂文章著，官应老病休。飘飘何所似？天地一沙鸥。'
    text_new = (''.join(random.choice(text) for i in range(number)))
    return text_new

# 随机取任意数量字符 （缺'_'）
def half_angle(number=1):
    text = r'~`!@#$%^&*()-+={[}]|\:;"<.,>?/'
    text_new = (''.join(random.choice(text) for i in range(number)))
    return text_new

#符号字符
def full_symbol(number=1):
    text = r'`~！#￥%……&*（）——-+={【}】|、《，》。？、：；"'
    text_new = (''.join(random.choice(text) for i in range(number)))
    return text_new


# 随机取任意数量字符，但是绘文字在前端中算2个字符
def emoji(number=1):
    text = '👌💋🚗🍰🐱🐶🐭🎁🎂'
    text_new = (''.join(random.choice(text) for i in range(number)))
    return text_new


# 随机取任意数量字符
def japanese(number=1):
    text = 'にほんごなくてないで'
    text_new = (''.join(random.choice(text) for i in range(number)))
    return text_new


# 随机取任意数量字符
def Arabic(number=1):
    text = "خلف سوق الذه"
    text_new = (''.join(random.choice(text) for i in range(number)))
    return text_new


# 除数字下划线字母以为的字符组合
def numberTitle(chi=1, japen=1, fullSymbol=1, halfSy=1):
    text = chinese(chi) + japanese(japen)  + full_symbol(fullSymbol)  +half_angle(halfSy)
    return text

# 把所有常用类型的字符拼接在了一起，默认都取一个字符
def usu_text(lower=1, upper=1, number=1, half_angle_symbol=1):
    text = lowercase(lower) + Uppercase(upper) + strNum(number) + half_angle(half_angle_symbol)
    return text


# 把所有不常用类型的字符拼接在了一起，默认都取一个字符
def ob_text(chi=1, japen=1, arabic=1, fullSymbol=1, Emoji=1):
    text = chinese(chi) + japanese(japen) + Arabic(arabic) + full_symbol(fullSymbol) + emoji(Emoji)
    return text


# 把所有常用和不常用类型的字符拼接在了一起，默认都取一个字符
def al_text(lower=1, upper=1, number=1, half_angle_symbol=1,chi=1, japen=1, arabic=1, fullSymbol=1, Emoji=1):
    text = usu_text(lower=lower, upper=upper, number=number, half_angle_symbol=half_angle_symbol) + ob_text(chi=chi, japen=japen, arabic=arabic, fullSymbol=fullSymbol, Emoji=Emoji)
    return text


# info 多少长度的文本  带空格
def _info(num):
    info = ''
    for i in range(int(num/5)):
       info = info + '%s ' % (f.pystr(min_chars=4, max_chars=4))
    return info


# get now time
def now_time():
    curTime = arrow.now()
    t = curTime.format('YYYY-MM-DD hh:mm:ss')
    return t


# get now timestamp
def now_timestamp():
    curTime = arrow.now()
    t = curTime.timestamp*1000
    return t


# get sys time
def get_system_time():
    return time.strftime('%Y-%m-%d %H:%M:%S', time.localtime())


# get anytime format
def getFormatTime(type='days', num=0, format='YYYY-MM-DD HH:mm:ss', tzinfo=None):
    t = arrow.now()
    # t = curTime.to(tz=timezone)
    if type == 'days':
        return t.shift(days=num).format(format)
    if type == 'weeks':
        return t.shift(weeks=num).format(format)
    if type == 'months':
        return t.shift(months=num).format(format)
    if type == 'years':
        return t.shift(years=num).format(format)


# get 当前天的间隔time
def getTimestamp(type='days', num=0, hour=00, minute=00, second=00 ):
    if type =='days':
        return arrow.now().shift(days=num).replace(hour=hour,minute=minute,second=second).timestamp*1000
    if type =='weeks':
        return arrow.now().shift(weeks=num).replace(hour=hour,minute=minute,second=second).timestamp*1000
    if type =='months':
        return arrow.now().shift(months=num).replace(hour=hour,minute=minute,second=second).timestamp*1000
    if type =='years':
        return arrow.now().shift(years=num).replace(hour=hour,minute=minute,second=second).timestamp*1000
    else:
        print('no value,please check void')


# 自定义时间
def getAnyTimestamp(year, month, day, hour=00, minute=00, second=00, tzinfo='+08.00'):
    return arrow.Arrow(year=year, month=month, day=day, hour=hour, minute=minute, second=second, tzinfo=tzinfo).timestamp*1000


# email
def email():
    email = f.free_email()
    return email


# error_email():
def error_email():
    return ['', ' ', '.1@1.1.1', '123.2123-1@1.1', '1+1.1@1.1', '1@1.1.', 5]


# phone
def phone():
    return f.phone_number()


#Chrome user-agent info
def ChromeUserAgent():
    return f.chrome()


# error phone
def error_phone():
    return ['', ' ', '@#$%^&!@', '0', '11000000000', '1999999999']


def invalid_email():
    return ['', '    ', '.1@1.1.1', '123.2123-1@1.1', '1+1.1@1.1', '1@1.1.', 5]


def getKeys(dir):
    list = []
    for i in dir.keys():
        list.append(i)
    return list


def getValue(dir):
    list = []
    for i in dir.values():
        list.append(i)
    return list


# 返回值为set 和 None
def checkKeys(pre,dir):
    res = set(dir.keys())
    if pre<=res:
        pass
    else:
        dif = pre - res
        return dif


def _string(n1, n2):
    str = f.pystr(min_chars=n1,max_chars=n2)
    return str


def ipv4():
    ip = f.ipv4()
    return ip


def user_agent():
    ua = f.user_agent()
    return ua


# 返回值为set 和 None
def checkValue(dir,key,value):
    if dir[key] != value:
        return key
    else:
        pass




# 生成时间戳
def timestr():
    start = (2000, 1, 1, 0, 0, 0, 0, 0, 0)
    end = (2020, 1, 1, 0, 0, 0, 0, 0, 0)
    begin = time.mktime(start)
    endless = time.mktime(end)
    return random.randint(begin, endless)


# 固定值拆分
def fixSum(len,sum):
    l = []
    for i in range(len):
        if i != len-1:
            i = random.randrange(0,sum)
            sum = sum - i
            l.append(i)
        else:
            i = sum
            l.append(i)
    return l


# 将列表拆分为n个子列表
def fixchoose(num, l_choose):
    l = []
    for i in range(num):
        if i != num-1:
            l1 = random.sample(l_choose, k=random.randrange(0, num + 1))
            l.append(l1)
            l_choose = [i for i in l_choose if i not in l1]
    l.append(l_choose)
    return l

# 时分计算
def hm_time():
    hour = random.randrange(0,25)*3600
    minu = random.randrange(0,60)*60
    tt = hour + minu
    return tt


# 随机获取一段时间内某一时间的时间戳
def strTimeProp(start='1971-01-01', end='2050-12-31', prop=random.random(), frmt='%Y-%m-%d'):
    stime = time.mktime(time.strptime(start, frmt))
    etime = time.mktime(time.strptime(end, frmt))
    ptime = stime + prop * (etime - stime)
    return int(ptime)



# 读取excel问卷
def readExcelFile(filename='protest-原话记录.xlsx'):
    lists = []
    workbook = xlrd.open_workbook(filename=filename)
    booksheet = workbook.sheet_by_index(0)
    for i in range(booksheet.nrows):
        lists.append("".join(booksheet.row_values(i)))
    return lists


if __name__ == '__main__':
   print(getTimestamp())