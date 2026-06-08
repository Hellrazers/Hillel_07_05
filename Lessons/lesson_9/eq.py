api_user = {
    'id_': 1,
    'name': 'oleksii',
    'is_student': True,
}
api_user_2 = {
    'id_': 2,
    'name': 'ivan',
    'is_student': True,
}
db_user = {
    'id_': 1,
    'db_name': 'oleksii',
    'has_student': True,
}

class ApiUser:
    def __init__(self, id_, name, is_student):
        self.id_ = id_
        self.name = name
        self.is_student = is_student

    def eq_method(self, other):
        # if isinstance(other, ApiUser):
        #     name_class = other.name
        #     is_student = other.is_student
        # else:
        #     name_class = other.db_name
        #     is_student = other.has_student

        name_class = other.name if isinstance(other, ApiUser) else other.db_name
        is_student = other.is_student if isinstance(other, ApiUser) else other.has_student

        # other_id = other
        if self.id_ != other.id_: # db_u = DbUser() DbUser(**db_user).id_
            return False
        if self.name != name_class:
            return False
        if self.is_student != is_student:
            return False
        return True

    def __eq__(self, other):
        # if isinstance(other, ApiUser):
        #     name_class = other.name
        #     is_student = other.is_student
        # else:
        #     name_class = other.db_name
        #     is_student = other.has_student

        name_class = other.name if isinstance(other, ApiUser) else other.db_name
        is_student = other.is_student if isinstance(other, ApiUser) else other.has_student

        # other_id = other
        if self.id_ != other.id_: # db_u = DbUser() DbUser(**db_user).id_
            return False
        if self.name != name_class:
            return False
        if self.is_student != is_student:
            return False
        return True


class DbUser:
    def __init__(self, id_, db_name, has_student):
        self.id_ = id_
        self.db_name = db_name
        self.has_student = has_student


#gt >
#le <=
#ge >=

# __ge
api_u = ApiUser(**api_user)
api_u2 = ApiUser(**api_user_2)
db_u = DbUser(**db_user)
print(isinstance(db_u, ApiUser))

api_u.eq_method(db_u)
api_u == api_u2

# print(api_u == db_u)
# print(api_u.__eq__(db_u))
# print(db_u == api_u)
# print(api_u == api_u2)

# print(db_u != api_u)
#
# print(api_u == api_u2)
# # print(api_u == db_user)


# assert api_user['id'] == db_user['id']
# assert api_user['name'] == db_user['db_name']