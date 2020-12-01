import requests
import json
import urllib3


def headers(tokenid=None):
    if tokenid is None:
        return {
            'Content-Type': 'application/json;charset=utf-8'
        }
    else:
        return {
            'Content-Type': 'application/json;charset=utf-8',
            'authorization': str(tokenid)
        }


# set a new headers
def headers_new(a=None, b=None):
    if a is None:
        return {
            'Content-Type': 'application/json;charset=utf-8',
        }
    else:
        return {
            'Content-Type': 'application/json;charset=utf-8',
            a: b
        }


# post
def post(url, data=None, token=None, form=None, file=None):
    if not token:
        header = headers()
    else:
        header = headers(token)
    if data:
        urllib3.disable_warnings()
        r = requests.post(url, json.dumps(data), headers=header, verify=False)
    elif form:
        urllib3.disable_warnings()
        r = requests.post(url, data=form, headers=header, verify=False)
    elif file:
        urllib3.disable_warnings()
        r = requests.post(url, files=file, headers=header, verify=False)
    else:
        urllib3.disable_warnings()
        r = requests.post(url, '{}', headers=header, verify=False)
    return r


# get
def get(url, params=None, token=None):
    if token is None:
        header = headers()
    else:
        header = headers(token)
    if not params:
        urllib3.disable_warnings()
        r = requests.get(url, headers=header, verify=False)
    else:
        urllib3.disable_warnings()
        r = requests.post(url, params=params, headers=header, verify=False)
    return r


# put
def put(url, data=None, token=None):
    if token is None:
        header = headers()
    else:
        header = headers(token)
    if data is None:
        urllib3.disable_warnings()
        r = requests.put(url, '{}', headers=header, verify=False)
    else:
        urllib3.disable_warnings()
        r = requests.put(url, json.dumps(data), headers=header, verify=False)
    return r


# delete
def delete(url, token=None, params=None):
    if token is None:
        header = headers()
    else:
        header = headers(token)
    if params:
        urllib3.disable_warnings()
        r = requests.delete(url, json=params, headers=header, verify=False)
    else:
        r = requests.delete(url, headers=header, verify=False)
    return r
