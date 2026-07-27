import pytest

@pytest.mark.positive
@pytest.mark.regression
class TestUserPositive:
    def test_user_first_1_2_200(self):
        result = 1 + 1

    @pytest.mark.negative
    @pytest.mark.api_test
    @pytest.mark.smoke_test
    def test_first_13(self, create_and_delete_user):
        assert True

    @pytest.mark.skip('jira_tiket/jira-1')
    def test_user_first_2_200(self):
        #TODO FIX HERE change response
        assert False


    @pytest.mark.smoke_test
    @pytest.mark.xfail
    def test_user_first_3_200(self):
        #TODO FIX HERE change response
        assert True