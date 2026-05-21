my_list = [1, 2, '12312', [234], {'asd': 34}, None, True]

first_v, second_v, *other=  my_list
# print(my_list)

# print(first_v)
# print(second_v)
# print(other)

# my_list_ = ['MON', 'TUE', 'WED', 'THU', 'FRI']
# # adding to list
# print(my_list)
# print(id(my_list))
# my_list.append('Oleksii')
# print(id(my_list))
#
# my_list.insert(0, 'Oleksii')
# my_list.insert(-1, 123123123)
# my_list.insert(6666, 34234234)
# print(my_list)
# my_list.insert(2, 'Oleksii')

# my_list.extend(my_list_)
# for k in my_list_:
#     my_list.append(k)

# print(my_list)


# Видалення

my_list = ['MON', 'TUE', 'WED', 'THU', 'FRI','WED','WED', 'WED', (1, 2)]
# print(my_list)
#
# # print(my_list.pop(0))
# print(my_list)
#
# print(my_list.remove('WED'))
# print(my_list)
#
# my_list.remove((1, 2))
#
# print(my_list)

# index_wed_1 = my_list.index('WED')
# print(index_wed_1)
# print(my_list.index('WED', index_wed_1 + 1)) # find
#
# print(my_list.count('WED')) # count(h)
# print(len(my_list))
# print(my_list)
#
# my_list[3] = 'SUND'
# print(my_list)

import copy

my_list = ['MON', 'TUE', 'WED', 'THU', 'FRI','WED','WED', 'WED', [1, 2, 4]]
# my_list_2 = my_list #не можна робити ніколи
my_list_2 = my_list.copy() # = [:]
# my_list_2 = copy.deepcopy(my_list) # -> ['MON', 'TUE', 'WED', 'THU', 'FRI','WED','WED', 'WED', [1, 2, 4]]
print(my_list)
# my_list_2  = my_list #
my_list[0] = 123


my_list[-1].append(123)
print(my_list)
print(id(my_list), 'my_list')
print(id(my_list[-1]), '[1, 2, 4]')
print(my_list_2)
print(id(my_list_2), 'my_list_2')
print(id(my_list_2[-1]), '[1, 2, 4]')

my_list_3 = my_list[-1]
print(id(my_list_3))

my_list_3.pop()
my_list_3.pop()

print(my_list)

#[1 , , 2 [1, 2, 4] ]
# [] -> append(*mylist)


# def func_list(value, list=[]):
#     list.append(value)
#     return list
# list_1 = func_list(1)
# print(list_1)
# print(id(list_1))
# list_2 = func_list(1)
# print(list_2)
# print(id(list_2))


car_data = {
  'Mercedes': ('silver', 2019, 1.8, 'sedan', 50000),
  'Audi': ('black', 2020, 2.0, 'sedan', 55000),
  'BMW': ('white', 2018, 3.0, 'suv', 70000),
  'Lexus': ('gray', 2016, 2.5, 'coupe', 45000),}

filter(car_data, key=lambda k: car_data[k][1] > 2016, reverse=True)
print(new_list)