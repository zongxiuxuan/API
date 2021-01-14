#!/usr/bin/env python
# -*- coding: utf-8 -*-
import logging
import pytest
from core.utils import api_yaml, request, log
from utils import getDir
from utils import read_yaml
from utils import send_email

_config = read_yaml.read_yaml(f"{getDir.proDir}/config.yaml")
log.Logging()


def pytest_runtest_call(__multicall__):
    try:
        __multicall__.execute()
    except KeyboardInterrupt:
        raise
    except:
        logging.exception('pytest_runtest_call caught exception:')
        raise


@pytest.fixture(scope='session')
def set_headers(user='admin_user'):
    url = f'{_config["env"]}/api/authorize/v2/token/'
    user = api_yaml.get_user(user)
    payload = {
        'is_home_page': False,
        'org_code': user['org_code'],
        'user_name': user['user_name'],
        'password': user['password']
    }
    result = request.post(url, payload=payload, env=False)
    token = f"Bearer {result.json()['data']['token']}"
    return token


@pytest.fixture(scope='session', autouse=True)
def send_report():
    print("test begin")
    yield
    send_email
