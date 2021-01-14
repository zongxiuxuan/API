# -*- coding: utf-8 -*-
from core.utils import request, api_yaml
import jsonpath

apis = api_yaml.read_api()
print(jsonpath.jsonpath(apis,'$..post_company_token'))