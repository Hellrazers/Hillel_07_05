class Car:
    def __init__(self, make, model):
        self.make = make          # Public attribute
        self._model = model        # Protected attribute
        self.__year = 2022         # Private attribute

    def display_model(self):
        print(f"Model: {self._model}")

    def update_year(self, new_year):
        self.__year = new_year
        print(self.__dict__)



class Honda(Car):
    def __init__(self, make, model):
        super().__init__(make, model)


    def change_year(self, new_year):
        self.__year = new_year
        print(self.__dict__)



# Створення об'єкта та використання атрибутів та методів
my_car = Car("Toyota", "Camry")
my_car_1 = Honda("Honda", "Camry")

# print(my_car.make)              # Public attribute, виведе: Toyota
# my_car.display_model()          # Protected method, виведе: Model: Camry
# my_car.update_year(2023)        # Private attribute update

print(my_car.__dict__)

my_car._Car__year = 19
print(my_car._Car__year)
print(my_car.__dict__)

my_car_1.change_year(2000)

print(my_car_1._Honda__year)


from lesson_10.func_view import greeting_1

greeting_1()