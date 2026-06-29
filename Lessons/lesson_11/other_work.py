# Поїзд складається з вагонів, перший вагон — локомотив.
#
# У поїзді може бути тільки один локомотив.
#
# Локомотив не може перевозити пасажирів.
#
# Кожен звичайний вагон може перевозити не більше 10 пасажирів.


class Wagon:
    MAX_PASSANGERS = 10
    def __init__(self, is_head_wagon: bool = False):
        self.__passangers = []
        self.is_head_wagon = is_head_wagon

    def add_passanger(self, passanger: str):
        '''

        :param passanger:
        :return:
        '''
        if  not self.is_head_wagon:
            self.__passangers.append(passanger)

    def get_passangers(self):
        return self.__passangers

    def __repr__(self):
        if self.is_head_wagon:
            return "Lokomotive"
        else:
            return f"Wagon with passangers {self.get_passangers()}"

    def __str__(self):
        if self.is_head_wagon:
            return "Lokomotive"
        else:
            return f"Wagon with passangers {self.get_passangers()}"

    def __setattr__(self, key, value):
        if key == 'passangers'  and len(value) > Wagon.MAX_PASSANGERS:
            raise ValueError('Людей більше 10 не може бути у вагоні ')
        if (key == 'passangers' and len(value) > 0) and (key == 'is_head_wagon' and value is True):
            raise ValueError('Людей у локомативі бути не може')
        super().__setattr__(key, value)



class Train:
    def __init__(self):
        self.train = [Wagon(is_head_wagon=True),]

    def __repr__(self):
        str_train = ''
        for index, element in enumerate(self.train):
            str_train += f'{index + 1} - '  + str(element) + ' '

        return str_train

    def __setattr__(self, key, value):
        if key == 'train' and len(value) > 5:
            raise ValueError("Більше 5 в>агонів")
    # def _

    def add_wagon(self, wagon: Wagon):
        self.train.append(wagon)


        #

train_1 = Train()

wagon_1 = Wagon()
wagon_2 = Wagon()
print(wagon_1)
# lokomotive = Wagon(is_head_wagon=True)
# wagon_2.add_passanger('ivan')
# print(wagon_2.get_passangers())
train_1.add_wagon(wagon_1)
print(len(train_1.train))

print(train_1)

wagon_1.add_passanger("Ivan")
wagon_1.add_passanger("Alex")
print(train_1.train)
train_1.add_wagon(wagon_2)
print(train_1.train)
wagon_2.add_passanger("Oleksii")
print(train_1.train)
train_1.add_wagon(wagon_2)
wagon_2.add_passanger("Ivan")
print(train_1.train)
train_1.add_wagon(wagon_2)
train_1.add_wagon(wagon_2)
train_1.add_wagon(wagon_2)

