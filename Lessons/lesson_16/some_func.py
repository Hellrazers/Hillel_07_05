# print(set(new_list))
def unify_and_verify(list_obj: list):
    # new_set, new_list_2 = set(), []
    #
    # for item in list_obj:

    #     if item not in new_set:
    #         new_set.add(item)
    #         print(new_set)
    #         new_list_2.append(item)
    #     else:
    #         print(f'{item} already exists in new_set')
    data_list = []

    for index, item in enumerate(list_obj):
        if list_obj.count(item) > 1:
            if list_obj.index(item) == index:
                data_list.append(item)
        else:
            data_list.append(item)

    return data_list
new_list = [1, 2, 'asd', 45, 'asd']
new_list_2 = [1, 2, 'asd', 45, 'asd']
new_list.extend(new_list_2)
print(new_list)
print(unify_and_verify(new_list))
new_list_3 = new_list + new_list_2
print(new_list_3)

