users = [
    {'id': 1, 'name': 'Den', 'age': 20, 'job': {'id': 1, 'title': 'QA'}},
    {'id': 2, 'name': 'Alex', 'age': 30},
    {'id': 3, 'name': 'Igor', 'age': 40, 'job': None},
    {'id': 4, 'name': 'Ivan', 'age': 50, 'job': {'id': 2, 'title': 'CEO'}},
    {'id': 5, 'name': 'Mor', 'age': 60, 'job': {'id': 1, 'title': 'QA'}},
    {'id': 6, 'name': 'Viktor', 'age': 70, 'job': {'id': 3, 'title': 'Retired'}},
    {'id': 7, 'name': 'Maria', 'age': 20, 'job': {'id': 1, 'title': 'QA'}},
    {'id': 8, 'name': 'Anna', 'age': 20, 'job': {}},
]


for user in users:
    user_job = user.get('job')
    if user_job is not None and user_job and user_job.get('title') == 'QA':
        print(f'{user.get('id')}, {user.get('name')}')
    else:
        print('Wrong users' + f'{user.get('id')}, {user.get('name')}')

# for user in users[:3]:
#     # щоб вивести тільки ключі, треба (for key in user), (for key in user.keys())
#     # щоб вивести тільки значення, треба  (for key in user.values())
#
#     # for key, value in user.items():
#     #     print(f'{key}: {value}')
#     print(user)
#     if user.get('id') == 3:
#         break
# else:
#     print('We finish our iteration')








# # print(type(range(15))) # 0.....14
# # print(tuple(range(15)))
# for number in range(1, 5): #range(1, 15) -> 1....4
#     if number % 2 == 1: # Всі непарні числа ми пропускаєм
#         continue
#     for number_2 in range(5, 10): # 5....9
#         if number_2 == 7: # обірви цикл на елменті під номер 7
#             break
#         print(f'{number} * {number_2} = {number * number_2}')
#     # break


'''
1  -> if number % 2 == 1: = True
2 -> if number % 2 == 1: = False
for number_2 in range(5, 10): # 5....9
        print(f'{number} * {number_2} = {number * number_2}')\
        
3 -> if number % 2 == 1: = True
....

'''
#
# for index, value in enumerate(users):
#     print(f'{index}: {value}')

# for user in users:
#     print(user)