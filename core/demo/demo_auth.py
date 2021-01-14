#!/usr/bin/env python
# -*- coding: utf-8 -*-
from core.bestcem import user
from core.utils import api_yaml
import sys

auth = user.Authorize()


def get_auth(user_type='admin_user'):
    params = api_yaml.get_user(user_type)
    r = auth.post_company_token(user_name=params['user_name'], password=params['password'], org_code='')
    if r.status_code != '200' and 'token' not in r.json().keys():
        sys.exit(0)
    global token
    token = f"Bearer {r.json()['data']['token']}"


if __name__ == '__main__':
    get_auth()
    print(token)
