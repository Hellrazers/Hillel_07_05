set1 = {1, 2, 3}
list_1 = [3, 4, 5]
set2 = {3,4,5}



#union
# logical_union = set1.union(list_1)
# print(logical_union)
# (set1.update(set2))
# print(set1)

# або
# logical_union = set1 | set2
# print(logical_union)


#intersection

logic_intersection = set1.intersection(set2)
# logical_intersection = set1 & set2
print(logic_intersection)
# print(logical_intersection)

# #difference
# left_difer = set1.difference(set2)
# print(left_difer)
# right_difer = set2.difference(set1)
# print(right_difer)

#symetric difference
sym_dif = set1.symmetric_difference(set2)
print(sym_dif)