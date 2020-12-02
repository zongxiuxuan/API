import requests
import json
import urllib3
from requests_toolbelt import MultipartEncoder

def headers(tokenid=None):
    if tokenid:
        return {
            'authorization': str(tokenid)
        }


# set a new headers
def headers_new(a=None, b=None):
    if a and b :
        return {
            a: b
        }


# post
def post(url, json=None, token=None, data=None, filepath=None):
    if not token:
        header = headers()
    else:
        header = headers(token)
    if json:
        urllib3.disable_warnings()
        r = requests.post(url, json=json, headers=header, verify=False)
    elif data and not filepath:
        urllib3.disable_warnings()
        r = requests.post(url, data=data, headers=header, verify=False)
    elif data and filepath:
        urllib3.disable_warnings()
        params={}
        for k,v in data.items():
            params[k]=(None,str(v))
        params['files'] = (filepath.split('/')[-1],open(filepath,'rb'))
        print(f'params is {params}')
        r = requests.post(url,headers=header,files=params,verify=False)
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
