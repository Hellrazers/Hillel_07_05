
#[<class '__main__.CatDog'>, <class '__main__.Cat'>, <class '__main__.Dog'>, <class 'object'>]


class Animal:
    def __init__(self, name, age, has_tail, legs):
        self.name = name
        self.age = age
        self.has_tail = has_tail
        self.legs = legs



class Dog(Animal):
    def __init__(self, sub_animals, **kwargs):
        super().__init__(**kwargs)
        self.sub_animals = sub_animals

    def __str__(self):
        return f'I\'m dog: {self.name}, {self.age}'

    @staticmethod
    def sound():
        print('Gaaaav')

class Cat(Animal):
    def __init__(self, is_alive, **kwargs ):
        super().__init__(**kwargs)

        self.is_alive = is_alive

    def __str__(self):
        return f'I\'m cat: {self.name}, {self.age}'
    @staticmethod
    def sound():
        print('Mewooo')

    def say_my_name(self):
        print(f'My name is {self.name}')

class CatDog(Dog, Cat):
    def __init__(self,  is_cat_dog , **kwargs):
        super().__init__(**kwargs)
        self.is_cat_dog = is_cat_dog
        # Cat.__init__(self, name, age, is_alive)
        # Dog.__init__(self, name, age, sub_animals)

    def __str__(self):
        return f'My name is : {self.name}, age: {self.age}'

# name, age, has_tail, legs
cat = Cat(name = 'Cat', age=45, is_alive=True, has_tail=True, legs=3)
cat_dog = CatDog(name='Cat_Dog', age=18, is_alive=True, sub_animals='blohi', is_cat_dog=True, has_tail=True, legs=3)

print(cat_dog.__dict__)
print(cat_dog.__str__())
print(cat_dog.__str__())
print(cat_dog.sound())

print(CatDog.mro())
# print(CatDog.__mro__)
print(cat_dog.__dict__)
# print(cat.__dict__)
print(Cat.mro())

# cat.say_my_name()
cat_dog.say_my_name()

# dict_1 = {'name' :'Cat', 'age'=45, 'is_alive'=True, 'has_tail'=True, 'legs'=3}
cat_2 = CatDog(**dict_1)
cat = Cat(name = 'Cat', age=45, is_alive=True, has_tail=True, legs=3)

assert  cat_2.is_cat_dog is True