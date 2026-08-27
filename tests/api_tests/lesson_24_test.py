import pytest


# 1. Define fixture that reads request.param
@pytest.fixture
def login(request):
    try:
        user, pwd = request.param
    except AttributeError:
        user, pwd = "", ""
    return f"Logging in as {user} with {pwd}"

# 2. Pass parameters to the fixture from the test using indirect=True
@pytest.mark.parametrize('login', [
    ("alice", "1234"),
    ("bob", "abcd")
], indirect=True)
def test_login(login):
    print(login)
    assert "Logging in" in login



# Визначення фікстури з параметром params
@pytest.fixture(params=[
    ("alice", "1234"),
    ("bob", "abcd")
])
def my_fixture(request):
    param_value = request.param
    print(f"Setup with param value: {param_value}")
    return "Setup with param value: {param_value}"

# Приклад використання фікстури у тесті
def test_using_fixture(my_fixture):
    print(my_fixture)


def test_logout(my_fixture):
    pass

@pytest.mark.parametrize('test_param', [*list(range(1,4))])
@pytest.mark.parametrize('my_fixture', [*list(range(4,7))])
@pytest.mark.api_test
def test_invalid_param(test_param, my_fixture):
    print(f"Test with invalid param value: {test_param} {my_fixture}")


@pytest.fixture()
def create_user():
    print('I"m create user')
    yield
    print("I'm delete user")

@pytest.mark.parametrize('role', ('user', 'admin', 'superuser'))
def test_upd_role(create_user, role):
    print(f'I"m update user with wthis role {role}')
    if role == 'user':
        assert role == 'user'
    if role == 'admin':
        assert role == 'admin'
    if role == 'superuser':
        assert role == 'superuser'
