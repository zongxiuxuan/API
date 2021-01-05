#!/usr/bin/env python
# -*- coding: utf-8 -*-
import yaml
import jsonpath
from core.utils import getDir

_APIS = yaml.safe_load(open(f'{getDir.coreDir}/bash_url.yaml'))
_CONFIG = yaml.safe_load(open(f'{getDir.proDir}/config.yaml'))


def get_api(expr):
    return jsonpath.jsonpath(_APIS, expr)[0]


def get_user(user_type='admin_user'):
    return _CONFIG[user_type]


def read_yaml(path):
    return yaml.safe_load(open(path))

if __name__ == '__main__':
    print(read_yaml(f'{getDir.proDir}/data/account_login.yml'))