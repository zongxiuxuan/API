# -*- coding: utf-8 -*-
import yaml


file = r'D://API/core/bash_url.yaml'
# s1 = yaml.safe_load(open(file))
# print(s1)
s2 = yaml.load(open(file), Loader=yaml.FullLoader)
print(s2)
print(s2['user']['group_tree']['get'])