#!/usr/bin/env python
# -*- coding: utf-8 -*-
import re
s = "投放"
if '[' in s:
	print("ok")
res = re.compile(r"[\u4e00-\u9fa5]+").findall(s)
t = res.findall(s)
print(t)