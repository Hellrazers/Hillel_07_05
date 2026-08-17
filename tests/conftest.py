import os
import random

import pytest
from dotenv import load_dotenv
from playwright.sync_api import Playwright, APIRequestContext, expect

from core.facad import ApiClient

load_dotenv()

@pytest.fixture(scope="session")
def api() -> ApiClient:
    return ApiClient()

@pytest.fixture()
def api_browser(playwright: Playwright):
    api_browser = playwright.request.new_context(
        base_url=os.getenv('BASIC_URL')
    )

    yield api_browser

    api_browser.dispose()

@pytest.fixture()
def api_pl(api_browser: APIRequestContext):
    response_login = api_browser.post(
        url='/api/auth/signin',
        data={
            "email": os.getenv('USER_LOGIN'),
            "password": os.getenv('USER_PASSWORD'),
        }
    )
    expect(response_login).to_be_ok()
    yield api_browser



@pytest.fixture
def delete_car_api(api):
    list_obj_to_delete = []
    yield list_obj_to_delete
    if list_obj_to_delete:
        for resp in list_obj_to_delete:
            car_id_to_delete = api.car.delete_car(resp)
            car_reps_id = api.car.get_car_by_id(resp, 404)


@pytest.fixture
def delete_car(api):
    list_obj_to_delete = []
    yield api, list_obj_to_delete
    if list_obj_to_delete:
        for resp in list_obj_to_delete:
            car_id = resp.json().get('data').get('id')
            car_id_to_delete = api.car.delete_car(car_id)
            car_reps_id = api.car.get_car_by_id(car_id, 404)


@pytest.fixture(scope="session")
def browser_context_args(browser_context_args):
    return {
        **browser_context_args,
        "ignore_https_errors": True,
        "viewport": {
            "width": 1920,
            "height": 1080,
        },
        "base_url": os.getenv('BASIC_URL'),
        "http_credentials": {
            "username": os.getenv('BASIC_AUTH_USER'),
            "password": os.getenv('BASIC_AUTH_PASS')
        }
    }

@pytest.fixture
def our_first_fixture():
    str_to_test = f'ID USER {random.choice(range(1, 23454))}'

    yield str_to_test
    print(f'I DELETE USER {our_first_fixture}')

@pytest.fixture
def create_and_delete_user(our_first_fixture):
    print(f'I CREATE USER {our_first_fixture}')
    yield our_first_fixture
    print(f'I DELETE USER {our_first_fixture}')


@pytest.fixture
def create_and_delete_user_1():
    print(f'I CREATE USER')

@pytest.fixture
def create_user():
    value_to_return = 'I CREATE USER {random.choice(range(1, 23454))} _V2'
    print(value_to_return)
    yield our_first_fixture

@pytest.fixture(scope='function')
def delete_user():
    object_values = []
    yield object_values
    if object_values:
        for value in object_values:
            ids = value
            print(f'DELETE USER {ids}')

#

@pytest.fixture
def create_and_delete_user_v2(create_user, delete_user):
    create_user, delete_user = create_user, delete_user
    yield create_user, delete_user
