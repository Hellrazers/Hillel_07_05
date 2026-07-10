
from time import time

from assertpy import assert_that

from contract.gorest_user.user_api import GorestUser

login_= get_token()

gorest_user = GorestUser()

def test_gorest():
    response_json = gorest_user.user_get()
    assert_that(len(response_json)).is_not_none()
    for user in response_json:
        assert_that(user['id']).is_not_none()


def test_gorest_with_id():
    exp_id = 8540122
    response_json = gorest_user.user_get(param={"id": exp_id, "name": 'Vishwamitra Malik'})

    # assert_that(len(response_json)).is_equal_to(1)
    # assert_that(response_json[0]['id']).is_equal_to(exp_id)


def test_gorest_create_user_post_positive():
    dict_validate = { "name": "Tenali Ramakrishna",
                      "email": f"tenali@{time()}.com",
                      "gender": "male",
                      "status": "active" }
    response_json = gorest_user.user_post(dict_validate=dict_validate)
    assert_that(response_json['id']).is_not_none()
    for key in dict_validate.keys():
        assert_that(response_json[key]).is_equal_to(dict_validate[key])

    # assert_that(response_json[0]['id']).is_equal_to(exp_id)
# `
# 12312312312312312312312312

def test_gorest_create_user_post_negative():
    dict_validate = { "name": "Tenali Ramakrishna", "email": "tenali@example.com", "gender": "male", "status": "active" }
    response_json = gorest_user.user_post(dict_validate=dict_validate, exp_status_code=422)[0]

    assert response_json['field'] == 'email'
    assert response_json['message'] == 'has already been taken'


def test_gorest_create_user_and_delete_him():
    dict_validate = { "name": "Tenali Ramakrishna",
                      "email": f"tenali{str(time())[:5]}@gmail.com",
                      "gender": "male",
                      "status": "active" }
    response_json = gorest_user.user_post(dict_validate=dict_validate)
    user_id = response_json['id']
    assert_that(user_id).is_not_none()
    response_json_delete = gorest_user.user_delete(user_id)
    response_json_get = gorest_user.user_get(param={"id": user_id})
    assert_that(len(response_json_get)).is_equal_to(0)