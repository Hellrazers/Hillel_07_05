class Cat(object):
    # HAS_TAIL = True

    def __init__(self, name):
        self.name = name
        self.age = 0

    def __setattr__(self, key, value):
        print(f'key: {key} value : {value}')
        if key.startswith('name') and len(value) < 1:
            raise AttributeError(f'{self.name} cannot be less than 1')

        # self.name = value
        super().__setattr__(key, value)

    def add_age(self, age):
        self.age += age

cat = Cat(name='Mr')
print(cat.name)

cat.name = '345'

print(cat.name)


cat.add_age(10)

# cat.HAS_TAIL = False