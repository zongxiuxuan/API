#!/usr/bin/env python
# -*- coding: utf-8 -*-

import os

# 获取当前文件路径
# currentDir = os.path.dirname(os.path.dirname(__file__))
currentDir = os.path.abspath(os.path.dirname(__file__))
# 截取根目录路径
proDir = os.path.split(currentDir)[0]


if __name__ == '__main__':
    print(currentDir)
    print(proDir)