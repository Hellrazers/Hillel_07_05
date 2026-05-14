
# new_value = input('Enter some text:')
#
# print(new_value)
# print(type(new_value))
# print( new_value  +  ' 2')
#


# id , len ,

#
# str_value = '12 3123 123 a'
#
# print(id(str_value))
#
# str_value = str_value + '123 12312 3123 '
# print(id(str_value))
#
#
# int_value = 1
#
# print(id(int_value))
#
# int_value += 5
# print(id(int_value))


list_of_elements = [1, 2, 3, 4, 5]
print(id(list_of_elements))
list_of_elements.append(6)
print(id(list_of_elements))


def my_function(value: int = 1, list_elements: list = []):
    list_elements.append(value)
    return list_elements


list_1 = my_function(value =5 ) # = [1]
list_2 = my_function(value = 14) # = [1]
print(list_1)
print(list_2)

print(id(list_1) == id(list_2))
# print(id(list_2))

def my_function_2(value:int = 1, list_elements: list = None):
    if list_elements is None:
        list_after_adding = []
    list_after_adding.append(value)
    return  list_after_adding

list_1 = my_function_2(value =5 ) # = [1]
list_2 = my_function_2(value = 14) # = [1]
print(list_1)
print(list_2)

print(id(list_1) == id(list_2))

id_of_list2 =  id(list_2)
list_2.append(5)
print(id_of_list2 == id(list_2))
