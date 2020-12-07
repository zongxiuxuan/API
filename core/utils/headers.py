import requests
import json
import urllib3
import logging


def headers(tokenid=None):
    if tokenid:
        return {
            'authorization': str(tokenid)
        }


# set a new headers
def headers_new(a=None, b=None):
    if a and b:
        return {
            a: b
        }


env = ''


def request(method, url, json=None, params=None, token=None, files=None, verify=False):
    if env == '':
        _url = url
    else:
        _url = f'{env}{url}'
    if not token:
        header = headers()
    else:
        header = headers(token)
    try:
        urllib3.disable_warnings()
        response = requests.request(
            method=method,
            url=_url,
            json=json,
            data=params,
            headers=header,
            files=files,
            verify=verify
        )
    except requests.RequestException as e:
        logging.error('RequestException URL : %s' % url)
        logging.error('RequestException Info: %s' % e)
        return

    except Exception as e:
        logging.error('Exception URL : %s' % url)
        logging.error('Exception Info: %s' % e)
        return

    time_total = response.elapsed.total_seconds()
    status_code = response.status_code

    logging.info("-" * 100)
    logging.info('[ api name    ] : {}'.format(url.rsplit("/")[-1]))
    logging.info('[ request url ] : {}'.format(response.url))
    logging.info('[ method      ] : {}'.format(method.upper()))
    logging.info('[ status code ] : {}'.format(status_code))
    logging.info('[ time total  ] : {} s'.format(time_total))

    if "application/json" in response.headers.get("Content-Type"):
        logging.info('[ response json ] : %s' % response.json())
    else:
        logging.info('[ response text ] : %s' % response.text)
    logging.info("-" * 100)

    return response


# post
def post(url, json=None, token=None, param=None, file=None):
    """
    :param url: 请求url地址
    :param json: 参数类型为json，传{}
    :param token: 是否需要token认证
    :param param: 参数为表单,传{}
    :param file: 上传文件的key值和地址，传()
    :return: response
    """
    if json:
        r = request('POST', url=url, json=json, token=token)
    elif param and not file:
        r = request('POST', params=param, token=token)
    elif param and file:
        params = {}
        for k, v in param.items():
            params[k] = (None, str(v))
        params[file[0]] = (file[1].split('/')[-1], open(file[1], 'rb'))
        r = request('POST', url=url, token=token, files=params)
    elif not param and file:
        file = {file[0]: (file[1].split('/')[-1], open(file[1], 'rb'))}
        r = request('POST', url=url, token=token, files=file)
    else:
        r = request('POST', url=url, json='{}', token=token)
    return r


# get
def get(url, params=None, token=None):
    if not params:
        r = request('GET', url=url, token=token)
    else:
        r = request('GET', url=url, params=params, token=token)
    return r


# put
def put(url, data=None, token=None):
    if data is None:
        r = request('PUT', url, '{}', token=token)
    else:
        r = request('PUT', url, json=data, token=token)
    return r


# delete
def delete(url, token=None, params=None):
    if params:
        r = request('DELETE', url, json=params, token=token)
    else:
        r = request('DELETE', url, token=token)
    return r
