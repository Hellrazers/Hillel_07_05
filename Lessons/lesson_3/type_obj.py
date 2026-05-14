# (       )       [       ]       {       }
# ,       :       .       ;       @


def asd():
    pass

tuple_value = (1, 2, 3, [])
list_value = [1, 2, 3, 1, 2, 3]
set_value = { None, True, 'a', 'b', False, True}
dict_value = {'Name': 'Oleksii', 'age': '29' , 1 + 1: 2, 'None': [1, 2, 3], (1,2,4): [123]}

print(len(tuple_value))
print(len(list_value))
print(list_value)
print(set_value)

print(len(set_value))
print(tuple(set_value)[0])
print(id(False))

print(tuple_value)
tuple_value[-1].append(3)
print(tuple_value)

print(dict_value['None'][0])

for item, non_item in dict_value.items():
    print(f'key: {item}, value: {non_item}')


print(type((1, )))
print(type((1)))
print(type([1]))