# -*- coding: utf-8 -*-
from core.utils import request, read_yaml
import jsonpath

apis = read_yaml.read_api()
print(jsonpath.jsonpath(apis,'$..post_company_token'))