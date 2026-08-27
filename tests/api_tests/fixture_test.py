import allure
import pytest
import random



def test_udpate( create_and_delete_user):
    print('I IT IN TESTING')
    print(f'I UPDATE USER {create_and_delete_user}')
    print(f'I GETby ID USER  {create_and_delete_user}')


def test_update_409( create_and_delete_user):
    str_user = create_and_delete_user
    # with allure.step('1) asdasd'):
    print('I IT IN TESTING')
    # resp_user_1['data']['email']
    print(f'I CREATE USER_{str_user}')
    print('ASSERT RETURN 409 ')
