import pytest


@pytest.mark.parametrize('name', ('Denis', 'ivan', 'Oleksii'))
@pytest.mark.parametrize('value_1', (1, 2,3,4))
@pytest.mark.parametrize('value_2', (1, 2, 3))
def test_sum(name, value_1, value_2):

    print(f'my name is {name}, and value_1: {value_1} and value_2: {value_2}')


