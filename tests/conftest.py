import random

import pytest


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
