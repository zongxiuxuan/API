#!/usr/bin/env python
# -*- coding: utf-8 -*-
import jsonpath
from utils import read_yaml

_APIS = read_yaml.read_yaml('/core/bash_url.yaml')
_CONFIG = read_yaml.read_yaml('/config.yaml')


def get_api(expr):
    return jsonpath.jsonpath(_APIS, expr)[0]


def get_user(user_type='admin_user'):
    return _CONFIG[user_type]


