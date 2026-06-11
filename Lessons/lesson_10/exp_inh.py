class Animal:
    def __init__(self, name, is_alive):
        self.name = name
        self.is_alive = is_alive


    def sound(self):
        pass  # Абстрактний метод

class Mammal(Animal):
    def __init__(self, name, num_legs, is_alive):
        Animal.__init__(self, name, is_alive)
        self.num_legs = num_legs

class Bird(Animal):
    def __init__(self, name, wingspan, is_alive):
        Animal.__init__(self, name, is_alive)
        self.wingspan = wingspan

    def make_sound(self):
        print('I make a sound')

class Bat(Bird,Mammal):  # Ромбовидне наслідування
    def __init__(self, name, num_legs, wingspan, is_alive):
        Mammal.__init__(self, name, num_legs, is_alive)
        Bird.__init__(self, name, wingspan, is_alive)

class Bat_1(Mammal):  # Ромбовидне наслідування
    def __init__(self, name, num_legs, wingspan, is_alive):
        Mammal.__init__(self, name, num_legs, is_alive)
        self.bird = Bird(name, wingspan, is_alive)


mammal = Mammal(name='asd', num_legs=34, is_alive=True)
bat = Bat(name='Bat', num_legs=3, wingspan=2, is_alive=True)

bat_1 = Bat_1(name='Bat', num_legs=3, wingspan=5, is_alive=True)
print(bat.__dict__)
print(bat_1.__dict__)
print(bat_1.bird.wingspan)

bat.make_sound()
bat_1.bird.make_sound()