import math as math



# res_math(2.1, 0)  -> ZeroDivisionError: division by zero
# int /(int, float) -> float
# int (*, +, -) int -> int
# (int/float) (*, +, -) (int/float) -> float
# print(4//3) == int( 4/3)
int_number=1
float_number: float = 3.14
CONST_VALUE = 123

def main(some_value: int) :
    uper_value = some_value.upper()
    print(uper_value)
    return 1, 2


some_str: str = 'Hello World'


# print(some_str.upper())

print(main('Hello World'))

True
False
None

first_dict: dict = {
    True: True,
    1 + 1 : 'asd'
}
first_list: list = [1, 2 ,3 , 'sadasdasd', first_dict]

first_tuple: tuple = (1, 3 ,4)
first_set: set = {1, 23, 345, 1, 2}

print(first_set)
first_list.append(1)
print(first_list)


print(some_str, 'Hello World')
print(1 + 1 )


float_result: float = 5 / 3
str_value_of_float = str(float_result)
print(type(str_value_of_float))
print(len(str_value_of_float))
print(str_value_of_float[:4])

print(math.ceil(5/23))
print(round(float_result, 2))


print(f"{float_result:.2f} 1+1 = {1 + 1}")
print(r"{float_result:.2i}")
a = 1
b = 2

new_text = ''


''' 
Hello asdasdas d 
'''
print( f'apple = {a} and banana = {b}')
print('apple =', a, 'and banana =', b , sep='9')
# print('asdasd {a} and {b}',for )
print('''apple = banana
1
and banana =
2''')

print(first_list)


print('-' * 90)


print(f"{float_result:.2}")


def res_math(value1: int , value2: int ) -> None :
    if type(value1 / value2) is float:
        print('Is Flaot ')
    else:
        print('Is  Int ')

new_string = f'{some_str} with new sting'
print(new_string)
