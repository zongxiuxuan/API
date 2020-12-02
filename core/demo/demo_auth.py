#!/usr/bin/env python
# -*- coding: utf-8 -*-
from core.utils import headers
from requests_toolbelt import MultipartEncoder
import requests


url = 'https://zxx01.xm-test.bestcem.com/api/member/members/ind/import/?member_type=1'
file_path = '/Users/mac/Downloads/1.xlsx'
s='Bearer eyJ0eXAiOiJKV1QiLCJhbGciOiJIUzI1NiJ9.eyJleHAiOjE2MDY5MzE0MTMsImlhdCI6MTYwNjkyNDIxMywiaXNzIjoiSURZOk1YIiwibmJmIjoxNjA2OTI0MjEzLCJvcmdfZXhwIjoiMjAyMi0wOS0wMSIsIm9yZ19jb2RlIjoienh4MDEiLCJvcmdfbmFtZSI6Inp4eF90ZXN0MDAxIiwib3JnX2lkIjoiNWRhOTEzNzVhYWNlNzAwMDA5MDBiMzc1IiwidWlkIjoiNWRhOTEzNzZjNTI1ZWQ3NDgzMjI5NDZlIiwidW5hbWUiOiJ6QHh4IiwiYXZhdGFyIjoiIiwic3VwZXIiOjF9.Fngu1Mc-sCBClCs6ZeRvXnAJMLVipJ014hiVhVcmxZM'

r = headers.post(url=url, token=s,data={'primary_key': 'mobile','null_update':'true','existed_update':'true'},filepath=file_path)
print(r.json())
