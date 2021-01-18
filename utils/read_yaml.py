#!/usr/bin/env python
# -*- coding: utf-8 -*-
import yaml
from utils import getDir


def read_yaml(path):
	path = f'{getDir.proDir}{path}'
	return yaml.safe_load(open(path))
