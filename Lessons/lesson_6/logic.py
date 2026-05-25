
list_1 = []

list_2 = list(range(1, 10)) #[1....9]

# list_1 = list_
for element in list_2:
    if element % 2 == 0:
        list_1.append(f"{element} - парне")
    else:
        list_1.append(f"{element} - не парне")

# for element in list_2:
#     list_1.append(element**2)
# list_4 = [element ** 2 for element in list_2]

print(list_1)
# list_3 = [f"{element} - парне" for element in list_2 if element % 2 == 0] # [змінна_яка_додасця for змінна_яка_додасця in Iter_obj]
list_3 = [f"парне" if element % 2 == 0 else f"не парне" for element in list_2 ]
# [k for k in list_k]

print(list_3)
# print(list_4)
# tuple_1 = tuple(k**2 for k in list_2)
# print(tuple_1)

