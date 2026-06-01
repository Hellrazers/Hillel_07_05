# base_numbers = [2, 4, 6, 8, 10]
# powers = [1, 2, 3, 4, 5]
#

#
# def sum_(a):
#     print(True)
#
# numbers_powers = map(sum_2_value, base_numbers, powers)
# numbers_powers = list(map(lambda value: value + 5, base_numbers))
# print(numbers_powers)
# # print(type(numbers_powers))
# # print(list(numbers_powers))  # [2, 16, 216, 4096, 100000]
# #
# # print(pow(6, 3))
# # list_compe = [pow(value,powers[index] ) for index, value in enumerate(base_numbers)] # value ** powers[index]      ||||| pow(value,powers[index] )->  value + powers[index]
# # print(list_compe)
# #
# # list_1 = []
# # for index, value in enumerate(base_numbers):
# #     list_1.append(value + powers[index])
# #
# #
# # base_numbers[0], powers[0]
# # base_numbers[1], powers[1]
# # base_numbers[2], powers[2]
# list_10 = list(range(1, 10))
# list_pairs = list(filter(lambda value: value % 2 == 0, list_10))
# print(filter(lambda value: value % 2 == 0, list_10))
# print(list_pairs)
# [k for k in list_10 if k % 2 == 0]



# all(iterable)
base_numbers = [2, 4, 6, 8, 10]
powers = [1, 2, 3, 4, 5]
def sum_2_value(value_1, value_2):
    return value_1 + value_2
numbers_powers = map(sum_2_value, base_numbers, powers)
list_compe_sum = [value + powers[index]  for index, value in enumerate(base_numbers)]


map_powers = list(map(pow, base_numbers, powers))

list_compe = [pow(value,powers[index] ) for index, value in enumerate(base_numbers)] # value ** powers[index]


# print(all([True, True, False]))
# print(any([True, True, False]))
#
# list_1 = [18, 25, 65]
#
# bool_1 = True
#
# for value in list_1:
#     if value < 20:
#         bool_1 = False
#         break
#
# print(False)
#
# list_1 = all([True if value > 20 else False for value in list_1])
# print(list_1)
#
# print(list_1[0] > 18 and list_1[1] > 18 and list_1[2] > 18)
#


list1 = [1, 2, 3,4 ]
list2 = ('a', 'b', 'c')
zipped = zip(list1, list2) # -> list[ tuple(list1[0],list2[0]).....
print(list(zipped))

print(list({'a': 1, 'b': 2, 'c': 3}))

# print(all(list_1))