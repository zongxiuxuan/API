import pandas as pd
from Common import method
import random
from faker import Factory
'''
file(问卷路径) n(数据量) ..(key=type)
type ='num' 3位int类型数字
      'phone'
      'id' 从0自增
      'ip'
      'num' 3位int
      'sex'
      'tag' 门店标签
      'code' 门店编号
      'email'
      'string' 5-10位字符串
      'sentence' 语句
      'user_agent'
type为其他时会将type值写入key列中
ex： '电话'='phone' 生成"电话"列，内容为随机电话号
'''
f = Factory().create('zh-CN')


def writefile(file, n, **kwargs):
    l={}
    ls = [i for i in kwargs.items()]
    for i in range(len(ls)):
        l[ls[i][0]] = []
        for k in range(n):
            if ls[i][1] == 'name':
                l[ls[i][0]].append('test_'+str(k))
            elif ls[i][1] == 'id':
                l[ls[i][0]].append(k)
            elif ls[i][1] == 'num':
                l[ls[i][0]].append(method.long_num(3))
            elif ls[i][1] == 'phone':
                l[ls[i][0]].append(method.phone())
            elif ls[i][1] == 'email':
                l[ls[i][0]].append(method.email())
            elif ls[i][1] == 'ip':
                l[ls[i][0]].append(method.ip())
            elif ls[i][1] == 'user_agent':
                l[ls[i][0]].append(method.user_agent())
            elif ls[i][1] == 'string':
                l[ls[i][0]].append(method._string(5, 10))
            elif ls[i][1] == 'sentence':
                l[ls[i][0]].append(f.sentence())
            elif ls[i][1] == 'sex':
                l[ls[i][0]].append(random.choice(['男', '女']))
            elif ls[i][1] == 'tag':
                l[ls[i][0]].append('test_'+str(k))
            elif ls[i][1] == 'code':
                l[ls[i][0]].append(random.choice(['code_1', 'code_2', 'code_3', 'code_4', 'code_5', 'code_6', 'code_7', 'code_8' 'code_9']))
            else:
                l[ls[i][0]].append(l[ls[i][0]])
    data = l
    df = pd.DataFrame(data)
    df.to_excel(file, index=False)


if __name__ == '__main__':
    writefile(file='code.xlsx')
    writefile(file='new1.xlsx', n=10, ID='id', 姓名='name', 手机号='phone', 邮箱='email', 性别='sex', 微信userid='string', 支付宝userid='string', 归属门店='code', 标签='tag')