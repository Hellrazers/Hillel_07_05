from abc import abstractmethod, ABC



class Animal(ABC):

    def __init__(self, name, has_tail, is_alive = True):
        self.name = name
        self.is_alive = is_alive
        self.has_tail = has_tail

    @abstractmethod
    def walking(self):
        pass

    @abstractmethod
    def sound(self):
        pass


class Dog(Animal):

    MY_TYPE = 'DOG'

    def __init__(self, age, size, **kwargs):
        super().__init__(**kwargs) #->   self.name = name self.is_alive = is_alive
        self.age = age
        self.size = size

    def sound(self):
        print('GAAAAAAAAAAAAVVVVVV')

    def walking(self):
        print('walking')

class Cow(Animal):
    MY_TYPE = 'COW'

    def sound(self):
        print('MOOOOOOOOOOOO')

    def walking(self):
        print('walking')

    # def __init__(self, age, size, *args):
    #     super().__init__(*args) #->   dog_1 = Dog('dog1', 123, 'Vasya', True)
    #
    #     self.age = age
    #     self.size = size

dog_1 = Dog(age='dog1', size=123, name= 'Vasya', is_alive = True, has_tail=True)
cow_1 = Cow(name= 'COW', is_alive = True, has_tail=True)
print(Dog.__mro__)
# print(dog_1.say_something())
#
# print(dog_1.name)
# print(dog_1.sound())
# cow_1.sound()
# print(len([1,23,423]))
# print(len('asd'))


# list_1 = [1,23,45]
# set_1 = {1, 2, 45}
# dict_1 = {1:2, 3:4}
#
# list_1.pop()
# set_1.pop()
# dict_1.pop(1)


















class Cat:

    HAS_TAIL = True

    def __init__(self, name, is_alive: bool = True):
        self.name = name
        self.is_alive = is_alive
        self.age = 0

    def my_age(self):
        self.age = self.age + 1
        return self.age

    def sound(self):
        print('Meow')


    def run(self):
        print('Im ruuning')


    def i_say_my_name(self):
        name = "Ivan"
        print(f'I say my {self.name}, i\'m alive {self.is_alive}')


    # @staticmethod
    # def say_my_name():
    #     self.name

# cat_1 = Cat('cat1')
# cat_5 = Cat('Vasya', False)
# print(cat_5.is_alive)
# cat_5.i_say_my_name()
# Cat.i_say_my_name(Cat('Alex', False))
# #
#
# cat_1.my_age()
# cat_1.my_age()
# print(cat_1.age)
#
#
# cat_2 = Cat('cat2')
# cat_3 = Cat('cat3')
#
#
# print(cat_1.HAS_TAIL)
#
#
# print(cat_2.HAS_TAIL)
# Cat.HAS_TAIL = False
# cat_4 = Cat('cat4')
# print(cat_4.HAS_TAIL)
# cat_4.HAS_TAIL = True
# print(cat_4.HAS_TAIL)
#
# # print(id(cat_1))
# # print(id(cat_2))
# # print(cat_1.i_say_my_name())
# # print(cat_2.i_say_my_name())
# # cat_2.run()
# # cat_1.age = 15
# # print(cat_1.age)