#!/usr/bin/env python
# -*- coding: utf-8 -*-
import yaml
import jsonpath
from core.utils import getDir

APIS = yaml.safe_load(open(f'{getDir.coreDir}/bash_url.yaml'))
CONFIG = yaml.safe_load(open(f'{getDir.coreDir}/config.yaml'))


def get_api(expr):
    return jsonpath.jsonpath(APIS, expr)[0]


def get_user(user_type='admin_user'):
    return CONFIG[user_type]
