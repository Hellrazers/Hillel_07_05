# # print(bool('')) #False
# # print(bool(tuple()))
# # print(bool([]))
# # print(bool(dict()))
# # print(bool(set()))
# # print(bool(None))
#
# # list_ = [1,]
# # if bool(list_):  #TRUE
# #     print(list_)
#
# login_ar = 'user'
# password_ar = ''
#
# login_exp = 'user'
# password_exp = ''
# print(login_ar != login_exp) #False
# print(password_ar != password_exp) #True False and True => False, False or True => True
# print( password_ar is not None)
# if login_ar == login_exp and password_ar == password_exp: #старт умови
#     print('User logged in')
#
# elif password_ar is not None: # True
#     print('Password is None')
#
# else:
#     print('SMth was wrong') #кінець
#
#
# if password_ar != password_exp:
#     print('User not logged in')



age = 25
is_student = True
has_experience = False
# True or False = TRUE
# if (age >= 18 and is_student) or (has_experience and age < 30): #
#     print("You are either an adult student or have experience and are under 30.")
# else:
#     print("You don't meet any of the specified conditions.")

# (age >= 18 and is_student) or (has_experience and age < 30) =
#  (True and True ) or (False and True)
#  True or False == True
if  18 <= age <= 60:
    print('You can drink alchhole ')
elif age < 18:
    print('You can\'t drink alchhole ')
elif  60 < age < 100:
    print('You emery')
else:
    print('Please enter correct age')
