import unittest
from faker import Faker

# faker = Faker('uk_UA')
#
# Faker('uk_UA').city()
# faker.city()

def sum_values(a , b):
    return a - b


class MyTestCasePositive(unittest.TestCase):

    def test_fun(self):

        self.assertRaises(TypeError, sum_values, '1', 2)

    


    def test_our_first_test(self):
        actual_result = "oleksii"
        exp_result = "oleksii"

        assert actual_result == exp_result


class MyTestCaseNegative(unittest.TestCase):
    faker = Faker('uk_UA')

    def setUp(self):
        print('-----------setUp------------')
        fake = Faker('uk_UA')

        self.email = fake.email()

        print(f'Create user with email {self.email}')
        dict_resp = {'status_code': 200,
                     'text': 'ok'}
        assert 200 == dict_resp.get('status_code')

    # def setUpClass(cls):
    #     print('-----------setUpClass------------')
    #     c
    #     # pass
    #
    # def tearDownClass(cls):
    #     print('-----------tearDownClass------------')
    #     pass

    def test_update_user_test(self):
        print('-----------Test_body------------')
        nickname = 'example'
        print(f'Update user with email {self.email} and change nickname {nickname}')
        assert nickname == 'example'

    def test_our_second_409_test(self):
        # errors = []
        # try:
        print('-----------Test_body------------')

        print(f'Create user with email {self.email}')
        dict_resp_second_create = {'status_code': 409,
                                   'text': 'Failed to create user'}
        self.assertEqual(dict_resp_second_create.get('status_code'), 409, 'is not equals')
        self.assertEqual(dict_resp_second_create.get('text'), 'Failed to create user', 'is not equals')


def test_get_all_users(self):
    print('-----------Test_body------------')
    print('GET ALL users')
    assert 1 == 1
    # except AssertionError as error:
    #     errors.append(error)
    # self.cleanUP()
    # if errors:
    #     raise AssertionError()


def tearDown(self):
    print('-----------tearDown------------')
    print(f'Remove user with email {self.email}')

# def cleanUP(self):

# def create_user(self):
#     print('-----------setUp------------')
#     self.email = 'example@com'
#     print(f'Create user with email {self.email}')
#     dict_resp = {'status_code': 200,
#                  'text': 'ok'}
#     assert 200 == dict_resp.get('status_code')

# @fixture
# def cleanUP()
#     print('-----------Test_body------------')
#     nickname = 'example'
#     print(f'Update user with email {self.email} and change nickname {nickname}')
#     assert nickname == 'example'
#     yield nickname, email
#     print('-----------tearDown------------')
#
#     print(f'Remove user with email {self.email}')
#
#
# def test_(cleanUP):
#     pass

# list= []
# for k in range(10):
#     list.append((k*2))
# print(list)
print('__name__ = ',__name__)
if __name__ == '__main__':
    print(__name__, ' is module')
    unittest.main(verbosity=2)