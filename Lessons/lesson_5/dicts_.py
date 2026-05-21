from dns.flags import Flag

new_varible = '123'

first_dict = {
    'name': 'Oleksii',
    1+1 : 1,
    (1,): [1, 2, 3,4],
    True: True,
    "new_dict": {
        'a': 2,
        'b': [1,2, 3, 4 ,5 , {1: {2:2}}],
    },
    # input('Enter name'): 123,
    new_varible: 'asd',
    'name' + '123': "Ivan"
} # лапки "", true/false,



#getting
values_return_list = first_dict[(1,)]
print(values_return_list)
print(values_return_list[-2])
print(first_dict['new_dict'])
print(first_dict['new_dict']['b'])
print(first_dict['new_dict']['b'][-1])
# print(first_dict[12312312312])
is_false = first_dict.get('new_dict', False)
print(is_false)
# if not is_false
#

print(first_dict)

#uppdate
first_dict['name'] = 'IVAN'


first_dict.update({'name123':"Oleksii"})

print(first_dict)
first_dict['SURNAME'] = 'IVAN'


first_dict.update({'AGE':"""Oleksii""", "IDS": 123, 123123 : [123]})
print(first_dict)


#remove

# var_pop = first_dict.pop('name')
# print(var_pop)
# print(first_dict)


# print(first_dict[2])
# print(first_dict['name123'])

#0 1 2 3454 .....42 ->

#
# for key, value in first_dict.items():
#     print(f'key = {key}, value = {value} ')
#
# for value in  first_dict:
#     print(value)
# print(hash('name123'))
#
# # print(hash(first_dict))


