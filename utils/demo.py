#!/usr/bin/env python
# -*- coding: utf-8 -*-
from utils import read_yaml
from utils import getDir

_config = read_yaml.read_yaml(f"{getDir.proDir}/config.yaml")
flag = _config['email']['flag']
stmp_address = _config['email']['stmp_address']
stmp_password = _config['email']['stmp_password']
stmp_server = _config['email']['stmp_server']
stmp_port = _config['email']['stmp_port']
send_to = _config['email']['send_to']
print(flag)
