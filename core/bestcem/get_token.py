# -*- coding: utf-8 -*-
from core.bestcem.user import Authorize
from core.utils import read_yaml
import sys
token = ''
auth = Authorize()


def get_auth(user_type):
    params = read_yaml.get_user(user_type)
    r = auth.post_company_token(user_name=params['user_name'], password=params['password'], org_code='')
    if r.status_code != '200' and 'token' not in r.json().keys():
        sys.exit(0)
    global token
    token = f"Bearer {r.json()['data']['token']}"

