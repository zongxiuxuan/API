#!/usr/bin/env python
# -*- coding: utf-8 -*-
import yaml
import jsonpath
from core.utils import getDir

APIS = yaml.safe_load(open(f'{getDir.coreDir}/bash_url.yaml'))


def get_api(expr):
	return jsonpath.jsonpath(APIS, expr)[0]


