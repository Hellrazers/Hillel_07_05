import unittest
from assertpy import assert_that, soft_assertions


# def testy_soft_assert(actual_result, expected_result):
#     error_list = []
#     try:
#         assert actual_result is expected_result
#         assert error_list == []
#         assert 1 == 2
#     except AssertionError as error:
#         error_list.append(error)
#     finally:
#         return error_list

class MyTestCasePositive(unittest.TestCase):

    def test_our_first_test(self):
        actual_result = "oleksii"
        exp_result = "oleksii"
        list_1 = [1,2,3,4,5,6,7,8,9,10]
        list_2 = [1,2,3,4,5,6,7,8,9,10]
        assert list_1 == list_2
        # assert actual_result is list_2
        #assert id(actual_result) == id(exp_result)
        # self.assertIs(list_1, list_2, msg=f'ITS MY MASAGE {list_1} ')
        assert 2 in list_2
        self.assertIn(2, list_2)
        # error_list = []
        # try:
        #     assert actual_result is expected_result
        # except AssertionError as error:
        #     error_list.append(error)
        #CORE
        assert  200 == 200
        name_ = 'nnaem_update'
        # assert_that(1, 'WE EQUAL TO 2').is_equal_to(2)

        with soft_assertions():
            assert_that('id').is_not_none()
            assert_that('name').is_equal_to(name_)
            assert_that(actual_result).is_equal_to(exp_result)
            assert_that(actual_result).is_none()
            assert_that(1).is_none()
            assert_that(1, 'WE EQUAL TO 2').is_equal_to(2)


