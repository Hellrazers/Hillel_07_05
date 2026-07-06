class All_Animals:
    def __init__(self):
        self.animal_iter = 0
        self.__all_animals = []

    def add_animal(self, animal):
        self.__all_animals.append({'id': len(self.__all_animals), 'type_of_animal': animal})

    def get_animals(self):
        return self.__all_animals

    def __iter__(self):
        return self

    def __next__(self):
        if self.animal_iter < len(self.__all_animals):
            animal_dict = self.__all_animals[self.animal_iter]
            self.animal_iter += 1
            return animal_dict
        raise StopIteration


class Animal:
    def __init__(self):
        self.all_animals = All_Animals()

    def add_animal(self, animal):
        self.all_animals.add_animal(animal)

    def get_animals(self):
        return  self.all_animals.get_animals()

    def __iter__(self):
        return self.all_animals

all_animal = All_Animals()

all_animal.add_animal('dog')
all_animal.add_animal('cat')
print(all_animal.get_animals())

dog = next(all_animal)
dog['id'] = 5
print(dog)

# print(all_animal.get_animals())
#
# for animal in all_animal:
#     print(animal)
#
# dog['new_value'] = True
#
# print(all_animal.get_animals())
#
#
# # print(all_animal.get_animals())
# # value = all_animal.get_animals()
# #
# # for animal in value:
# #     print(animal)
# #
# # print(next(all_animal))
# # print(next(all_animal))
# #
# # # print(all_animal.get_animals())
# # # for animal in all_animal:
# # #     print(animal)
# # # for all_animal in all_animal:
# # #     print(all_animal.get_animals())
# #
# # for animal in Animal():
# #     print(animal)
#
