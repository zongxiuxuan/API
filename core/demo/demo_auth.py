#!/usr/bin/env python
# -*- coding: utf-8 -*-
import base64
import json

import requests
from requests.auth import HTTPBasicAuth

url = 'http://0.0.0.0:9999/demo1.txt'
r = requests.get(url)
rs = json.loads(base64.b64decode(r.content))
print(rs)
