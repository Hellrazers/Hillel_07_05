# def greetings():
#     print("Greetings")
#
# def say_bye():
#     print("say_bye")
#
# def say_my_name(name, fn):
#     fn()
#     print(f"My name is {name}")
#
#
#
# # first_fn = say_my_name
# # greetings()
# # first_fn('Ivan')
# # say_bye()
# # first_fn('Ivan')
# #
# say_my_name('ivan', greetings)
#
# say_my_name('ivan', say_bye)




def say_my_name_1(fn):
    def wrapper(*args, **kwargs):
        print('Before FUNCTION')
        value = fn(*args, **kwargs)
        print('After FUNCTION')

        return value
    return wrapper



@say_my_name_1
def greetings():
    print("Greetings")


@say_my_name_1
def my_name(name):
    print(f'My name is {name}')

@say_my_name_1
def my_name_and_age(name, age):
    print(f'My name is {name} and {age} years old')

# greetings()
#

from time import time

tm_1  = time()


my_name(name='John')

my_name_and_age(name='John', age=20)
my_name_and_age('John', 20)
tm_2  = time()

print(tm_2 - tm_1)

# asd(())