#!/usr/bin/env python
# -*- coding: utf-8 -*-
import Common.method as method
from functools import wraps
from Common.method import now_time
from Common import getDir
getDir = getDir.proDir

# log for html
def fail_log(parameter, expect, result, text=None, time=None):
    if text is None:
        return 'timestamp:' + str(time) + ' ' + 'parameter:' + str(parameter) + ' ' + 'expect:' + str(
            expect) + ' ' + 'actual:' + str(result)
    else:
        return str(text) + ' ' + 'parameter:' + str(parameter) + ' ' + 'expect:' + str(expect) + ' ' + 'actual:' + str(
            result)


# # log for file
def create_log(timestamp, item, rescode, url, data, text, result=None):
    if result is not None:
        log = 'time: {time}, timestamp: {tstamp}, testItem: {item},res_code: {rescode}\n$posturl: {posturl}\n' \
              '$postdata: {postdata}\n$resdata: {rsdata}\n$res_error: {res_error}\n---\n' \
            .format(time=method.get_system_time(), tstamp=timestamp, item=item, rescode=rescode, posturl=url,
                    postdata=data,
                    rsdata=text, res_error=str(result))
        return log
    else:
        log = 'time: {time}, timestamp: {tstamp}, testItem: {item},res_code: {rescode}\n$posturl: {posturl}\n' \
              '$postdata: {postdata}\n$resdata: {rsdata}\n---\n' \
            .format(time=method.get_system_time(), tstamp=timestamp, item=item, rescode=rescode, posturl=url,
                    postdata=data,
                    rsdata=text)
        return log


# 带参数的装饰器，在函数中嵌入装饰器，日志类场景
def logit(logfile = "out.log"):
	def logging_decorator(func):
		@wraps(func)
		def warpping_function(*args, **kwargs):
			log_string = func.__name__ + " was called"
			with open(logfile,'a') as open_file:
				open_file.write("{} {} \n".format(now_time(),log_string))
			return func(*args, **kwargs)
		return warpping_function
	return logging_decorator

