#!/usr/bin/env python
# -*- coding: utf-8 -*-

import os
#获取当前目录
currentDir=os.path.dirname(__file__)
# 获取core目录
coreDir = os.path.dirname(currentDir)
# 截取项目路径
proDir = os.path.split(coreDir)[0]


if __name__ == '__main__':
    print(coreDir)
    print(currentDir)
    print(proDir)