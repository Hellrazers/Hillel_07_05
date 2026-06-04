#
# # def sep_fuction():
# #     print('-' *  80)
# #     print('Hello word')
# #     print('-' *  80)
# #
# # def sep_fuction_2(value_1: str, value_2: int | float) -> None:
# #     print('-' *  80)
# #     print(f'{value_1} * {value_2} = {value_1 * value_2}')
# #     print('-' *  80)
# #     return value_1 * value_2
# #
# # def sep_fuction_3(value_1, value_2):
# #     print('-' *  80)
# #     print(f'{value_1} * {value_2} = {value_1 * value_2}')
# #     print('-' *  80)
# #
# # # sep_fuction()
# # # sep_fuction()
# # # sep_fuction()
# # # sep_fuction()
# # # sep_fuction()
# # # sep_fuction()
# # sep_fuction_2(value_1=1, value_2=2)
# # sep_fuction_2(1, 2)
# # sep_fuction_2(value_1=1, value_2=2)
# # new_varible = sep_fuction_3('1', 5)
# #
# # print(new_varible)
# # print(sep_fuction_2(value_1=1, value_2=2))
#
#
# def sum_value(value1, value2) -> None:
#     print(value1 + value2)
#
# def sum_value_with_return(value1, value2):
#     sum_value = value1 + value2
#
#     return sum_value, value1, value2, 'asdasd', (123,3)
#
# def sum_value_with_return_1(value1: int | float, value2: int | float) -> int | float | None:
#     '''
#     This func sum 2 values
#     :param value1: int | float first value
#     :param value2: int | float second value
#     :return: int | float sum of two values
#     '''
#     sum_value = value1 + value2
#
#     return sum_value
#
#
# sum_values = sum_value_with_return(1, 2)
# print(sum_values)
# # value_sum_1 = sum_value_with_return_1(value1=2, value2=3)
# # value_sum_2 = sum_value_with_return_1(value1 = value_sum_1, value2=3)
#
# value_sum_2 = sum_value_with_return_1(value1 = sum_value_with_return_1(value1=2, value2=3), value2=3)
# print(value_sum_2)
# # list_str = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
# #
# # list_str.append(5)
# # print(list_str)
# # print(list_str.append(1111111111))
# # print(list_str)








# dict_ = {'name': 1}
# # print(dict_.get('job', False))
#
# def hello(surname='a', name = 'alex', nickname = None):
#     if nickname:
#         print(f"{name} {surname} {nickname}")
#     else:
#         print(f"Hello {name} and {surname}!")
#
#
def list_fun_append( value_1 = 45, list_1 = None):
    # if list_1 is None:
    #     list_1 = []

    if not list_1:
        list_1 = []
    print(id(list_1))
    list_1.append(value_1)
    return list_1
#


list_1 = (list_fun_append())
list_2 = (list_fun_append(value_1= 66, list_1 = [1]))
list_3 = (list_fun_append(list_1= [1, 2, 3], value_1= 4))
list_4 = (list_fun_append())
print(list_1)
print(list_2)
print(list_3)
print(list_4)
list_fun_append(1, [])

# print(list_fun_append([1, 2, 3],4))


# hello(name='alex',nickname='alex')
# hello()
# hello(surname='Smith')
# hello(name='Jonh', surname='Smith', nickname='MR.Smith')
#
#
# list_sorted = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
# print(sorted(list_sorted, reverse = False))
# print(sorted(list_sorted, reverse = True))
# print(sorted(list_sorted))
