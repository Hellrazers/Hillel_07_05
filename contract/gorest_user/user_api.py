import os

import requests
from assertpy import assert_that
from dotenv import load_dotenv

load_dotenv()


class Api:

    def __init__(self):
        self.session= None
        self.BASE_URL = "https://api.gorest.com"

    def get_token(self):
        if not self.session:
            session = requests.Session()

            session.headers.update({"Authorization": f"Bearer "})



# class GorestUser(Api):
#     def __init__(self):
#         super().__init__()




# # # Налаштування адаптера з кількістю спроб 3
# # adapter = HTTPAdapter(max_retries=3)
#
# # Додавання адаптера до сесії
# session.mount('http://', adapter)
# session.mount('https://', adapter)
#
# # Виконання запиту з автоматичною повторною спробою
# response = session.get('https://example.com')




class GorestUser(Api):
    BASE_URL = os.getenv('URL')
    PATH = f'public/v2/users'
    TOKEN = os.getenv('TOKEN')

    def user_get(self, param = None, exp_status_code = 200):
        '''
        We get users all by the pass public/v2/users
        in the gorest site
        :param param: query parameter for reequsers
        :param exp_status_code: defult value 2000
        :return: response json
        '''
        response = requests.get(url=f'{self.BASE_URL}/{self.PATH}', params = param, headers={"User-Agent": "Mozilla/5.0"})
        assert_that(response.status_code, f'wrong status code: {response.status_code}').is_equal_to(exp_status_code)
        return response.json()

    def user_post(self, dict_validate = None, exp_status_code = 201):
        response = requests.post(url=f'{self.BASE_URL}/{self.PATH}',
                      headers={"User-Agent": "Mozilla/5.0",
                               "Authorization": f"Bearer {self.TOKEN}"},
                      data=dict_validate)
        assert_that(response.status_code, f'wrong status code: {response.status_code}').is_equal_to(exp_status_code)
        return response.json()

    def user_delete(self, user_id, exp_status_code = 200):
        response = requests.delete(url=f'{self.BASE_URL}/{self.PATH}/{user_id}', headers={"User-Agent": "Mozilla/5.0"})
        assert_that(response.status_code, f'wrong status code: {response.status_code}').is_equal_to(exp_status_code)
        return response.json()