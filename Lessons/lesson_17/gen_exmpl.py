# def value(list_values):
#     for value in list_values:
#         print(f'before {value}')
#         yield value
#         print()
#         print(f'after {value}')
#
#
# list_values = [1, 2, 3, 4, 5]
#
# func_1 = value(list_values)
# value_1 = next(func_1)
# print('-' * 80)
# next(func_1)
# print('-' * 80)
# next(func_1)


def new_value():
    value = 0
    while True:
        yield
        value += 1
        print(value)
func = new_value()
for k in range(10000000):
    (next(func))