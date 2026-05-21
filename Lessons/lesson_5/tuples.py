my_tuple = (1, 2, 3, 4, 5, 6, 7, 8, 9, 10)
my_tuple = (*my_tuple, 1)

# my_tuple[0] = 10

print(my_tuple)
my_tuple_2 = (*my_tuple, 1)
print(my_tuple_2)


def my_function():
    return 1, 2



print(my_function())

print(my_tuple)


print(my_tuple_2[:8])
print(my_tuple[-1])


MY_NAME = "Oleksii"



MY_NAME = MY_NAME + 's'

COLUMS  = ('id', 'name', 'age')

my_tuple_with_one_elemnt = (5,) #-> int(5)
print(my_tuple_with_one_elemnt)
print(type(my_tuple_with_one_elemnt))




my_tuple = (1, [2], 3, 4, 5)

first_element, other_elemtns, *asdasd, last_element = my_tuple


print(first_element)
print(other_elemtns)
print(last_element)

# first_variable = my_tuple[0]
# last_variable = my_tuple[-1]
#
# print(first_variable)


var_1 = (1, )
var_2 = (2, )

var_1, var_2 = var_2, var_1

# var_3 = var_1
# var_1 = var_2
# var_2 = var_3

print(var_1)
print(var_2)

print(hash(var_1))
print(hash((1, 2, )))




my_string = "Привіт, світ!"
list_123 = [1, 2, 3, ]

tuple_from_string = tuple([my_string])
format_to_tuple = tuple(list_123)
print(format_to_tuple)
print(list(format_to_tuple))
print(tuple_from_string)

print(len(var_1))
var_str = 'var_1'
print(id(var_str))
var_3 = var_str + var_str
print(id(var_3))