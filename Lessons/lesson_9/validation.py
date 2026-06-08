class People(object):

    def __init__(self, name:str, age:int, is_men:bool):

        self.name = name
        self.age = age
        self.is_men = is_men

    def __setattr__(self, key, value):
        if key=='name' and len(value) == 0:
            raise AttributeError
        if key=='age' and value <= 0:
            raise AttributeError
        super().__setattr__(key, value)

    def minus_age(self, value):
        self.age = self.age - value


people_1 = People(name='oleksii', age=22, is_men=True)
people_1.minus_age(18)
print(people_1.age)