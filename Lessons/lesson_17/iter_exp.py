import sys

list_1 = list(range(1000))

# for child in list_1:
#     print(child)


iter_1 = iter(range(1000))
print(type(iter_1))

first_element = next(iter_1)
# print(first_element)

# first_element += 5
# print(first_element)
# print(next(iter_1))
#
print(sys.getsizeof(list_1))
print(sys.getsizeof(iter_1))
print(sys.getsizeof(first_element))
# print(list((1,23,4)))
# next(iter_1)
# next(iter_1)
# next(iter_1)
# next(iter_1)
# for i in iter_1:
#     print(i)
# next(iter_1)