from datetime import datetime


class Children:
    def __init__(self, name, age):
        self.name = name
        self.age = age

    def iniz_2 (self):
        return datetime.now().year

    @classmethod
    def inizilization(cls, name, age):
        import datetime
        datetime = datetime.datetime.now().year
        age = datetime - age
        return cls(name, age)

alex = Children(name='Alex', age=5)

vasya = Children.inizilization(name='Vasya', age=2010)
print(vasya.age)
print(vasya.iniz_2())