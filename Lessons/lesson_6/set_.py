fruits_list = ["яблуко", "банан", "банан", "апельсин", "банан", "банан", "банан" ] # hash(obj_1 ) ......hash(
# print(fruits_list)
# # fruits_2 = {(1, 2)}
# print(len(fruits_list))
# fruits_set = set(fruits_list)
# print(fruits_set)
# print(len(fruits_set))
# #deleting
# print(fruits.pop())
# fruits.remove('банан')
# print(fruits)

# set_ = {"банан","банан","банан","банан","банан","банан","банан","банан","банан","банан","банан","банан","банан","банан","банан","банан","банан","банан","банан","банан","банан","банан","банан","банан","банан","банан","банан","банан","банан","банан","банан","банан","банан","банан",}
#
# # print(set_)
# # print(set_.pop())
# # print(set_) # {} ->set()
#
# set_.remove('банан')

#adding
new_list_to_add = ['asdasdasdasd', 'asdasdas55345', '4343434']
set_frut = {"яблуко",  "апельсин", "банан"}
print(set_frut)
set_frut.add('мандарин')
print(set_frut)
set_frut.update()
print(set_frut)
set_frut.update([1, 2, 3])
print(set_frut)
# for k in new_list_to_add:
#     set_frut.add(k)
set_frut.update([11])
print(set_frut)



#
# count_ex, c



# fruits_list = ["яблуко", "банан", "банан", "апельсин", "банан", "банан", "банан" ] #list(range(1, 50))#
# new_list_with_fruit = fruits_list[:]
# for index, fruit in enumerate(fruits_list):
#     if new_list_with_fruit.count(fruit) > 1:
#         for element in new_list_with_fruit:
#             if element == fruit:
#                 new_list_with_fruit.remove(element)
# print(new_list_with_fruit)
#
# assert fruits_list == new_list_with_fruit, 'Becouse we ww8 uniq items '

# set_comp, list_with_not_uniq = set(), list()
# print(bool((list_with_not_uniq)))
# print(bool(fruits_list))
# for fruit in fruits_list:
#     if fruit not in set_comp:
#         print(f'Uniq item {fruit}')
#         set_comp.add(fruit)
#
#     else:
#         print(f'Fruit exists "{fruit}"')
#         list_with_not_uniq.append(fruit)
# if len(list_with_not_uniq) > 1 : # бо список не пустий | список пустий ======= FALSE    if list_with_not_uniq == len(list_with_not_uniq) > 1
#     print('WE FAIL, BECAUSE WE w8 ONLY UNIC ITEMS')
# else:
#     print('WE PASS')
#
# print(set_comp)
# print(list_with_not_uniq)