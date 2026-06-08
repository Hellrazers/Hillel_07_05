
course_dict = {
    'name' : "oleksii",
    'courses_name': 'math',
    'students': ["Ivan", 'Denis', 'Viktoria'],
    'avarage_score': 89
}
course_dict_2 = {
    'name' : "ivan",
    'courses_name': 'lith',
    'students': ["Ivan", 'Denis', 'Viktoria'],
    'avarage_score': 456
}


class Course:
    def __init__(self, name: str, courses_name: str, avarage_score: int,  students: list = None):
        self.name = name
        self.courses_name = courses_name
        self.students = students or []
        self.avarage_score = avarage_score

    def __str__(self):
        if self.name == 'oleksii':
            return f'{self.name}, {self.courses_name}, {self.students}, {self.avarage_score}'
        else:
            return 'Nithing to see'

    def __len__(self):
        return len(self.students)

    def __repr__(self):
        return f'Course(name=\'{self.name}\', courses_name=\'{self.courses_name}\', students={self.students}, avarage_score={self.avarage_score})'


math = Course(**course_dict) # name= c.....
lit = Course(**course_dict_2)
math_2 = Course(name='oleksii', courses_name='math', students=['Ivan', 'Denis', 'Viktoria'], avarage_score=89)
list_2 = [lit]
print(list_2)
print(str(math))
len(math)

# str_math = str(math)
# print(str_math)
# print(list_2)
# len(lit)
# len(list_2)
# str_math = str(math)
# print(str_math)
# print(len(math))
# print(math)
# print(math.__dict__)
# math.students.append(1)
# math_1 = Course(**course_dict)
# math_1.students.append(5)
# print(math.students)
# print(math_1.students)





# def add_in_list (some_value, list = []):
#     list.append(some_value)
#     return list
#
#
# list_1 = add_in_list(1)
# print(list_1)
# list_2 = add_in_list(2)
# print(list_2)