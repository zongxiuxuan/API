#!/usr/bin/env python
# -*- coding: utf-8 -*-
import yaml


def read_yaml(path):
    return yaml.safe_load(open(path))
