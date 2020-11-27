import logging
import logging.handlers
from Common import getDir, method
from loguru import logger
import os


proDir = getDir.proDir
ReportDir = os.path.join(proDir, "Output", "API_report", "log", method.getFormatTime(format='YYYY_MM_DD') + ".log")
logger.add(ReportDir, level='ERROR', encoding='utf-8', format='{time:YYYY-MM-DD HH:mm:ss} {level} {function} {message}')
lg = ''


def init_log(filename=""):
    # 1.创建1个logger对象：
    # 初始化记录错误日志
    proDir = getDir.proDir
    lg = logging.getLogger("Error")
    lg.setLevel(level=logging.INFO)
    ReportDir = os.path.join(proDir, "Output", "API_report", "log", filename, method.getFormatTime(format='YYYY_MM_DD') + ".log")
    if len(lg.handlers) == 0:  # 避免重复
        # 2.创建handler(负责输出，输出到屏幕streamhandler,输出到文件filehandler)
        fh = logging.FileHandler(ReportDir, mode="a", encoding="utf-8")
        fh.setLevel(level=logging.ERROR)
        sh = logging.StreamHandler()
        sh.setLevel(level=logging.INFO)
        # 3.创建formatter：
        formatter=logging.Formatter(fmt='%(asctime)s - %(levelname)s - Model:%(filename)s - Fun:%(funcName)s - Message:%(message)s ')
        # 4.绑定关系：①logger绑定handler
        lg.addHandler(fh)
        lg.addHandler(sh)
        # # ②为handler绑定formatter
        fh.setFormatter(formatter)
        sh.setFormatter(formatter)
    return lg


# 格式化log输出
def format_log(rescode, url, data, text):
    log = '\n$res_code: {rescode}\n$posturl: {posturl}\n' \
          '$postdata: {postdata}\n$resdata: {rsdata}\n---' \
        .format(rescode=rescode, posturl=url, postdata=data, rsdata=text)
    return log


if lg == '':
    lg = init_log()
