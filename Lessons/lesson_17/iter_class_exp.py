class Animal:
    def __init__(self):
        self.__all_animals = []
        self.__all_animals_2 = []

        self.__animal_iter = 0

    def add_animal(self, animal):
        self.__all_animals.append({'id':len(self.__all_animals), 'type_of_animal':animal})

    def get_animals(self):
        return self.__all_animals

    def __iter__(self):
        return self

    def __next__(self):
        if self.__animal_iter < len(self.__all_animals):
            animal = self.__all_animals[self.__animal_iter]
            self.__animal_iter += 1
            return animal
        raise StopIteration

all_animal = Animal()
all_animal.add_animal('dog')
all_animal.add_animal('cat')
print(all_animal.get_animals())

dog = next(all_animal)
dog['id'] = 5
print(dog)

print(all_animal.get_animals())

for animal in all_animal:
    print(animal)

dog['new_value'] = True

print(all_animal.get_animals())


# print(all_animal.get_animals())
# value = all_animal.get_animals()
#
# for animal in value:
#     print(animal)
#
# print(next(all_animal))
# print(next(all_animal))
#
# # print(all_animal.get_animals())
# # for animal in all_animal:
# #     print(animal)
# # for all_animal in all_animal:
# #     print(all_animal.get_animals())
#
# for animal in Animal():
#     print(animal)

