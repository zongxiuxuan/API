#!/usr/bin/env python
# -*- coding: utf-8 -*-
import pytest
from core.utils import request

class Testproject:
	def test_add(self):
		token = 'Bearer eyJ0eXAiOiJKV1QiLCJhbGciOiJIUzI1NiJ9.eyJleHAiOjE2MDczNTc1OTUsImlhdCI6MTYwNzM1MDM5NSwiaXNzIjoiSURZOk1YIiwibmJmIjoxNjA3MzUwMzk1LCJvcmdfZXhwIjoiMjAyMi0wOS0wMSIsIm9yZ19jb2RlIjoienh4MDEiLCJvcmdfbmFtZSI6Inp4eF90ZXN0MDAxIiwib3JnX2lkIjoiNWRhOTEzNzVhYWNlNzAwMDA5MDBiMzc1IiwidWlkIjoiNWRhOTEzNzZjNTI1ZWQ3NDgzMjI5NDZlIiwidW5hbWUiOiJ6QHh4IiwiYXZhdGFyIjoiIiwic3VwZXIiOjF9.D-TK7zhw8Pw-eJQOdIpotjh0s6wUYX6vHItgk68_NVY'
		url = 'https://zxx01.xm-test.bestcem.com/api/qdes/v3/projects/5fce3928aace70000aa461ef/read/'
		r = request.put(url, payload={"badge_status": 1}, token=token)
		assert r.json()['code'] == 0