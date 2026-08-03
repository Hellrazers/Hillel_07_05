import logging
import os

import requests
from dotenv import load_dotenv

load_dotenv()

logger_api = logging.getLogger('api')
class ApiSession:


    def __init__(self , token = None):
        self.user_login = os.getenv("USER_LOGIN")
        self.user_password = os.getenv("USER_PASSWORD")
        self.base_url = os.getenv("BASIC_URL")
        self.session = requests.Session()
        self.__token = token

    def get_token(self):
        resp = self.session.post(url=f'{self.base_url}/api/auth/signin',
                                 json={"email": self.user_login,
                                       "password": self.user_password,
                                       "remember": False}

        )
        if resp.status_code != 200:
            raise AttributeError("Authentication failed")
        token = resp.cookies.get('sid')
        if token is None:
            raise AttributeError("Something problem with token")

        self.__token = token


    def auth(self):
        if self.__token is None:
            self.get_token()
        else:
            self.session.cookies.update({'sid': self.__token})

    def get(self, **kwargs):
        self.auth()
        # if 'item_id' in kwargs:
        #     url_ = f'{self.base_url}{self.path}/{kwargs.get("item_id")}'
        # else:
        #     url_ = f'{self.base_url}{self.path}'
        logger_api.info(f'Request -> Method: GET for url:{self.base_url}{kwargs.get("path")}')
        resp = self.session.get(url=f'{self.base_url}{kwargs.get("path")}', params=kwargs.get("params"))
        logger_api.info(f'Response <- status code: {resp.status_code} resp:{resp.json()}')
        return resp

    def post(self, **kwargs):
        self.auth()
        logger_api.info(f'Request -> Method: POST for url:{self.base_url}{kwargs.get('path')} Payload:{kwargs.get("data")}')
        resp = self.session.post(url=f'{self.base_url}{kwargs.get('path')}', json=kwargs.get("data"))
        logger_api.info(f'Response <- status code: {resp.status_code} resp:{resp.json()}')
        return resp

    def delete(self, **kwargs):
        self.auth()
        logger_api.info(f'Request -> Method: DELETE for url:{self.base_url}{kwargs.get('path')}')
        resp = self.session.delete(url=f'{self.base_url}{kwargs.get('path')}')
        logger_api.info(f'Response <- status code: {resp.status_code} resp:{resp.json()}')
        return resp



