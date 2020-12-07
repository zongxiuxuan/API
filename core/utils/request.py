import requests
import urllib3
import logging
from core.utils import log
log.Logging()


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
    logging.info('[      api      ] : {}'.format(url))
    logging.info('[  request url  ] : {}'.format(response.url))
    logging.info('[     method    ] : {}'.format(method.upper()))
    if json:
        logging.info(f'[  request data ] : {json}')
    if params:
        logging.info(f'[  request data ] : {params}')
    if files:
        logging.info(f'[  request data ] : {files}')
    logging.info('[  status code  ] : {}'.format(status_code))
    logging.info('[   time total  ] : {} s'.format(time_total))

    if "application/json" in response.headers.get("Content-Type"):
        logging.info('[ response json ] : %s' % response.json())
    else:
        logging.info('[ response text ] : %s' % response.text)
    logging.info("-" * 100)

    return response


# post
def post(url, payload=None, token=None, params=None, file=None):
    """
    :param url: 请求url地址
    :param json: 参数类型为json，传{}
    :param token: 是否需要token认证
    :param param: 参数为表单,传{}
    :param file: 上传文件的key值和地址，传()
    :return: response
    """
    if file:
        for k, v in params.items():
            params[k] = (None, str(v))
        params[file[0]] = (file[1].split('/')[-1], open(file[1], 'rb'))
        return request('POST', url=url, token=token, files=params)
    else:
        return request('POST', url=url, json=payload, params=params, token=token, files=file)


# get
def get(url, params=None, token=None):
    return request('GET', url=url, params=params, token=token)


# put
def put(url, payload=None, token=None):
    return request('PUT', url=url, json=payload, token=token)


# delete
def delete(url, token=None, payload=None):
    return request('DELETE', url, json=payload, token=token)
