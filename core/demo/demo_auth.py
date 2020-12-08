#!/usr/bin/env python
# -*- coding: utf-8 -*-
from core.utils import request
from requests_toolbelt import MultipartEncoder
import requests


url = '/api/user/users/{ID}'
file_path = '/Users/mac/Downloads/1.xlsx'
token = 'Bearer eyJ0eXAiOiJKV1QiLCJhbGciOiJIUzI1NiJ9.eyJleHAiOjE2MDc0MjUwNzAsImlhdCI6MTYwNzQxNzg3MCwiaXNzIjoiSURZOk1YIiwibmJmIjoxNjA3NDE3ODcwLCJvcmdfZXhwIjoiMjA5OS0xMi0zMSIsIm9yZ19jb2RlIjoiYnZ0Iiwib3JnX25hbWUiOiJidnQiLCJvcmdfaWQiOiI1ZmM4Yjk5NmFhY2U3MDAwMGNiMWFjMmIiLCJ1aWQiOiI1ZmM4Yjk5NmM2N2RhZWRkMjVkYWNmMDMiLCJ1bmFtZSI6Im5hbWUiLCJhdmF0YXIiOiJodHRwOi8vdGhpcmR3eC5xbG9nby5jbi9tbW9wZW4vUTNhdUhnend6TTdGaWNFblJkNUFpY2tlWENxRHVjTVU1dWdwRjRNZkdUdDRuWUJ1ZmN6TWljSEc4U1A3amR4Qk5iZFd3V3NWbTJIaE5KaGR0STZEdmRwUXdQbVdYbWtweTRlZGliV3kxQTdzdWdZLzEzMiIsInN1cGVyIjoxfQ.KHoPOIbqlKb8DoCJNK86XjzzEsKOzwu52U78o0Zmrtk'
def onetest(ID):
    r = request.put(url=url, token=token, payload={'status': '1'}, ID=ID)


if __name__ == '__main__':
    onetest('5fcf183baace70000ba46382')