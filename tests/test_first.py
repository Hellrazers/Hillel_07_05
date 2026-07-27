
import pytest

from tests.conftest import create_user


@pytest.mark.api_test
@pytest.mark.smoke_test
def test_first_13_123(create_user, delete_user):
    response, delete = create_user , delete_user
    delete.append(response)
    assert 200 == 200
@pytest.mark.api_test
@pytest.mark.smoke_test
def test_create_user_13_123(delete_user):
    asd = '2134345435456'
    assert 200 == 201

    delete_user.append(asd)


@pytest.mark.regression
class TestClass:
    def test_first_1_2(self):
        result = 1 + 1

    @pytest.mark.negative
    @pytest.mark.api_test
    @pytest.mark.smoke_test
    def test_first_13(self):
        assert True

    @pytest.mark.skip('jira_tiket/jira-1')
    def test_user_first_2(self):
        # TODO FIX HERE change response
        assert False

    @pytest.mark.xfail
    def test_first_3(self):
        # TODO FIX HERE change response
        assert True



