#!/usr/bin/env python
# -*- coding: utf-8 -*-
import pymongo
from sshtunnel import SSHTunnelForwarder
"""
操作mongo数据库
"""


db_host = ''
class ExecuteSQL(object):

    # 传入需要连接的数据库的名称dbname和待执行的sql语句sql
    def __init__(self, dbname, set, type, sql, limit=None, do=None):
        """
        :param dbname: 数据库名
        :param set: 表名，集合
        :param type: 数据操作类型
        :param sql: 查询filter
        :param limit: 查询限制数
        :param do: 筛选结果操作
        """
        self.dbname = dbname
        # filter 条件
        self.sql = sql
        self.set = set
        self.type = type
        self.limit = limit
        # do 可以是 select中的projection 也可以是update中的set操作 多filter可用and连接
        self.do = do

    def execute_sql(self):
        with SSHTunnelForwarder(
                # 跳板机地址和端口号
                ssh_address_or_host=('52.83.126.92', 42222),
                # private key地址，Robo 3T中的地址复制出来即可
                ssh_pkey='/Users/mac/.ssh/id_rsa',
                # 跳板机的user name
                ssh_username='work',
                # db的地址和端口号
                remote_bind_address=(db_host.host, 30000)
        ) as server:
            # 打开数据库连接
            client = pymongo.MongoClient('127.0.0.1', username=db_host.username,
                                         password=db_host.password, port=server.local_bind_port)
            # connect db
            db = client[self.dbname]
            # connect set
            collection = db[self.set]
            # operation
            if self.type == 'select':
                if limit is None:
                    try:
                        # 执行sql
                        result = collection.find(self.sql, projection=self.do)
                        return list(result)
                    except Exception as e:
                        print('Error: select fail，%s' % e)
                    finally:
                        client.close()
                else:
                    try:
                        # 执行sql
                        result = collection.find(self.sql, projection=self.do).limit(self.limit)
                        return list(result)
                    except Exception as e:
                        print('Error: select fail，%s' % e)
                    finally:
                        client.close()

            elif self.type == 'delete':
                try:
                    # 执行sql
                    collection.delete_many(self.sql)
                    result = collection.find()
                    return list(result)
                except Exception as e:
                    print('Error: delete fail，%s' % e)
                finally:
                    client.close()
            elif self.type == 'insert':
                try:
                    for record in self.sql:
                        # 执行sql
                        collection.save(record)
                        result = collection.find()
                        return list(result)
                except Exception as e:
                    print('Error: insert fail，%s' % e)
                finally:
                    client.close()
            elif self.type == 'update':
                try:
                    # 执行sql
                    collection.update_many(self.sql, self.do)
                    result = collection.find()
                    return list(result)
                except Exception as e:
                    print('Error: update fail，%s' % e)
                finally:
                    client.close()
            else:
                print('invalid type')
                client.close()


if __name__ == '__main__':
    # data和collection为查询的字段
    dbname = 'course'
    set = 'ClubBrief2'
    type = 'select'
    # sql为查询语句 {'enterpriseAccountId': {'$exists': False}} 为筛余不存在key为'enterpriseAccountId'的文档；
    # projection={'_id': False, 'id': True} 为只输出id，不输出_id ；limit 限制查询数量
    sql = {'enterpriseAccountId': {'$exists': False}}
    do = {'_id': False, 'id': 1}
    limit = 3
    connect = ExecuteSQL(dbname, set, type, sql, limit, do)
    print(connect.execute_sql())