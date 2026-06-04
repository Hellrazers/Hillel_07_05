space_academy = {
    "academy_name": "Galaxy Horizon Advanced Academy", # (academy_name , "Galaxy Horizon Advanced Academy")
    "location": "Orbit of Mars, Sector 7-G",
    "established_year": 2142,
    "is_active": True,
    "administration": {
        "dean": "Dr. Elena Vance",
        "vice_dean": "Commander Rex Jarvis",
        "contacts": {"email": "admin@gha.edu", "subspace_freq": "884.2-A"},
    },
}



print(space_academy)
list_of_space_academy = list(space_academy.items()) #-> перетворення DICT на list [(key, value)]
print(list_of_space_academy)

# for data in list_of_space_academy:
#     # key, value = data
#     # print(f'{key}: {value}')
#     print(f'{data[0]}: {data[1]}')
#     print("-" * 80)


# for key, value in list_of_space_academy:
#     print(f'{key}: {value}')
#     print("-" * 80)# for
#
#
# list_1 = [(1, 2, 3), (1, 2, 3),(1, 2, 3),(1, 2, 3),(1, 2, 3),(1, 2, 3),(1, 2, 3),]
# for index,(first, second, third) in enumerate(list_1):
#     print(index, first, second, third)


for key, value in space_academy.items():
    print(f'{key}: {value}')
    print("-" * 80)# for