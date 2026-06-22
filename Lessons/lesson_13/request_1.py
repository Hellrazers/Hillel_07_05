import logging.config
import time

logging.config.fileConfig('loggin_conf.ini')

# Використання логера
logger = logging.getLogger('api')



response_1 = {
    'status_code': 500,
    'headers': {
        'Content-Type': 'application/json',
    },
    'text': 'System_error'

}
response_2 = {
    'status_code': 200,
    'headers': {
        'Content-Type': 'application/json',
    },
    'text': 'System_error'

}


def request( method, url, data=None, response = None, json=None ):

    url_path = url
    logger.info(f"→ Method: {method}  Url path: {url_path}")
    if method.upper() not in ("GET", "DELETE"):
        payload = json if json is not None else data
        if payload:
            safe_payload = {k: "***" if k == "password" else v for k, v in payload.items()}
            logger.info(f"  Payload: {safe_payload}")



    logger.info(f"← Status code: {response['status_code']} Response time: 1000 ms")
    if response['status_code'] >= 400:
        try:
            logger.critical(f"  ✗ Error response: {response.json()}")
        except Exception:
            logger.critical(f"  ✗ Error response: {response['text']}")
    if response['status_code'] == 200 and method == 'POST':
        logger.info(f'Response from API: {response}')
    return response

# request('DELETE', 'example.com')
# request('POST', 'example.com')


def api_get_user(method, path, **kwargs):

    resp = request(method=method, url=path ,**kwargs)
    return resp

def api_post_user(method, path, **kwargs):

    resp = request(method=method, url=path ,**kwargs)
    return resp

api_get_user('GET', 'example.com', response=response_1)
api_post_user('POST', 'example.com', response=response_2)
